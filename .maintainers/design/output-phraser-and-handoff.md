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
comprehension. Validator B proves the final package is faithful, complete and safe. Only Validator B may
advance the engagement to `handed-over`.

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

## Final gate ownership

`library/playbooks/playbook-discovery-to-deliverable.md` owns this order:

```text
Validator A pass
  -> Output Phraser candidate package
  -> mandatory non-technical-owner persona preflight
  -> real owner comprehension and acceptance
  -> Validator B pass
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
engagement. The first real run must retain persona misses, owner questions, Validator B findings and
revision count. Those observations decide whether the checklist should become a skill or the system
needs a different boundary.
