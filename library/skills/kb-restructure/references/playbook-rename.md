# Playbook — rename / move / re-nest (1→1)

Detailed steps for engine phases 2–9 when the operation is a 1→1 mutation: rename in place, move to a new parent, or re-nest (the parent chain changes). All three share one ref-mapping: every live inbound reference rewrites OLD path string → NEW path string. Numbering note: steps 1–9 implement engine phases 2–9 — phase 6 "Fix" spans steps 5–6, so step numbers sit one below phase numbers until they re-sync at 7.

## Steps

1. **Preflight.** Clean git tree (or explicit user acceptance of dirty). One-line scope statement. Extract the workspace policy's HISTORICAL patterns as anchored EREs, one per line (e.g. `(^|/)\.archive/`, `(^|/)logs/`), into a temp file OUTSIDE the tree — refscan validates them and exits 2 on any bad line. The policy's live-authority list is consumed later, at classification (rule 5), not by refscan. Run `symcheck.sh <kb-root>`, save output as the pre-existing-breakage baseline; pre-existing breaks are recorded, not fixed.
2. **Discover.** Run `refscan.sh "<needle>" <kb-root> [patterns-file]` once per alias form, and union the hit lists:
   - full old path — always;
   - basename — always; also surfaces line-wrapped full-path refs. Files: the filename (`file.md`). Directories: the trailing segment WITH separator (`guides/`); the bare segment word only when prose-noise is tolerable (it over-reports on ordinary words) — triage the noise as not-a-ref;
   - `REFSCAN_ICASE=1` pass with the full path — on case-insensitive filesystems (macOS/Windows defaults), where a case-variant ref still resolves;
   - extension-less basename — only if the KB uses wiki-style extension-less links;
   - URL-encoded full path (`%2F` separators) — only if the KB holds exported HTML/Notion payloads.
   Save the union verbatim. Hits with hint `symlink` (raw target text OR resolved target hits the needle) get classified at step 3 like every other hit — a superstring target or a link inside a frozen container is not automatically live. Alias scans over-report by design — triage is step 3's job, never a reason to skip a scan.
3. **Classify.** Verdict-log every hit per `references/classification.md`: live | historical | not-a-ref (alias hit that resolves to a different file). Keep the log OUTSIDE the tree, or pre-log its self-hits (classification § Self-reference). No fix happens before every hit has a logged verdict.
   **For any hit whose class is not obvious, READ ITS PARENT MANIFEST's row for that file or directory** — the manifest is where the host KB declares class (Immutable, Compiled, append-only). Nothing else in the procedure sends you there, and the hint never carries it. Read the CLASS column, not the prose description (classification rule 2): a row *described* as archived while *classed* blank does not freeze anything. Check the workspace policy list too — if neither names it frozen, it is not frozen.

   **MANDATORY PRECEDENT CHECK — run this before verdicting ANY hit `historical`.** Classification rule 7 says the host KB's own record beats your judgment, but nothing will remind you to go look. So look, mechanically:
   ```bash
   git log --oneline -3 --follow -- <the file>      # has a prior mutation already touched it?
   git log -p --follow -- <the file> | grep -i 'rename\|archive\|-> \|moved'
   ```
   Then read the file AROUND the hit. **If a sibling line — or the same line — carries a path that a PREVIOUS mutation already rewrote, this KB treats that file as LIVE. Follow that precedent, or overrule it and LOG WHY.** Do not verdict it `historical` on a theory the file itself contradicts.
   Two live runs got this wrong, both times by reasoning from first principles about "dated documents" instead of checking. The second was decisive: a dated note's completed checklist item was left stale as "rewriting falsifies the record" — while the checklist item on the line ABOVE it had had its path rewritten by an earlier sweep. Adjacent lines, identical shape, opposite treatment. **A KB that classifies the same file two ways in two mutations is incoherent in a way neither choice alone would be.**
