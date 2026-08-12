# Composition Rules

The catalog gives you the words. This gives you the grammar.

## Document skeleton

```
<header>     kicker, title, subtitle, properties
<callout>    optional one-line summary; only if the header does not already say it
<h1 id>      section 1
  <p lede>   optional one-line preview
  body       prose and components
<h1 id>      section 2
...
<footer>     who it is about, and when it was last updated
```

Plus a fixed `<nav class="toc">` outside `<main>` when there are three or more sections.

## Section count

| Sections | Verdict |
|---|---|
| 1 | Wrong shape — it is a callout inside some other document |
| 2-3 | A short brief; no sidebar needed |
| 4-6 | The sweet spot; sidebar required |
| 7 or more | Too long — split it, or collapse sections into each other |

## Section anatomy

1. A heading: one short noun phrase, with an optional two-digit number.
2. An optional lede: a single sentence. If it previews what follows, delete it.
3. The body, built from components.

**Density rule: alternate prose and visual.** Do not stack three paragraphs in a row, and do not stack
three components without a sentence connecting them.

## Callout discipline

**Two or three callouts in the whole document.** Each one must:

1. Carry information that is not in the prose beside it.
2. Be the point of its surroundings, not a summary of them.
3. Survive the deletion test — if removing it loses nothing, remove it.

When a callout restates the paragraph above, delete the callout, not the paragraph.

## A visual replaces prose; it never duplicates it

If a chart carries the arithmetic, do not follow it with a "what this means" list. Either the chart
stands alone with one short callout for the conclusion, or the arithmetic needs interpreting and you
replace the chart with a paragraph. One or the other, never both.

The same holds for tables, structure diagrams and scope lists. The visual is the explanation.

## Status pills, not status sentences

Wrong:

> The inbox step is finished. Price matching is partly finished. New customers, one-off discounts and the
> monthly summary have not been started.

Right: a scope list, one row per item, each with its pill. The reader scans pills; nobody reads that
sentence twice.

## When to use the structure diagram

Use it when the items have:

- **A dependency** — a step reads a file, and a person maintains that file.
- **A chain** — one part produces what the next part consumes.
- **A stack** — what runs on top, and what it stands on.

Do not use it when the items are parallel and unrelated. A diagram of five independent checks invents a
structure that is not there, and the owner will try to read meaning into the arrows.

## When to use the comparison chart

Use it when:

- Two or three magnitudes share a baseline — before and after, handled and still manual.
- The numbers came from somewhere real: the owner told you, or you counted them from records.

Do not use it for:

- A range you estimated. An invented bar looks exactly like a measured one, which is why it is worse
  than no chart.
- More than three rows — it stops being readable.
- Anything over time. This chart compares parts of a whole, not a trend.

## When to use the featured block

Use it when one thing is acutely more urgent than everything around it — the date the owner first runs
the process alone, or the single step most likely to break. The reader's first instinct on opening the
page should be to read that box.

One per document. A second one makes both ordinary.

## Section ordering

There is no fixed order. The shapes that work:

| Document | Order |
|---|---|
| Handover | What it does / How to run it / What to check / What to do when it goes wrong |
| Process reconstruction | How it runs today / Where it varies / The exceptions / What I need you to confirm |
| Status update | What changed / What is open / What is next |
| Closing summary | What was built / What was left out / What to watch / What I need from you |

Pick the order that a reader who was not in the room can follow.

## Closing the document

End with one of:

1. `<h3>What I need from you</h3>` and a numbered list — one decision per item, each of them a decision
   only the owner can make. Not tasks you could have done yourself.
2. A single pull quote, if the document asks for nothing.

Then an optional toggle for where the numbers came from, then `<hr>`, then the footer.

## Length

| Document | Words |
|---|---|
| Status update | 300-600 |
| Handover | 600-1200 |
| Closing summary | 600-1200 |
| Process reconstruction | 1000-2500 |

Past these, it has become a report nobody finishes. Cut.
