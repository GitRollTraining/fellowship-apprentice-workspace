---
name: kb-restructure
description: Rename, move, re-nest, or ARCHIVE a KB file/dir without breaking inbound refs — discover, classify live-vs-historical, execute, fix, verify (split/merge staged). Fire on any structural mutation ask.
argument-hint: "<operation: rename|move|re-nest|split|merge|archive> <target-path> [destination]"
---

# KB Restructure

> Operation-agnostic engine for structural mutations of existing KB content, plus one playbook per operation. Exists because ad hoc sweeps provably miss inbound references (hidden dirs, gitignored files, INDEX manifest rows) and text search cannot see symlink breakage at all. The engine is portable: it hardcodes no workspace paths and reads each workspace's own rename/move policy at preflight.

## Scope guard

- Mechanical structural mutations of EXISTING content only. Taxonomy redesign — new top-level structure, rethinking what goes where — is macro, human-owned (KB SOP principle: human controls macro; agents control micro). If the ask is a redesign, stop and surface it instead of executing. A user-requested mechanical rename/move of one existing node — root-level included — is in scope; redesign means changing the taxonomy's shape, not a node's name or location.
- One mutation per engine run. A follow-up mutation, even minutes later, is a new full run (see Gotchas).

## Inputs

- `<operation>` — `rename` | `move` | `re-nest` | `archive` (FULL) · `split` | `merge` (STUB — engine phase 1 stops on these)
- `<target-path>` — file/dir being mutated, KB-root-relative
- `[destination]` — new path (required for 1→1 operations)

Missing args → ask. KB root = walk up from cwd until the repository root (`.git/`). **Prerequisite: a git-managed KB** — root discovery, the clean-tree gate, history-preserving `git mv`, and the commit record all assume git; on a non-git tree, stop and say so.

## Engine (every operation runs these phases)

