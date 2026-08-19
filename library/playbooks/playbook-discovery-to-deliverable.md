---
style: descriptive
role: playbook
status: draft — authored, not yet run on a client engagement
serves: D-06, D-28
---

# Discovery to Deliverable

Use this playbook after the owner has confirmed the current-state process and before implementation
begins. It turns confirmed discovery into a signed-off product requirements document (PRD), tests those
requirements against a proportionate automation approach, produces the technical specification, and
builds the agreed deliverable.

The common deliverable in this workspace is one `deliverable/skill.md`. That is a default, not a
constraint. The agreed solution may contain multiple skills, scripts, integrations, services or a larger
system. This playbook preserves the same evidence, decision and review chain regardless of delivery
shape.

## What this playbook does not claim

No Fellow has run this procedure on a client engagement. The rules below make artifact ownership,
traceability and stage gates explicit; they are not evidence that following the procedure improves a
solution. Record the first real run before changing that claim.

This playbook does not conduct the discovery interview, phrase the stakeholder handoff or itself operate
production access. Those belong to the Interview, Output Phraser and client-authorised deployment work
respectively. It does own the order of the final gates, including operational acceptance, and invokes
the specialised validators rather than asking those playbooks to call one another.

## Required artifact chain

Paths are relative to `engagements/<client-slug>/`.

| Artifact | Authority | Produced or maintained by |
|---|---|---|
| `interview/session-<date>/` | What was recorded or shown | Interview playbook |
| `interview/discovery-record.md` | What was heard, kept apart from what the Fellow concluded | Interview playbook |
| `process/confirmation-<process>-v<n>.md` | The owner's confirmed account of how the process works now | Interview close-out |
| `spec/requirements.md` | The signed-off future behaviour, scope, user stories, requirements and acceptance criteria | This playbook |
| `spec/automation-approach.md` | Detailed technical recommendation, Fellow decision, assumptions and residual risk | `choose-automation-approach` |
| `decision-register.md` | Canonical current position and stage status for engagement decisions | This playbook and every later decision owner |
| `spec/specification.md` | The build contract joining the signed PRD to the technical decisions | This playbook |
| `deliverable/` | The thing the business will operate | The builder selected by this playbook |
| `verification/deliverable-report.md` | Validator A's evidence and verdict for the exact delivery manifest | Validate Deliverable playbook |
| `handover/owner-account.*` and versioned package | The explanation and exact candidate package the owner receives | Output Phraser |
| `verification/handoff-source-map.md` | Internal claim-to-authority and render/package derivation chain | Output Phraser |
| `verification/persona-preflight.md` | Mandatory constrained non-technical-reader result | This playbook invoking the persona |
| `verification/owner-acceptance.md` | The real owner's comprehension and acceptance against exact candidate bytes | This playbook and owner |
| `verification/handoff-report.md` | Validator B's verdict for the comprehension-accepted candidate package | Validate Handoff playbook |
| `verification/operational-acceptance.md` | Client deployment and one independent owner run of the unchanged B-passed package | This playbook, deployment operator and owner |
| `progress-log.md` | When work or a decision changed and why | Every stage, append-only |

The chain is not optional:

```text
session evidence
  -> confirmed current-state process
  -> PRD draft
  <-> automation feasibility and approach
  -> owner-signed PRD
  -> technical specification
  -> deliverable
  -> Validator A pass
  -> owner-facing phrasing and comprehension gates
  -> Validator B pass
  -> client-authorised deployment and independent owner run
  -> handed-over
```

Validator A, Output Phraser, persona preflight, real-owner acceptance, Validator B and operational
acceptance run in that order. Each component owns its specialised work; this playbook owns their order,
invalidation routes and final status transition. No earlier pass permits a later gate to be skipped.

## Who decides what

| Matter | Authority |
|---|---|
| How the business works now | The owner confirms; the session record remains the source |
| Desired behaviour, scope, workaround, business boundary and acceptance result | The owner signs off in the PRD |
| Technical recommendation and implementation design | The Fellow, assisted by `choose-automation-approach` |
| External law, organisational policy, provider limits and tool authorisation | Factual constraints, not preferences either party can silently override |

