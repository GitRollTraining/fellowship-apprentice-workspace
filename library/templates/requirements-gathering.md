---
style: descriptive
role: template
produces: engagements/<client-slug>/spec/requirements.md
---

# Product requirements document

This is the PRD-like requirements document for an engagement. It turns an owner-confirmed current-state
process into the future behaviour, scope, user stories, constraints and acceptance results the owner is
prepared to sign off. The filename remains `requirements.md`; the document type and stakeholder-facing
title are Product Requirements Document.

It does not choose the implementation. `choose-automation-approach` tests the draft for feasibility and
records technical analysis in `spec/automation-approach.md`. Any workaround that changes what a user
does, sees, approves or receives comes back here before sign-off.

## When it is written

Write PRD v1 after the owner has confirmed the reconstructed current-state process and before the final
specification. Run the first automation-approach pass on the draft, revise it for accepted workarounds,
then obtain owner sign-off. `library/playbooks/playbook-discovery-to-deliverable.md` owns the sequence.

## Where it goes

- File: `engagements/<client-slug>/spec/requirements.md`.
- Add or update its row in `engagements/<client-slug>/spec/INDEX.md` in the same operation.
- Keep restricted client information inside its permitted boundary. Record a requirement or restriction,
  not a secret value or prohibited source content.

## Source and status rules

Use `H1`, `H2` and so on for heard rows in `interview/discovery-record.md`; use `C1`, `C2` and so on for
the Fellow's marked conclusions. A `C*` source may appear in a draft, but it cannot reach a signed PRD
unless the owner confirms it. Preserve the original source and record the durable sign-off that accepted
the version.

Use these PRD identifiers:

- `US-001` onward — user stories;
- `R-001` onward — requirements and constraints;
- `AC-001` onward — acceptance criteria (each `AC` is one **A**cceptance **C**riterion); and
- `OQ-001` onward — open questions.

The canonical glossary for these and the source-record prefixes is
`library/reference/terminology.md`.

Normalising a statement may change grammar, not substance. Do not add a frequency, threshold, deadline,
guarantee or priority the owner did not state or sign off.

Statuses are `draft`, `signed-off` and `superseded`. A signed-off version is immutable. When a material
requirement changes, bump the version, preserve the earlier version or durable change record, and obtain
sign-off again.

## Template

