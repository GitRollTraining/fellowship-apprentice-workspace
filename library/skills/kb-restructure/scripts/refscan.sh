#!/usr/bin/env bash
# refscan.sh — inbound-reference discovery for a structural mutation (rename/move/split/merge/archive).
#
# Usage: refscan.sh <old-path-string> <tree-root> [policy-patterns-file]
#        REFSCAN_ICASE=1 refscan.sh ...   # case-insensitive matching (case-insensitive filesystems)
# Output: one hit per line, TAB-separated:  <path-relative-to-tree-root><TAB><hint>
#
# Hints are pattern-derived classification SUGGESTIONS, not verdicts — the live-vs-historical
# call is agent judgment against the workspace rename/move policy (see references/classification.md).
# Hint precedence: archive-segment > manifest > policy-pattern > content. A live INDEX.md keeps
# its `manifest` hint even when a broad policy pattern also matches it; only an INDEX inside an
# .archive/ tree hints historical.
#   historical  .archive/ path segment, or matches a policy pattern
#   manifest    an INDEX.md manifest (rows must be fixed at BOTH ends of a move)
#   symlink     a symlink whose target — raw text OR physically resolved path — hits the old path
#   content     everything else (prose links, frontmatter, registries, code, binary)
#
# Search MUST NOT silently skip hidden or gitignored files: plain rg/grep skips dot-dirs and
# anything gitignored, producing a false-clean sweep. Hence --hidden --no-ignore, fixed-string.
# rg/find errors (unreadable dirs) pass through to stderr — ANY stderr means the sweep may be
# incomplete; resolve before trusting the hit list. Suppressed by design: cd failures on broken
# symlink targets (symcheck's job) and the policy-regex validation probe (fail-fasts with its
# own file:line message). Unreadable symlinks are WARNed, not dropped silently.
# --binary included: a binary (PDF, image metadata) carrying the path IS an inbound ref; it is
# reported for classification (usually regenerate-or-leave), not for text fixing.
#
# Known limits (by design — cover via the playbook's alias-form scans + triage):
# - Literal substring match: a ref whose text differs from the needle (bare filename, relative
#   form, extension-less wiki link, URL-encoded, line-wrapped) needs its own alias scan.
# - No path-boundary semantics: short needles over-report (alpha/beta also hits alpha/beta-x);
#   prefer full paths; classify superstring hits as not-a-ref.
#
# NOT-KB-CONTENT TREES ARE PRUNED, not merely hinted. Two kinds:
# 1. Nested checkouts (universal, auto-detected): any directory below the root holding a `.git`
#    entry — a git worktree, submodule, or vendored clone. A worktree's `.git` is a FILE, so the
#    `**/.git/**` glob does NOT exclude it and rg scans the whole duplicate checkout. Every hit
#    inside one is a phantom duplicate of a real hit, in a tree you must not edit. Measured on a
#    live KB: one stale worktree contributed 641 of 2743 hits.
# 2. Vendored/tooling dirs (universal, by name): node_modules, .venv, venv, __pycache__.
# Workspace-specific non-content trees (an agent's own planning/scratch dirs) are NOT universal —
# exclude them via a `!`-prefixed policy line (below), so the skill stays portable.
#
# [policy-patterns-file]: one extended-regex per line (# comments, blank lines OK), matched
# against each hit's relative path. Populate it from the workspace's rename/move policy section —
# the patterns live in workspace policy, not here. Any invalid regex line aborts with exit 2:
# silent policy degradation is worse than a hard stop.
#   pattern    -> hint `historical` (a point-in-time citation; leave it alone)
#   !pattern   -> EXCLUDE from the scan entirely (not KB content; never a ref, never a fix)
# The `!` form exists because a HINT does not reduce noise: a workspace's own gitignored task dirs
# can dominate a hit list (1337 of 2743 on the KB this was built against) and, worse, a run's own
# verdict log lives there and self-hits its own residue gate.
set -uo pipefail

