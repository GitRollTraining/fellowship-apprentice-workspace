---
style: descriptive
role: template
serves: D-29
---

# Handover template

Two documents, one shape each. Copy the blocks below out of this file; `library/` is read-only.

| Document | Destination | Who reads it | Produced by |
|---|---|---|---|
| The owner's account | `engagements/<client-slug>/handover/owner-account.md` | The business owner | Step 20 of `library/playbooks/playbook-interview.md` |
| The comprehension check | `engagements/<client-slug>/handover/comprehension-check.md` | You | Step 21 of the same playbook |

## What travels, and what does not

The account is a PDF the owner reads and keeps. The `skill.md` in `engagements/<client-slug>/deliverable/`
is the thing that runs, and it travels separately, as a file installed into the owner's own agent. A PDF
is not executable.

Say so in the account, near the top, in the owner's words. Model wording, to be rewritten in theirs:

> You have two things. This booklet says what the process does, what it will not do, and what to check.
> The other thing is a file. The file is the part that does the work, and it goes into the assistant on
> your computer. Printing this booklet does not give you the file, and the file is not something you
> read.

## Register: their words, not yours

The account is written in the explanation register, which is a different genre from the discovery record
and must not be merged with it. Rules, from `library/reference/explanation-style.md` and step 20 of the
interview playbook:

1. **Use the words they used.** Any term that did not come out of their mouth during the session is cut,
   or defined in their words at the point it is used. Ordinary English is not the constraint;
   unexplained jargon is.
2. **No definition may use an undefined word.** Order the account so nothing is needed before it is
   defined.
3. **Carry one real instance the whole way.** One order, one invoice, one appointment from their own
   week, and every section said inside it. Do not switch instance halfway: a new one resets the reader,
   a carried one accumulates.
4. **Retire the instance the moment it would assert something the process does not do.** A worked
   example carried one step too far invents a claim.
5. **Convert rates into counts, and give every number its comparison.** "It gets it right nine times out
   of ten" is unreadable; "about four a week come back to you, out of forty" is not.
6. **Say what was expected before what happens**, so each line lands as a confirmation or a correction
   rather than as free-floating fact.
7. **This is not the specification and not a summary of your record.** It is the thing they read when
   you are not there.

## Rendering it: the input contract

Both files are markdown. The owner reads a PDF. `library/renderers/build-document-pdf.py` compiles one
from the other; `library/renderers/check-document-pdf.py` says whether it survived.

```bash
python3 library/renderers/build-document-pdf.py engagements/<client-slug>/handover/owner-account.md
python3 library/renderers/check-document-pdf.py engagements/<client-slug>/handover/owner-account.md
```

The build needs `pandoc` on the path and a Chromium browser through Playwright. The check needs
`pdftotext`. The PDF is written beside the markdown. The markdown is the source of truth: never
hand-edit the PDF, and never let the two diverge.

**Run the check every time.** The build reports success whether or not the tables became tables.

### Four things the file must carry

| Fill in | Exactly | If you omit it |
|---|---|---|
| Frontmatter, opening on line 1 | Three dashes as the very first line of the file, nothing above them, and a `footer:` key inside the block | The builder does not see the block at all. The footer key never takes effect and the frontmatter lines can render into the page |
| The footer key | `footer: "Rosewood Bakery — the morning order run"`. Quote the value; the builder strips the quotes, and an unquoted colon breaks the block | The footer falls back to the title text, and with no title to the file name. Every page of a bakery's account then reads `owner-account` |
| Exactly one line starting with a single hash | The title, and it is the only first-level heading in the file | The subtitle style below attaches itself to the first later title that does have a paragraph under it, and the real title has none |
| One paragraph directly under that line | Nothing between the title and it — not a quote block, not a table, not a list | No subtitle line, or a subtitle somewhere else in the document |

Tables are the fifth requirement and the one that fails silently. Every header row needs a separator row
directly beneath it — one cell of dashes per column, between pipes — every row needs the same number of
columns as its header, and every table starts at the left margin rather than indented inside a list.
Without the separator row pandoc stops seeing a table and prints the pipes as prose: the build succeeds,
the page count does not change, and the section is unreadable.

```markdown
| Check | When | Right looks like |
|---|---|---|
| The Friday list | Every Friday | Nine names, and the last one is yours |
```

### The table shapes the renderer knows

Column widths are chosen from the header row, so the header decides the layout.

