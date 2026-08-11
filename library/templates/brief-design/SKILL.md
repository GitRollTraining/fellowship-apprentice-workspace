---
name: brief-design
description: Design system for a single-page HTML brief — the finished document a business owner opens in a browser and prints. Tokens, components, composition rules, starter file.
style: descriptive
---

# Single-page brief — design system

A brief is one HTML file. No build step, no image files, no server: it opens in any browser, prints to
PDF from the browser, and travels as an email attachment.

This directory supplies the visual language. It does not write the document — the words and the
judgement are yours.

## What it is for

| Document | Who reads it | Target length |
|---|---|---|
| Handover — what the skill you built does, how to run it, what to check | The business owner | 600-1200 words |
| Process reconstruction — the steps, the boundaries, the exceptions, put back in front of the owner to confirm | The owner, and whoever else runs the process | 1000-2500 words |
| Status update part-way through an engagement | The owner | 300-600 words |
| Closing summary — what was built, what was left out, what to watch | The owner | 600-1200 words |

Not for: the owner's own customer-facing material (that follows their brand, not this one), slide
decks, or a document that has to match a house style someone else set. This is one style and it does
not blend with another.

## The visual language in one line

Warm palette, single column, earned callouts, status pills instead of status sentences, a diagram when
the content has structure, prose cut hard.

Full statement: [`reference/philosophy.md`](reference/philosophy.md)

## Two routes to a finished document

| Route | You write | You get | Use when |
|---|---|---|---|
| This design system | HTML, starting from `reference/base.html` | one `.html` file; the browser prints it to PDF | the owner reads it on screen, and the document carries status, structure or a diagram |
| `library/renderers/build-document-pdf.py` | a markdown file | an A4 PDF, serif, formal | the document is prose and tables, and the owner wants something printed |

The renderer reads markdown; it will not take `base.html`. Pick one route per document rather than
maintaining the same content twice.

## Gotchas

- **Cards on cards, identical grids, one big hero number.** The default instinct is landing-page
  structure. Correct: flatten the hierarchy, and vary structure by what the content actually is —
  status, dependency, priority — never a uniform grid of equal boxes.
- **More than three callouts in one document.** The wrong default is a callout per notable fact.
  Correct: hard cap at three, pick the most important, demote the rest to bold prose.
- **"Why this matters" tail paragraphs and ledes that preview the section below them.** Better
  structure removes the need for the explanation; cut it.
- **Emoji and icon sets.** Markers in this style are typographic: a tracked uppercase label, a section
  number, a colored pill. Nothing that depends on an emoji font rendering the same way on the owner's
  machine as on yours.
- Full catalog: [`reference/anti-patterns.md`](reference/anti-patterns.md) — typography, color, layout,
  components, motion, content, and a five-question check before you send it.

## Workflow

1. Read [`reference/composition.md`](reference/composition.md) — section flow and density rules.
2. Read [`reference/components.md`](reference/components.md) — the catalog, with copy-paste snippets.
3. Skim [`reference/anti-patterns.md`](reference/anti-patterns.md) — what not to do.
4. Copy [`reference/base.html`](reference/base.html) to your output path.
5. Compose: replace each `REPLACE` block with sections built from the catalog.
6. Open the file in a browser and print it to PDF. Fix anything that breaks across a page badly.
7. Save the result under `engagements/<client-slug>/handover/`.

## Files here

| File | What it holds |
|---|---|
| `SKILL.md` | This page |
| `reference/philosophy.md` | The eight principles the rest of the system follows from |
| `reference/tokens.md` | Color, type, spacing, radius, print settings |
| `reference/components.md` | Every component, with a snippet and a worked example |
| `reference/composition.md` | How the components go together into a document |
| `reference/anti-patterns.md` | The regressions to prevent, plus the pre-send check |
| `reference/base.html` | The starter file — tokens, all component CSS, and placeholder body |

## How to start

```
cp library/templates/brief-design/reference/base.html \
   engagements/<client-slug>/handover/handover.html
```

Then replace every `<!-- REPLACE: ... -->` block. Anything you do not use, delete — an unused component
left in the file is a placeholder the owner will read.

## When to reach for this

When the request is any of: a single-page brief, a handover document, "make this look finished", "send
the owner something they can read without me", or a status page that has to survive being forwarded.

## Design decisions (locked)

| Decision | Choice |
|---|---|
| File structure | Single file, CSS inline — portable, one attachment, no build |
| Table of contents | Included in `base.html`; easier to delete than to add |
| Content | The system supplies visual vocabulary only, never document structure |
| Markers | Typographic — no emoji, no icon set, nothing that needs a font to be installed |
| Color mode | Light only. There is no dark variant and adding one is out of scope |

## Quality guidelines

Adhere to:

- `library/reference/agent-quality-guidelines.md` (runtime behavior)
- `library/reference/skill-architecture.md` (structural principles)
