#!/usr/bin/env bash
# linkcheck.sh — resolve every relative link in a tree and report the ones that do not exist.
#
# Usage: linkcheck.sh <tree-root> [policy-patterns-file] [subtree]
# Output: one broken link per line, TAB-separated:  <file><TAB><link-target-as-written>
# Exit:   0 = no broken links, 1 = broken links found, 2 = usage.
#
# WHY THIS EXISTS.  A reference scan finds the old path STRING.  It cannot tell you whether a link
# RESOLVES.  Two failure classes are invisible to any text search, and both shipped on live content:
#   1. Rewriting a ref's path segment does not touch its `../` depth, so a "fixed" relative link can
#      still be dead — `](../x/y.md)` rewritten to `](../x/z.md)` is just as broken if the `../` was
#      wrong to begin with.  A live run found a template exemplar link that had been dead for months.
#   2. Moving content changes its ancestor depth, so every outward relative link inside it silently
#      mis-resolves with ZERO text change.  Nothing in the file differs; only where it sits.
# Run this after EVERY mutation, over the WHOLE affected tree — never scoped to the one file that
# prompted it (a file-scoped check goes green while its siblings stay broken).
#
# The gate is the DELTA against a pre-mutation baseline, not zero: most KBs carry pre-existing dead
# links, and fixing them is a different job from not breaking new ones.  Capture a baseline first:
#   LC=/abs/path/to/linkcheck.sh                       # ABSOLUTE: a relative path silently fails
#   [ -x "$LC" ] || { echo "not executable"; exit 1; }
#   run() { local rc=0; "$LC" . policy.txt > "$1" || rc=$?
#           if   [ "$rc" -gt 1 ];                  then echo "checker FAILED"; exit 1
#           elif [ "$rc" -eq 1 ] && [ ! -s "$1" ]; then echo "exit 1 but NO output -> not looking"; exit 1
#           fi; }
#   run before.txt      # BEFORE the mutation
#   # ... do the mutation ...
#   run after.txt       # AFTER
#   diff before.txt after.txt   # must be empty
#
# TWO TRAPS, BOTH PROVEN LIVE.
# 1. `|| rc=$?` is load-bearing.  Exit 1 ("broken links found") is the EXPECTED state on any real KB;
#    under `set -e` that status kills the script AT the linkcheck line, so `rc=$?` never runs and the
#    gate dies BEFORE the mutation.  `|| rc=$?` exempts it from `set -e` and captures the status.
# 2. A STATUS CHECK ALONE IS NOT ENOUGH.  A checker that cannot be EXECUTED (lost +x, bad interpreter,
#    wrong path) ALSO arrives as 1 under `set -e` (127 collapses), and it prints nothing — so before
#    and after are both empty, `diff` is clean, and the gate CERTIFIES A TREE IT NEVER LOOKED AT.
#    Exit 1 MEANS "links found": exit 1 with EMPTY output is a self-contradiction.  Test for it.
# CHECK THE EXIT STATUS.  Exit 2 = the checker itself failed (no python3, bad root, missing policy
# file) and it prints NOTHING — so a naive `diff` of two empty files is EMPTY, and the gate reports
# clean while the checker never ran.  That is a hollow green, and it CERTIFIES.  0 = clean,
# 1 = broken links found, 2 = the checker is broken.  Never conflate 2 with 0.
#
# STDIN HAZARD (this is why the loop below reads from a FILE, not a pipe into a while-read):
#   A command that reads stdin, placed inside a `while read` loop that has no explicit input
#   redirection, EATS THE LOOP'S OWN INPUT.  `rg` with no path argument is the classic case: it
#   searches stdin, consuming the rest of the loop's list, so the loop exits after one iteration and
#   every remaining item is silently reported clean.  This shipped once and scanned 1 of 25 paths
#   while the gate went green — a "hollow green" is worse than no gate, because it certifies.
#   Defences, all three used here: give every command an explicit path argument; add `</dev/null` to
#   any command inside a read-loop; and re-scan independently, in a fresh process, at the end.
#   Same hazard with ssh, ffmpeg, mysql — anything that reads stdin.
set -uo pipefail

