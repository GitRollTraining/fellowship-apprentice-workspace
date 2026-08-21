---
style: descriptive
---

# The setup record

`training/onboarding/setup-record.md`, in the apprentice's own fork, committed.

It exists so a second session knows what a first session settled. Without it every session re-drives
nineteen items, and the eight that only the apprentice can confirm get re-asked forever.

## Where it lives, and why there

`training/` holds work from before there is a client, and it is one of only three trees the
apprentice's agent may write — `engagements/`, `training/` and `reference/`. Writes under
`library/` are denied outright, so a record kept beside the skill could never be written by the
agent that needs to write it.

`training/INDEX.md` says one directory per module. `onboarding/` is not a module, so it is admitted
by an explicit row in that manifest rather than by the naming convention. When you create
`training/onboarding/`, give it an `INDEX.md` whose first line is the upstream pointer:

```
<!-- upstream: training/INDEX.md -->
```

## The four states

| State | Means | Re-ask next session? |
|---|---|---|
| `verified` | a command checked it and passed | no |
| `confirmed` | the apprentice said so; no command can check it | no |
| `outstanding` | not done, or the apprentice could not confirm it | **yes** |
| `not applicable` | genuinely does not apply, with the reason written down | no |

`not applicable` is for one real case — the plugin install when the apprentice is using Codex.
Do not use it to retire something inconvenient.

## The shape

```markdown
# Onboarding setup record

Apprentice: <name>
Agent: Claude Code | ChatGPT desktop application, Codex mode
Started: YYYY-MM-DD
Last session: YYYY-MM-DD

| Item | State | Date | Evidence or note |
|---|---|---|---|
| Read: version control systems | confirmed | 2026-08-21 | |
| Read: Git and GitHub | outstanding | | |
| GitHub account | verified | 2026-08-21 | username resolves |
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
| Session logging on entire.io | outstanding | | |
| Joined Google Classroom | outstanding | | needs the link from the trainer |
| Joined Discord | outstanding | | needs the invite from the trainer |
| Workspace cloned and skills symlink resolving | verified | 2026-08-21 | test -L passed |
| Workspace plugins installed | not applicable | 2026-08-21 | using Codex; no plugin mechanism |
| Opened Classroom and read one subject | outstanding | | |
| Office hours in the calendar | outstanding | | |

## Still outstanding

- Read: Git and GitHub
- Session logging on entire.io
- Joined Google Classroom, Joined Discord — both need the link the trainer sends privately
- Opened Classroom and read one subject
- Office hours in the calendar
```

## Rules

**Never write a joining link or a course code into this file.** The record says *whether* they
joined, never *how* to join. The repository is public.

**Every non-empty state carries a date.** A row with a state and no date cannot be resumed, because
nothing distinguishes "confirmed last week" from a guess.

**Record the small piece of evidence where one exists** — the subject name they opened, the version
string, the account the sign-in named. `confirmed` with no note is weaker than `confirmed` with the
subject name beside it, and the difference matters when a trainer reads the record.

**Keep the "Still outstanding" list in step with the table.** It is what the apprentice reads and
what the next session re-asks from. Rewrite it whenever the table changes.

**Two rows can be added, and only two:** an extra line under `Evidence or note`, and a new row if
the checklist itself grows. Do not restructure the table — a later session parses it.
