# AI Fellowship — apprentice workspace

The tools and the working structure an AI Fellowship apprentice uses for the whole program, as one
plugin for your coding agent. Install it once; then, in every repository you work in, one skill sets
up the folder your work goes in, with the rules your agent follows there.

**Two halves, and the difference matters.**

| Half | Where it is | Who owns it |
|---|---|---|
| The plugin: skills, playbooks, personas, standards, templates (`library/`) | installed in your coding agent | Ours. Read-only: read it, run it, copy from it, do not edit it |
| `apprentice-workspace/`: engagements, training, reference | in each repository you work in | You. Everything you produce goes here |

## Start here

1. **Install the plugin** in your coding agent — commands below. You do not clone this repository.
2. **Open your agent in the repository you work in** and start `onboarding` the first time, or
   `setup` in every repository after that. Either one creates `apprentice-workspace/` there.
3. Read `apprentice-workspace/AGENTS.md` — how to work in the workspace — and
   [`library/sops/working-standards.md`](library/sops/working-standards.md), the four rules.
4. Run [`library/playbooks/playbook-environment-setup.md`](library/playbooks/playbook-environment-setup.md),
   then run [`library/playbooks/playbook-interview.md`](library/playbooks/playbook-interview.md) with its
   runbook wrapper on your first engagement.
5. After current-state confirmation, run
   [`library/playbooks/playbook-discovery-to-deliverable.md`](library/playbooks/playbook-discovery-to-deliverable.md). It
   owns PRD sign-off, automation choice, build, both validators, owner-facing phrasing, comprehension,
   operational acceptance and final handoff. The Output Phraser invokes the renderer for the owner
   account.

Starting a skill: in the ChatGPT app, type `@` and pick it; in Claude Code, type
`/apprentice-workspace:` and its name, for example `/apprentice-workspace:setup`.

## Install

**ChatGPT desktop app (Codex).** Open the app's plugin screen, choose to add a plugin marketplace, and
enter:

```text
GitRollTraining/fellowship-apprentice-workspace
```

Then install `apprentice-workspace` from that marketplace and start a new chat.

**Claude Code:**

```bash
claude plugin marketplace add GitRollTraining/fellowship-apprentice-workspace
claude plugin install apprentice-workspace@fellowship-apprentice-workspace
```

**Codex command-line tool:**

```bash
codex plugin marketplace add GitRollTraining/fellowship-apprentice-workspace
codex plugin add apprentice-workspace@fellowship-apprentice-workspace
```

Then install the plugins `library/sops/agent-settings.md` lists; `onboarding` walks you through it.

## Updating

| Agent | Update |
|---|---|
| ChatGPT app | upgrade the marketplace from the plugin screen, then start a new chat |
| Claude Code | `claude plugin marketplace update fellowship-apprentice-workspace`, then `claude plugin update apprentice-workspace@fellowship-apprentice-workspace`, then restart |
| Codex command-line tool | `codex plugin marketplace upgrade fellowship-apprentice-workspace` |

Updating never touches `apprentice-workspace/` in your repositories: that folder is yours. After an
update, start `setup` again in each repository you work in: it adds anything new, offers to replace
the rules file `apprentice-workspace/AGENTS.md` if yours is older than the plugin's, and changes
nothing else.

## Already cloned this repository?

The clone keeps working as it is. Do not pull it: the folders you wrote in have moved, so a pull
can stop with a conflict. To switch: install the plugin, start `setup` in the repository where you
work, and move anything you wrote under the clone's `training/`, `engagements/` or `reference/` into
the same place under that repository's `apprentice-workspace/`. Then the clone can go.

## What is in the plugin

Every skill in `library/skills/`, including all 23 skills the cloned workspace had; none was left
out. `setup` is new: it creates `apprentice-workspace/` in the repository you are in. The list with
what each is for: `library/skills/INDEX.md`, or ask `workspace-help`.

## Status

First cut shipped 2026-08-11; the automation-approach skill was added 2026-08-13, and the security-scan
wrapper and complete Environment Setup draft followed on 2026-08-14. The workspace became an
installable plugin on 2026-09-26. Every layer remains thinly populated on purpose. Only Environment
Setup has had a disposable structural smoke test; none of the full engagement chain has been run by a
Fellow with a real owner. The workspace is built to be extended, and evidence limits are written down
rather than assumed.
