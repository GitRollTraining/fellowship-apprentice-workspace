# Output Phraser and handoff design record

## Status

- **Components:** Output Phraser, non-technical-owner preflight, handoff source map, owner acceptance,
  package assembly and Validator B integration
- **Type:** locally authored, engagement-bound playbook system
- **Initial design:** 2026-08-15
- **Evidence state:** structurally specified; not yet run on a Fellow or client engagement

## Why this record exists

Writing the Output Phraser exposed inherited instructions that cannot all be true at once. The changes
are therefore design rulings, not editorial cleanup. This record gives reviewers the original conflict,
the chosen resolution and the reason a different inherited instruction changed.

## Conflicts resolved

### 1. Interview close-out versus final handoff timing

**Inherited behaviour:** the Interview runbook sent steps 20 and 21 directly to
`handover/owner-account.md` and `handover/comprehension-check.md`, then said the engagement ended when the
owner opened the final PDF.

**Conflict:** at interview close-out there is no signed PRD, automation approach, specification,
implemented deliverable or Validator A evidence. A document written then can explain only the current
state; calling it the final handoff makes later implementation claims either impossible or invented.

**Ruling:** Interview steps 20 and 21 finish current-state confirmation. The final owner account is
created only after Validator A passes the implemented deliverable. Discovery to Deliverable owns the
complete cross-playbook order.

### 2. Output Phraser verification versus Validator verification

**Inherited behaviour:** the Output Phraser stub required verification or a handoff to Validator, while
the Validator stub also claimed the pre-ship verification responsibility.

**Conflict:** if the Phraser can approve its own readable output, comprehension can be mistaken for
correctness. If both components rerun the same checks, their verdict and invalidation rules can diverge.

**Ruling:** Validator A proves the candidate works. Output Phraser changes presentation and assembles a
candidate package but issues no release verdict. A constrained persona and the real owner check
comprehension. Validator B proves the final package is faithful, complete and safe enough to release to
operational acceptance. Only a later client deployment and independent owner run may advance the
engagement to `handed-over`.

### 3. Concatenated `skill.md` versus an installable deliverable

**Inherited behaviour:** `make-the-handover-file.md` stripped frontmatter from the owner account and one
`deliverable/skill.md`, concatenated both into one markdown file and rendered the result as a PDF.

**Conflict:** the agreed deliverable may be several skills, scripts, services or a larger system. File
structure, executable content and configuration are part of what Validator A passed. Flattening them
into prose destroys installability, can omit sibling files and creates a second stale copy. It can also
move internal comments or configuration into an owner-facing document.

**Ruling:** render only the owner account. Package the exact A-passed `deliverable/` tree beside it,
unchanged. The PDF explains; the delivery files execute. The default transport is a versioned zip, not a
single PDF pretending to be both.

### 4. Canonical operating instructions versus handover prose

**Inherited behaviour:** the handover account was expected to be complete enough for the owner to
operate the skill, while later design work put deployment and operations responsibilities in the
deliverable.

**Conflict:** two complete instruction sets drift. A handover-friendly summary cannot be the technical
authority for install, rollback, recovery or credential rotation.

**Ruling:** `deliverable/deployment.md` and `deliverable/operations.md` are canonical and travel inside
the package. The owner account explains when to use them, who owns each action and where to start; it
does not reproduce them line for line.

### 5. Comprehension simulation versus hidden implementation knowledge

**Inherited behaviour:** no persona contract constrained what a simulated owner could know.

**Conflict:** an agent that can read the specification, source map and implementation can answer gaps
the actual non-technical owner cannot. Such a preflight certifies its context window, not the handoff.

**Ruling:** the non-technical-owner persona sees the candidate owner-facing material plus only direct
owner statements and recorded owner corrections from discovery. It may not read Fellow conclusions,
the PRD/specification, implementation, source map or validation reports. The exact knowledge boundary is
recorded with every run.

### 6. Optional process diagram versus the highest-value confirmation moment

**Inherited behaviour:** the process-confirmation template said a diagram was “worth more” but left its
creation discretionary and the Interview runbook associated flowchart mainly with reconstruction.

**Conflict:** the clearest routine use is when the reconstructed current-state sequence goes back to
the owner for correction. Leaving it as a general suggestion makes the tool easiest to skip at the
moment it is most useful.

**Ruling:** a checked flowchart is the default companion to current-state confirmation whenever the
process has a meaningful sequence, decision, loop or handoff. A Fellow may omit it only with a recorded
reason that the visual would add no relationship the owner needs to inspect.

### 7. Brief-design inventory alias versus the real path