usage() { echo "usage: linkcheck.sh <tree-root> [policy-patterns-file] [subtree]" >&2; exit 2; }
[[ $# -ge 1 && $# -le 3 ]] || usage
ROOT="$1"
[[ "$ROOT" != "/" ]] && ROOT="${ROOT%/}"
[[ -d "$ROOT" ]] || { echo "linkcheck: tree-root not a directory: $ROOT" >&2; exit 2; }
POLICY="${2:-}"
[[ -n "$POLICY" && ! -f "$POLICY" ]] && { echo "linkcheck: policy-patterns-file not found: $POLICY" >&2; exit 2; }
SUB="${3:-.}"
command -v python3 >/dev/null || { echo "linkcheck: python3 required" >&2; exit 2; }

# [policy-patterns-file]: the SAME file refscan takes. Only its `!`-prefixed EXCLUDE lines are used
# here (the historical HINTS are meaningless for link resolution). Without them, a tree the workspace
# has declared not-KB-content — an agent's own gitignored scratch dirs — floods the report with dead
# links you neither own nor should fix. On a real KB that was 142 phantom breaks against 250 genuine
# pre-existing ones: a gate that cries wolf is a gate that gets ignored.
python3 - "$ROOT" "$SUB" "$POLICY" <<'PY'
import os, re, sys

root, sub, policy = sys.argv[1], sys.argv[2], sys.argv[3]
base = os.path.normpath(os.path.join(root, sub))

EXCLUDES = []
if policy:
    for line in open(policy, encoding='utf-8', errors='replace'):
        line = line.strip()
        if line.startswith('!'):
            EXCLUDES.append(re.compile(line[1:]))

def excluded(rel):
    return any(x.search(rel) for x in EXCLUDES)
PRUNE = {'.git', 'node_modules', '.venv', 'venv', '__pycache__'}
# ](target) — markdown link/image, minus the #anchor and any "title"
LINK = re.compile(r'\]\(\s*<?([^)>\s#]+)[^)]*\)')
# A Markdown fence may be indented at most 3 spaces; 4+ spaces is a literal indented code block, NOT
# a fence. Matching `^\s*` treated those as fences, so two of them made the parity EVEN — the
# odd-parity guard never fired and everything between them was silently blanked. 15 real files in the
# host KB carry indented backtick lines, so this was live.
FENCE = re.compile(r'^ {0,3}(```|~~~)', re.M)
CODESPAN = re.compile(r'`[^`\n]*`')
broken = 0

def strip_code(text, path=None):
    """Drop fenced blocks and inline-code spans before looking for links.

    A `](path)` inside backticks is a SYNTAX SPECIMEN, not a link — Markdown renderers do not
    linkify inside code spans either, so neither do we.  Without this, every doc that TEACHES the
    link syntax reports its own examples as broken, and the noise trains you to ignore the gate.

    UNBALANCED FENCES.  A file with an ODD number of fence markers (an unclosed block — exactly what
    a truncated or work-in-progress doc looks like) would otherwise leave `fenced` stuck True and
    BLANK THE REST OF THE FILE, silently hiding every link after it.  A checker that skips content
    without saying so is the hollow green this whole skill exists to kill.  So: count first, and if
    the parity is odd, do NOT strip fences in that file — scan it whole and WARN.  Over-reporting a
    specimen is a nuisance; under-reporting a real dead link is a defect.
    """
    lines = text.split('\n')
    if sum(1 for ln in lines if FENCE.match(ln)) % 2:
        print(f"linkcheck: WARN unbalanced code fence, scanning whole file: {path}", file=sys.stderr)
        return '\n'.join(CODESPAN.sub('', ln) for ln in lines)
    out, fenced = [], False
    for line in lines:
        if FENCE.match(line):
            fenced = not fenced
            continue
        out.append('' if fenced else CODESPAN.sub('', line))
    return '\n'.join(out)

for dirpath, dirnames, filenames in os.walk(base):
    dirnames[:] = [d for d in dirnames
                   if d not in PRUNE and not os.path.exists(os.path.join(dirpath, d, '.git'))]
    for fn in filenames:
        if not fn.endswith('.md'):
            continue
        f = os.path.join(dirpath, fn)
        if excluded(os.path.relpath(f, root)):
            continue
        try:
            text = strip_code(open(f, encoding='utf-8', errors='replace').read(), os.path.relpath(f, root))
        except OSError:
            continue
        for m in LINK.finditer(text):
            t = m.group(1)
            # skip absolute URLs, mailto/anchors, and template placeholders ({slug}, {{x}})
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', t) or t.startswith('#') or '{' in t:
                continue
            # a link is resolved from the directory of the file that CONTAINS it — not from the root.
            target = os.path.normpath(os.path.join(dirpath, t))
            if not os.path.exists(target):
                print(f"{os.path.relpath(f, root)}\t{t}")
                broken += 1

sys.exit(1 if broken else 0)
PY
