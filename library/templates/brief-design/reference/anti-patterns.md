# Anti-Patterns

The regressions to prevent. Each one happens by default unless you push against it.

## Typography

Never:

- **A remote web font in a supposedly portable one-file brief.** Use the supplied local system stack;
  do not create a network request or an unstated client-data disclosure merely for typography.
- **Monospace as decoration.** `<code>` is for a real file path, a real identifier, a real command.
- **Bold and italic and uppercase and colored** on the same words. Pick one form of emphasis.
- **All-caps headings.** Uppercase belongs on small tracked labels and nowhere else.

## Color

Never:

- **Pure black.** Text is `#37352f`. A `#ffffff` page background is correct; `#000` anywhere is not.
- **Gradient text on a number.** A number is a number; a gradient hides it.
- **The machine-generated palette:** cyan on dark, purple-to-blue gradients, neon on black. This style is
  light only.
- **Dark mode with glow.** It looks considered without any decision having been made.
- **More than three accent hues in one section.** Each section has one dominant color story.

## Layout

Never:

- **Cards inside cards.** Flatten it.
- **A container around everything.** A paragraph does not need a box. Most prose sits directly under its
  heading.
- **Centered text.** Left-aligned and asymmetric reads as designed; centered reads as a template.
- **An icon or emoji beside every heading.** A marker on every heading is a marker on none of them, and
  an emoji is a font dependency that prints as an empty box.
- **A grid of identical cards.** If there are six things, six equal boxes is the wrong answer — find the
  real structure (status, dependency, priority) and show that.
- **The hero-number layout** — one huge figure, a small label, supporting statistics, a gradient. It is
  the shape of every product landing page.

## Components

Never:

- **More than three callouts in a document.** Hard cap. A fourth means you have stopped choosing; pick
  the one that matters and demote the rest to bold prose.
- **A callout that summarizes the prose above it.** If it can be deleted without loss, delete it.
- **A "what this means" list after a chart.** The chart already said it. One short callout, or trust the
  visual.
- **A three-bullet "why now" list.** It always reads as a pitch. One sentence if it is needed at all.
- **A status sentence where a pill belongs.** Not "this part is currently pending" — a `Pending` pill.
- **A structure diagram for parallel items.** The diagram is for dependency and layering. Parallel items
  are a list or a two-column block.
- **A pull quote that restates the heading.** A pull quote is the point beneath the point.
- **A chart built on numbers you estimated.** If the figures came out of your head, drop the chart. Chart
  only what the owner told you or what you counted.

## Motion and interaction

Never:

- **Bounce or elastic easing.** Dated, and it makes the reader wait.
- **Animating width, height or padding.** Transform and opacity only — and in this style you should
  mostly not be animating at all.
- **Decorative hover effects.** Hover is functional only: the sidebar highlight and the toggle.

## Content

Never:

- **A lede that previews the section under it.** Make it earn its line or delete it.
- **A "why this matters" paragraph at the end of a section.** If the section needs that, the section
  needs restructuring.
- **Bullets added for weight.** Each bullet carries information or it goes.
- **Hedged recommendations.** "It might be worth potentially considering" is not advice. Write the
  recommendation, then the caveat, in that order.
- **A sentence telling the reader how not to read a number.** Say what the number counts. If it is only
  safe to print with a warning attached, it is not ready to print.

## Before you send it

Five questions:

1. **Cut test.** Delete every callout — does the document still read? If yes, the callouts were not
   earning their place.
2. **Duplication.** Is there anywhere a chart or table is followed by a list saying the same thing?
3. **Section purpose.** Can you state each section's purpose in one sentence? If not, it is doing two
   jobs.
4. **Pills.** Did any status end up as a sentence?
5. **Print.** Print it to PDF and read the PDF. Does it come out as two or three clean pages, with no
   diagram split across a break and nothing the reader needs hidden inside a toggle?

Any wrong answer is a revision, not a caveat.
