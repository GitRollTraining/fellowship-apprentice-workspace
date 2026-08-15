---
style: descriptive
role: template
produces: engagements/<client-slug>/notes.md
---

# Engagement notes

One file per engagement, holding everything a person who has forgotten the engagement needs in order to
pick it up: what it produces, where current decisions are recorded, what constrains it, and which files
matter. An engagement is one client, one relationship, start to end — the unit of work and the unit of
filing.

## Where it goes

- File: `engagements/<client-slug>/notes.md`, beside that directory's `INDEX.md`.
- Current decisions: `engagements/<client-slug>/decision-register.md`, created from
  `library/templates/engagement-decision-register.md`.
- Companion while the engagement is running: `engagements/<client-slug>/progress-log.md`, the session
  log. Its format is `library/templates/engagement-progress-log.md`.
- Creating any of these files means adding a row to `engagements/<client-slug>/INDEX.md` in the same
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
**Decisions:** `decision-register.md`

---

## Objective    (both modes)

{What this engagement produces, concretely. Name the process, name who runs it today, and name the
agreed delivery shape under `deliverable/`. One agent-executable skill is the common default, not the
only valid result.}

## How you will know it worked    (lined up: rough is fine; running: firm and checkable)

- [ ] The owner runs the deliverable without you in the room and accepts the result.
- [ ] {criterion}
- [ ] {criterion}

<!-- everything below is filled in once the engagement is running -->

## First runnable slice    (running)

{The smallest version of the deliverable that does one real step of the real process on one real case,
and how you will know it worked. Define this early; build it once the PRD and specification gates permit
implementation, then prove it before widening. A slice the owner has run beats an untested broad build.}

## Context    (running)

{How the engagement came about, what the owner said they wanted, and what the business does. Enough
for a cold reader who has met nobody.}

## Decision state    (running)

The current decision areas, constraints, owners and stage gates are in `decision-register.md`. Do not
copy the register here. State only the next unresolved gate, or `none`.

- **Next unresolved gate:** {decision ID and stage, or none}

## Materials    (running)

### Read first

| File | What it holds | Why it matters |
|---|---|---|
| `decision-register.md` | Current decisions, unresolved decision areas and stage gates | The canonical current state; do not reconstruct it from session history |
| `interview/discovery-record.md` | What was heard, kept apart from what was concluded | The source for every claim downstream |
| `process/confirmation-{process-slug}-v{n}.md` | The owner-confirmed current-state process | Requirements may not be written from an unconfirmed reconstruction |
| `{path}` | {what} | {why} |

### Being produced

| File | What to do |
|---|---|
| `process/process-{name}.md` | {create or update} |
| `spec/requirements.md` | {draft, obtain sign-off or revise} |
| `spec/automation-approach.md` | {create, confirm or revisit} |
| `spec/specification.md` | {create or update from the signed PRD and current decisions} |
| `deliverable/skill.md` | {create or update — default shape; replace this row with the agreed package inventory when larger} |

### Reach for when needed

| File | What it holds | When |
|---|---|---|
| `library/playbooks/playbook-interview.runbook.md` | Which step's output goes in which file | Before every session |
| `library/playbooks/playbook-discovery-to-deliverable.md` | PRD, automation approach, specification and build gates | After the owner confirms the current-state process |
| `{path}` | {what} | {when} |
```

## Rules

1. A lined-up engagement stays minimal. An objective and a summary is the whole job.
2. Once it is running, write to the session log as work happens, not afterwards. A record that lags
   the work is the failure this file exists to prevent.
3. Durable decision state belongs in `decision-register.md`. This file points at the next gate; it does
   not keep a second summary that can drift.
4. Anything the owner said must not leave the business does not go in this file. Record that the
   constraint exists and where it applies; keep the restricted content out of the tracked record.
5. Before flipping Status to `handed-over`, read this file, the decision register and the session log
   end to end and confirm every success measure is actually checked, not assumed.
6. Names of people belong here only where you need them to do the work. Everything under
   `engagements/<client-slug>/` is deletable as a unit when the relationship ends, which is the point.
