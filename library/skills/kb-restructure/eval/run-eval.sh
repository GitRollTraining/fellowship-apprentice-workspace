#!/usr/bin/env bash
# run-eval.sh — mechanized eval for kb-restructure scripts against eval/baseline-output.md.
# Builds the planted fixture from eval/baseline-input.md in a temp dir, runs refscan + symcheck,
# asserts every case. Exit 0 = all green, 1 = any mismatch.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REFSCAN="$HERE/../scripts/refscan.sh"
SYMCHECK="$HERE/../scripts/symcheck.sh"
[[ -x "$REFSCAN" && -x "$SYMCHECK" ]] || { echo "FATAL: scripts missing or not executable" >&2; exit 1; }

pass=0; fail=0
ok(){ printf 'PASS  %s\n' "$1"; pass=$((pass+1)); }
bad(){ printf 'FAIL  %s\n' "$1"; fail=$((fail+1)); }

FIX="$(mktemp -d)"; MINI="$(mktemp -d)"
trap 'rm -rf "$FIX" "$MINI"' EXIT
mkdir -p "$FIX/alpha/beta" "$FIX/docs" "$FIX/.claude/logs" "$FIX/.archive" "$FIX/vendor/node_modules"
echo "payload" > "$FIX/alpha/beta/file.md"
echo "see alpha/beta/file.md" > "$FIX/docs/note.md"
echo "log: alpha/beta/file.md" > "$FIX/.claude/logs/2026-01-01.md"
echo "| row | alpha/beta/file.md |" > "$FIX/docs/INDEX.md"
echo "old alpha/beta/file.md" > "$FIX/.archive/old.md"
( cd "$FIX" && git init -q . 2>/dev/null; echo "secret.md" > .gitignore \
    && echo "gitignored ref alpha/beta/file.md" > secret.md )
ln -s "../alpha/beta/file.md" "$FIX/docs/link.md"
ln -s "beta/file.md" "$FIX/alpha/rel-link.md"                        # R1: raw text lacks needle
printf 'ref alpha/beta/file.md then\x00binary tail' > "$FIX/docs/blob.bin"   # R1: binary
echo "vendored alpha/beta/file.md" > "$FIX/vendor/node_modules/pkg.md"       # R1: must be pruned
echo "[see](./beta/file.md)" > "$FIX/alpha/sib.md"                   # R1: relative literal
echo "Alpha/Beta/file.md" > "$FIX/docs/case.md"                      # R1: case variant

# R2 (round 02, from the live dogfood): trees that are NOT KB content must be PRUNED, not hinted.
# A git worktree's .git is a FILE, so `--glob '!**/.git/**'` does not exclude it and the whole
# duplicate checkout gets scanned. On the live KB this contributed 641 of 2743 hits.
mkdir -p "$FIX/nested-wt" "$FIX/.venv"
printf 'gitdir: /elsewhere/.git/worktrees/nested-wt\n' > "$FIX/nested-wt/.git"   # a FILE, not a dir
echo "phantom dup alpha/beta/file.md" > "$FIX/nested-wt/dup.md"      # must NEVER be reported
echo "vendored alpha/beta/file.md" > "$FIX/.venv/lib.md"             # must NEVER be reported
mkdir -p "$FIX/scratch"
echo "agent scratch alpha/beta/file.md" > "$FIX/scratch/notes.md"    # reported by default; `!`-excludable

scan(){ "$REFSCAN" "$@" | LC_ALL=C sort; }

expected_case1="$(printf '%s\n' \
  ".archive/old.md	historical" \
  ".claude/logs/2026-01-01.md	content" \
  "alpha/rel-link.md	symlink" \
  "docs/INDEX.md	manifest" \
  "docs/blob.bin	content" \
  "docs/link.md	symlink" \
  "docs/note.md	content" \
  "scratch/notes.md	content" \
  "secret.md	content" | LC_ALL=C sort)"

# Case 1 — full-path needle, no policy file
actual1="$(scan "alpha/beta/file.md" "$FIX")"
if [[ "$actual1" == "$expected_case1" ]]; then ok "case 1: all plants found, exclusions absent, hints as expected"
else bad "case 1: refscan output mismatch"; diff <(printf '%s\n' "$expected_case1") <(printf '%s\n' "$actual1") | sed 's/^/      /'; fi

# Case 2 — policy patterns file flips the log hit to historical, rest unchanged
POL="$MINI/pol-good"; echo '^\.claude/logs/' > "$POL"
actual2="$(scan "alpha/beta/file.md" "$FIX" "$POL")"
if grep -q '^\.claude/logs/2026-01-01.md	historical$' <<<"$actual2" \
   && [[ "$(grep -v '2026-01-01' <<<"$actual2")" == "$(grep -v '2026-01-01' <<<"$actual1")" ]]; then
  ok "case 2: policy file flips log hit to historical, rest unchanged"
else bad "case 2: policy injection failed"; printf '%s\n' "$actual2" | sed 's/^/      /'; fi

