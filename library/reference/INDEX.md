<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# library/reference

## Purpose

GitRoll's own cross-engagement material: the defined terms, the curated tool cut, and the doctrine the
shipped skills route to. It sits inside `library/` rather than in the writable `reference/` because a
definition anyone can silently edit is not a definition, and a tool cut anyone can silently edit is not
a cut.

Everything here is hashed in the provenance record and denied to writes by `.claude/settings.json`.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `terminology.md` | The defined terms, each in plain words. Define them, never rename them | Instruction |
| `tool-inventory.md` | Every skill, plugin, persona and MCP server that is in, what it serves, and why the rest are out | Instruction |
| `skill-architecture.md` | The skill-authoring standard. `create-skill` loads it, and the fellow's own deliverable is graded against it | Instruction |
| `agent-quality-guidelines.md` | Runtime principles the shipped skills route to | Instruction |
| `explanation-style.md` | The explanation register. `explain` routes to it and copies none of it | Instruction |

The last three are vendored from GitRoll's doctrine repository because five shipped skills instruct the
agent to read them. Before this round they were pointed at and not shipped, so every one of those
instructions resolved to nothing.

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| three unchanged references | 2026-08-11 | Instruction | first cut; provenance recorded per file |
| `terminology.md` | 2026-08-15 | Instruction | engagement artifact identifier prefixes defined; provenance updated |
| `tool-inventory.md` | 2026-08-13 | Instruction | automation-approach skill added; provenance updated |

## Where the apprentice's own reference material goes

`reference/` at the repository root — writable, yours, and not hashed.