The skill's recommendation is not the Fellow's decision. The Fellow's decision is not permission to
change a business requirement. When technical feasibility requires a stakeholder-visible workaround,
change the PRD and obtain sign-off before changing the specification.

## Workflow

### 1. Resolve the engagement and check the entry gate

Resolve the workspace root and client slug from the current repository; never invent either. Read
`notes.md`, `decision-register.md`, `progress-log.md`, the discovery record, the reconstructed process,
the boundary and failure-mode files, the ambiguity list, and the latest process-confirmation file.

Do not proceed until all of these hold:

- the current-state process has been confirmed by the owner, synchronously or asynchronously;
- every correction is also a new heard entry in `interview/discovery-record.md`, with a durable pointer
  to the confirmation session, comment or returned document;
- the confirmation file names its version, date, owner role and source;
- no still-open discovery ambiguity could change the process trigger, steps, business rules,
  boundaries, failure behaviour or definition of done; and
- the Decision Register has no `open` decision required before the current stage.

If the process is not confirmed, return to the Interview runbook. Do not turn an unconfirmed
reconstruction into requirements.

### 2. Draft PRD v1

Use `library/templates/requirements-gathering.md` to create `spec/requirements.md`. The PRD describes
what the future solution must accomplish, not how it will be implemented. It includes the problem and
desired outcome, stakeholders and roles, scope, user stories, requirements, constraints, representative
acceptance cases and open questions.

Normalising the owner's words into a user-story or requirement shape may change grammar, not substance.
Every material clause retains its origin. Do not turn a usual practice into a rule, a hoped-for benefit
into a guaranteed outcome, or a vague quantity into a number.

Use these identifiers:

- `US-001` onward for user stories;
- `R-001` onward for requirements and constraints;
- `AC-001` onward for acceptance criteria; and
- `OQ-001` onward for open questions.

`library/reference/terminology.md` defines these and the other cross-artifact prefixes in one place.

The first draft remains `draft`. Owner sign-off happens only after the feasibility pass below.

### 3. Run the automation feasibility and approach pass

Invoke `choose-automation-approach` with the PRD draft, confirmed process, boundaries, failure modes and
current Decision Register in context. Do not ask the Fellow to repeat information already on disk. Save
the decision brief to `spec/automation-approach.md`.

At the top of the saved engagement brief, add an **Engagement basis** section naming the exact
`spec/requirements.md` version and status, current-state confirmation version, Decision Register review
date, preparer and review date. The reusable skill owns the analysis shape; this playbook owns these
engagement-specific provenance fields. Update them whenever the brief is revised.

Treat this first pass as provisional. Its purpose before PRD sign-off is to find material conflicts such
as an unavailable operation, an unacceptable data crossing, an unsupported runtime assumption or a
human approval that the proposed workflow removed.

Route each new question by what kind of truth would answer it:

| Question type | Record it in |
|---|---|
| A missing or contradictory fact about how the business works now | `interview/ambiguities.md`; resolve it with the owner and add the answer to the discovery record |
| A choice about desired behaviour, scope or an acceptable workaround | `spec/requirements.md`, under Open questions |
| A technical implementation, runtime, integration or credential decision | `spec/automation-approach.md` and the corresponding Decision Register row |

If a workaround changes what a user does, sees, approves or receives, revise the PRD. A workaround that
exists only in the automation brief has not been accepted by the owner.

### 4. Decide which questions block which gate

Every PRD open question names one of `PRD sign-off`, `specification`, `build`, `deploy` or `none` in its
`Blocks before` field.

A question blocks the specification when its answer could change scope, a user story, acceptance
behaviour, a business rule, the delivery shape, a required input or output, a data boundary, a human
approval point, runtime, access method or basic feasibility.

A question may remain open only when its answer cannot change the current component contract and a later
stage owns the decision. For example, the final name of a client-owned OAuth credential may wait until
deploy; its owner, permission model, storage mechanism and revocation path may not remain unknown if they
affect the design.

### 5. Obtain owner sign-off on the PRD

Give the owner the PRD version that includes every stakeholder-visible workaround from the feasibility
pass. The owner signs off business behaviour, scope, boundaries and observable acceptance results — not
the Fellow's implementation preference.

