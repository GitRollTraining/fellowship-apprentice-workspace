---
style: descriptive
role: template
produces: engagements/<client-slug>/process/confirmation-<process-slug>-v<n>.md
---

# Process confirmation

The document you give back to the owner so they can correct your reconstruction before anything is
built from it. It describes one process as you understood it — the steps, the systems, the exceptions,
the boundaries — and it invites correction on every line.

It is not a summary and it is not a proposal. Its whole job is to be marked up.

## Where it goes

- File: `engagements/<client-slug>/process/confirmation-<process-slug>-v1.md`.
- Each time the owner returns corrections, write the next version as a new file, `-v2.md`, and keep the
  earlier one. What changed between versions is part of the record.
- Corrections the owner makes are things heard from the owner, so they also belong in the heard half of
  `interview/discovery-record.md`. A correction that lives only in a later version of this file is a
  fact with no source.

## Frontmatter for the output

```yaml
---
style: descriptive
audience: the business owner
client: {client-slug}
process: {the process, in the owner's words}
version: v1
sent: YYYY-MM-DD
returned: YYYY-MM-DD | not yet
source: interview/discovery-record.md
---
```

## Voice

The document reads as a neutral description of the process, in the owner's own words for their own
things. If they call it "the book", it is the book — not "the manual scheduling record".

| Rule | Write | Not |
|---|---|---|
| No first person | "Orders are entered on the office machine the same afternoon." | "We understood that you enter orders..." |
| No second-person address | "The person who takes the delivery signs the docket." | "You sign the docket." |
| No attribution to a person | "Described during the session as the slowest part of the morning." | "Maria said this was the slowest part." |
| Steps as observed facts | "The order list is built from last week's sales." | "She walked through how she builds the order list." |
| Prompts as noun phrases | "Whether the second delivery is checked against the docket, or only against the invoice." | "Do you check the second delivery against the docket?" |
| Present tense for how it runs now; past tense only for what was said in the session | "The list goes to the supplier by email." / "Described during the session as..." | "You would then...", "If you wanted to...", "You should..." |

The reason for the neutrality is mechanical, not stylistic: the owner has to be able to strike a line
and write "no, it's the other way round" without it becoming a disagreement with a person.

Plain words throughout. Short sentences. No terms from this repository — the owner has never read it.

## Sections of the output document

### Header

- Title: `# {Business} — {the process}, as understood`
- `## Where this came from`: the date of the session, who was in the room by role, and one line on what
  was covered.
- Two or three sentences stating that the document sets out the process as it was understood, that
  anything wrong or missing should be marked, and that nothing is built until it comes back.

### What this covers

The process, in one numbered line, plus a sentence on where it sits — what happens immediately before
it starts and immediately after it finishes. If more than one process is covered, number them and give
each its own section below.

End this section with the marking instruction, word for word. It appears here and again at the end,
because owners read one end of a document or the other:

> Steps described wrongly, and steps missing from this document, should be marked for correction before
> anything is built from it.

### Per-process sections

For each process, a `## {N}. {Process name}` section with four subsections, in this order.

#### Step by step

A numbered list. Each step is one bullet: a short bold name for what happens, then one to three plain
sentences describing it. Concrete enough that the owner can tell whether it is right.

- **Build the order list.** Last week's sales are read off the till report, and the quantities are
  written into the order sheet on the office machine.
- **Send it to the supplier.** The sheet is emailed to the supplier before eleven on Monday.

Name the actual tool or record where one was named. Do not generalise "the green notebook" into "the
record system" — the specific thing is what makes the step checkable.

A diagram of the step order is worth more than the prose for confirming sequence, and the owner will
spot a swapped pair in a picture that they will read past in a list. `library/skills/flowchart/` builds
one.

#### Systems and records used

One bullet per system, record or piece of paper the process touches, with a short clarifier — inside
the business, the supplier's, a public source, on paper. Where a name was unclear in the session,
write it as it was heard and say the spelling needs confirming.

#### Exceptions, approvals and what happens when it breaks

The things the process does when the normal path does not apply, drawn from what the owner described:

- Named exceptions — the case where the supplier is out of stock, the case where the order comes in
  after eleven. Named cases, not a general statement that exceptions occur.
- What must not be automated, and who has to approve before the work continues.
- What may not leave the business.
- What is done today when an input is missing or wrong, and what happens further down when it fails.

Nothing new appears here. This section confirms what was described; it does not add exceptions you
thought of afterwards.

#### Open items

Noun-phrase prompts, one per bullet, each pointing at something specific that was incomplete,
ambiguous, or open to two readings in the session:

- "Whether the stock check happens before the order sheet is filled in, or after."
- "The correct name and spelling of the ordering system."
- "How often the late-order exception actually comes up — roughly, in a normal month."

Only items about whether the description is right. Questions about access, logins, exports and
subscriptions are not confirmation questions; they belong in the requirements document,
`library/templates/requirements-gathering.md`.

### Closing

Repeat the marking instruction word for word, then one sentence on what happens once it comes back: a
PRD is drafted from the confirmed process, tested against an automation approach, returned for owner
sign-off, and then turned into the specification and deliverable.

## How the owner marks it up

Say which of these applies, in one line, at the top of the document. An owner who is not told how to
respond does not respond.

| Route | Works when |
|---|---|
| Printed, marked with a pen, photographed back | The default for anyone who does not work in documents all day |
| Comments in whatever document tool they already use | They already live in one; do not introduce a new one for this |
| Read aloud together, corrections written down by you, then sent back for a yes | The process is short, or reading is a barrier. The corrections still have to be written and confirmed |

Whichever route, the marked-up version is filed with the engagement. A correction that exists only in
your memory of the phone call is not a correction.

## Rules

1. Every statement traces to the session record. Where something is not known, it goes in Open items —
   never asserted as a guess to be corrected later.
2. Nothing about how the work will be automated. Method, tools and design belong in the specification.
3. No estimates, no cost, no proposal framing.
4. Search the draft for every person's name. Outside the header, rewrite the sentence to remove it.
5. Keep each process to about one page. A step-by-step running past eight steps is usually two
   processes described together — split them and number them separately.
6. Bump the version on every return, keep the previous file, and log the round in the engagement's
   session log.