1. **Select playbook** — read its declared ref-mapping (table below). Stub playbook → stop and say so; do not improvise the operation.
2. **Preflight** — confirm a git KB (`git rev-parse --show-toplevel`; failure → stop, prerequisite unmet). Require a clean git tree (or the user's explicit acceptance of a dirty baseline). Write a one-line scope statement (what mutates, why). Load workspace policy: search the workspace rules directory (commonly `.claude/rules/`) for its rename/move policy section; extract the historical-pattern list to a temp patterns file for refscan. No policy section → empty list, classification falls to judgment alone. Run `scripts/symcheck.sh <kb-root>` and save the output as the pre-existing-breakage baseline — those breaks are not yours to fix.
3. **Discover** — `scripts/refscan.sh "<needle>" <kb-root> [patterns-file]` over the whole tree, run once per ALIAS FORM of the old path as the needle (full path always; basename always; more per the playbook — a ref that spells the path differently still breaks). Output contract: one hit per line, `path<TAB>hint`, hints `historical | manifest | symlink | content`. Never substitute ad hoc `rg`/`grep` (see Gotchas). Union the hit lists.
4. **Classify** — log a verdict (live | historical | not-a-ref) for every hit per `references/classification.md`. Script hints are suggestions, never verdicts. Log format: path, hint, verdict, one-line rationale.
5. **Execute** — per playbook (`git mv` for 1→1 so history survives).
6. **Fix** — every LIVE hit, per the operation's declared ref-mapping — plus the STANDING OBLIGATIONS that never text-hit the old path: manifests at both ends (where the KB keeps per-dir manifests), the moved node's own parent-pointer, and stem-derived companions (sync snapshots, gitignored sidecars) that move WITH the file. Playbook step 6 enumerates all of them.
7. **Symlink pass** — `scripts/symcheck.sh <kb-root>` over the whole tree, not just the moved subtree. Output must equal the preflight baseline; any new entry is breakage this mutation caused — fix and re-run.
8. **Verify** — re-run refscan on the OLD path (all alias forms): every remaining hit must already be in the verdict log as historical or not-a-ref (residue == logged leave-set exactly; the bar is not zero). Symcheck delta empty. **`scripts/linkcheck.sh` delta empty** — every relative link still resolves; a rewritten ref is not a working ref. Both INDEX ends confirmed. **Never trust a script's exit status alone.** 2 = the checker failed. But a checker that cannot be EXECUTED arrives as 1 under `set -e` — identical to "findings found" — and prints nothing, so empty output reads as clean. Assert the invariant: a non-zero "findings" status MUST come with non-empty output.
9. **Record** — run report (§ Output) + counts in the commit message.

## Playbooks

| Operation | Declared ref-mapping | Status |
|---|---|---|
| rename / move / re-nest | 1→1 — every live ref rewrites old→new; INDEX row moves ends | FULL — `references/playbook-rename.md` |
| split | 1→N — each live ref re-targets the piece that now holds the content it cited; one INDEX row becomes N | STUB — round 02+ |
| merge | N→1 — live refs of every source re-target the merged doc (section anchor where needed); N INDEX rows collapse to one | STUB — round 02+ |
| archive | 1→archived — live refs re-point to the successor or gain a supersession note; the archived body itself is never rewritten; INDEX row annotated, not removed | FULL — `references/playbook-archive.md` |

**Archive is not a move with a different destination.** Four of the 1→1 standing obligations INVERT (the parent row is annotated not repointed; the destination wants a BATCH manifest not a directory manifest; the archived node's own parent-pointer is PRESERVED not repointed; and the frozen body's outbound relative links still must be recomputed). See the archive playbook's § Divergences before reusing any 1→1 habit.

**Archive delegation:** where the host KB has a scheduled archive sweep (in this workspace: `wei-archive-sweep`), that sweep keeps DETECTION (what needs archiving) and ORCHESTRATION (scheduling, batching, human gates). This playbook owns per-item EXECUTION. Consumer skills reference this skill by name, never by file path — plugin extraction moves paths. (The host sweep's NAME is an example, not a dependency: the skill runs unchanged in a KB that has no sweep.)

## Gotchas

- **Plain `rg`/`grep` reports false-clean.** Default search skips hidden dirs and gitignored files, and never reads symlink targets. Correct: `scripts/refscan.sh` only (`--hidden --no-ignore -F` + a symlink-target pass).
- **NEITHER end's manifest reliably produces a text hit.** The new parent's manifest references nothing yet — obviously invisible. But the OLD parent's row is invisible too, because **manifests cite their children by BARE NAME** (`| \`beta/\` | ... |`), which contains no full path. Both live runs proved it: one target's parent manifest referenced it TWICE and the full-path scan returned ZERO manifest hits. Wrong default: fix only discovered hits, trusting the full-path scan. Correct: the mandatory basename alias scan (phase 3) plus the both-ends standing obligation (phase 6) — belt and braces, because this is the single most-missed reference in the KB.
- **A rewritten ref is not a working ref.** Rewriting the path string inside a RELATIVE reference (`](../x/y.md)`) leaves its `../` depth untouched — the ref can be "fixed" and still dead. Correct: resolution-test every rewrite from its own file's directory (playbook step 5).
- **Not-KB-content trees flood the hit list.** A nested git checkout (worktree/submodule: its `.git` is a FILE, so a `.git` glob misses it), a vendored dir, an agent's own scratch tree. On a live KB these were 76% of all hits — every one a phantom duplicate in a tree you must not edit. refscan prunes nested checkouts and vendor dirs automatically; declare workspace-specific non-content trees with a `!` policy line.
- **A green gate that never looked is worse than no gate.** Scope every gate to the whole affected tree (a file-scoped check passes while its siblings stay broken), negative-control at least one (break it, confirm RED, restore), and re-scan in a FRESH process — a scanner bug must never self-certify.
- **A command inside a `while read` loop EATS THE LOOP'S INPUT.** `rg`/`grep` with no path argument searches stdin — which, inside a read-loop, is the rest of your list. The loop exits after one iteration and every remaining item is reported clean. This shipped once and scanned 1 of 25 paths while the gate went green. Defences: always give an explicit path argument, add `</dev/null` to every command inside a read-loop, and prefer the scripts here (which do the walk in one process) over hand-rolled loops. Same hazard with `ssh`, `ffmpeg`, `mysql`.
- **A gate must be able to fail for the thing it names.** Assert the POSITIVE end state (the row exists AND names the new path), not merely the absence of the old string — deleting the row satisfies "absence" trivially. Compare SETS, not counts, against a baseline measured on the SAME tree you are checking. Four gates in this skill's own round-02 validation passed while the failure they named was present.
- **Symlinks break with zero text change.** A re-nest changes ancestor depth; relative targets break silently anywhere in the tree. Correct: whole-tree symcheck, compared against the preflight baseline.
- **Over-fixing is a defect, not thoroughness.** Historical/append-only hits are point-in-time citations; rewriting them falsifies the record. Correct: leave them; verify against residue == historical set.
- **Follow-up mutation = full re-run.** A second move touching the same area needs the entire engine again for the new path — the first run's hit list is stale the moment the tree changes. No incremental shortcut.
- **Machine-regenerated files: never hand-edit.** Sync snapshots, compiled digests — fix the source or let the owning pipeline regenerate; hand-edits break the pipeline's own drift detection.
- **A ref that spells the path differently still breaks.** `./beta/file.md` from a sibling, a bare filename in a manifest row, a case-variant on a case-insensitive filesystem, a line-wrapped path — none contain the full old path string. Correct: alias-form scans per the playbook; the basename scan is mandatory, not optional.
- **Alias scans over-report by design.** A superstring path (`alpha/beta-archive/`) or a same-named different file is not an inbound ref. Correct: verdict `not-a-ref`, logged like any other — never silently dropped, never "fixed".

## Constants

| Key | Value |
|---|---|
| Scripts | `scripts/refscan.sh` (find refs), `scripts/symcheck.sh` (symlinks resolve), `scripts/linkcheck.sh` (relative links resolve) |
| Classification rule | `references/classification.md` |
| 1→1 playbook | `references/playbook-rename.md` |
| 1→archived playbook | `references/playbook-archive.md` |
| Eval baseline | **not shipped in this copy** — see the Eval section |

**symcheck exit codes:** 0 = no broken symlinks, 1 = broken links found, 2 = usage. On any KB with pre-existing breakage it returns 1 on EVERY run — so never wrap it in `set -e` and never read its exit code as the gate. **The gate is the DELTA against the preflight baseline**, not the exit code. (Also: reading the code through a pipe — `symcheck.sh . | tee` — gets you `tee`'s status, not symcheck's.)

## Output

Run report, terse: scope statement · hit table (path / hint / verdict / action) · symcheck delta vs baseline · verify result (residue == logged leave-set: yes/no) · manifest + companion obligations confirmed. Report goes to the requester (chat); counts go in the commit message.

## Eval

**The eval fixtures do not ship with this copy.** Upstream they are a planted fixture, a baseline
output, a runner and a judgment-regression set, all built against GitRoll's own knowledge base. They
were dropped rather than travelled because a fixture that names another organisation's directories
tests nothing here and discloses something.

What this costs you, stated plainly: after any edit to `references/classification.md` there is no
regression set to walk, so a classification change is unverified until someone builds one. Building
that fixture — one planted reference per failure class — is a good first contribution to this library.

## Quality Guidelines

Adhere to the house standards where installed (they live at the user level, not in this skill; on a foreign install without them, skip):
- `library/reference/agent-quality-guidelines.md` (runtime behavior)
- `library/reference/skill-architecture.md` (structural principles)
