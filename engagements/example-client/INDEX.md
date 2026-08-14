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
| `spec/` | The specification under construction | Mutable |
| `deliverable/` | The `skill.md` that is handed over | Mutable |
| `handover/` | The owner's own account of it | Mutable |

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| all five | 2026-08-14 | Mutable | empty; root control files are created after copying |

## Where the interview playbook's steps land

`library/playbooks/playbook-interview.runbook.md` maps all twenty-one steps to files in these five
directories. Read it before the first session, not after.