Record the decision, owner role, date and a durable source in the PRD. A reply, document comment or
recorded confirmation is sufficient; an unrecorded verbal yes is not. Update corrections in the source
chain before marking the PRD `signed-off`.

A signed-off PRD version is immutable. If a later technical finding changes a signed requirement, copy
forward to the next version, mark the old one superseded, obtain sign-off again and retain the earlier
version or its durable change record.

### 6. Finalise the automation approach and synchronize engagement state

Re-run or revise the automation approach if PRD sign-off materially changed its inputs. It is stable
enough for specification when:

- the signed PRD version is named in the brief;
- no open question can still change scope, architecture, data flow or approval behaviour;
- delivery shape, runtime, access method and material trust boundaries are at least `provisional`,
  `agreed` or `not-applicable`;
- high-stakes actions and required human approvals are identified; and
- every accepted workaround appears in the signed PRD.

The reusable skill owns the analysis. This playbook owns the engagement-specific synchronization. In
the same working session:

1. Update `AA-001` through `AA-005`, plus any affected `DP-001` or `DR-001` row, in
   `decision-register.md`.
2. Record the Fellow's actual decision, not the skill's recommendation.
3. Preserve `open` and `provisional` states; writing a brief does not make a decision agreed.
4. Point `Source` at `spec/automation-approach.md` and carry over a concrete revisit trigger.
5. Append what changed and why to `progress-log.md`.

Keep comparisons and rationale in the brief rather than copying them into the register. Never record a
secret value in the PRD, brief, register or log.

### 7. Write the technical specification

Use `library/templates/specification.md`. The default shape maps to one skill; adapt it when the signed
solution requires more. The specification may choose components and interfaces, but it may not change a
signed business behaviour. A conflict returns to the PRD version-and-sign-off loop.

Maintain this trace chain:

```text
session pointer -> discovery H/C row -> PRD US/R/AC item
  -> specification section -> deliverable component -> verification
```

Technical choices additionally cite the relevant `AA-*`, `DP-*` or `DR-*` decision. The specification's
traceability matrix gives every signed PRD item an explicit disposition and verification target. A
multi-hop pointer is valid only when every hop resolves.

### 8. Build the agreed deliverable

Before invoking a builder, copy only the marked `COPY` blocks from
`library/templates/deliverable-deployment.md` and `library/templates/deliverable-operations.md` into
`deliverable/deployment.md` and `deliverable/operations.md`. Draft the selected runtime, required entry
filename, client roles and whole-bundle install contract from the signed specification and current
decisions. This gives the builder's installation test a real target; fill exact commands, signals and
recovery as implementation makes them knowable.

For the default single-skill shape, invoke `create-skill` with the signed PRD, specification and
Decision Register as its answered build interview, then write `deliverable/skill.md`. Ask the owner or
Fellow only for a genuinely missing build input; do not reopen signed requirements. The build is
transcription from the specification plus target-specific implementation work, not a new requirements
session.

For a larger solution, adapt the same template and inventory the components under `deliverable/INDEX.md`.
The template's larger-system example names the common concerns; this playbook does not attempt to teach
an experienced Fellow how to architect every possible system.

For every delivery shape, complete the canonical operating instructions inside the delivery boundary:

- `deliverable/deployment.md` covers prerequisites, installation, configuration, start, verification,
  upgrade or replacement, rollback and uninstall where applicable; and
- `deliverable/operations.md` covers normal use, monitoring, failure response, recovery, credential
  rotation or revocation, maintenance and escalation.

For a skill, run `create-skill`'s mandatory checklist only after these instructions contain the exact
disposable installation path. For another delivery shape, run its equivalent clean-environment install
check. Never ship the template wrapper or `COPY` markers.

Keep detailed technical choice rationale in `spec/automation-approach.md`. Later handover material may
summarise and point to the two operating files, but must not create a conflicting second authority. Add
a client-runnable smoke or health check when practical and inventory it with the other components.

No deliverable component may introduce new business behaviour. If implementation reveals one, stop and
return to the PRD or technical-decision step that owns it.

### 9. Run adversarial review and dispose every finding

