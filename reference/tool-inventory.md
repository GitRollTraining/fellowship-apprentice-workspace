---
style: descriptive
---

# Tool inventory

Every skill, plugin, persona and MCP server that is in this workspace, what taught capability it serves,
and why the rest are out.

## How the cut was made

Three tests, applied in this order. Failing any one is out.

1. **Does it serve a domain the curriculum actually teaches?** Seventeen of twenty-seven domains are
   taught; the list is in `terminology.md`. A tool justified by a deferred or ruled-out domain is a
   tool for something nobody is learning.
2. **Is it portable?** No GitRoll-specific destinations, no Notion or roadmap coupling, no personal data.
3. **Can you install it without GitRoll's credentials?**

Starting pool: 51 skills across three scopes, 6 plugins, 10 reachable MCP servers. What survived is below.

## What is in

The block below is the machine-readable cut. Columns: `kind`, `name`, `domains`, `reference`, `why`. A `repo:` reference is a path inside this
repository; `plugin:` and `mcp:` are installed or connected by you, not shipped here.

```tsv
kind	name	domains	reference	why
plugin	skill-builder	D-06,D-29	plugin:gitroll-dev/skill-builder@2.1.0	The deliverable IS a skill.md, and this plugin's packager compresses a skill directory into a .skill archive a non-technical owner installs through the desktop application. That is the handover problem solved, in-house and already working
plugin	planning-with-files	D-02	plugin:planning-with-files	Task state written to files and re-injected each turn. Context engineering made concrete, and an engagement spans days
plugin	superpowers	D-06,D-04	plugin:superpowers	The brainstorming to writing-plans to writing-skills chain is spec-before-build, which is what specification writing for AI delegation asks for, plus its verification-before-completion discipline
plugin	ralph-specum	D-05	plugin:ralph-specum	Multi-layer completion verification that never trusts a self-report. That is output verification and failure-mode literacy, exactly
skill	wei-create-skill	D-06	repo:library/skills/wei-create-skill	Loads the skill-authoring standard the fellow's own deliverable is graded against. The playbooks are authored to the same standard
skill	wei-explain	D-29	repo:library/skills/wei-explain	Owner handover explanation is taught, and this is the only skill aimed at explaining to a non-expert. Explanation is a separate genre from a fact-sheet
skill	wei-flowchart	D-24	repo:library/skills/wei-flowchart	A reconstructed process is confirmed by an owner looking at a diagram
skill	wei-digest-doc	D-27	repo:library/skills/wei-digest-doc	Coverage and boundary elicitation means reading what the business already has. Resolves its destinations at runtime, so it travels
skill	kb-restructure	D-02	repo:library/skills/kb-restructure	An engagement directory that grows needs renaming and re-nesting without breaking what points at it. Keeping a workspace navigable is context engineering applied to a filesystem
persona	adversarial-reviewer	D-05,D-06	repo:library/personas/adversarial-reviewer.md	Nobody grades their own work, and a solo engagement has nobody else in the room
mcp	notion	D-27	mcp:claude.ai/notion	Where an engagement's notes and, often, the business's own documentation live. Account-level connector, connected with the client's credentials
mcp	google-drive	D-27	mcp:claude.ai/google-drive	The small-business document reality. Account-level connector, connected with the client's credentials
mcp	claude-in-chrome	D-12	mcp:extension/claude-in-chrome	Operating-environment literacy means seeing the tools the business actually uses, in the browser they use them in
```

## Connected per engagement, not by default

| Server | Why it is not in the base set |
|---|---|
| Slack | Real but not universal. Needs the client's own workspace authorisation |
| Gmail | Same, and the blast radius of a mistake is higher — it can send |
| Google Calendar | Same, and rarely load-bearing for process reconstruction |

Ship the instructions, not the connection. A connector authorised with GitRoll's account against a
client's data is the wrong answer even when it works.

## Documented, deliberately not enabled

| Tool | Why |
|---|---|
| `computer-use` | Genuinely relevant to desktop automation, and it needs a per-session human grant plus native-application access. Too sharp for an unsupervised first engagement, and enabling it by default trains the fellow to click through the grant without reading it |

## Out, and why

| Class | Examples | Reason |
|---|---|---|
| Notion and roadmap coupled | `wei-notion-sync`, `wei-ticket-create`, `wei-ticket-review`, `wei-publish-meeting-actions`, `ray-notion-brief` | Wired to GitRoll's own Notion databases. Nothing to point at from here |
| Meeting pipeline | `wei-process-meetings`, `wei-meeting-prep`, `wei-meeting-summary`, `wei-meeting-plaud` | Runs GitRoll's transcript pipeline against GitRoll's records |
| Our deliverables, not theirs | `wei-deck`, `wei-journey-map`, `wei-web-capture`, `wei-deploy-web` | Producing decks and deploying sites is our job, not a fellow's |
| Repository tooling | `wei-review-pr`, `wei-draft-pr`, `wei-commit-plan`, `wei-techdebt`, `wei-test-and-fix`, `wei-ux-lint`, `wei-codebase-snapshot` | Software-engineering work, which the programme puts outside its stopping point |
| Personal | `wei-disk-cleanup`, `wei-time-tracker`, `wei-youtube`, `wei-linkedin-post` | Nothing to do with an engagement |
| Plugins out | `frontend-design`, `caveman` | The deliverable is a skill.md, not a user interface; caveman was retired in July 2026 |
| MCP out | figma, plaud, chrome-devtools, skill-builder-audio | figma and plaud serve no taught domain, chrome-devtools is developer tooling, and the audio server arrives with its own plugin |

## One judgement call, flagged rather than hidden

`wei-prep-goal` serves autonomy calibration [D-03] and evaluation methodology [D-04] well. It is out on
**weight, not fit** — its five-gate, five-pass discipline is heavy for a first engagement. This is the
one entry a reasonable person could overturn, and it is named here so they can.

## Revalidation

The tool layer turns over roughly annually — one protocol course in this field was retired seven months
and twenty-two days after publication. **Owner and cadence: unassigned, twelve months.** Without both,
this list ships stale, and that is the failure the programme record already named against itself.
