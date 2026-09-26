---
style: descriptive
---

# AI Fellowship apprentice workspace — catalog

## Purpose

The source of the `apprentice-workspace` plugin: the curated library of skills, playbooks, personas
and standards an AI Fellowship apprentice works with, and the `setup` skill that creates the
apprentice's workspace folder in any repository.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `README.md` | What this is, how to install it, Start here | Instruction |
| `.claude-plugin/marketplace.json` | The marketplace file both Claude Code and Codex read: one plugin, `apprentice-workspace`, whose skills are in `library/skills/` | Data |
| `library/` | Ours, read-only once installed. Playbooks, skills, personas, SOPs, templates, renderers, reference | Instruction |
| `library/skills/setup/template/apprentice-workspace/` | The workspace folder `setup` copies into a repository: the rules (`AGENTS.md`), `engagements/`, `training/`, `reference/` | Instruction |
| `.maintainers/` | Provenance, cut decisions and high-level library design records | Record |

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| `library/` | 2026-09-26 | Instruction | installable as a plugin; `setup` skill added; skills say where `library/` is |
| `library/skills/setup/template/apprentice-workspace/` | 2026-09-26 | Instruction | the former root `engagements/`, `training/`, `reference/` and `CLAUDE.md`, moved here |
| `.maintainers/` | 2026-09-26 | Record | provenance rows updated for the files this change edited or added |

## Conventions

The workspace rules live in `library/skills/setup/template/apprentice-workspace/AGENTS.md`, which
`setup` copies into each repository. In short: `library/` is read-only, every governed work area
carries an `INDEX.md`, `UPPERCASE.md` means a workflow requires the file, and client material lives
under `engagements/` so it can be deleted as a unit.