For every delivered agent skill, first run `library/skills/scan-agent-skill/` against the complete
installable unit, including companion scripts and references. Record the scanner version, command,
input hash, report and disposition in `progress-log.md` or permitted verification evidence. A clean
scan is triage, not proof of safety. If the scanner cannot run in the authorised environment, record
`not run`, the reason and the manual inspection used; do not imply it passed.

Run `library/personas/adversarial-reviewer.md` on every delivered skill with its applicable checklist.
The existing persona is specific to `skill.md`; do not claim that it reviewed a service or larger system
it was not designed to inspect.

- Fix every `BLOCKING` finding, then run the reviewer again.
- Write every accepted `NON-BLOCKING` finding to `deliverable/known-defects.md`.
- If a finding exposes a wrong business claim, repair the source chain and re-run the affected stages;
  editing only the deliverable hides the defect.
- Record the review input, date and disposition in `progress-log.md`.

Final behavioural testing belongs to Validate Deliverable (Validator A), not this review.

### 10. Run Validator A

After the structural checks below pass, run
`library/playbooks/playbook-validate-deliverable.md`. That playbook applies the reusable whole-deliverable
review, executes behavioural and operational cases, freezes a content manifest and writes the internal
report under `verification/`.

Do not start owner-facing phrasing unless the latest report says `pass` and its manifest matches the
current `deliverable/` exactly. A blocked result returns to the PRD, specification or build stage that
owns the defect. A later delivery-file change invalidates the pass and requires the affected checks to
run again.

## Structural checks before Validator A

Do not declare this playbook complete until all of the following hold:

- The current-state confirmation and PRD sign-off have durable sources.
- Every PRD `US-*`, `R-*` and `AC-*` identifier is unique and has a source.
- Every signed requirement has an acceptance criterion or an explicit reason one does not apply.
- Every PRD item has a specification disposition: implemented, deferred with owner acceptance, or
  not-applicable with a reason.
- Every specification behaviour points to the PRD, and every PRD pointer resolves to discovery evidence
  or durable owner confirmation.
- Every deliverable component points to a specification responsibility or a named technical necessity.
- No relevant Decision Register row remains `open` past its `Required before` gate.
- `automation-approach.md`, the Decision Register and the signed PRD describe the same current choice.
- Every adversarial-review finding has a disposition.
- `deliverable/deployment.md` and `deliverable/operations.md` describe the canonical operating path.
- The `spec/` and `deliverable/` INDEX files and `progress-log.md` are current.

These checks establish structural consistency, not that the deliverable works. Hand the result to the
Validate Deliverable playbook for behavioural evidence.

### 11. Run Output Phraser

After Validator A passes, run `library/playbooks/playbook-output-phraser.md`. It writes one owner-facing
authoring source, its rendered output where applicable, an internal handoff source map, a plain package
manifest and the versioned candidate archive.

The Phraser may simplify language, order and presentation. It may not change a delivered file or invent
a business claim. A delivery-file change returns to Validator A. An untraceable presentation claim
blocks here until its governing source is corrected or the claim is removed.

The Phraser's exit means `ready for comprehension testing`. It is not a release verdict.

### 12. Run the mandatory non-technical-owner preflight

Start `verification/persona-preflight.md` from `library/templates/persona-preflight.md`, then invoke
`library/personas/non-technical-owner.md` in a fresh context against the client-visible views rendered
from the exact candidate-package documents.

The persona receives only:

- the rendered client-visible material from the candidate package, including canonical deployment and
  operations instructions but excluding invisible comments and anchors; and
- direct `H*` owner statements and later owner corrections, copied with durable pointers into the
  report's Allowed prior knowledge table.

Record each packaged-byte hash, render/export method and supplied-view hash. It must not receive Fellow
conclusions, the PRD, specification, unpresented implementation source or configuration, source map,
Validator reports or prior answers. Record every supplied document and hash, then check that boundary.
A contaminated run is `blocked`, not reusable evidence.

Persona preflight is mandatory but never substitutes for the real owner. On `blocked`, return to Output
Phraser, revise the account or navigation, rebuild the package and run the persona again. Preserve the
old report as superseded; do not edit a failed run into a pass.

