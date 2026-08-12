---
style: descriptive
role: template
produces: engagements/<client-slug>/notes.md
---

# Engagement notes

One file per engagement, holding everything a person who has forgotten the engagement needs in order to
pick it up: what it produces, what has been settled, what constrains it, and which files matter. An
engagement is one client, one relationship, start to end — the unit of work and the unit of filing.

## Where it goes

- File: `engagements/<client-slug>/notes.md`, beside that directory's `INDEX.md`.
- Companion while the engagement is running: `engagements/<client-slug>/progress-log.md`, the session
  log. Its format is `library/templates/engagement-progress-log.md`.
- Creating either file means adding a row to `engagements/<client-slug>/INDEX.md` in the same
  operation.

## Two modes

An engagement directory is one of two things. Fill only what the mode needs.

| Mode | When | Status | Filled in | Session log? |
|---|---|---|---|---|
| Lined up | A business has agreed to talk, no session held yet | `not-started` | Title, one-line summary, Objective. Success measures may be rough | No |
| Running | The first session is booked or held | `running` | Everything below, firm success measures, a first runnable slice | Yes — create it and keep it current |

A lined-up engagement graduates: flip Status to `running`, fill the rest, create the session log. Do
not demand the running-mode sections of an engagement that has not started.

Two statuses end an engagement: `handed-over` when the owner is running the deliverable without you,
and `dropped` when it stopped for any other reason. Say which in one line at the top rather than
deleting the file.

## The shape

```markdown
---
style: descriptive
---

# {Business} — {the process being automated}

> {One or two sentences: what this engagement produces, and for whom.}

**Created:** {YYYY-MM-DD}
**Status:** not-started | running | handed-over | dropped
**Owner:** {the person who runs the process, and how to reach them}

---

## Objective    (both modes)

{What this engagement produces, concretely. Name the process, name who runs it today, and name the
file that gets handed over: the agent-executable skill.md in deliverable/.}

## How you will know it worked    (lined up: rough is fine; running: firm and checkable)

- [ ] The owner runs the deliverable without you in the room and accepts the result.
- [ ] {criterion}
- [ ] {criterion}

<!-- everything below is filled in once the engagement is running -->

## First runnable slice    (running)

{The smallest version of the deliverable that does one real step of the real process on one real case,
and how you will know it worked. Build this before widening. A slice the owner has run beats a
specification nobody has tested.}

## Context    (running)

{How the engagement came about, what the owner said they wanted, and what the business does. Enough
for a cold reader who has met nobody.}

## What is settled, and what constrains it    (running)

- {a decision made, and when}
- {a constraint: what must not be automated, who has to approve, what may not leave the business —
  recorded in full in `process/boundaries.md`, summarised in one line here}

## Materials    (running)

### Read first

| File | What it holds | Why it matters |
|---|---|---|
| `interview/discovery-record.md` | What was heard, kept apart from what was concluded | The source for every claim downstream |
| `{path}` | {what} | {why} |

### Being produced

| File | What to do |
|---|---|
| `process/process-{name}.md` | {create or update} |
| `spec/{name}.md` | {create or update} |
| `deliverable/skill.md` | {create or update} |

### Reach for when needed

| File | What it holds | When |
|---|---|---|
| `library/playbooks/playbook-interview.runbook.md` | Which step's output goes in which file | Before every session |
| `{path}` | {what} | {when} |
```

## Rules

1. A lined-up engagement stays minimal. An objective and a summary is the whole job.
2. Once it is running, write to the session log as work happens, not afterwards. A record that lags
   the work is the failure this file exists to prevent.
3. Anything the owner said must not leave the business does not go in this file. Record that the
   constraint exists and where it applies; keep the restricted content out of the tracked record.
4. Before flipping Status to `handed-over`, read this file and the session log end to end and confirm
   every success measure is actually checked, not assumed.
5. Names of people belong here only where you need them to do the work. Everything under
   `engagements/<client-slug>/` is deletable as a unit when the relationship ends, which is the point.
