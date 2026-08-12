---
style: descriptive
role: template
produces: engagements/<client-slug>/spec/requirements.md
---

# Requirements gathering

A written list of everything the deliverable will need in order to run inside the business: the systems
it touches, the information it reads, where it runs, what the business already pays for, what may not
leave, and who to ask when something is missing. One file per engagement, covering every process
confirmed with the owner.

## When it is written

After the owner has confirmed the reconstructed process — the document produced from
`library/templates/process-confirmation.md` — and before the specification is written. Requirements for
a process the owner has not confirmed are requirements for a process you may have wrong.

## Where it goes

- File: `engagements/<client-slug>/spec/requirements.md`.
- Add the row to `engagements/<client-slug>/spec/INDEX.md` in the same operation.
- Answers describing the business's systems, logins and contracts are the business's own information.
  They stay inside the engagement directory, which is deletable as a unit when the relationship ends.

## Frontmatter for the output

```yaml
---
style: descriptive
client: {client-slug}
process: {the process, in the owner's words}
source: process/confirmation-{process-slug}-v{n}.md
version: v1
updated: YYYY-MM-DD
---
```

`source` names the confirmed process document. This file has no authority of its own: every requirement
in it traces to a step the owner has already agreed is real.

## How the answers are collected

This is a checklist you fill in, not homework you send. A small-business owner who is running the
business will not complete a questionnaire, and a document returned blank has taught you nothing.

| Route | Use it when |
|---|---|
| You ask, and write the answers in | The default. Twenty minutes at the counter, the file filled in afterwards |
| The owner sends it back annotated | They asked for it in writing, or the answers need someone else in the business to look them up |
| Split | You fill in what you can see, and leave the rest marked as open for the one person who knows |

Whichever route, read the filled-in answers back before building on them. An answer you wrote down is
an answer you may have misheard.

## Voice

Prompts are written as things to be established, not as questions fired at a person. The reason is
practical: a list of noun phrases can be worked through in any order, partly filled, handed to someone
else in the business, and marked up without it reading as an interrogation.

| Rule | Write | Not |
|---|---|---|
| Prompts as noun phrases | "Scheduling software — whether appointments can be exported, and in what form." | "Can you export your appointments?" |
| No second-person address | "The spreadsheet the dispatcher keeps on the office machine." | "Your dispatch spreadsheet." |
| Systems named neutrally | "The ordering system named during the session (spelling to confirm)." | "That thing you mentioned." |
| Roles, not people | "The person who closes the till." | "Dave's job." |
| A response hint is allowed, if it stays a noun phrase | "(export available / manual copy only / not established)" | "(please tell us which)" |

In a business of four people a role often has exactly one holder. Write the role anyway. It survives
the holder changing, and it keeps the document about the process rather than about a person.

## Sections of the output document

### Header

Title `# {Business} — what the deliverable will need`. Beneath it, one line naming the confirmed process
document and the date the owner confirmed it, then two or three sentences stating that the file collects
what the deliverable needs in order to run, and that gaps are marked `not established` rather than
guessed.

### Processes in scope

One line per confirmed process, numbered, drawn from the confirmation document. Read-only context —
nothing new is claimed here.

### Per-process requirements

For each confirmed process, a `## Process N requirements — {name}` section with the six subsections
below, in order. Where one genuinely does not apply, write "Not applicable — {one sentence why}" rather
than deleting the heading; a missing heading reads as an oversight.

#### Systems access

Every system the deliverable reads from or writes to. One bullet each: name, whether it needs to read,
write or both, and what part of the data.

- "Ordering system — read; the last twelve weeks of wholesale orders, delivery dates and quantities."
- "Shared mailbox — read and write; the folder the supplier confirmations arrive in, and the ability to
  send from the same address."

#### Information it needs

Every source of information the deliverable depends on. One bullet each: where it lives, what a sample
looks like, what form it comes in, and how far back it goes.

- "Supplier price list — one representative copy, as it is actually sent (a PDF attachment); current
  version plus the one before it, to see what changes between them."
- "The paper diary at the front desk — photographs of two representative weeks; no electronic form
  exists."

Ask for a representative sample, not everything. Bulk comes later, if the specification proves it is
needed.

#### Where it runs

- The machine the process is run on today — one office computer, a laptop that goes home, a phone, or a
  mix.
- Who can sign in to each system — one login shared by everyone, one account per person, or one person
  who holds every password.
- Where the records live — inside the software, on one machine's drive, on a shared drive, on paper.
- Whether the systems can be reached from outside the premises.
- What happens to the deliverable when the person who set it up is not there.

#### Tools and subscriptions it assumes

Every paid tool or subscription the process leans on. For each: what plan the business is on, whether
anything other than a person clicking can get data out of it (an export, a scheduled email, a
programmatic interface), and whether the contract says anything about automated or AI use of the data.

- "Accounting package — current plan; monthly export to spreadsheet available / not established;
  contract terms on automated access not established."

For a small business, whether the data can be exported at all matters more than which plan it is on.
Establish the export first.

#### What must not leave, and what must be kept

- Information the owner has said may not leave the business — copied from `process/boundaries.md`, not
  restated from memory.
- Records that must be kept, and for how long, because a regulator, an accountant or a customer
  contract says so.
- Who inside the business may see the deliverable's output.
- What the business is obliged to do if the deliverable gets something wrong.

#### Who to ask

| Role | What they hold | When they are needed |
|---|---|---|
| {the person who closes the till} | {the daily takings file, and the password to it} | {once, to see one real day} |
| {the outside bookkeeper} | {the accounting login} | {before anything writes to the accounts} |

### Requirements that cross every process

- Where the finished deliverable runs — the owner's own machine, or something set up for it. If it
  needs an account somebody has to pay for, name the account and the cost now, not at handover.
- Which AI provider account the business will use, and whether the plan they are on keeps their
  material out of training.
- When the owner is actually available, and the periods when they are not — the week before a holiday
  for a bakery, month end for a dental practice, the first working day after a weekend for a logistics
  firm.
- Anything inside the business that has to be approved before you get access or data.

### Closing

One short section stating how answers come back (inline, under each prompt), what a returned answer
looks like when it is a file rather than a sentence (attached separately, named for the prompt it
answers), and what happens next: the specification is written from this, then the deliverable.

## Rules

1. Every requirement traces to a confirmed step. If it does not, the process reconstruction is
   incomplete and this file is premature.
2. Unknowns are written `not established`, never guessed. A guess here becomes a design assumption two
   files later and nobody remembers it was a guess.
3. No effort estimates, no pricing, no proposal language. This file establishes what exists.
4. No implementation content. How the deliverable will do the work belongs in the specification.
5. Roles, not people, everywhere except the contact table's own "what they hold" column.
6. Bump `version` each time the answers change, and keep what changed visible in the engagement's
   session log.
7. Re-read the whole file for second-person drift before it goes anywhere. It appears first in the
   cross-process section and in the closing.
