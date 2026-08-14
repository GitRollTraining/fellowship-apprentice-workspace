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
3. Run `library/playbooks/playbook-environment-setup.md`, then run
   `library/playbooks/playbook-interview.md` with its runbook wrapper on your first engagement.
4. After current-state confirmation, run `library/playbooks/playbook-discovery-to-deliverable.md`. It
   owns PRD sign-off, automation choice, build, both validators, owner-facing phrasing, comprehension
   gates and final handoff. The Output Phraser invokes the renderer for the owner account.

## Setup

```bash
git clone <this repo>
cd <this repo>
ls -l .claude/skills          # should resolve to ../library/skills
```

Then install the four plugins — the install is interactive and cannot be scripted. Commands and reasons
are in `library/sops/agent-settings.md`.

## Status

First cut shipped 2026-08-11; the automation-approach skill was added 2026-08-13, and the security-scan
wrapper and complete Environment Setup draft followed on 2026-08-14. Every layer remains thinly
populated on purpose: five authored playbook drafts with no remaining stubs, eleven skills and two
personas. Only Environment Setup has had a disposable structural smoke test; none of the full engagement
chain has been run by a Fellow with a real owner. It is built to be extended, and evidence limits are
written down rather than assumed.
