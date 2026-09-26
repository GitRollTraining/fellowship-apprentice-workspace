---
style: descriptive
---

# The setup record

`apprentice-workspace/training/onboarding/setup-record.md`, in the repository the apprentice ran
onboarding in.

**Their repository, and not necessarily pushable.** For most apprentices that is the folder they made
by hand before installing their agent, which has no GitHub copy at all. No step in this skill creates
one. Ask whether the repository has a GitHub copy they can write to before suggesting a push. If it
does not, say plainly that the record is local, and leave it committed locally.

**Committing it is a step, not an assumption.** The agent asks before `git add` and `git commit`. At
the end of a session, show the apprentice what changed and offer to commit it:

```bash
git add apprentice-workspace/training/onboarding/
git commit -m "Onboarding: record setup progress"
```

If they decline, say plainly that the record still exists on disk and the next session will find
it. Do not tell them to push unless you have established they have somewhere to push to.

It exists so a second session knows what a first session settled. Without it every session re-drives
all nineteen items, and the ones only the apprentice can confirm get re-asked forever.

## Where it lives, and why there

`training/` holds work from before there is a client; it sits inside `apprentice-workspace/` with
`engagements/` and `reference/`, the three trees that are the apprentice's own. `library/` is the
plugin's read-only copy, which the next plugin update replaces, so a record kept beside the skill
would not survive.

`training/INDEX.md` says one directory per module. `onboarding/` is not a module, so it is admitted
by an explicit row in that manifest rather than by the naming convention.

**The directory and its `INDEX.md` are created by the `setup` skill.** Do not create them by hand;
if they are missing, run `setup`. What you owe is the manifest update that the workspace rules
(`apprentice-workspace/AGENTS.md`) require of anyone who adds a file: set the Freshness row for
`setup-record.md` in `apprentice-workspace/training/onboarding/INDEX.md` to
today's date — **every session that writes the record, not only the first.** A freshness row that is
only ever set once is stale from the second session onward, which is worse than an empty one because
it looks maintained.

## The six states

| State | Means | Re-ask next session? |
|---|---|---|
| `verified` | a command checked it and passed, and any value it printed belongs to this apprentice | no |
| `confirmed` | the apprentice said so; no command can check it | no |
| `outstanding` | not done, and the apprentice can do it themselves | **yes** |
| `blocked` | not done, and they cannot proceed until someone else acts — the trainer sends a link, grants access, answers | **yes, and name who is blocking** |
| `contradicted` | the apprentice said one thing and a command showed another | **yes — resolve it, do not average it** |
| `not applicable` | genuinely does not apply, with the reason written down | no |

**`blocked` and `outstanding` look identical in a table and are not the same thing.** Several items
on this list cannot start until the trainer sends something. An apprentice reading one long
`outstanding` list cannot tell which of those rows they could clear tonight and which will sit there
until somebody replies. Separate them.

**When one row changes, check the rows that depended on it.** Correcting a mistyped GitHub username
silently falsifies "GitHub username sent to Ray" — they sent the wrong one. Resolving a
`contradicted` row is the usual trigger. Re-ask the neighbour rather than leaving a `confirmed` row
that is now false.

**`contradicted` exists because it happens.** An apprentice gives a GitHub username; the lookup
returns 404. An identity check prints a name that is not theirs. Recording either as `verified`
because the command exited zero is the failure this state prevents. Write both values down — what
they said and what the command returned — and leave it for the next session or the trainer.

`not applicable` is for one real case — a plugin from `library/sops/agent-settings.md` that is not
offered for the agent the apprentice uses. Do not use it to retire something inconvenient.

## The shape

