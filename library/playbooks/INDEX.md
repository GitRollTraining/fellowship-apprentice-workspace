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
| `playbook-elicitation-to-sop.md` | **STUB** | Specified, not written |
| `playbook-validator.md` | **STUB** | Specified, not written |
| `playbook-output-phraser.md` | **STUB** | Specified, not written |

Three stubs remain. Environment Setup is the first stub promoted to a complete draft. Its file and gate
transitions have been checked in a disposable copy; no Fellow has run it on a client engagement, so it
does not claim real-world validation.

## A warning about the word

"Playbook" means two incompatible things in GitRoll's repositories. In this workspace it means
engagement-bound guidance or procedure. In the cross-programme curriculum standard it is a self-serve
reference document for a subject the course does not teach — content only, no steps. Material written
for one sense is wrong for the other, and the conflict has never been reconciled.