**Inherited behaviour:** `library/templates/INDEX.md` listed both `brief-design.md` and
`brief-design/`, but no `library/templates/brief-design.md` file existed.

**Conflict:** an Output Phraser told to use the first path reaches nothing, while the actual design
system and its `SKILL.md` live under the directory.

**Ruling:** remove the nonexistent alias and retain `library/templates/brief-design/` as the single
inventory entry and invocation path. No compatibility alias is added because nothing valid could have
resolved through the missing file.

### 8. Explanation trigger versus an owner confirming their own process

**Inherited behaviour:** the Interview runbook invoked `explain` when writing the owner's current-state
version.

**Conflict:** the `explain` skill fires when the reader is unfamiliar with a field. The process owner is
the authority on their own process; the confirmation document should make correction easy, not teach
the domain back through an analogy. Applying the explanation register there can introduce narrative the
neutral confirmation template explicitly avoids.

**Ruling:** current-state confirmation uses the plain process-confirmation template and default
flowchart. The final Output Phraser uses `explain` because the owner may genuinely be unfamiliar with the
automation delivery and operating concepts it must make legible.

### 9. Renderer code commentary versus the renderer contract

**Inherited behaviour:** the PDF builder's module documentation said the handover renderer assembled a
document “out of two pieces,” reflecting the old owner-account-plus-`skill.md` concatenation path.

**Conflict:** the executable code renders one markdown input, and the new handoff contract deliberately
keeps the validated `deliverable/` tree intact. Leaving the old description beside the code invites a
future maintainer to restore a lossy packaging behaviour that the runbook now rejects.

**Ruling:** describe the builder as a single owner-account renderer. Its runbook owns build and visual
inspection; the Output Phraser owns client-package assembly.

### 10. Persona context restriction versus client-readable operating documents

**Initial draft:** the persona could read the owner-facing account but prohibited both implementation
and canonical operating files as hidden technical context.

**Conflict:** `deliverable/deployment.md` and `deliverable/operations.md` are canonical precisely because
the client receives and uses them. A simulated owner that cannot follow the account into those documents
does not test the delivered navigation or operating explanation.

**Ruling:** supply and hash every client-readable document in the candidate package, including canonical
deployment, operations, known-defect and client-verification instructions. Continue to prohibit
unpresented implementation source or configuration, the PRD/specification and all internal validation
context. The persona may learn from what the client receives, never from what only the Fellow knows.

### 11. Package validation versus actual operation

**Inherited behaviour:** a Validator B pass plus owner comprehension changed engagement status directly
to `handed-over`, while the status definition said the owner was running the deliverable without the
Fellow.

**Conflict:** reading and accepting a package does not prove its deployment instructions work in the
intended client runtime or that the owner can operate one case independently.

**Ruling:** Validator B releases exact bytes to operational acceptance. A client-authorised operator
deploys those bytes, and the owner completes one safe representative run without the Fellow taking over.
Only an accepted `verification/operational-acceptance.md` permits `handed-over`.

### 12. Authoring filename versus runtime skill entry point

**Inherited behaviour:** `create-skill` wrote engagement output to the already-existing
`deliverable/` directory as lowercase `skill.md`, but its collision check rejected any existing target,
its checklist required uppercase `SKILL.md` under `library/skills/`, and its test assumed direct slash
invocation.

**Conflict:** the scaffold always creates `deliverable/`; lowercase is the content convention, while
common agent runtimes discover uppercase `SKILL.md`. Companion files and workspace-only footer links
also make handing over one markdown file non-installable.

**Ruling:** collision checks apply to intended files, not the scaffold directory. The checklist accepts
an explicit authoring file, and engagement deployment installs the complete delivered bundle under the
target runtime's documented entry name in a disposable environment before reliance.

### 13. Documented commands versus the supported runtime

**Inherited behaviour:** the flowchart render example omitted required arguments; Validator A labelled
a Bash-only `read -d` pipeline as portable `sh`; and Validator B's archive commands omitted the
engagement-relative `handover/` path.

**Conflict:** all three fail when copied literally by a novice. The manifest pipeline could still exit
zero and leave a plausible empty file.

**Ruling:** examples now name every required path. Validator A uses a portable Python manifest builder
that rejects empty candidates, symlinks and paths unsafe for its TSV representation. Runnable examples
are smoke-tested exactly as printed.

### 14. External transcription convenience versus the engagement data boundary

**Inherited behaviour:** the recording skill told the Fellow to supply their own speech-service key and
uploaded the interview without first resolving the workspace data, identity and retention decisions.