4. **Execute.** `mkdir -p` the destination's parent directory first — `git mv` does not create it and fails. Then `git mv <old> <new>` — one command for a directory; confirm via `git status` that every child moved (rename pairs, no deletes; gitignored files do NOT show — companions are step 6's job).
5. **Fix live refs.** For each live hit, rewrite the old path string to the new one. Match on path boundaries — `a/b` must not rewrite inside `a/b-c` or `a/bd`. Append-only operative records (classification rule 4): append an old→new mapping line, never rewrite existing lines. Re-read each edited span after writing.
   **Then RESOLUTION-TEST every ref you rewrote** — from the containing file's own directory, not from the KB root. Rewriting the path string does not make the reference work: a ref in RELATIVE form (`](../x/y.md)`) keeps its own `../` depth, which the rewrite never touches. Resolve each rewritten target and confirm it exists. A dead result is one of THREE things — the third is easy to miss and a live run missed it:
   - **(a) A bad rewrite** — you broke it. Fix it.
   - **(b) A PRE-EXISTING dead link with a real target** — the file exists, the path was wrong (usually the `../` depth). Fix the depth too: shipping a link you rewrote and left dead is not defensible. LOG it as pre-existing, not as your breakage. (A live run found a template exemplar link that had been dead for months this way.)
   - **(c) The target NEVER EXISTED** — a plan's un-produced deliverable, a consolidated output, a path that was always aspirational. There is nothing to repoint TO. Do NOT invent a target: guessing a substitute inside a planning record falsifies what was planned. LOG it as a pre-existing dead ref with "target never existed" and move on. Renaming its directory does not make it your defect, but leaving it UNLOGGED does — a later reader cannot tell your rewrite from a real pointer.
   Whichever branch: every dead result gets a LOG ROW. Silence is the defect.
6. **Standing obligations — none of these ever appears in the hit list.** Same operation, not deferred:
   - Old parent manifest: row removed or repointed. **A manifest row usually cites its children by BARE NAME, so the full-path scan never hits it** — this is not a new-parent-only problem (see Gotchas). Go to the manifest; do not wait for a hit.
   - New parent manifest: row added. Destination directory new or manifest-less → CREATE the manifest per the host KB's convention (manifest file + line-1 parent pointer), then add the row. **Match the host KB's existing precedent** for how it rows this kind of entry — read a sibling manifest before inventing a shape.
   - **Manifest freshness fields**: a manifest you edited is a file you changed. Bump its own `last updated` / freshness value at BOTH ends. Nothing in discovery will remind you, and a stale freshness stamp silently defeats the KB's staleness sweep.
   - Moved node's OWN parent-pointer (workspace-declared line-1 upstream comment or similar): repointed at the new parent. Vacuous for single-file targets.
   - Stem-derived companions: files named from the moved file's stem — sync snapshots (`.{stem}.*-snapshot.*`), gitignored sidecars (`{stem}.<class>.md`) — contain no old-path text and no scan finds them. Move/rename them WITH the file: `git mv` if committed, plain `mv` if gitignored. Update every field or marker that names them (frontmatter `snapshot:`, in-file redaction markers).
   - Relative links INSIDE any moved node whose resolution depends on the node's location: outward `../` links after any re-parent, AND — for single-file moves — bare same-directory sibling links (`sibling.md`, `./x.md`) that stop resolving once the file leaves the directory. Sweep the moved content's own relative links and recompute.