# Case 4 — basename alias scan catches relative-literal + case-variant refs (run pre-move)
actual4="$(scan "file.md" "$FIX")"
if grep -q '^alpha/sib.md	content$' <<<"$actual4" && grep -q '^docs/case.md	content$' <<<"$actual4"; then
  ok "case 4: basename alias scan finds relative-literal and case-variant refs"
else bad "case 4: alias scan missed sib.md or case.md"; printf '%s\n' "$actual4" | sed 's/^/      /'; fi

# Case 5 — ICASE output = case-1 set plus exactly the case-variant ref; default lacks it
actual5="$(REFSCAN_ICASE=1 "$REFSCAN" "alpha/beta/file.md" "$FIX" | LC_ALL=C sort)"
expected5="$(printf '%s\n%s\n' "$expected_case1" "docs/case.md	content" | LC_ALL=C sort)"
if [[ "$actual5" == "$expected5" ]] && ! grep -q 'case.md' <<<"$actual1"; then
  ok "case 5: REFSCAN_ICASE=1 output = case-1 set + case-variant ref exactly; default lacks it"
else bad "case 5: ICASE set mismatch"; diff <(printf '%s\n' "$expected5") <(printf '%s\n' "$actual5") | sed 's/^/      /'; fi

# Case 6 — invalid policy regex aborts with exit 2 naming the line
POLBAD="$MINI/pol-bad"; printf '^plans/\na[\n' > "$POLBAD"
err6="$("$REFSCAN" "alpha/beta/file.md" "$FIX" "$POLBAD" 2>&1 >/dev/null)"; rc6=$?
if [[ $rc6 -eq 2 ]] && grep -q ':2:' <<<"$err6"; then ok "case 6: invalid policy regex -> exit 2 naming line 2"
else bad "case 6: expected exit 2 + line ref, got rc=$rc6: $err6"; fi

# Case 7 — trailing-slash root output identical to case 1
actual7="$(scan "alpha/beta/file.md" "$FIX/")"
[[ "$actual7" == "$actual1" ]] && ok "case 7: trailing-slash root keeps paths root-relative" \
  || { bad "case 7: trailing-slash output differs"; diff <(printf '%s\n' "$actual1") <(printf '%s\n' "$actual7") | sed 's/^/      /'; }

# Case 8 — broken symlink NAMED node_modules still reported (dirs pruned, symlinks not)
ln -s /nonexistent "$MINI/node_modules"
out8a="$("$SYMCHECK" "$MINI")"; rc8a=$?
out8b="$("$SYMCHECK" "$MINI/")"; rc8b=$?
if [[ "$out8a" == "node_modules" && $rc8a -eq 1 && "$out8b" == "node_modules" && $rc8b -eq 1 ]]; then
  ok "case 8: node_modules-named symlink reported, trailing slash safe (exit 1)"
else bad "case 8: got [$out8a]/rc=$rc8a and [$out8b]/rc=$rc8b"; fi
rm "$MINI/node_modules"

# Case 9 (R2) — nested checkout + vendored dirs are PRUNED, never reported.
# Regression guard for the live-run defect: a stale worktree and a .venv contributed 76% of a
# real scan's hits. A hint cannot fix this — the tree must not be scanned at all.
if ! grep -q 'nested-wt' <<<"$actual1" && ! grep -q '\.venv' <<<"$actual1"; then
  ok "case 9: nested checkout (.git FILE) and .venv pruned, not reported"
else bad "case 9: not-KB-content tree leaked into the hit list"; grep -e 'nested-wt' -e '\.venv' <<<"$actual1" | sed 's/^/      /'; fi

# Case 10 (R2) — a `!`-prefixed policy line EXCLUDES a tree; a plain line only HINTS it.
# The two must not be confused: a hint still reports the hit (and a run's own verdict log,
# living in such a tree, would then self-hit its residue gate).
POLEX="$MINI/pol-exclude"; printf '!^scratch/\n' > "$POLEX"
POLHINT="$MINI/pol-hint"; printf '^scratch/\n' > "$POLHINT"
actual10ex="$(scan "alpha/beta/file.md" "$FIX" "$POLEX")"
actual10hint="$(scan "alpha/beta/file.md" "$FIX" "$POLHINT")"
if ! grep -q 'scratch/notes.md' <<<"$actual10ex" \
   && grep -q '^scratch/notes.md	historical$' <<<"$actual10hint" \
   && [[ "$(grep -v 'scratch/' <<<"$actual10ex")" == "$(grep -v 'scratch/' <<<"$actual1")" ]]; then
  ok "case 10: '!' policy line excludes the tree; plain line only hints historical"
else bad "case 10: exclude/hint semantics wrong"; printf 'exclude:\n%s\nhint:\n%s\n' "$actual10ex" "$actual10hint" | sed 's/^/      /'; fi