| First header cell | How the first column renders |
|---|---|
| `Stage`, `Step`, `Week`, `Phase`, `#` or `No.` | A narrow index, seven percent of the width. Use these only when the cell really holds an index like `1` or `Week 2`. A sentence in that column is squeezed into seven percent |
| Anything else | A bold label at forty percent of the width, then the rest. Keep the first cell to a few words |
| No header row at all, three columns | A grey index, a bold name, then a description |

A label cell may carry a name, an em dash, and a gloss in italics: the name stays bold and the gloss
drops to grey italic. That is the shape for a table of the owner's own words. Tables of four rows or
fewer are held whole across a page break; longer ones may split across pages.

### What the check catches

Four checks, each of them written after that failure was observed rather than imagined: a header row
with no separator row under it; a row with more or fewer columns than its header; a pipe character
surviving into the PDF text, which is the downstream proof of the first; and a replacement glyph, which
is a character the font does not have rendering as a blank or a box. The check exits non-zero on any of
them.

It also prints a page count. **The page count is not a check.** The failure it exists to catch leaves
the count unchanged.

## Template A — the owner's account

```markdown
---
style: explanation
footer: "<business name> — <their name for the process>"
client: <client-slug>
---

# <Their name for the process>

<One sentence, directly under the title with nothing between: what it does and who it is for. This line
becomes the small-capitals line under the title in the PDF.>

## What you have been given

<Two things, in their words: this account, and the file that does the work. Model wording is in the
template notes.>

## What it does

<One real instance of their own work, carried the whole way through this section.>

| # | What happens | Where you see it |
|---|---|---|
| 1 | <the action, in their words> | <the screen, the folder, the inbox> |

## What it will not do

| It will not | What happens instead |
|---|---|
| <the case it does not cover> | <who does it, and when> |

## What to check

| Check | When | Right looks like | Wrong looks like |
|---|---|---|---|
| <what to look at> | <after each run, every Friday> | <observable, and countable> | <observable, and countable> |

## When it goes wrong

| What you see | What it means | What to do |
|---|---|---|
| <the symptom, as they would describe it> | <the cause, plainly> | <the action, and who to tell> |

## The words used here

<Every word in this account that they did not use themselves, with what it means in their words. An
empty table here is a good outcome, not a missing section.>

| Word | What it means |
|---|---|
| <the word> | <what it means, in their words> |
```

## Template B — the comprehension check

```markdown
---
style: descriptive
footer: "<business name> — comprehension check"
client: <client-slug>
---

# Comprehension check — <their name for the process>

<One sentence, directly under the title: which account was tested, on what date, with whom.>

## How this was run

<Hand them the account. Ask them to tell you, from the document and without your help, what the process
does and what to do when it fails. Do not answer, do not prompt, do not finish the sentence. Record what
they could not answer. Revise the account. Run it again.>

## Round 1 — <date>

| What I asked them to tell me | What they could not answer | What I changed |
|---|---|---|
| <the question, as you asked it> | <what came back, in their words, or nothing> | <the edit to the account, or nothing, because they answered it> |

## Round 2 — <date>

| What I asked them to tell me | What they could not answer | What I changed |
|---|---|---|
| | | |

## Where this stopped

<Which round ended it, and against which line below.>

| Line | Met |
|---|---|
| From the account and without you, the owner can say what the process does, spot when it has gone wrong, and check the result | yes |
| The owner could also run the whole process by hand | no, and it is a bonus rather than the exit condition |
```

## Before you call it done

- **Agreement is not comprehension.** "Does that make sense?" returns agreement from anyone being
  polite. The question is what they can tell you from the document with you silent.
- **An empty comprehension check is not a pass.** It means the check was not run. A round in which they
  answered everything is still a round, and it is recorded with "nothing" in the last two columns.
- **The exit condition is the first line of the table, not the second.** The programme's standard is
  that the owner can verify the work without you. Re-executing the process by hand is a larger bar that
  the programme does not set, because the agent is what executes.
- **A higher published standard exists and is worth holding as an aspiration, not as the exit
  condition** — someone with limited experience of the procedure reproducing it unsupervised, and the
  draft tested by somebody other than its writer. Step 21 of the interview playbook cites it and says
  plainly that it is the larger standard. On a solo engagement the owner is the only other reader you
  have, so the comprehension check is the whole of the external test.
- **Build the PDF, then run the check, then read the PDF.** A clean build is not evidence, and a defect
  that is invisible in the markdown is often obvious on the page.