7. **Symlink pass.** Retarget every symlink hit VERDICTED LIVE at step 3 to the new path (recompute relative depth from the link's own directory); historical/not-a-ref symlink hits stay untouched. Then `symcheck.sh <kb-root>` — **check its exit status: 0 = clean, 1 = broken links found, 2 = the checker itself failed. Never treat 2 as 0** (a dead checker prints nothing, and on a KB with a clean baseline "nothing" equals the baseline — a hollow green). Output must equal the preflight baseline; new entries are breakage this move caused — fix the link target's relative depth, re-run until the delta is empty.
8. **Verify.** Re-run every alias-form refscan from step 2: every remaining hit must match a logged HISTORICAL or NOT-A-REF verdict — residue == logged leave-set exactly. Expect the basename rescan to re-hit every ref you just FIXED (the new path contains the old basename): these are self-matches, batch-log them `not-a-ref` (rule 0); the full-path scan is the primary residue gate. Expect your own FIXES to appear as residue too (append-only mapping lines, strike-throughs, provenance and migration notes) — pre-log them (classification § Self-reference). Other unlogged residue → return to step 3 for that hit. Re-run symcheck one final time. Confirm every step-6 obligation by reading the files.
   **Link-resolution gate — `scripts/linkcheck.sh <kb-root> [policy-file]`** (whole tree, not just what you touched). It resolves every relative link from its own file's directory. Capture a baseline BEFORE the mutation and diff: the bar is ZERO NEW broken links, not zero broken links (most KBs carry pre-existing dead ones, and fixing those is a different job).
   ```bash
   KB="<kb-root>"                                                     # absolute path to the KB root
   POLICY="<policy-patterns-file>"                                    # the same file refscan took
   LC="$KB/.claude/skills/kb-restructure/scripts/linkcheck.sh"        # ABSOLUTE — a relative path does
   [ -x "$LC" ] || { echo "linkcheck not executable: $LC"; exit 1; }  # not resolve from the KB root
   run() {                       # $1 = output file
     local rc=0
     "$LC" "$KB" "$POLICY" > "$1" || rc=$?
     # THREE-WAY LIVENESS INVARIANT. `rc` ALONE CANNOT TELL A DEAD CHECKER FROM A CLEAN ONE:
     # under `set -e`, a command that cannot be EXECUTED (lost +x, bad interpreter, wrong path)
     # arrives as rc=1 — identical to "broken links found", the expected state on any real KB —
     # and it prints NOTHING, so before/after are both empty and `diff` is clean. Hollow green.
     # The invariant closes it: exit 1 MEANS "links found", so exit 1 with EMPTY output is a
     # self-contradiction and proves the checker never looked.
     if   [ "$rc" -gt 1 ];                        then echo "linkcheck FAILED (exit $rc)"; exit 1
     elif [ "$rc" -eq 1 ] && [ ! -s "$1" ];       then echo "linkcheck exit 1 but produced NO output — the checker is not looking"; exit 1
     fi
   }
   run /tmp/links-before.txt     # BEFORE the mutation
   # ... execute the mutation ...
   run /tmp/links-after.txt      # AFTER
   diff /tmp/links-before.txt /tmp/links-after.txt    # must be empty
   ```
   **Two traps, both proven live.** (1) `|| rc=$?` is load-bearing: exit 1 ("broken links found") is the EXPECTED state on any real KB, and under `set -e` that status kills the function before `rc=$?` runs — the gate aborts on SUCCESS, before the mutation. (2) **A status check alone is not enough**: a checker that cannot RUN also arrives as 1 under `set -e` and prints nothing, so `diff` of two empty files is clean and the gate CERTIFIES A TREE IT NEVER LOOKED AT. Only the emptiness invariant above catches that. This is the hollow green the whole skill exists to kill, and it shipped inside the skill's own flagship link gate.
   **CHECK THE EXIT STATUS — 2 is not 0.** A checker that fails to RUN (no `python3`, bad root, missing policy file) exits 2 and prints NOTHING. Two empty files `diff` clean, so a naive recipe reports a green gate while the checker never looked. That is the hollow green this skill exists to kill, and it is easiest to commit in your own gate. `0` = clean · `1` = broken links found · `2` = the checker is broken. The same trap applies to `symcheck.sh`: on a KB whose baseline is empty, a symcheck that dies also "equals the baseline".
   Scope it to the whole affected tree, never to the one file that prompted it — a check scoped to a single file passes while its siblings stay broken.
   **A delta gate baselined on a git ref can only compare TRACKED content.** The baseline is a clean checkout; your working tree also holds gitignored files. Every pre-existing dead link in a gitignored tree therefore shows up as NEW — a false RED that is indistinguishable from real breakage. Exclude gitignored non-content trees from the delta (`!` policy lines), or take the baseline from the same tree you are checking. (Found post-merge on a live KB: the gate went RED on main over a years-dead link in a private gitignored directory the baseline could not contain. Nothing had broken.)
   **Negative-control at least one gate:** break one instance deliberately, confirm the gate goes RED, restore. A gate never observed failing is not known to work. And re-run the final scan in a FRESH process — a scanner bug must never be able to self-certify.
9. **Record.** Run report per SKILL.md § Output. **Stage every change** — the moved files, every ref fix, and any manifest you CREATED (a new manifest is untracked; `git mv` alone stages only the rename, so a commit made without staging ships the move with none of its fixes). Commit message: what moved where, hits found / fixed / left-historical counts, symlinks retargeted.

## Re-nest warning

Highest symlink risk of the three: changing ancestor depth breaks every relative symlink crossing the changed chain — anywhere in the tree, with zero text change. The whole-tree symcheck delta is the only reliable catch. Never scope symcheck to the moved subtree.

## Failure modes this playbook exists to catch

| # | Failure | Caught by |
|---|---------|-----------|
| 1 | Refs in hidden dirs skipped by plain search | refscan `--hidden` (step 2) |
| 2 | Refs in gitignored files skipped by plain search | refscan `--no-ignore` (step 2) |
| 3 | INDEX manifest rows never identified as inbound referencers | manifest hint (step 2) + both-ends obligation (step 6) |
| 4 | Plain content refs missed (headers, prose links) | full-tree fixed-string scan (step 2) + residue check (step 8) |
| 5 | Symlink resolution breakage, invisible to text search | raw + RESOLVED target pass (step 2) + whole-tree symcheck delta (step 7) |
| 6 | Over-fixing historical/append-only citations | verdict log (step 3) + residue == leave-set, not zero (step 8) |
| 7 | Relative-literal refs (`./x.md`, bare filename in a row) that never contain the full path | mandatory basename alias scan (step 2) |
| 8 | Case-variant refs live on case-insensitive filesystems | `REFSCAN_ICASE=1` alias pass (step 2) |
| 9 | One invalid policy regex silently disabling all policy hints | refscan fails fast, exit 2 (script contract) |
| 10 | Superstring / same-name false positives from alias scans | `not-a-ref` verdict, logged (step 3) |
| 11 | Moved node's own parent-pointer (upstream line-1 comment) names the old parent without the old path text | third manifest obligation (step 6) |
| 12 | Location-dependent relative links inside a moved node (outward `../`; same-dir sibling links on file moves), zero text change | moved-content relative-link sweep (step 6) + symcheck for the symlink analog (step 7) |
| 13 | Stem-derived companions (snapshots, sidecars) carry no old-path text; gitignored ones invisible to `git status` | companion obligation (step 6) |
| 14 | A rewritten ref that still does not RESOLVE — relative form keeps its own `../` depth, which the path rewrite never touches | resolution test (step 5) + **`scripts/linkcheck.sh`** delta gate (step 8) |
| 15 | The OLD parent's manifest row cites the child by bare name, so the full-path scan never hits it | mandatory basename alias scan (step 2) + both-ends obligation (step 6) |
| 16 | A hit frozen on a manifest row's prose DESCRIPTION when its class column says otherwise | read the CLASS column (step 3; classification rule 2) |
| 17 | A manifest edited but its own freshness stamp left stale, defeating the KB's staleness sweep | manifest-freshness obligation (step 6) |
| 18 | The run's own FIXES re-introduce the old path and read as residue | classification § Self-reference (step 8) |
| 19 | Not-KB-content trees (nested checkouts, vendored dirs, agent scratch) flood the hit list with phantoms | refscan prunes nested checkouts + vendor dirs; workspace non-content trees via a `!` policy line |
| 20 | A commit that ships the move without its ref fixes (new manifests untracked; `git mv` stages only the rename) | stage-everything (step 9) |