### 13. Obtain real-owner comprehension and acceptance

Only after persona pass, start `verification/owner-acceptance.md` from
`library/templates/owner-acceptance.md` and give the real owner the exact candidate version named in the
preflight.

Ask the owner to explain or demonstrate from the package, without prompting:

- what was delivered, its trigger and visible result;
- what it will not do and where a person acts;
- how to distinguish success from failure;
- the first recovery or escalation action;
- where deployment and operations instructions live; and
- who owns credentials, maintenance and ongoing cost.

“Does this make sense?” records agreement, not comprehension. An unrecorded verbal yes is not an
acceptance source. Record the owner's answers, role, date, route and durable evidence pointer.

This is a hard gate. `rejected`, unanswered or materially corrected output returns to Output Phraser
and leaves the engagement `running`. Rebuild the package and repeat both persona and owner checks after
any owner-facing byte changes. A delivery-file change returns further to Validator A.

### 14. Run Validator B and release the package for operational acceptance

After owner `accepted`, run `library/playbooks/playbook-validate-handoff.md` against the unchanged
candidate archive. Validator B verifies Validator A integrity, package inventory and boundary, claim
fidelity, limitation visibility, rendering, comprehension evidence, archive path safety and the final
archive hash.

Route a `blocked` result to the stage that owns it:

| Finding | Return to |
|---|---|
| Delivery path or hash differs from Validator A | Build and Validator A |
| Owner-facing claim or navigation is wrong | Output Phraser, persona and owner |
| Persona context or result is invalid | Persona, then owner if owner-facing bytes changed |
| Owner acceptance does not match exact bytes | Real-owner check |
| Archive-only assembly or boundary defect | Output Phraser package assembly, then affected comprehension gates |

Validator B `pass` makes the unchanged package release-ready for the deployment and independent-owner
run below. It does **not** by itself change engagement status to `handed-over`. Record the package path,
hash, owner acceptance and B report in `progress-log.md` before leaving this stage.

### 15. Deploy with client authority, obtain operational acceptance and transition status

Start `verification/operational-acceptance.md` from
`library/templates/operational-acceptance.md`. An authorised client operator follows the packaged
`deliverable/deployment.md` in the intended client runtime. The owner then completes one safe,
representative run from the packaged operating instructions without the Fellow taking over or filling
an undocumented gap.

Before extraction, convey Validator B's approved archive SHA-256 through the authorised out-of-band
route named by the deployment contract, such as the delivery message or client portal record. The
operator computes the received archive hash and compares it. Never embed the expected archive hash in
the archive it authenticates.

Use the exact package and B-report hashes. Do not change package bytes during this check and never put
secret values in the record. A delivery or canonical-instruction defect returns to Build and Validator
A; an owner-facing or package-only defect returns to Output Phraser and repeats its affected gates; an
environment or authorisation constraint returns to its owning PRD, automation or deployment decision.

Only `accepted` operational evidence for the unchanged B-passed package permits `handed-over`. In the
same working session:

1. update the engagement status in both `notes.md` and the Decision Register;
2. record the package hash, B report and operational-acceptance record in `progress-log.md`;
3. update affected INDEX files; and
4. confirm the retention, revocation, delivery and ongoing-ownership positions.

The status update records an already-proven transition; it does not create the proof. A package that
was merely sent, explained or validated is not yet handed over under this workspace contract.

## Stop conditions

Stop and report rather than filling a gap when:

- the owner has not confirmed the current-state process;
- a material claim has no source;
- a conclusion is being promoted to a requirement without owner confirmation;
- a feasibility workaround changes stakeholder-visible behaviour but is absent from the signed PRD;
- an open question has reached the gate it blocks;
- a signed PRD and the current automation decision contradict each other;
- a requested action would cross a data, credential or authorisation boundary; or
- a blocking review finding remains unresolved;
- Validator A or its manifest no longer matches the candidate;
- a material handoff claim has no authoritative source;
- persona preflight is blocked or used prohibited context;
- real-owner acceptance is missing, rejected or tied to different bytes; or
- Validator B is not a current `pass` for the final package hash; or
- client deployment or the independent owner run is rejected, missing or tied to different bytes.
