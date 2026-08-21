---
name: onboarding
description: Walk a new AI Fellowship apprentice from a fresh machine to a working workspace, verifying each step that a command can verify and recording the ones only they can confirm. Use on an apprentice's first session, and again on any later session while the record still shows unfinished items. Do not use it to set up a client engagement — that is playbook-environment-setup.md, which assumes everything this skill installs.
---

# Onboarding — get an apprentice to working state

Nineteen things have to be true before an apprentice can do the work. This skill walks them, checks
what a command can check, and writes down what only the apprentice can confirm so the next session
knows what is still outstanding.

**Where this sits.** `library/playbooks/playbook-environment-setup.md` sets up a *client
engagement* and assumes a working machine; it says in its own preconditions that missing base
setup "is an onboarding problem: report it and stop". This skill is what happens on the other side
of that stop.

## Input

Nothing is required. Ask for what each step needs, when the step needs it.

Two things you must ask for and never guess, because they are not in this repository and must not
be — the repository is public:

- the **Google Classroom** joining link or course code, which the trainer sends each apprentice
  privately;
- the **Discord** invite, sent the same way.

If the apprentice does not have them, that is not a failure. Record it as outstanding and tell them
to ask their trainer. Never search for, reconstruct, or store either value in this repository.

## How to behave

**Answer questions; do not deliver lectures.** Say in one line what is about to happen and why it
matters, then do it. Apprentices are expected to ask, and when they ask, explain properly — as long
as they want. Do not pre-empt with a tutorial nobody requested.

**Expect permission prompts, and say so before the first one.** Inside this repository the agent's
allow-list covers only `git status`, `git diff` and `git log`. Every version check, every `gh`
command, even `ls -l`, raises an approval prompt. Tell the apprentice this once, up front:
approving those prompts is the intended path, not a warning sign.

**Say which items you cannot check.** Several of the nineteen happen somewhere this agent cannot
see — a browser tab, a calendar, a chat membership. Ask, record the answer with the date, and move
on. Do not perform a check you cannot actually perform, and do not imply you did.

**Where a command CAN check something the apprentice also told you, compare the two.** If they
disagree, that is its own recorded state — not a tie to break in your head, and not a reason to
prefer the command. Say what each one said and leave it visible.

## Workflow

### 1. Open the record before anything else

Read `training/onboarding/setup-record.md` in the apprentice's fork.

- **It does not exist** — this is a first session. Create it from `references/record-format.md`,
  then work the whole list.
- **It exists** — this is a later session. Read it, tell the apprentice in one line what is already
  done, and work only the rows whose state is **not** `verified`, `confirmed` or `not applicable`.
  Do not re-run machine checks that already passed unless the apprentice says something broke.

  Take the remaining rows in this order, because it is the order that respects their time:
  `contradicted` first — something is wrong and they can fix it now; then `outstanding` — theirs to
  do; then `blocked` — read these out so they know what to chase, but do not make them sit through
  each one.

  A record written before this skill gained the `blocked` and `contradicted` states will have
  everything filed as `outstanding`. Read the note column, sort them yourself, and rewrite the
  states as you go.

Ask which agent they are using — Claude Code or the ChatGPT desktop application in Codex mode — and
record it. It changes exactly one step, the plugin install, and it is better known at the start.

### 2. Before day one — four items

| Ask | What to record |
|---|---|
| Have you read the notes on **version control systems**? | their answer, with the date |
| Have you read the notes on **Git and GitHub**? | their answer, with the date |
| Do you have a **GitHub account**? | the username, which the next step needs |
| Have you **sent your GitHub username to Ray**? | their answer |

Only the third can be checked at all, and only loosely: `gh api users/<name> --jq .login` proves
the account exists, not that it is theirs.

**That command needs the GitHub tool, which is installed and signed in two sections later.** Do not
stop here to install it. Take the username, record it as `confirmed`, and come back to check it
after the sign-in step — then upgrade the row to `verified`, or to `contradicted` if the lookup
returns 404 for the name they gave you.

Sending the username to Ray gates repository *access* later, not the clone, so it does not block the
rest of this session. It does block their own fork later, so record it as `blocked` on the trainer
rather than as merely outstanding.

