---
style: descriptive
role: SOP
serves: D-03, D-09
---

# Agent settings

What is configured in this workspace, and why each setting exists. The live file is `.claude/settings.json`
at the repo root; this file is the reasoning behind it, which a JSON file cannot carry.

## The two ideas behind every setting here

**Deterministic guardrail engineering [D-09].** A rule an agent is asked to remember is a rule that
drifts. A rule enforced by a hook, a permission or a file check is a rule that holds. Prefer the second
whenever the check is mechanical.

**Autonomy calibration and gating [D-03].** Autonomy is not a dial you set once. It is set per action
class: reading is free, writing inside the engagement is free, anything that leaves the machine is
gated.

## Settings, and the reason for each

| Setting | Value | Why |
|---|---|---|
| `permissions.allow` | read/search tools, and writes under `engagements/` | The fellow's own work is theirs to write without asking |
| `permissions.ask` | anything that leaves the machine — network posts, sends, deploys | An unsupervised first engagement must not be able to email a client by accident |
| `permissions.deny` | writes under `library/` | The library is ours and read-only. Its provenance record is decoration if anyone may edit what it hashes |
| MCP base set | Notion, Google Drive, Chrome | Where a small business's documents and tools actually live |
| MCP per-engagement | Slack, Gmail, Calendar | Real but not universal, and each needs the client's own credentials. Ship the instructions, not the connection |
| MCP documented, not enabled | computer-use | Genuinely relevant to desktop automation and too sharp for an unsupervised first engagement. It needs a per-session human grant; enabling it by default trains the fellow to click through the grant |

## The MCP servers are NOT configured by this repository, and that is not an omission

There is deliberately no `.mcp.json` here. Notion, Google Drive, Gmail, Calendar and Slack are
**account-level connectors** — you authorise them in your own Claude account, and they then appear in
every project you open. Chrome is a browser extension, and `computer-use` ships with the desktop
application. None of the six is a project-scoped server, so a `.mcp.json` naming them would be a file
that configures nothing while looking like it configures something.

Check what you actually have connected:

```bash
claude mcp list
```

**The rule that matters more than the mechanism:** a connector you enable is authorised with *someone's*
credentials. On an engagement it must be the client's, obtained by the client, and revocable by the
client when the engagement ends. Never connect a client's workspace through a GitRoll account, and never
connect your own personal account to a client's data.

A project-scoped `.mcp.json` is still the right place for a server the *client* runs — a local database,
an internal tool with a stdio server. Create it at the repo root when an engagement needs one, and keep
credentials in the environment, never in the file.

## Installing the plugins

The install is interactive and cannot be scripted. **Two plugins, one of which lives in a third-party
marketplace that has to be added first.** Run these in a live session, one at a time, and confirm each
loads before moving on:

```text
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files

/plugin install plugin-dev@claude-plugins-official
```

Codex and Copilot CLI install the same plugins with `codex plugin add` and `copilot plugin install`.

**Three plugins were removed from this list on 2026-08-23 and should not be re-added without a
decision.**

`superpowers` is a drag on current harnesses, and the ten skills it was listed for are engineering
practice — test-driven development, subagent-driven development, dispatching parallel agents — for an
audience this programme defines as having no technical background.

`ralph-specum` was here for one skill, `interview-framework`. `library/playbooks/playbook-interview.md`
covers the same ground with the programme's own questions.

`skill-creator` duplicates the house `create-skill` for the part an apprentice needs, and its own
addition — an eval harness, benchmarking with variance analysis, description tuning — is 485 lines and
seventeen files including seven Python scripts. That is scale tooling. What the assessment asks for is
the skill run against real data and observed, which is an execution record, not an eval loop.

## Which skills earn each plugin

A plugin installs as a unit, so installing one gets you everything inside it. These are the skills
that earned the install. Anything else that arrives with them is not part of this toolbox, and you
are not expected to use it.

| Plugin | Skill | What you do with it |
|---|---|---|
| `planning-with-files` | `planning-with-files` | Keeps the engagement's state on disk across days |
| `claude-plugins-official` | `skill-development` | The reference for what a `SKILL.md` must contain |
| `claude-plugins-official` | `agent-development` | How to install a persona as a subagent, which this repository asks you to do |
| `claude-plugins-official` | `mcp-integration` | How to author a project-scoped `.mcp.json` for a server the client runs |
| `claude-plugins-official` | `command-development` | How to give the owner a simple explicit trigger for the finished automation |

## One thing you cannot install, and it is not your fault

There is a tool that packages a finished skill into an installer a non-technical owner double-clicks.
It lives in a private repository, and the marketplace-add returns 404 for anyone outside the
organisation that owns it. It is therefore not part of this toolbox.

What you do instead: ship the exact validated delivery tree in the versioned handoff zip, with the
owner account, package manifest and canonical `deployment.md` and `operations.md`. For an agent skill,
the deployment instructions install the whole bundle into the client's runtime — including companion
references/scripts — and name its required runtime entry filename. Do not hand over one flattened
`skill.md` and assume it is installable. Keep the manual installation step and its owner visible in the
handoff and prove it during operational acceptance.

## Making the skills visible to the agent

The curated skills live in `library/skills/`, which is where provenance can guard them. Claude Code
looks in `.claude/skills/`. The repo ships a symlink so both are true at once:

```bash
ls -l .claude/skills     # -> ../library/skills
```

On a filesystem without symlinks, copy instead — and re-copy after every `git pull`, or the library and
what the agent loads will silently disagree:

```bash
cp -R library/skills .claude/skills
```