```markdown
---
style: descriptive
client: <client-slug>
process: <the process in the owner's words>
status: draft
version: v1
built-from: process/confirmation-<process-slug>-v<n>.md
automation-approach: not run
updated: YYYY-MM-DD
---

# <Business> — Product Requirements Document — <process>

**Status:** draft | signed-off | superseded
**Version:** v<n>
**Current-state confirmation:** `process/confirmation-<process-slug>-v<n>.md`, confirmed YYYY-MM-DD
**Automation feasibility:** not run | `spec/automation-approach.md`, reviewed YYYY-MM-DD

## Problem and desired outcome

| Field | Statement | Source |
|---|---|---|
| Problem to solve | <what is costly, slow, fragile or unavailable today> | <H#, confirmed-process step or durable owner confirmation> |
| Desired outcome | <what should be different for the business> | <source> |
| Why now | <the event or constraint that makes this worth doing now, or not established> | <source> |

## Current-state reference

- **Process:** `process/process-<name>.md`
- **Confirmation:** `process/confirmation-<process-slug>-v<n>.md`
- **Boundaries:** `process/boundaries.md`
- **Failure modes:** `process/failure-modes.md`
- **Open discovery ambiguities:** <none that block this PRD | IDs and paths>

Do not reproduce the current process here. Name the confirmed sources and describe only the change this
PRD requests.

## Stakeholders and operating roles

| Role | Uses, approves, receives or maintains | Need or concern | Source |
|---|---|---|---|
| <role, not person> | <relationship to the future workflow> | <what must be true for this role> | <source> |

## Goals and success measures

| ID | Goal | Observable success measure | Source |
|---|---|---|---|
| R-001 | <business result> | <what the owner can observe without the Fellow present> | <source> |

## Scope

| In scope | Source |
|---|---|
| <process slice, user or outcome> | <source> |

| Out of scope | Source |
|---|---|
| <explicit exclusion> | <source> |

## User stories

Use the form `As a <role>, when <situation>, I want <capability or outcome>, so that <business result>`.
The form is authored; every business claim inside it still needs a source. Do not force boundaries,
retention rules or system constraints into user-story grammar.

| ID | User story | Importance | Source | Acceptance criteria |
|---|---|---|---|---|
| US-001 | As a <role>, when <situation>, I want <capability>, so that <result>. | required / desired / deferred / not established | <source for every material clause> | AC-001, AC-002 |

## Functional requirements and business rules

| ID | Requirement or rule | Applies to | Source | Acceptance criteria |
|---|---|---|---|---|
| R-002 | <one testable statement; no implementation method> | <US-* or process step> | <source> | <AC-*> |

## Operational, data and boundary requirements

| ID | Requirement or constraint | Source | Acceptance criteria |
|---|---|---|---|
| R-003 | <availability, volume, retention, approval or data boundary, only as established> | <source> | <AC-* or reason not applicable> |

Include, where relevant:

- what must never be automated and who must approve before which action;
- what information may not leave the business, who may see output and what must be retained;
- time and volume as observed or explicitly required, never guessed;
- what the business must do if the deliverable is wrong; and
- periods when the owner or operator is unavailable.

## Current environment and dependencies

This section establishes feasibility inputs, not the chosen technical design.

### Systems access

| System | Read, write or both | Data or operation | Current access or export | Source |
|---|---|---|---|---|
| <system> | <read/write> | <part of the data or operation> | <available / not established> | <source> |

### Information and representative samples

| Information | Where it lives | Form and representative sample | History needed | Source |
|---|---|---|---|---|
| <source> | <system, file or paper> | <one safe representative sample or where it can be inspected> | <period or not established> | <source> |

Ask for a representative sample, not bulk data. Bulk comes later only if the specification proves it is
needed and the boundary permits it.

### Tools, subscriptions and operating environment

| Dependency | Current plan or environment | Relevant capability or restriction | Owner | Source |
|---|---|---|---|---|
| <tool, machine, account or contract> | <known value or not established> | <export, automated access, location or policy> | <role> | <source> |

### People to consult

| Role | What they can establish | Needed before |
|---|---|---|
| <role> | <access, rule, data or approval they own> | <PRD sign-off / specification / build / deploy> |

## Acceptance criteria and representative cases

Each criterion describes an observable result, not a preferred implementation. Include at least one
normal case, one relevant exception and one failure or missing-input case.

| ID | Given | When | Then | Covers | Source |
|---|---|---|---|---|---|
| AC-001 | <starting state or representative input> | <trigger or action> | <observable right result> | <US-* and R-*> | <source> |

## Assumptions and accepted workarounds

| Item | Status | Effect on users or scope | Source / decision |
|---|---|---|---|
| <assumption or feasibility workaround> | unconfirmed / owner-accepted | <none, or the visible change> | <source or `spec/automation-approach.md` plus sign-off> |

An unconfirmed assumption that changes behaviour is an open question, not a requirement.

## Open questions

`Blocks before` takes one of `PRD sign-off`, `specification`, `build`, `deploy` or `none`.

| ID | Question | Owner | Blocks before | Status | Resolution source |
|---|---|---|---|---|---|
| OQ-001 | <one material unknown> | <role> | <controlled value> | open / resolved / deferred | <source or —> |

## Owner sign-off

The owner confirms future behaviour, scope, boundaries, accepted workarounds and observable acceptance
results. This is not approval of the Fellow's technical implementation preference.

| PRD version | Owner role | Decision | Date | Durable confirmation source |
|---|---|---|---|---|
| v1 | <role> | signed-off / changes requested | YYYY-MM-DD | <recording pointer, returned document, email or comment> |
```

## Before marking the PRD signed-off

- The current-state process has an owner-confirmed version and every correction is represented in the
  discovery record.
- Every `US-*`, `R-*` and `AC-*` ID is unique and has a source.
- Every required user story and requirement has observable acceptance coverage.
- No `C*` conclusion has become a signed requirement without owner confirmation.
- The first `choose-automation-approach` pass has run, and every stakeholder-visible workaround is in
  the PRD.
- No open question whose `Blocks before` is `PRD sign-off` remains open.
- The owner confirmed the exact version, and the role, date and durable source are recorded.
- No secret or prohibited client content appears in the document.
