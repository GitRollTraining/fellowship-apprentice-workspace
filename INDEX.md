---
style: descriptive
---

# AI Fellowship apprentice workspace — catalog

## Purpose

The working repository for one AI Fellowship apprentice: the structure for client engagements, and the
curated library of skills, playbooks, personas and standards they work with.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `CLAUDE.md` | How to work in this repository. Read first | Instruction |
| `README.md` | What this is, and setup | Instruction |
| `.claude/settings.json` | Permissions and autonomy gating. Reasoning in `library/sops/agent-settings.md` | Data |
| `engagements/` | Your work, one directory per client | Mutable |
| `training/` | Your work from before you have a client: coursework, exercises, practice | Mutable |
| `library/` | Ours, read-only. Playbooks, skills, personas, SOPs | Instruction |
| `reference/` | Terms, the tool inventory, worked examples | Mutable |

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| `library/` | 2026-08-11 | Instruction | first cut |
| `engagements/example-client/` | 2026-08-11 | Mutable | empty example, safe to delete |
| `training/` | 2026-08-11 | Mutable | empty until Stage 1 starts |
| `reference/` | 2026-08-11 | Mutable | first cut |

## Conventions

Set out in `CLAUDE.md`. In short: `library/` is read-only, every directory carries an `INDEX.md`,
`UPPERCASE.md` means a workflow requires the file, and client material lives under `engagements/` so it
can be deleted as a unit.
