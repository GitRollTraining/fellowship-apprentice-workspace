<!-- upstream: library/reference/INDEX.md -->
---
style: descriptive
---

# library/reference/setup-reading

## Purpose

Copies of the material the onboarding checklist tells an apprentice to read, so an agent can answer
"what is version control?" or "what is entire.io?" from programme material instead of searching the
public web. Every file here is a mirror of something authored elsewhere; the original always wins.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `version-control-systems.md` | What a version control system is and why developers use one. Mirror of a third-party course note, GNU General Public License v3 | Immutable |
| `git-and-github.md` | Git and GitHub in practice — repositories, commits, branches, remotes. Mirror of a third-party course note, GNU General Public License v3 | Immutable |
| `entire-io-session-logging.md` | Installing and enabling Entire so AI sessions are captured. Mirror of the programme's own Notion page, plus one recorded open question about the ChatGPT desktop application | Immutable |

The fourth checklist reading topic, the Codex application manual, is deliberately **not** here. It is
marked internal and this repository is public, so apprentices reach it through Google Classroom
instead. The routing for all four topics is `library/skills/onboarding/references/reading.md`.

## Conventions

- **A mirror is never edited.** Editing one makes it a fork nobody is tracking, and `library/` is
  read-only in any case. If a mirror is wrong or stale, re-cut it from its source and record the new
  hash in `.maintainers/CANON.md`.
- Each file states its source URL, the date it was taken, and its licence in a block at the top.
  Keep that block if you quote the file elsewhere.
- The two third-party notes are shared under the GNU General Public License, Version 3, from
  `github.com/bloombar/knowledge-kitchen`. They are mirrored unmodified and kept as separate files,
  which is the form that licence permits for an aggregate.

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| `version-control-systems.md` | 2026-08-22 | Immutable | first cut; unmodified mirror |
| `git-and-github.md` | 2026-08-22 | Immutable | first cut; unmodified mirror |
| `entire-io-session-logging.md` | 2026-08-22 | Immutable | first cut; carries one open question on the ChatGPT desktop application, unresolved |