# Case 3 — symcheck clean pre-move; exactly the two planted links break post-move
pre="$("$SYMCHECK" "$FIX")"; pre_rc=$?
mv "$FIX/alpha/beta/file.md" "$FIX/alpha/file.md"
post="$("$SYMCHECK" "$FIX" | LC_ALL=C sort)"; post_rc=$?
[[ -z "$pre" && $pre_rc -eq 0 ]] && ok "case 3a: symcheck clean pre-move (exit 0)" || bad "case 3a: symcheck not clean pre-move: $pre"
expected3="$(printf 'alpha/rel-link.md\ndocs/link.md\n')"
[[ "$post" == "$expected3" && $post_rc -eq 1 ]] && ok "case 3b: symcheck reports exactly both broken links post-move (exit 1)" \
  || { bad "case 3b: symcheck post-move mismatch (rc=$post_rc)"; printf '%s\n' "$post" | sed 's/^/      /'; }


# Case 11 (R2) — linkcheck: the ONLY gate for F5 ("a rewritten ref is not a working ref") was itself
# untested. It must (a) catch a genuinely dead relative link, (b) resolve a live one, (c) NOT report a
# link inside a code span or fenced block (a specimen, not a link), (d) exit 1 when broken / 0 when
# clean / 2 on its own failure — an exit-2 checker that emits nothing reads as "clean" and certifies.
LCK="$HERE/../scripts/linkcheck.sh"
mkdir -p "$FIX/lc/sub"
printf '[live](sub/ok.md)\n[dead](sub/gone.md)\n' > "$FIX/lc/page.md"
printf 'ok\n' > "$FIX/lc/sub/ok.md"
printf 'specimen in a code span: `](../x/y.md)` and fenced:\n\n```\n[x](../nope/z.md)\n```\n' > "$FIX/lc/spec.md"
lc_out="$("$LCK" "$FIX" "" lc 2>/dev/null)"; lc_rc=$?
if [[ "$lc_out" == "lc/page.md	sub/gone.md" && $lc_rc -eq 1 ]]; then
  ok "case 11: linkcheck finds the dead link, ignores the live one and both code-span/fenced specimens (exit 1)"
else bad "case 11: linkcheck output/exit wrong (rc=$lc_rc)"; printf '%s\n' "$lc_out" | sed 's/^/      /'; fi

rm "$FIX/lc/page.md"
lc_out2="$("$LCK" "$FIX" "" lc 2>/dev/null)"; lc_rc2=$?
[[ -z "$lc_out2" && $lc_rc2 -eq 0 ]] && ok "case 12: linkcheck exits 0 with no output when clean" \
  || bad "case 12: expected clean/exit 0, got rc=$lc_rc2: $lc_out2"

"$LCK" /nonexistent-tree-xyz >/dev/null 2>&1; lc_rc3=$?
[[ $lc_rc3 -eq 2 ]] && ok "case 13: linkcheck exits 2 on its own failure (a gate must not read this as clean)" \
  || bad "case 13: expected exit 2 on bad root, got $lc_rc3"

# Case 15 (R2) — linkcheck must NOT treat an INDENTED backtick line as a fence. A Markdown fence may
# be indented at most 3 spaces; 4+ is a literal code block. The pre-fix `^\s*` matched those, so TWO of
# them made the parity EVEN, the odd-parity guard never fired, and every link between them was silently
# blanked. 15 real files in the host KB carry indented backticks — this was LIVE. Without this case,
# reverting the regex passes all 89 gates: a behavioral fix with no test is one that silently regresses.
mkdir -p "$FIX/lc2"
printf 'intro\n\n    ```\n\n[dead](./nope/gone.md)\n\n    ```\n\ntail\n' > "$FIX/lc2/indented.md"
lc_ind="$("$LCK" "$FIX" "" lc2 2>/dev/null)"; lc_ind_rc=$?
if [[ "$lc_ind" == "lc2/indented.md	./nope/gone.md" && $lc_ind_rc -eq 1 ]]; then
  ok "case 15: 4-space-indented backticks are NOT fences — the dead link between them is reported"
else bad "case 15: indented-fence link hidden (the ^\\s* regression)"; printf '%s\n' "$lc_ind" | sed 's/^/      /'; fi
rm -rf "$FIX/lc2"

# Case 14 (R2) — linkcheck honors the policy `!` exclude, so a not-KB-content tree does not flood it.
mkdir -p "$FIX/lc/scratchtree"
printf '[dead](../../nowhere/q.md)\n' > "$FIX/lc/scratchtree/notes.md"
POLLC="$MINI/pol-lc"; printf '!^lc/scratchtree/\n' > "$POLLC"
lc_noex="$("$LCK" "$FIX" "" lc 2>/dev/null | grep -c 'scratchtree' || true)"
lc_ex="$("$LCK" "$FIX" "$POLLC" lc 2>/dev/null | grep -c 'scratchtree' || true)"
[[ "$lc_noex" -eq 1 && "$lc_ex" -eq 0 ]] && ok "case 14: linkcheck '!' policy exclude drops the not-KB-content tree" \
  || bad "case 14: exclude semantics wrong (without=$lc_noex, with=$lc_ex)"
rm -rf "$FIX/lc"

printf '\n%d PASS, %d FAIL\n' "$pass" "$fail"
[[ $fail -eq 0 ]]