usage() { echo "usage: [REFSCAN_ICASE=1] refscan.sh <old-path-string> <tree-root> [policy-patterns-file]" >&2; exit 2; }
[[ $# -ge 2 && $# -le 3 ]] || usage
NEEDLE="$1"
ROOT="$2"
POLICY="${3:-}"
ICASE="${REFSCAN_ICASE:-0}"
[[ -n "$NEEDLE" ]] || usage
[[ "$ROOT" != "/" ]] && ROOT="${ROOT%/}"
[[ -d "$ROOT" ]] || { echo "refscan: tree-root not a directory: $ROOT" >&2; exit 2; }
command -v rg >/dev/null || { echo "refscan: rg (ripgrep) required" >&2; exit 2; }

# Validate policy patterns up front; one bad regex must not silently disable the rest.
# `!`-prefixed lines are EXCLUDES (not KB content); the rest are historical HINTS.
PATTERNS=()
EXCLUDES=()
if [[ -n "$POLICY" ]]; then
  [[ -f "$POLICY" ]] || { echo "refscan: policy-patterns-file not found: $POLICY" >&2; exit 2; }
  lineno=0
  while IFS= read -r pat || [[ -n "$pat" ]]; do
    lineno=$((lineno+1))
    [[ -z "${pat//[[:space:]]/}" ]] && continue
    [[ "$pat" =~ ^[[:space:]]*# ]] && continue
    is_exclude=0
    [[ "$pat" == '!'* ]] && { is_exclude=1; pat="${pat#!}"; }
    grep -qE -e "$pat" </dev/null 2>/dev/null
    [[ $? -le 1 ]] || { echo "refscan: invalid regex at $POLICY:$lineno: $pat" >&2; exit 2; }
    if [[ "$is_exclude" == 1 ]]; then EXCLUDES+=("$pat"); else PATTERNS+=("$pat"); fi
  done < "$POLICY"
fi

excluded() {  # policy `!` excludes — not KB content, never reported
  local rel="$1" pat
  for pat in ${EXCLUDES[@]+"${EXCLUDES[@]}"}; do
    grep -qE -e "$pat" <<<"$rel" && return 0
  done
  return 1
}

hint_for() {
  local rel="$1" pat
  case "$rel" in .archive/*|*/.archive/*) echo historical; return ;; esac
  case "$rel" in INDEX.md|*/INDEX.md)     echo manifest;   return ;; esac
  for pat in ${PATTERNS[@]+"${PATTERNS[@]}"}; do
    grep -qE -e "$pat" <<<"$rel" && { echo historical; return; }
  done
  echo content
}

# Vendored/tooling dirs (universal, by name) + nested checkouts (universal, auto-detected).
VENDOR=(.git node_modules .venv venv __pycache__)
NESTED=()
while IFS= read -r -d '' g; do
  d="$(dirname "${g#./}")"
  [[ "$d" == "." || -z "$d" ]] && continue     # the root's own .git — not nested
  NESTED+=("$d")
done < <(cd "$ROOT" && find . -mindepth 2 -name .git -print0 2>/dev/null | LC_ALL=C sort -z)
[[ ${#NESTED[@]} -gt 0 ]] && printf 'refscan: pruning %s nested checkout(s): %s\n' "${#NESTED[@]}" "${NESTED[*]}" >&2

lc() { tr '[:upper:]' '[:lower:]'; }
contains_needle() {  # honors REFSCAN_ICASE
  local hay="$1"
  if [[ "$ICASE" == "1" ]]; then
    [[ "$(lc <<<"$hay")" == *"$(lc <<<"$NEEDLE")"* ]]
  else
    [[ "$hay" == *"$NEEDLE"* ]]
  fi
}

# Pass 1 — text hits: every file whose CONTENT contains the old path string.
# --hidden --no-ignore: dot-dirs + gitignored included. -F: literal. -l --null: NUL-safe file list.
# Globs anchored with **/ so vendored/git dirs are excluded at ANY depth (matching pass 2's prune).
RG_FLAGS=(--hidden --no-ignore --binary -F -l --null)
for v in "${VENDOR[@]}"; do RG_FLAGS+=(--glob "!**/$v/**"); done
for n in ${NESTED[@]+"${NESTED[@]}"}; do RG_FLAGS+=(--glob "!$n/**"); done
[[ "$ICASE" == "1" ]] && RG_FLAGS+=(-i)
while IFS= read -r -d '' rel; do
  rel="${rel#./}"
  [[ -n "$rel" ]] || continue
  excluded "$rel" && continue
  if [[ "$rel" == *$'\n'* ]]; then
    printf 'refscan: WARN filename contains newline, reported escaped: %s\n' "${rel//$'\n'/\\n}" >&2
    rel="${rel//$'\n'/\\n}"
  fi
  printf '%s\t%s\n' "$rel" "$(hint_for "$rel")"
done < <(cd "$ROOT" && rg "${RG_FLAGS[@]}" -- "$NEEDLE" . | LC_ALL=C sort -z)

# Pass 2 — symlink hits: rg reads file contents, never link targets. Match the needle against the
# RAW target text and the PHYSICALLY RESOLVED root-relative path — a relative target like
# `beta/file.md` textually lacks the needle yet resolves straight into it. Resolution uses
# cd + pwd -P (target's parent must exist; broken links fall back to raw text and are symcheck's
# job anyway). Prune only DIRECTORIES named node_modules/.git — a symlink named node_modules is
# still a symlink and must be scanned.
ROOTP="$(cd "$ROOT" && pwd -P)"
PRUNE=()
for v in "${VENDOR[@]}"; do PRUNE+=(-name "$v" -o); done
for n in ${NESTED[@]+"${NESTED[@]}"}; do PRUNE+=(-path "$ROOT/$n" -o); done
unset 'PRUNE[${#PRUNE[@]}-1]'   # drop the trailing -o
while IFS= read -r -d '' link; do
  rel_link="${link#"$ROOT"/}"
  excluded "$rel_link" && continue
  target="$(readlink "$link")" || { printf 'refscan: WARN unreadable symlink skipped: %s\n' "${rel_link//$'\n'/\\n}" >&2; continue; }
  hit=""
  contains_needle "$target" && hit=1
  if [[ -z "$hit" ]]; then
    tdir="$(dirname "$target")"
    case "$target" in
      /*) resolved_dir="$(cd "$tdir" 2>/dev/null && pwd -P)" ;;   # broken targets expected: symcheck's job
      *)  resolved_dir="$(cd "$(dirname "$link")" 2>/dev/null && cd "$tdir" 2>/dev/null && pwd -P)" ;;
    esac
    if [[ -n "${resolved_dir:-}" ]]; then
      resolved="$resolved_dir/$(basename "$target")"
      contains_needle "${resolved#"$ROOTP"/}" && hit=1
    fi
  fi
  [[ -n "$hit" ]] && printf '%s\t%s\n' "$rel_link" symlink
done < <(find "$ROOT" -type d \( "${PRUNE[@]}" \) -prune -o -type l -print0)
exit 0
