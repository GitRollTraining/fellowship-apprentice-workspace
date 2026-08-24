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
| `deliverable-review-checklist.md` | Shape-independent review surface for finding concrete contract, boundary, operating and evidence defects before Validator A issues a verdict | Instruction |
| `skill-architecture.md` | The skill-authoring standard. `create-skill` loads it, and the fellow's own deliverable is graded against it | Instruction |
| `agent-quality-guidelines.md` | Runtime principles the shipped skills route to | Instruction |
| `explanation-style.md` | The explanation register. `explain` routes to it and copies none of it | Instruction |
| `setup-reading/` | Copies of the four onboarding reading topics, so the agent answers from programme material rather than the public web | Immutable |

The last three are vendored from GitRoll's doctrine repository because five shipped skills instruct the
agent to read them. Before this round they were pointed at and not shipped, so every one of those
instructions resolved to nothing.

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| three unchanged references | 2026-08-11 | Instruction | first cut; provenance recorded per file |
| `terminology.md` | 2026-08-15 | Instruction | engagement and handoff claim identifier prefixes defined; provenance updated |
| `tool-inventory.md` | 2026-08-15 | Instruction | handoff transport, renderer and real-use evidence gaps updated; provenance recorded |
| `deliverable-review-checklist.md` | 2026-08-15 | Instruction | first draft; no client review yet |
| `setup-reading/` | 2026-08-23 | Mixed | two third-party mirrors plus `entire-io-session-logging.md`, authored here since the Notion page was archived; the Codex manual deliberately not mirrored, see its INDEX |

## Where the apprentice's own reference material goes

`reference/` at the repository root — writable, yours, and not hashed.
