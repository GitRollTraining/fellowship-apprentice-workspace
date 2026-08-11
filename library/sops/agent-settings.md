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
| `permissions.deny` | writes under `library/` | The library is ours and read-only. `CANON.md` provenance is decoration if anyone may edit what it hashes |
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

The plugin install is interactive and cannot be scripted. Run these in a live session, one at a time,
and confirm each loads before the next:

```text
/plugin install skill-builder
/plugin install planning-with-files
/plugin install superpowers
/plugin install ralph-specum
```

What each is for, and which taught domain it serves, is in `reference/tool-inventory.md`.

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
