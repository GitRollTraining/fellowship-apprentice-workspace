# AI Fellowship — apprentice workspace

The workspace an AI Fellowship apprentice works in. Clone it, and you have the directory structure for
a client engagement, the curated agent skills, the playbooks, the personas and the working standards —
already in place.

**Two halves, and the difference matters.**

| Half | Who owns it |
|---|---|
| `engagements/` | You. Everything you produce for a client goes here |
| `library/` | GitRoll. Read-only. `CANON.md` records where every file came from |

## Start here

1. Read `CLAUDE.md` — how to work in this repository.
2. Read `library/sops/working-standards.md` — the four rules.
3. Run `library/playbooks/playbook-interview.md` with its runbook wrapper on your first engagement.

## Setup

```bash
git clone <this repo>
cd <this repo>
ls -l .claude/skills          # should resolve to ../library/skills
```

Then install the four plugins — the install is interactive and cannot be scripted. Commands and reasons
are in `library/sops/agent-settings.md`.

## A note on `scripts/canon-check.sh`

It answers "has anything moved upstream since this library was cut?" — a question for whoever maintains
the library, on a machine that has GitRoll's source repositories checked out. Run on your own machine it
prints `GONE` for every vendored file, which means "the source is not here", not "the source was
deleted". You are not the audience for it.

## Status

First cut, 2026-08-11. Every layer is present and thinly populated on purpose: one worked playbook, four
stubs, five skills, one persona. It is built to be extended, and what each extension must contain is
written down rather than assumed.