```markdown
# Onboarding setup record

Apprentice: <name>
Agent: Claude Code | ChatGPT desktop application, Codex mode
Started: YYYY-MM-DD
Last session: YYYY-MM-DD, session <n>

| Item | State | Date | Evidence or note |
|---|---|---|---|
| Read: version control systems | confirmed | 2026-08-21 | |
| Read: Git and GitHub | outstanding | 2026-08-21 | asked; not read yet |
| GitHub account | contradicted | 2026-08-21 | they said `sam-demo`; the lookup returned 404 |
| GitHub username sent to Ray | confirmed | 2026-08-21 | |
| Codex application | confirmed | 2026-08-21 | in Codex mode, not chat |
| Package manager | verified | 2026-08-21 | 4.x |
| Code editor | verified | 2026-08-21 | 1.x |
| Git | verified | 2026-08-21 | 2.x |
| GitHub command-line tool | verified | 2026-08-21 | 2.x |
| Node.js and Python | verified | 2026-08-21 | both present |
| Git name and email | verified | 2026-08-21 | apprentice confirmed both values are theirs |
| Signed in to GitHub from the terminal | verified | 2026-08-21 | account named |
| Whole machine, one pass | verified | 2026-08-21 | every row PASS |
| Session logging on entire.io | blocked | 2026-08-21 | trainer: setup page not sent yet |
| Joined Google Classroom | blocked | 2026-08-21 | trainer: join link not sent yet |
| Joined Discord | blocked | 2026-08-21 | trainer: invite not sent yet |
| Apprentice workspace plugin installed | verified | 2026-08-21 | ChatGPT app (Codex); this skill ran from it |
| Workspace folder set up in this repository | verified | 2026-08-21 | apprentice-workspace/AGENTS.md and the root AGENTS.md block present |
| Workspace plugins installed | not applicable | 2026-08-21 | using Codex; <plugin name> not offered for Codex |
| Opened Classroom and read one subject | blocked | 2026-08-21 | trainer: cannot open until they are in Classroom |
| Office hours in the calendar | outstanding | 2026-08-21 | asked; not added yet |

## You can do these now

- Read: Git and GitHub
- Office hours in the calendar

## Waiting on the trainer

- Session logging on entire.io — needs the setup page
- Joined Google Classroom, Joined Discord — both need the link, sent privately
- Opened Classroom and read one subject — follows from Classroom

## Needs sorting out

- GitHub account — the username given does not resolve. Check the spelling, or the account
```

## Rules

**Never write a joining link or a course code into this file.** The record says *whether* they
joined, never *how* to join. The repository is public.

**Every non-empty state carries a date.** A row with a state and no date cannot be resumed, because
nothing distinguishes "confirmed last week" from a guess.

**Never write a caveat into the note of a `verified` row.** A note recording *how* something passed
is fine — `copied, not linked` is a method, not a doubt. A note that undercuts the pass is not: if it
needs the word "but", or names a value belonging to someone else, the state is wrong — use
`contradicted`. A row reading `verified` with a note saying the value belongs
to somebody else is the worst artifact this format can produce: it looks settled to a later session,
to a trainer skimming the table, and to the apprentice. Downgrade the state instead of qualifying
it.

**Record the small piece of evidence where one exists** — the subject name they opened, the version
string, the account the sign-in named. `confirmed` with no note is weaker than `confirmed` with the
subject name beside it, and the difference matters when a trainer reads the record.

**Keep the three lists under the table in step with it.** They are what the apprentice actually
reads, and what the next session re-asks from. Rewrite them whenever the table changes.

Keeping them separate is the point: an apprentice who can see which rows are actually theirs to
clear tonight will clear them. One undifferentiated list reads as a wall and gets nothing done.

**The table has more rows than the checklist has items, and that is deliberate.** Setting up the
workspace is three independent jobs with different outcomes — the `apprentice-workspace` plugin, the
workspace folder in this repository, and the plugins from `library/sops/agent-settings.md` — and one
can be `not applicable` while the others are `verified`. One row cannot hold three states, so it
gets three.

**Do not remove or rename a row.** A later session reads this table by its row labels. Adding a row
when the checklist grows is fine; adding a line under `Evidence or note` is fine. Renaming
`Joined Discord` to something tidier is what breaks the next session.

**One exception, made once.** A record written while the workspace was a cloned repository has the row
`Workspace cloned and skills symlink resolving`. The thing it checked no longer exists: replace that
row with `Apprentice workspace plugin installed` and `Workspace folder set up in this repository`,
check both, and note the old row's date in the new rows' notes.

**That rule is about the table only.** The lists underneath are rewritten every session by design —
replace them wholesale to match the table as it now stands. A record written before this format had
three lists will have one, possibly under a heading that no longer appears here. Replace it. Nothing
is lost: the table is the record, and the lists are a reading of it.