### 3. Your machine — nine items, and these come first

Do these before the workspace step. The repository assumes a working machine and will tell the
apprentice to stop if it finds one missing.

Run the checks in `references/checks.md`. In short: the **Codex** application, a **package
manager**, a **code editor**, **Git**, the **GitHub command-line tool**, **Node.js and Python**,
then **your Git name and email**, then **signing in to GitHub from the terminal**, and finally one
pass that shows a version number for every tool with no errors.

Three of those checks have a wrong-looking obvious form. `references/checks.md` gives the right one
and says why; use it rather than improvising, because two of the three fail *silently*.

If the apprentice is on Windows, say plainly that this repository takes no position on Windows
tooling — it names no package manager for it anywhere — and that you are working from general
practice rather than from a house standard.

### 4. Day one — six items

**Session logging on entire.io comes first**, before the other five, because it records the whole
programme and anything done before it is set up is not recorded. This repository says nothing about
entire.io at all, so ask the apprentice to follow the setup page their trainer gave them and tell
you when it is running.

**If they do not have that page yet, do not stall the session.** Record it as `blocked` on the
trainer, say once and plainly that this session's work will not appear in their log, and carry on.
The alternative is an apprentice who does nothing at all while waiting — worse on every axis, and
the machine section does not depend on it.

Then: **join Google Classroom** and **join Discord**, both using the links you asked for at the
start. Then **set up the workspace**. Then **open Classroom, open one subject and read the first
page** — record which subject, so the record shows they actually got in. Then **put office hours in
your calendar**.

**Setting up the workspace is two jobs, and only the first works everywhere.**

1. Clone the repository and confirm the skills symlink resolves. This is a filesystem check and
   works identically under either agent.
2. Install the plugins listed in `library/sops/agent-settings.md`. Run the commands from that page
   rather than from a count remembered here — its prose and its command block disagree about how
   many there are. These are Claude Code plugins. **In Codex there is no equivalent** —
   record the step as not applicable, say so plainly, and move on. It is not the apprentice's
   fault and nothing later in this skill depends on it.

For a Claude Code apprentice, the install is interactive: the commands are in
`library/sops/agent-settings.md`. Two of them add a marketplace first. Read
`references/checks.md` before running them — the block does not behave the way its own
introduction describes, and knowing that in advance turns a confusing failure into a known one.

### 5. Close

Write the record. Then tell the apprentice, in two lines, what is still outstanding and who to ask.

Then point them at the next thing:

> Setup is done. From here, when you want to know how something in this workspace works — where a
> file goes, what a playbook is, which skill to reach for — run `/workspace-help` and ask it in
> plain words.

## The record

`training/onboarding/setup-record.md`, in the apprentice's own fork, committed. Shape and the rules
for resuming: `references/record-format.md`.

It lives under `training/` because that is where work-before-a-client belongs and because it is one
of the three trees the apprentice's own agent is allowed to write. `library/` is denied outright,
so a record kept beside this skill could never be written by the agent that needs to write it.

## Gotchas

- **Putting a joining link in a file.** This repository is public. Ask the apprentice for the link
  each time; never write it down here, and never carry one between apprentices.
- **Running the workspace step before the machine steps.** The clone will succeed and the plugin
  install will fail in a way that reads as a repository problem rather than a missing tool.
- **Treating a permission prompt as an error.** It is the settings file doing its job. Warn once,
  early, and keep going.
- **Marking a reminder as done because the apprentice said "yeah".** Record the date and, where
  there is one, the small piece of evidence — the subject name they opened, the username they sent.
  A record with no date cannot be resumed.
- **Re-driving settled steps on a later session.** Read the record first. An apprentice made to
  re-run nine version checks to reach the one thing they still owe will stop running this skill.
- **Repairing something in `library/`.** If a library file is wrong, report it. Do not fix it in
  place — the provenance record hashes every file in that tree.

## Quality guidelines

Adhere to:

- `library/reference/agent-quality-guidelines.md` for runtime behavior.
- `library/reference/skill-architecture.md` for structural principles.