**Conflict:** consent to record is not permission to send client audio to any provider or bill it to a
personal account.

**Ruling:** upload is blocked until `EW-001` through `EW-003` permit the provider, authorised identity,
credential storage, retention and deletion route. Credential values remain outside tracked files.

### 15. Recursive INDEX rule versus companion bundles

**Inherited behaviour:** the manifest contract required an INDEX in every directory at every depth,
while shipped skills, session directories and validation evidence legitimately contain nested companion
folders with no separate navigation role.

**Conflict:** literal compliance creates recursive manifest paperwork and contradicts the repository's
own structure; ignoring it leaves a novice unsure which rule matters.

**Ruling:** structural and independently navigated work areas require an INDEX. Companion
implementation, generated, session and evidence directories may be inventoried as a unit by the nearest
governing INDEX or component entrypoint until they become independently navigated.

### 16. Fixed current reports versus immutable evidence

**Inherited behaviour:** validators and comprehension gates write fixed current filenames and advise
preserving superseded reports, but no rule froze the mutable manifest, source map or evidence those old
reports cited.

**Conflict:** archiving only a report makes it appear to refer to a later run's evidence.

**Ruling:** before rerun, snapshot the complete cited run set under a timestamped `verification/history/`
bundle, inventory and hash it, and point the new record's `supersedes` field to the archived record.
Frontmatter is the single canonical verdict in every report.

### 17. Packaged instructions versus the archive's own hash

**Initial draft:** packaged `deliverable/deployment.md` contained a field for the final handoff archive's
expected SHA-256.

**Conflict:** the deployment file is itself inside that archive. Writing the archive hash into one of
its own inputs changes the archive and therefore the hash.

**Ruling:** the package records its version, while Validator B records the final archive hash. The
client receives that expected hash through a trusted out-of-band delivery route and compares it before
extraction; it is never embedded in the archive it authenticates.

### 18. Human-readable skill descriptions versus valid YAML

**Inherited behaviour:** two vendored skills used an unquoted colon-plus-space in their frontmatter
`description` values.

**Conflict:** the sentence reads normally to a person but is invalid YAML, so a strict skill loader can
silently omit `digest-doc` or `interview-recording` exactly when the Interview runbook asks for them.

**Ruling:** quote both complete description values, make the generated skill skeleton quote its
description, and include constrained frontmatter parsing in the pre-pilot structural gate.

### 19. Temporary package copies versus the data boundary

**Inherited behaviour:** the Phraser copied client delivery files into an operating-system temporary
directory and described that directory as disposable, but neither deleted it nor checked whether that
location was authorised.

**Conflict:** a successful zip could leave a second untracked client-data copy outside the engagement
boundary, while a failed or interrupted command would leave it silently.

**Ruling:** resolve the staging location through `EW-001` and `EW-003`, mark it with an ownership
sentinel and install cleanup traps before copying. Residue is a blocking retention event, not harmless
scratch space. Validator B uses the same pattern for extraction.

### 20. Archive-safety claims versus a path-list printout

**Inherited behaviour:** Validator B listed absolute paths, traversal, collisions and residue as
blocking, but its example only ran `unzip -t` and printed filenames.

**Conflict:** neither command fails on every stated policy violation, so a novice could record a clean
run after merely looking at an unsafe path list.

**Ruling:** run a fail-closed path-policy checker before extraction. It rejects non-canonical or
out-of-root paths, duplicates, case collisions, symlinks, hidden residue and empty archives, then uses
sentinel-constrained temporary extraction for the client-visible smoke path.

### 21. Archived reports versus live relative pointers

**Inherited behaviour:** a verification report retained engagement-relative evidence paths after being
copied below `verification/history/`, without defining the root used to resolve them.

**Conflict:** opening an old report could resolve its manifest or source map against the current run,
making historical evidence appear fresh.

**Ruling:** every timestamped bundle is a synthetic engagement root with a hashed
`snapshot-manifest.tsv`. Relative pointers in archived reports resolve only inside that root; a new
record's `supersedes` field names the full archived record path.

### 22. Exact packaged source versus what a client can see

**Initial draft:** the non-technical-owner persona received exact Markdown or HTML package bytes.

**Conflict:** those sources intentionally contain invisible source-map pointers and claim anchors. A
model reading raw bytes sees internal trace context that the client-facing renderer hides.

**Ruling:** pin every packaged source hash, but give the persona only the client-visible view produced
by the intended renderer or application. Record the render method and supplied-view hash; inability to
produce a faithful view blocks the preflight.

### 23. Implementation creation versus rediscovering signed requirements

