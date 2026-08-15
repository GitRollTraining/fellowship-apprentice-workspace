<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# playbooks

Playbooks are guidance and procedures tightly coupled to running an AI Fellowship engagement. They may
assume the engagement stages, workspace structure, required artifacts, stakeholder interactions or
handoff process, and may compose multiple skills. If a procedure remains meaningful and usable without
those engagement assumptions, it belongs under `skills/` instead.

## Inventory

| File | State | What it is |
|---|---|---|
| `playbook-interview.md` | shipped verbatim, **never executed** | Eliciting an undocumented process from the person who runs it. Twenty-one numbered steps |
| `playbook-interview.runbook.md` | authored here | Where each step's output goes in this workspace, and which shipped tool it uses |
| `playbook-environment-setup.md` | authored here, **disposable smoke test only** | Creates or resumes a bounded engagement, initialises its control files and gates safe discovery without deciding the final automation |
| `playbook-discovery-to-deliverable.md` | authored here, **never executed** | Turns confirmed discovery into a signed-off PRD, proportionate automation decisions, a traceable specification and the agreed deliverable |
| `playbook-validate-deliverable.md` | authored here, **never executed** | Validator A: freezes the candidate, reviews it and collects behavioural, deployment and operational evidence against the signed contract |
| `playbook-output-phraser.md` | authored here, **never executed** | Turns the A-passed candidate into a traced, owner-facing account and versioned package without changing delivery behaviour |
| `playbook-validate-handoff.md` | authored here, **never executed** | Validator B: checks that the comprehension-accepted candidate faithfully contains the A-passed deliverable and releases exact bytes to operational acceptance |

No stubs remain. Environment Setup, Discovery to Deliverable, Output Phraser and both Validators are
complete draft contracts. Environment Setup's file and gate transitions passed a disposable smoke test;
the other four have not had even that narrower run. The final orchestration and artifact contracts are
now present, but none has been run by a Fellow on a real engagement or claims outcome validation.

## A warning about the word

"Playbook" means two incompatible things in GitRoll's repositories. In this workspace it means
engagement-bound guidance or procedure. In the cross-programme curriculum standard it is a self-serve
reference document for a subject the course does not teach — content only, no steps. Material written
for one sense is wrong for the other, and the conflict has never been reconciled.
