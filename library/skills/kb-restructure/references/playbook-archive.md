# Playbook — archive (1→archived)

Detailed steps for engine phases 2–9 when the operation is ARCHIVING: retiring content whose central thesis is dead or dormant, by relocating it into the host KB's archive container.

**Archive is not a move with a different destination.** The ref-mapping differs, and four of the 1→1 playbook's standing obligations INVERT. Read § Divergences before reusing any rename-playbook habit.

## Ref-mapping (1→archived)

| Element | Mapping |
|---|---|
| Live inbound refs | Re-point to the SUCCESSOR if one exists; otherwise keep the ref and add a supersession note (`[ARCHIVED: date, reason, superseded-by: path?]`). A ref with no successor is not deleted — a reader following it must land somewhere that explains the retirement. |
| The archived body | **Never rewritten.** Header tag only. Its internal path citations become frozen history the moment it is archived. |
| Old parent manifest row | **ANNOTATED, not removed** — the row records that the content existed and where it went. |
| Archive container manifest | A BATCH manifest is CREATED (host KB's convention — often a README, not the per-directory manifest file). |
| The archived node's own parent-pointer | **NOT repointed** (see § Divergences D3). |

## Divergences from the 1→1 playbook (each cost a real run)

- **D1 — The parent manifest row is annotated, not repointed.** A move says "the row follows the content." An archive says "the row records the retirement." Removing it erases the fact that the content ever existed at that location, which is the one thing a reader six months later needs.
- **D2 — The destination manifest is a BATCH manifest, not a directory manifest.** Archive containers group by batch (a dated, reason-slugged directory), and host KBs typically manifest a batch with a README carrying thesis + date + inventory + decision record — not with the ordinary per-directory manifest file. Read the host KB's existing batches and MATCH them; do not impose the 1→1 playbook's "create a manifest" reflex.
- **D3 — The archived node's own parent-pointer is NOT repointed.** The 1→1 playbook repoints it at the new parent. That is WRONG here: an archived manifest is part of the frozen record, and its pointer preserves where the content lived. Verify against the host KB's existing batches — if archived manifests there still name their pre-archive parent, preserve yours. (Confirmed on live content: the 1→1 reflex would have falsified the record.)
- **D4 — The body is frozen, but its OUTBOUND relative links still break.** Archiving usually changes ancestor depth (content descends into a dated batch directory). Every relative link INSIDE the archived content silently mis-resolves, with zero text change — and "never rewrite the archived body" appears to forbid fixing them. It does not: a link target is not body content. Recompute relative depth (rule below) while leaving prose, figures, and claims untouched. This is the single most-missed archive defect.

**D4 rule.** "Never alter an Immutable body" governs CLAIMS, not link RESOLUTION. Rewriting `../x` → `../../x` so it still resolves preserves the record; leaving it broken destroys it. Fix the depth; change nothing else. Record the link-depth fixes in the batch manifest so the edit is auditable.

## Steps

1. **Preflight.** As the 1→1 playbook (clean tree, scope statement, policy patterns, symcheck baseline). Additionally: read the host KB's EXISTING archive batches and record their conventions — batch-slug format, batch-manifest filename and shape, whether archived manifests keep their pre-archive parent-pointer (D3), whether a dormant batch carries a separate revival guide.
2. **Confirm the thesis is actually retired.** Archive is for retired/dormant content, not for content that is merely old or inconveniently placed. Relocating misplaced-but-LIVE content is a `move`, not an archive — dispatch the 1→1 playbook instead. If the host KB requires human approval for directory-level archiving, the engine FLAGS and stops; it does not decide.
3. **Discover.** Alias-form refscans exactly as the 1→1 playbook (full path always; basename always; ICASE / extension-less / URL-encoded per the host KB). Union the hit lists.
4. **Classify.** Verdict-log every hit per `classification.md`. One extra question per LIVE hit that the 1→1 playbook never asks: **does a successor exist?** Re-point live refs to the successor; where there is none, the fix is a supersession NOTE, not a re-point. Log which of the two each live hit gets.
5. **Execute.** History-preserving move into `{archive-container}/{batch-slug}/`, preserving the content's original relative layout below the batch directory. Add the `[ARCHIVED: date, reason, superseded-by?]` header to each archived file — header only, body untouched.
6. **Fix live refs** per step 4's re-point-or-note decision. Append-only operative records take append-fixes (never rewrite existing lines).
7. **Standing obligations** — none of these ever appears in the hit list:
   - Old parent manifest row → **ANNOTATE** (D1).
   - Batch manifest → **CREATE** per the host KB's convention (D2): thesis, date, reason, inventory, decision record, and any deliberate skips (e.g. Immutable bodies whose stale citations were deliberately left).
   - Archived node's own parent-pointer → **PRESERVE** (D3).
   - Stem-derived companions (sync snapshots, gitignored sidecars) travel WITH their main file. See § Companions.
   - **Outbound relative links inside the archived content** → recompute for the new depth (D4), then RESOLUTION-TEST each one.
8. **Symlink pass.** Whole-tree symcheck; delta against the preflight baseline must be empty.
9. **Verify.** Residue == logged leave-set. Every rewritten ref RESOLUTION-TESTED (a rewritten link is not a working link — see the 1→1 playbook's step-8 resolution gate). Plus the archive-specific gates:

Each gate is a COMMAND a fresh agent can run — not a description of one. `{area}`, `{batch}`, `{base-ref}` are yours to fill.

| # | Gate | Method |
|---|------|--------|
| 0a | **Decision record complete** | One row per decision unit; every verdict in the allowed set; every protected unit carries the protected verdict. A batch whose decision record is missing rows is a batch nobody can audit — and the rows you forgot are exactly the ones you did not think about. |
| 0 | **Protected paths still live** | `test -d` / `test -f` every path you promised NOT to touch. Run it FIRST — the cheapest way to catch a mutation that ran wider than its scope. |
| 1 | Live path vacated | `test ! -e {area}/{old-path}` |
| 2 | Batch complete | every archived unit present under `{area}/.archive/{batch}/` at its preserved relative path |
| 3 | File conservation | `git diff --name-status -M {base-ref}...HEAD` → renames only, **zero `D` entries** |
| 4 | No husk directories | snippet below — a directory left holding only a manifest and nothing else |
| 5 | No ignored-file leak | `leak="$(git diff --name-only {base-ref}...HEAD \| git check-ignore --stdin || true)"; [ -z "$leak" ]` — **`git check-ignore` exits 1 when NOTHING is ignored**, i.e. on the PASSING case, so a bare pipeline under `set -e` aborts on success. Capture the output and test it empty. |
| 6 | Headers + batch manifest | `[ARCHIVED]` header on every archived file; batch manifest present; Immutable bodies unaltered below the header |
| 7 | **Links resolve** | `scripts/linkcheck.sh <kb-root> <policy-file>` — compare against the pre-mutation baseline; the delta must be EMPTY (D4). **Status alone is NOT enough.** A checker that cannot RUN arrives as exit 1 under `set -e` (identical to "links found") and prints nothing, so a naive diff of two empty outputs reports clean. Assert the invariant: exit 1 MUST come with non-empty output, or the checker never looked. Use an ABSOLUTE path and an `[ -x ]` precheck. Covers both the archived content's own outward links and every inbound ref you rewrote. **A git-ref baseline compares TRACKED content only** — exclude gitignored trees from the delta or their pre-existing dead links all read as NEW. |
| 8 | Refs | `scripts/refscan.sh` per alias form → residue == the logged leave-set, set-equality both directions |

```bash
# Gate 4 — husk directories. TWO traps, both shipped live at least once:
#  1. `</dev/null` on the inner command: a command inside a read-loop that reads stdin EATS THE LOOP'S
#     OWN INPUT. (But NEVER put it on the loop's own input pipeline — that feeds the loop /dev/null and
#     silently disables it. Guard the commands INSIDE the loop, never the pipe feeding it.)
#  2. `if` — NOT `[ "$n" -eq 0 ] && echo ...`. A trailing AND-list makes the LOOP's exit status the
#     LAST iteration's test, i.e. "was the final directory a husk?" — so under `set -e` a normal tree
#     (last dir not a husk) returns 1 and KILLS THE GATE SCRIPT, skipping every check after it.
#     A gate that aborts on success is as useless as one that certifies on failure.
find {area} -type d -not -path '*/.archive/*' | while IFS= read -r d; do
  n=$(find "$d" -mindepth 1 -maxdepth 1 -not -name 'INDEX.md' </dev/null | wc -l | tr -d ' ')
  if [ "$n" -eq 0 ]; then echo "HUSK: $d"; fi     # NOT `[ ] && echo` — see below
done
```

**Negative-control at least one gate per run:** break one instance deliberately, confirm the gate goes RED, restore. **A gate never observed failing is not known to work** — and a gate that cannot fail is not a gate. Assert the POSITIVE end state, not merely the absence of the old string: "the parent row no longer names the old path" is satisfied by DELETING the row, which is failure mode 1. Compare SETS against a baseline measured on the SAME tree, never counts against a baseline from a different one.

## Links vs provenance strings (a blanket repoint corrupts the record)

Not every occurrence of an archived path is a link to fix. Distinguish:
- **Links** — a reader clicks them and expects to land somewhere. Repoint them.
- **Bare provenance strings** in citations ("sourced from `{path}`", a source column, a footnote) — they record WHERE a claim came from at a moment in time. A KB with several dated batches will contain provenance strings pointing into OLDER batches, and a blanket find-and-replace silently re-resolves them into the NEW batch. The citation then attributes a claim to a document it never came from. **That is corruption of the record, not a fix.**

Where provenance strings are numerous, leave them and add ONE banner to the containing doc explaining where paths of that era now resolve. One banner beats a hundred rewrites, and it cannot mis-attribute.

## Companions

A gitignored sidecar named from its main file's stem is a COMPANION and travels with it — the main file's reconstruction pointer breaks otherwise. This does NOT license touching a standalone confidential tree that merely happens to be gitignored: that is separate content with its own lifecycle, out of scope for any mutation of an unrelated file. The test is derivation, not ignore-status: does this file's NAME derive from the moved file's stem, or does the host KB declare it a companion? Yes → it travels. No → leave it where it is.

## Dormant vs dead

When the thesis is "de-prioritized, revival possible" rather than "disproven", the batch needs a second manifest — a REVIVAL guide — beside the inventory: what is in the batch, which parts are evergreen vs snapshot-stale (names, numbers, dates, org charts, regulatory citations all expire), the extraction pattern (copy out, strip the archived header, re-verify, re-file — never edit in place), and where any content that stayed live now lives. Cold-read it with a fresh agent before shipping: if a reader who has seen nothing else cannot re-enter the work from it, it is not done.

## Delegation

A scheduled archive sweep keeps DETECTION (what needs archiving) and ORCHESTRATION (cadence, batching, human approval gates, isolation, the PR). It delegates per-item EXECUTION to this playbook and carries zero copied procedure. Consumer skills reference this skill BY NAME, never by file path — plugin extraction moves paths.

## Failure modes this playbook exists to catch

| # | Failure | Caught by |
|---|---------|-----------|
| 1 | Parent manifest row deleted, erasing that the content ever existed | D1 / step 7 |
| 2 | Directory manifest imposed on an archive batch that wants a batch manifest | D2 / step 1 convention read |
| 3 | Archived manifest's parent-pointer repointed, falsifying the frozen record | D3 / step 7 |
| 4 | Relative links inside archived content silently mis-resolve after the depth change | D4 / step 7 + gate 7 |
| 5 | "Never rewrite the body" misread as "leave broken links" | D4 rule |
| 6 | Live refs blanket-repointed into the archive when a successor exists | step 4 successor question |
| 7 | Live refs with NO successor left dangling | step 4 supersession note |
| 8 | Archived body edited beyond the header tag | gate 6 |
| 9 | Live-but-misplaced content archived instead of moved | step 2 |
| 10 | Directory-level archive auto-executed without human approval | step 2 |
| 11 | Husk directory left behind | gate 4 |
| 12 | Delete+recreate instead of a history-preserving move | gate 3 |
| 13 | A green gate that never looked (scanner self-certifying) | step 9 negative control |
