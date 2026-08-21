---
style: descriptive
---

# The setup record

`training/onboarding/setup-record.md`, in the apprentice's own fork.

**Committing it is a step, not an assumption.** Writing the file is covered by the permission list;
`git add` and `git commit` are not, so both raise an approval prompt. At the end of a session, show
the apprentice what changed and offer to commit it:

```bash
git add training/onboarding/
git commit -m "Onboarding: record setup progress"
```

If they decline, say plainly that the record still exists on disk and the next session will find it,
but nothing is backed up until it is committed and pushed.

It exists so a second session knows what a first session settled. Without it every session re-drives
all nineteen items, and the ones only the apprentice can confirm get re-asked forever.

## Where it lives, and why there

`training/` holds work from before there is a client, and it is one of only three trees the
apprentice's agent may write — `engagements/`, `training/` and `reference/`. Writes under
`library/` are denied outright, so a record kept beside the skill could never be written by the
agent that needs to write it.

`training/INDEX.md` says one directory per module. `onboarding/` is not a module, so it is admitted
by an explicit row in that manifest rather than by the naming convention.

**The directory and its `INDEX.md` already ship with the repository.** Do not create them; they are
there in a fresh clone. What you owe is the manifest update that `CLAUDE.md` requires of anyone who
adds a file: set the Freshness row for `setup-record.md` in `training/onboarding/INDEX.md` to
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
on this list cannot start until the trainer sends something. An apprentice reading a list of eight
`outstanding` rows cannot tell which four they could clear tonight. Separate them.

**When one row changes, check the rows that depended on it.** Correcting a mistyped GitHub username
silently falsifies "GitHub username sent to Ray" — they sent the wrong one. Resolving a
`contradicted` row is the usual trigger. Re-ask the neighbour rather than leaving a `confirmed` row
that is now false.

**`contradicted` exists because it happens.** An apprentice gives a GitHub username; the lookup
returns 404. An identity check prints a name that is not theirs. Recording either as `verified`
because the command exited zero is the failure this state prevents. Write both values down — what
they said and what the command returned — and leave it for the next session or the trainer.

`not applicable` is for one real case — the plugin install when the apprentice is using Codex.
Do not use it to retire something inconvenient.

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
| Read: Git and GitHub | outstanding | | |
| GitHub account | contradicted | 2026-08-21 | they said `sam-demo`; the lookup returned 404 |
| GitHub username sent to Ray | confirmed | 2026-08-21 | |
| Codex application | confirmed | 2026-08-21 | in Codex mode, not chat |
| Package manager | verified | 2026-08-21 | 4.x |
| Code editor | verified | 2026-08-21 | 1.x |
| Git | verified | 2026-08-21 | 2.x |
| GitHub command-line tool | verified | 2026-08-21 | 2.x |
| Node.js and Python | verified | 2026-08-21 | both present |
| Git name and email | verified | 2026-08-21 | both non-empty |
| Signed in to GitHub from the terminal | verified | 2026-08-21 | account named |
| Whole machine, one pass | verified | 2026-08-21 | every row PASS |
| Session logging on entire.io | blocked | 2026-08-21 | trainer: setup page not sent yet |
| Joined Google Classroom | blocked | 2026-08-21 | trainer: join link not sent yet |
| Joined Discord | blocked | 2026-08-21 | trainer: invite not sent yet |
| Workspace cloned and skills symlink resolving | verified | 2026-08-21 | test -L passed |
| Workspace plugins installed | not applicable | 2026-08-21 | using Codex; no plugin mechanism |
| Opened Classroom and read one subject | blocked | 2026-08-21 | trainer: cannot open until they are in Classroom |
| Office hours in the calendar | outstanding | | |

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

**Never write a caveat into the note of a `verified` row.** If the note needs the word "but", the
state is wrong — use `contradicted`. A row reading `verified` with a note saying the value belongs
to somebody else is the worst artifact this format can produce: it looks settled to a later session,
to a trainer skimming the table, and to the apprentice. Downgrade the state instead of qualifying
it.

**Record the small piece of evidence where one exists** — the subject name they opened, the version
string, the account the sign-in named. `confirmed` with no note is weaker than `confirmed` with the
subject name beside it, and the difference matters when a trainer reads the record.

**Keep the three lists under the table in step with it.** They are what the apprentice actually
reads, and what the next session re-asks from. Rewrite them whenever the table changes.

Keeping them separate is the point: an apprentice who can see that only two of eight items are
theirs to clear tonight will clear those two. One undifferentiated list of eight reads as a wall and
gets nothing done.

**The table has more rows than the checklist has items, and that is deliberate.** Setting up the
workspace is two independent jobs with two different outcomes — cloning with a working skills link,
and installing the plugins — and under Codex the second is `not applicable` while the first is
`verified`. One row cannot hold two states, so it gets two.

**Do not remove or rename a row.** A later session reads this table by its row labels. Adding a row
when the checklist grows is fine; adding a line under `Evidence or note` is fine. Renaming
`Joined Discord` to something tidier is what breaks the next session.

**That rule is about the table only.** The lists underneath are rewritten every session by design —
replace them wholesale to match the table as it now stands. A record written before this format had
three lists will have one, possibly under a heading that no longer appears here. Replace it. Nothing
is lost: the table is the record, and the lists are a reading of it.
