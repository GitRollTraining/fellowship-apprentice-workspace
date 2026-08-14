---
style: descriptive
---

# Terminology

Defined terms, each in plain words. **Define a term; never rename it.** Substituting a friendlier
synonym does not remove a lookup — it creates a translation problem between this document and every
other document in the programme.

| Term | What it means |
|---|---|
| **fellow** | The apprentice on the programme. The programme thesis says "apprentice" in places; they are the same person |
| **engagement** | One client, one relationship, start to end. The unit of work and the unit of filing |
| **domain** | A named area of capability the curriculum covers. Written `D-01` through `D-35`, and not every one is taught |
| **competency** | Something a fellow can be watched doing on a real task, producing an artifact you can point at |
| **playbook** | A procedure the fellow runs repeatedly, across engagements. Ours are the worked examples |
| **deliverable** | One SOP for one business process, written for one client. Same artifact type as a playbook, different audience |
| **skill.md** | The agent-executable form the deliverable takes. What the business receives and installs |
| **persona** | A role an agent takes for one job, defined precisely enough that two people invoking it get the same behaviour |
| **provenance** | Where a file came from and the hash it was at when it was copied |
| **assessment engine** | The instrument that grades a fellow's work at a gate. Not the same as the validator playbook, which checks before every ship |

## Workspace identifier prefixes

These are workspace conventions, not universal standards. `US` and `AC` are familiar product and
requirements shorthand; the other prefixes are short forms chosen for this workspace. Their meaning is
scoped to the artifact named below. Preserve the identifier when another artifact cites it, and do not
reuse a retired identifier for a different statement.

| Prefix | Meaning | Used for | Why these letters |
|---|---|---|---|
| `D-` | Domain | Programme capability areas in this file and `serves` metadata | **D**omain |
| `H` | Heard | Direct evidence rows in `interview/discovery-record.md` | **H**eard from the owner or source |
| `C` | Conclusion | Fellow-derived rows in `interview/discovery-record.md` | **C**onclusion drawn from cited evidence |
| `X` | Possible exception | A named exception with no datable instance yet in `process/exceptions.md` | `X` marks an unverified e**x**ception candidate |
| `B` | Boundary | Human-approval, non-automation and information-boundary rows in `process/boundaries.md` | **B**oundary |
| `F` | Failure mode | Observed current-state failure rows in `process/failure-modes.md` | **F**ailure mode |
| `US-` | User Story | User stories in `spec/requirements.md` | **U**ser **S**tory |
| `R-` | Requirement | Goals, requirements, business rules and constraints in `spec/requirements.md` | **R**equirement |
| `AC-` | Acceptance Criterion | One observable condition used to accept a user story or requirement in `spec/requirements.md` | **A**cceptance **C**riterion |
| `OQ-` | Open Question | Material unresolved questions in `spec/requirements.md` | **O**pen **Q**uestion |
| `HC-` | Handoff Claim | Material owner-facing claims mapped to authoritative sources in `verification/handoff-source-map.md` | **H**andoff **C**laim |
| `EW-` | Engagement Workspace decision | Decisions about the Fellow's engagement workspace in `decision-register.md` | **E**ngagement **W**orkspace |
| `DP-` | Deliverable Package decision | Decisions about what the client handoff may contain in `decision-register.md` | **D**eliverable **P**ackage |
| `DR-` | Deliverable Runtime decision | Decisions about the installed deliverable's data and system boundaries in `decision-register.md` | **D**eliverable **R**untime |
| `AA-` | Automation Approach decision | Decisions about lifecycle, runtime, integration, credentials and controls in `decision-register.md` | **A**utomation **A**pproach |

The numbering shapes are intentionally inherited from their artifact schemas: discovery and process
records use `H1`, `C1`, `X1`, `B1` and `F1`; the PRD and Decision Register use zero-padded forms such as
`US-001`, `AC-001` and `EW-001`; handoff claims use `HC-001` onward. Do not silently convert one style
into the other.

## The domains this programme teaches

Seventeen of the twenty-seven defined domains are taught. The rest are deferred or ruled out, and a tool
justified by one of those is a tool for something nobody is learning.

| Taught | |
|---|---|
| D-01 | Agent operating model |
| D-02 | Context engineering |
| D-03 | Agent autonomy calibration and gating |
| D-04 | AI evaluation methodology |
| D-05 | AI output verification and failure-mode literacy |
| D-06 | Specification writing for AI delegation |
| D-09 | Deterministic guardrail engineering |
| D-12 | Operating-environment literacy |
| D-21 | Interview framing |
| D-22 | Non-directive questioning |
| D-23 | Past-instance evidence |
| D-24 | Process reconstruction in context |
| D-25 | Answer-directed follow-up |
| D-26 | Grounding and confirmation |
| D-27 | Coverage and boundary elicitation |
| D-28 | Traceable synthesis |
| D-29 | Owner handover explanation |

**Not taught, and why it matters:** D-07 and D-08 are deferred, D-10 and D-11 are out, D-30, D-33 and
D-34 are deferred, D-31, D-32 and D-35 are out. D-13 to D-20 do not exist — the numbering is deliberately
disjoint so the technical and communication halves can be read side by side.
