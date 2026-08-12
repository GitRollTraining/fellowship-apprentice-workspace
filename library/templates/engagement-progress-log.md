---
style: descriptive
role: template
produces: engagements/<client-slug>/progress-log.md
---

# Engagement progress log

The running record of one engagement: one entry per working session, appended, never rewritten. It
exists so that a session picked up after a week starts from what happened rather than from memory.

## Where it goes

- File: `engagements/<client-slug>/progress-log.md`, beside `notes.md`.
- Created when the engagement starts running, not before. A lined-up engagement has no sessions to log.
- Class `Mutable`, status `append-only, one line per session` in the directory's `INDEX.md`.

## What belongs here, and what does not

| Belongs here | Belongs elsewhere |
|---|---|
| That a session happened, and what changed because of it | What the owner said — `interview/session-<date>/` and `interview/discovery-record.md` |
| A decision you made and would otherwise forget | The reconstructed process itself — `process/` |
| What is stuck, and what the next session starts with | What you will do differently next time — `interview/self-audit-<date>.md`, and one line in `reference/self-audit-log.md` |

A log entry that reproduces the discovery record is two copies of one fact, and they drift.

## The shape

```markdown
---
style: descriptive
---

# Progress — {Business} — {the process being automated}

> Session log. One entry per working session. Appended, not rewritten.

**Engagement:** `engagements/{client-slug}/`
**Status:** running

---

## {YYYY-MM-DD} — session {n}

- **Did:** {what actually got done}
- **Verified:** {what you checked and what came back — the owner confirmed the step order out loud, the
  draft ran on last Tuesday's real order and produced the right total, the diagram was corrected in
  two places. Evidence, not a claim that it is fine}
- **Decided:** {any decision made; the ones that outlive the session get copied into notes.md}
- **Stuck:** {what is unresolved, and what it is waiting on}
- **Next:** {the first thing the next session picks up}
```

## Rules

1. Write the entry during or immediately after the session. An entry reconstructed a week later is a
   guess with a date on it.
2. "Verified" means something happened that could have come out the other way: a real case run, a
   correction the owner made, a check that failed. "Looks right" is not verification.
3. Never edit an old entry. If it was wrong, say so in today's entry and name the date it corrects.
4. Copy durable decisions into `notes.md`. The log is where a decision is recorded first, not where it
   is looked up later.
5. Before flipping the engagement to `handed-over`, read this log end to end. It is the only place the
   whole sequence exists.
