<!-- upstream: engagements/INDEX.md -->
---
style: descriptive
---

# example-client

## Purpose

An empty engagement directory shape. Environment Setup copies it to the client slug, then creates
`notes.md`, `decision-register.md` and, once running, `progress-log.md` from the shared templates.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `interview/` | Everything from talking to the owner | Mutable |
| `process/` | What you reconstructed from it | Mutable |
| `spec/` | The signed PRD, automation decision brief and specification under construction | Mutable |
| `deliverable/` | The agreed deliverable; one `skill.md` is the default shape | Mutable |
| `handover/` | The owner's own account of it | Mutable |
| `verification/` | Internal validation reports, manifests and permitted evidence; excluded from the client package | Mutable |

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| all six | 2026-08-15 | Mutable | empty; root control files are created after copying |

## Where the interview playbook's steps land

`library/playbooks/playbook-interview.runbook.md` maps all twenty-one steps to the applicable work areas.
Read it before the first session, not after.
