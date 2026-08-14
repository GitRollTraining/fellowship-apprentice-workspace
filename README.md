# AI Fellowship — apprentice workspace

The workspace an AI Fellowship apprentice works in. Clone it, and you have the directory structure for
a client engagement, the curated agent skills, the playbooks, the personas and the working standards —
already in place.

**Two halves, and the difference matters.**

| Half | Who owns it |
|---|---|
| `engagements/` | You. Everything you produce for a client goes here |
| `library/` | Ours. Read-only: read it, run it, copy from it, do not edit it |

## Start here

1. Read `CLAUDE.md` — how to work in this repository.
2. Read `library/sops/working-standards.md` — the four rules.
3. Run `library/playbooks/playbook-interview.md` with its runbook wrapper on your first engagement.
4. When the work is written, follow `library/renderers/make-the-handover-file.md` — it turns your
   markdown into the one file the owner opens.

## Setup

```bash
git clone <this repo>
cd <this repo>
ls -l .claude/skills          # should resolve to ../library/skills
```

Then install the four plugins — the install is interactive and cannot be scripted. Commands and reasons
are in `library/sops/agent-settings.md`.

## Status

First cut shipped 2026-08-11; the automation-approach skill was added 2026-08-13 and the security-scan
wrapper on 2026-08-14. Every layer remains thinly populated on purpose: one worked playbook, four stubs,
eleven skills, one persona. It is built to be extended, and what each extension must contain is written
down rather than assumed.
