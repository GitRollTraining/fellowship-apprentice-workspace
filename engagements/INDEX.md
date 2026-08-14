<!-- upstream: INDEX.md -->
---
style: descriptive
---

# engagements

## Purpose

One directory per client engagement. This is the unit of work: an engagement starts, it ends, and it
belongs to one client — so it is filed as a unit and can be deleted as a unit when the relationship ends.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `example-client/` | An empty engagement with the five subdirectories in place. Environment Setup copies it, then creates the engagement's notes and decision register | Mutable |

## The five subdirectories, in the order the work happens

| Directory | What lands there |
|---|---|
| `interview/` | Transcripts, session notes, the pre-session note, the discovery record, the ambiguity list |
| `process/` | The reconstructed process, its boundaries, its exceptions, what happens when it breaks |
| `spec/` | The specification under construction |
| `deliverable/` | The agent-executable `skill.md` the business receives, and its known-defects list |
| `handover/` | The owner-facing account, in the owner's own vocabulary |

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| `example-client/` | 2026-08-14 | Mutable | empty directory template; root control files are created per engagement |

## Conventions

Directory name is the client slug in kebab-case. Nothing about one client goes in another client's
directory, and nothing shared across clients goes in either — that belongs in `reference/`.
