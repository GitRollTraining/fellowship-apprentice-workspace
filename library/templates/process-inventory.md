---
style: descriptive
role: template
produces: engagements/<client-slug>/process/inventory.md
---

# Process inventory

One document listing every process the owner surfaced during a session, whether or not it is the one
you will build. It is written after the session, from the session record, and it is the basis for
choosing which single process the engagement automates.

An owner talking about the thing that annoys them will name four other things on the way. Written down
at the time they are a menu; recalled a week later they are gone.

## Where it goes

- File: `engagements/<client-slug>/process/inventory.md`.
- Written from `interview/session-<date>/` and `interview/discovery-record.md`, after the session, not
  during it.
- The one process you select then gets its own full reconstruction at
  `process/process-{name}.md` — step 7 of the interview playbook, which the runbook
  (`library/playbooks/playbook-interview.runbook.md`) maps to that file.

## One word to avoid

This repository already uses **domain** for a named area the curriculum covers, so do not use it for an
area of the business. Write "area" — ordering, scheduling, invoicing, dispatch — and keep `domain` for
what `library/reference/terminology.md` defines it as.

## Frontmatter for the output

```yaml
---
style: descriptive
client: {client-slug}
session: YYYY-MM-DD
source: interview/session-{YYYY-MM-DD}/
updated: YYYY-MM-DD
---
```

## Sections of the output document

Four sections. All of them appear. Where one is empty, write "None surfaced" rather than deleting it.

### 1. Where this came from

A short block, readable by a person, mirroring the frontmatter:

```markdown
**Session:** {what it was — first discovery session, follow-up on the ordering process}
**Date:** YYYY-MM-DD
**Record:** `interview/session-{YYYY-MM-DD}/`
**Present:** {roles — the owner, the person who does the ordering}
**Inventory written:** YYYY-MM-DD
```

### 2. The table

Every process surfaced, one row each, most costly first.

```markdown
| # | Process | What it covers | Area | How often | Hurts | Chosen |
|---|---|---|---|---|---|---|
| 1 | {short name, in the owner's words} | {one line} | {ordering} | {every Monday} | named | [ ] |
| 2 | ... | ... | ... | ... | felt | [ ] |
```

The `Hurts` column takes one of three values, and each one is a statement about evidence rather than a
judgement of severity:

| Value | Meaning |
|---|---|
| named | The owner stated a cost: hours, money, a mistake that actually happened, someone they had to hire |
| felt | Mentioned as friction, with no figure and no incident attached |
| passing | Mentioned once, with no sign it troubles them |

### 3. One entry per process

Numbered to match the table. Fixed shape, so that two entries can be compared without reading both in
full:

```markdown
#### {N}. {Process name}

- **Area:** {ordering}
- **How often:** {every Monday morning, about forty minutes}
- **Who runs it:** {role, not name}
- **Hurts:** named | felt | passing
- **Chosen:** [ ]
- **What it is:** {two to four sentences: what starts it, what it produces, how it is done today.}
- **Where it stops:** {what is inside this process and what is the next one along. Which other
  processes it hands to or takes from.}
- **What was said:**
  > "{verbatim, as the owner said it}" — owner, session 2026-05-14, 00:18:40
  > "{verbatim}" — the person who does the ordering, session 2026-05-14, live notes page 2
```

### 4. Closing notes

```markdown
**Processes surfaced:** {N}
**Chosen, and why:** {one paragraph, written after the selection pass, naming the process and which of
the tests below it passed}
**How they depend on each other:** {process 3 cannot start until process 1 has produced its list;
processes 5 and 7 both read the same spreadsheet}
**Open, and going to the owner:** {anything mentioned but not explained enough to write down cleanly,
including any system name the recording may have mangled — these become open items in the
confirmation document}
```

## Choosing one

You choose, and nobody reviews the choice. Five tests, and a process that fails the last two is a bad
first engagement however much it hurts:

| Test | Why it matters |
|---|---|
| It happens often | A process run twice a year cannot be observed, corrected, or shown to work |
| It has a definite trigger and a definite finished output | Without both, there is nothing to specify and nothing to say is done |
| The information it needs is already written down somewhere | If it lives only in the owner's head, the engagement becomes an elicitation project with no deliverable |
| The owner can tell when the result is wrong | Nobody can hand over something whose failure is invisible |
| Nothing bad happens if it is wrong once | The first thing you build is the wrong place to discover the cost of a bad run |

Run the selection as its own pass, on a different day from writing the inventory. Every `Chosen` box is
`[ ]` in the first draft.

## Rules

1. Every process traces to the session record. No process appears here because it seemed likely.
2. Quotes are verbatim, with a pointer back to where in the session they came from — a timestamp if the
   session was recorded, a page of the live notes if it was not. One quote per process minimum, two
   where the cost was stated.
3. What you heard and what you concluded stay apart. "What was said" holds the owner's words; "What it
   is" holds your reconstruction, and it may be wrong.
4. A system name the recording may have mangled is written as it was heard, in quotes, and added to the
   open list for the owner to correct. Do not silently repair it into the name you assume it is.
5. No implementation content. This is the process as it runs today. What an agent would do about it
   belongs in the specification.
6. No effort estimates. The inventory is for understanding and for choosing.
