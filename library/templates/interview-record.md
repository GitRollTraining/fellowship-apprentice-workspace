---
style: descriptive
role: template
binds: library/playbooks/playbook-interview.md
serves: D-23, D-26, D-28
---

# Interview record

Copy this file's marked blocks into the engagement. Do not edit it here — `library/` is read-only.

| This template produces | Copy it to | Playbook step | Write it |
|---|---|---|---|
| The discovery record: what you heard, then what you concluded | `engagements/<client-slug>/interview/discovery-record.md` | 15 and 16 | the same day as the session |
| The ambiguity list | `engagements/<client-slug>/interview/ambiguities.md` | 17 | the same day as the session |

Both halves of the discovery record live in one file. The ambiguity list is a separate file because it
is the agenda for the next session.

## The four rules this shape enforces

1. What was **heard** is written before, and visibly apart from, what was **concluded**. A reader must be able to tell which is which without asking you.
2. One statement per row, in the owner's own words. Two statements in one row means you have started summarising.
3. Every heard row carries a pointer — where in the session that statement came from. **The pointer column is never removed and never left blank.** A pointer that does not resolve is a fail, not a blemish.
4. Every ambiguity carries a disposition: **settled in the session**, or **still open**. An empty ambiguity list after a real conversation is a finding about the interviewer, not a clean run.

The rule that makes rule 3 self-enforcing: **a statement you cannot point at is not something you
heard.** Move it to the concluded half. Nobody else is reading this before it is used, so the blank
cell is the only thing that will show you the omission.

Every table below carries one example row in italics, all from the same imagined engagement: a bakery's
weekly wholesale order to its flour supplier. Delete the italic rows.

---

<!-- copy from here into engagements/<client-slug>/interview/discovery-record.md -->

## Discovery record — {process name}

Frontmatter for the file you are creating:

```yaml
---
style: descriptive
session: {YYYY-MM-DD}
process: {process name in the owner's words}
---
```

### Session

| Field | Value |
|---|---|
| Client slug | |
| Process discussed | |
| Person interviewed, and their role | |
| Do they do this work themselves | yes / no — if no, say so again in Part 2 |
| Session date | |
| Recording | `interview/session-{date}/` — or: none, and why |
| This record written on | |

If the person interviewed is not the person who does the work, every row below is evidence of how the
process is *supposed* to run. That is a different claim, and it has to be visible here.

### Part 1 — What was heard

One statement per row, quoted. Do not tidy the wording.

| # | What they said | Pointer | Instance or general | Said back to them |
|---|---|---|---|---|
| *H1* | *"I put the wholesale order in Friday morning, once Thursday's counts are on the sheet."* | *recording 00:07:41* | *instance — 6 March* | *confirmed* |
| H2 | | | | |
| H3 | | | | |

| Column | What goes in it | Blank cell means |
|---|---|---|
| # | `H1`, `H2`, and so on. Other files cite these row numbers, so they do not get renumbered once written | not allowed |
| What they said | One statement, quoted. If you only have a paraphrase, start the cell with `paraphrase:` and say why the quote is unavailable | not allowed |
| Pointer | Where in the session it came from: a recording timestamp, a line in the live notes, a document or a screen you were shown. It must resolve for someone who was not in the room | **not allowed — an unpointed statement moves to Part 2** |
| Instance or general | `instance — {date or nameable occasion}` when it rests on one real occurrence; `general` when it is still "we usually". Both may survive; only one of them is evidence | not allowed |
| Said back to them | `confirmed`, `corrected`, or `not said back`. A correction gets its own new row, and the row it corrects is annotated with the new row's number | not allowed |

A correction is a better outcome than a confirmation. If nothing in this column reads `corrected`, check
that you asked *where is that wrong* rather than *does that make sense*.

What a pointer looks like, in descending order of how well it resolves:

| Form | Example |
|---|---|
| Recording timestamp | `recording 00:07:41` |
| Live notes, by line | `session-2026-03-06/notes.md line 22` |
| A document or screen you were shown | `session-2026-03-06/images/02-order-sheet.jpg` |
| Your memory | not a pointer — the statement belongs in Part 2 |

### Part 2 — What was concluded

Nothing in this table was said by the owner. Each row is yours, and each row names the heard rows it
rests on.

| # | What you concluded | Rests on | Why it follows | Confidence |
|---|---|---|---|---|
| *C1* | *Order quantity is set from the weather forecast, not from last week's sales* | *H4, H7* | *both rows describe checking the forecast before setting quantities; neither mentions prior sales* | *medium* |
| C2 | | | | |

Confidence takes exactly three values:

| Value | Use it when |
|---|---|
| `solid` | more than one heard row, at least one of them a datable instance, and it was said back and confirmed |
| `medium` | one instance, or confirmed but not datable |
| `untested` | no instance behind it, or never said back |

Every `untested` conclusion is copied into the ambiguity list as `still open`. A conclusion you never
put to the owner is a guess with a row number.

### Before you file this

- Written the same day as the session.
- Every Part 1 row has a pointer, and you opened at least three of them to check they resolve.
- No conclusion is sitting in Part 1.
- Everything the process, the boundaries or the deliverable will rest on is either a Part 1 row with a pointer, or a Part 2 row citing the rows it rests on.
- Anything you were told must not leave the business is recorded as a constraint in `engagements/<client-slug>/process/boundaries.md` — the constraint, not the information itself.
- `engagements/<client-slug>/interview/INDEX.md` updated in the same operation.

<!-- copy to here -->

---

<!-- copy from here into engagements/<client-slug>/interview/ambiguities.md -->

## Ambiguities — {process name}

Frontmatter for the file you are creating:

```yaml
---
style: descriptive
session: {YYYY-MM-DD}
process: {process name in the owner's words}
---
```

Every vague term, unexplained number and contradiction from the session. Each one gets a disposition.

| # | The term, number or contradiction, quoted | Pointer | Disposition | Settled to, or the question to ask next |
|---|---|---|---|---|
| *A1* | *"a big order"* | *recording 00:12:03* | *settled in the session* | *more than 40 trays — owner said so at 00:12:40* |
| *A2* | *"we usually get it in Friday, but the standing order goes Wednesday"* | *notes.md line 22* | *still open* | *which of the two covers the wholesale order — first question next session* |
| A3 | | | | |

The disposition column takes exactly two values, written exactly like this:

| Value | Meaning |
|---|---|
| `settled in the session` | the owner gave you the answer during the conversation, and the last column records it with its own pointer |
| `still open` | anything else. "Probably fine" is `still open`. "I think I understood" is `still open` |

What belongs on this list:

- a word whose meaning you assumed: big, urgent, regular, the usual, a while
- a number with no unit, no basis, or no source
- two statements that cannot both be true
- a person, tool or document named once and never explained
- anything you wrote down phonetically during the session and have not confirmed the spelling of
- every `untested` conclusion from Part 2 of the discovery record

### Count

| | Count |
|---|---|
| Settled in the session | |
| Still open | |
| Total | |

A total of zero after a real conversation means you did not look, and counts as a fail rather than a
clean run. Ambiguity is the normal state of a process nobody has written down.

### Where the still-open items go next

1. Into `engagements/<client-slug>/interview/pre-session-note.md` for the next session, as the unknowns it has to close.
2. Any question stem that got one of these settled, and would work on another client, goes into `reference/question-bank.md`. A client's answer never goes there — a stem is a question, not what somebody said.

<!-- copy to here -->