**Inherited behaviour:** `create-skill` started by interviewing a user and its deployment fields were
filled after the build, even when Discovery already held a signed PRD, approach and specification.

**Conflict:** asking again can drift from signed engagement truth, while generating a skill before
declaring its installation boundary makes the runtime proof circular or incomplete.

**Ruling:** Discovery passes the existing PRD, specification, decisions and open questions as an
accepted build contract instead of re-interviewing. The reusable builder accepts a supplied contract
generically and does not own engagement bookkeeping. Draft deployment and operations constraints first,
build the complete bundle, then fill exact commands and prove installation in a clean disposable runtime.

### 24. Recording consent versus storage and publication classes

**Inherited behaviour:** recorded audio and provider output had generic session paths, while refined
notes could be mistaken for client-safe evidence.

**Conflict:** consent and provider permission do not decide whether raw or derived interview material
may be committed, shared with a client or retained after the engagement.

**Ruling:** keep audio and raw provider output in explicit `*.local.*` paths by default. Classify each
derived artifact through `EW-001`, and record the permitted processor, identity, credential, retention
and deletion decisions before upload or publication.

### 25. Self-contained HTML versus unrecorded network font calls

**Inherited behaviour:** the brief-design base loaded Google Fonts although it was presented as a
single-file client brief.

**Conflict:** opening the handoff could disclose client access metadata, fail offline or silently change
appearance without a dependency decision.

**Ruling:** the base uses a system font stack and makes no external request. A future external asset
requires an explicit dependency and data-boundary decision.

### 26. Presentation status versus engagement status

**Inherited behaviour:** the brief-design example displayed `Handed over` as a decorative default.

**Conflict:** a Fellow could render that label before Validator B or operational acceptance, creating a
client-visible status that contradicted the canonical engagement state.

**Ruling:** examples show package version or candidate state. Only Discovery to Deliverable updates the
engagement to `handed-over` after accepted operational evidence.

## Final gate ownership

`library/playbooks/playbook-discovery-to-deliverable.md` owns this order:

```text
Validator A pass
  -> Output Phraser candidate package
  -> mandatory non-technical-owner persona preflight
  -> real owner comprehension and acceptance
  -> Validator B pass
  -> client-authorised deployment and independent owner run
  -> engagement status: handed-over
```

Child playbooks define their own work and return artifacts or a verdict. They do not call one another or
advance the engagement around the orchestrator.

## Artifact boundaries

| Artifact | Boundary and authority |
|---|---|
| `deliverable/` | Exact client-operated files Validator A passed; canonical implementation, deployment and operations |
| `handover/owner-account.*` | Owner-facing explanation; presentation derived from authoritative sources |
| `handover/package-manifest.md` | Plain inventory placed in the client package |
| `handover/<client>-handover-v<n>.zip` | Default final transport; exact hash is recorded by Validator B |
| `verification/handoff-source-map.md` | Internal claim-to-source map; never packaged |
| `verification/persona-preflight.md` | Internal constrained-reader result; never packaged |
| `verification/owner-acceptance.md` | Internal record of the real owner's result against exact bytes; never packaged |
| `verification/handoff-report.md` | Internal Validator B evidence and verdict; never packaged |
| `verification/operational-acceptance.md` | Internal evidence of deployment and independent owner operation against the unchanged B-passed package; never packaged |

## Source-map pointer

Material owner-facing claims receive `HC-*` identifiers in the internal map. Markdown, HTML and SVG
sources carry an invisible comment pointing to the map and may carry invisible claim anchors. Generated
PDFs are not hand-edited to add metadata: their source file carries the pointer and the map records both
source and rendered hashes. This preserves traceability without showing internal identifiers to the
client.

## Defaults, not universal constraints

- The package is a zip unless the signed specification chooses another transport.
- The owner account is formal markdown-to-PDF for prose and tables, or single-file HTML for a genuinely
  visual one-page brief. Maintain one authoring source, not parallel markdown and HTML copies.
- A future-state diagram is used only when sequence, branching, handoff or recovery is material to owner
  operation. The current-state confirmation diagram has its separate default earlier in the engagement.
- A client-runnable smoke or health check is included when practical; impossibility or disproportionate
  cost is stated rather than hidden.

## Not yet proven

This design resolves document-level contradictions and makes invalidation mechanically checkable. It
does not prove that the persona predicts real-owner comprehension or that the package improves an
engagement. The first real run must retain persona misses, owner questions, Validator findings,
deployment/operation failures and revision count. Those observations decide whether the checklist
should become a skill or the system needs a different boundary.
