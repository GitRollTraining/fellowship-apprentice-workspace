# Component Catalog

Every component in the system: when to use it, the HTML, and the variants. All snippets assume the CSS
in `base.html` is loaded.

The worked examples all use one running case — a bakery that takes wholesale orders by email, checks
them against a price list, and confirms them. Substitute your own engagement.

---

## Header block

**When:** every brief opens with one. It carries identity and the facts the reader needs before the
first section.

```html
<header class="header">
  <div class="kicker">Handover</div>
  <h1 class="title">Wholesale order intake, running on its own</h1>
  <p class="subtitle">What it does, how to run it, and what to check each week · 2026-03-04</p>

  <dl class="props">
    <dt>Business</dt><dd>Riverside Bakery</dd>
    <dt>Contact</dt><dd><span class="mention">Dana</span> · owner</dd>
    <dt>Process</dt><dd>Wholesale orders arriving by email, Monday to Friday</dd>
    <dt>Status</dt><dd><span class="tag green">Handed over</span> &nbsp; run by the shop since 2026-03-01</dd>
    <dt>Last checked</dt><dd>2026-03-04</dd>
  </dl>
</header>
```

**Variants:**

- `kicker` — the document kind in one or two words: Handover, Process, Status, Closing summary. It
  renders as a small uppercase tracked label above the title.
- Properties — free-form label and value pairs; three to five rows is the sweet spot. Tag colors:
  `green` positive, `red` a caution, `blue` neutral information, `yellow` needs attention.

**Anything given to you in confidence does not belong in this document.** A brief is a file the owner
will forward to a bookkeeper or a family member. Material you were told to keep inside the business
stays in an untracked sidecar file, not behind a label in the header.

---

## Section heading

**When:** every top-level section. Optionally a one-line lede under it.

```html
<h1 id="what-it-does"><span class="h-num">01</span> What it does</h1>
<p class="lede">One sentence. Delete this line if it only previews the section below.</p>
```

**Convention:** the `id` matches the sidebar anchor. The number is optional but useful in a document the
owner will refer back to over the phone.

---

## Callout

**When:** to carry information that is not in the prose beside it. Two or three per document, maximum.

```html
<div class="callout accent">
  <div class="co-label">Note</div>
  <div class="co-body"><strong>It stops at the price.</strong> Any order line whose price does not match
  the price list is left in the drafts folder for you, rather than confirmed.</div>
</div>
```

**Color variants:**

| Class | Meaning | Label that usually fits |
|---|---|---|
| (none) | Neutral background context | Note |
| `accent` | Positive, a signal, the headline finding | Note, Result |
| `warn` | Negative — a risk, a blocker, something that broke | Risk |
| `yellow` | Needs attention before it bites | Check |
| `blue` | Reference or a definition | Definition |
| `purple` | About the reference material the process reads | Source |
| `orange` | Time-sensitive, one action | Next |

The label is a word, not a sentence; it renders uppercase and tracked.

**Do not** use a callout to summarize the paragraph above it. If deleting the callout loses nothing,
delete it.

---

## Checklist

**When:** discrete items with a state — done, part-way, not started.

```html
<ul class="todo">
  <li class="done"><span class="box"></span><span class="txt"><b>Orders read from the inbox</b> — every message in the wholesale folder</span></li>
  <li class="partial"><span class="box"></span><span class="txt"><b>Prices checked</b> — the standing list is covered; one-off discounts still come to you</span></li>
  <li><span class="box"></span><span class="txt"><b>New customers</b> — still set up by hand</span></li>
</ul>
```

**States:** `done` renders a filled check and strikes the text through; `partial` renders a half-filled
box; no class renders an empty box. Both marks are drawn in CSS, so they print.

---

## Scope list (`scope` block)

**When:** numbered items each carrying a status, and optionally a badge saying which part of the process
they belong to. Use it for what you agreed to build, or for the steps of a process with their state.

```html
<div class="scope">
  <div class="scope-header">
    <span class="scope-title">What we agreed to build</span>
    <span class="scope-prog">3 of 5 running · 2 left</span>
  </div>
  <div class="scope-progbar">
    <div class="seg done"></div>
    <div class="seg done"></div>
    <div class="seg done"></div>
    <div class="seg partial"></div>
    <div class="seg pending"></div>
  </div>

  <div class="scope-item">
    <div class="scope-n">01</div>
    <div class="scope-body">
      <b>Read the wholesale inbox</b>
      <div class="d">Every message in the wholesale folder, once an hour.</div>
      <span class="scope-layer agent">Runs on its own</span>
    </div>
    <div class="scope-status done">Done</div>
  </div>

  <div class="scope-item">
    <div class="scope-n">02</div>
    <div class="scope-body">
      <b>Check each line against the price list</b>
      <div class="d">Anything that does not match is left for you.</div>
      <span class="scope-layer material">Reads the price list</span>
    </div>
    <div class="scope-status partial">Partial</div>
  </div>

  <div class="scope-item">
    <div class="scope-n">03</div>
    <div class="scope-body">
      <b>Approve anything above the standing discount</b>
      <div class="d">Comes to you in the drafts folder.</div>
      <span class="scope-layer human">You decide</span>
    </div>
    <div class="scope-status pending">Pending</div>
  </div>
</div>
```

**Status pills:** `done`, `partial`, `pending`.

**Badges:** `agent` blue (a step that runs on its own), `material` purple (reference material the step
reads), `human` orange (a point where a person decides). The colors are fixed — see `tokens.md`.

**Progress bar:** one segment per item, in the same order; segment classes `done`, `partial`, `pending`.

---

## Structure diagram (`arch` block)

**When:** the items depend on each other — steps that read a file someone else maintains, a chain where
one part produces what the next consumes. Three rows maximum.

```html
<div class="arch">
  <div class="arch-title">Wholesale order intake · what depends on what</div>

  <div class="arch-layer-label">Runs each hour</div>
  <div class="arch-row three">
    <div class="arch-box agent built"><b>Read the inbox</b><span class="desc">wholesale folder</span></div>
    <div class="arch-box agent built"><b>Match to the price list</b><span class="desc">line by line</span></div>
    <div class="arch-box agent"><b>Draft the confirmation</b><span class="desc">one per order</span></div>
  </div>

  <div class="arch-arrow">reads</div>

  <div class="arch-layer-label">Reference material</div>
  <div class="arch-row two">
    <div class="arch-box material"><b>Price list</b><span class="desc">spreadsheet, one row per item</span></div>
    <div class="arch-box material"><b>Customer list</b><span class="desc">name, address, standing discount</span></div>
  </div>

  <div class="arch-arrow">kept up to date by</div>

  <div class="arch-layer-label">People</div>
  <div class="arch-row two">
    <div class="arch-box human"><b>Owner</b><span class="desc">prices, first Monday of the month</span></div>
    <div class="arch-box human"><b>Counter staff</b><span class="desc">adds a new customer when one calls</span></div>
  </div>
</div>
```

**Box classes:** `agent` blue left border, `material` purple, `human` orange. Add `built` to any box that
is already working — it turns green and appends "· built" to the name.

**Row layouts:** `.three` for three columns, `.two` for two. More than three boxes in a row means they
probably do not belong in one row.

**The arrows are drawn in CSS**, pointing up at the row above. The text says what the relationship is —
"reads", "kept up to date by", "escalates to".

---

## Comparison chart (`cost-chart` block)

**When:** two or three magnitudes that share a baseline. Hours per week, orders per month, money — the
unit does not matter, but the numbers must be real.

```html
<div class="cost-chart">
  <div class="chart-title">Order intake · hours per week</div>

  <div class="cost-row total">
    <div class="cr-label">Before<span class="sub">counted over two weeks</span></div>
    <div class="cr-bar"><div class="cr-fill" style="left:0;width:100%"></div></div>
    <div class="cr-num">6.0<span class="sub">hours</span></div>
  </div>

  <div class="cost-row captured">
    <div class="cr-label">Now runs on its own<span class="sub">reading, matching, drafting</span></div>
    <div class="cr-bar"><div class="cr-fill" style="left:0;width:67%"></div></div>
    <div class="cr-num">4.0<span class="sub">hours</span></div>
  </div>

  <div class="cost-row remaining">
    <div class="cr-label">Still by hand<span class="sub">new customers, odd prices</span></div>
    <div class="cr-bar"><div class="cr-fill" style="left:67%;width:33%"></div></div>
    <div class="cr-num">2.0<span class="sub">hours</span></div>
  </div>
</div>
```

**Row classes:**

- `total` — gray, the baseline at 100%
- `captured` — green, the part now handled
- `expandable` — purple, the part that could be handled next
- `remaining` — orange, the part that stays manual

**Bar math:** `left` and `width` are percentages of the baseline, and you compute them. The `total` row
is always at `width:100%` so the reader can see the scale.

**Do not** follow the chart with a four-bullet "what this means" list. Either the chart carries it with
one short callout beneath, or you did not need the chart.

---

## Featured block

**When:** one acute thing that must not be missed — a cutover date, the single step most likely to break
first. One per document, at most.

```html
<div class="featured">
  <div class="featured-head">
    <h3>First week running without me</h3>
    <span class="when">Mon 2026-03-09</span>
  </div>
  <p><strong>What to do:</strong> open the drafts folder each morning before you bake.</p>
  <ul>
    <li>Confirm the drafts that look right — one click each.</li>
    <li>Anything sitting there for a second day is one it could not price. Send it yourself.</li>
    <li>Write down what it could not price; that list is what gets fixed next.</li>
  </ul>
  <p><strong>Do not:</strong> change the price list format. The matching reads the column headers by name.</p>
</div>
```

**Convention:** orange bordered box, solid orange date pill. Using it twice destroys the effect it exists
for.

---

## Two-column block

**When:** parallel categories — before and after, done and open, what it handles and what it does not.

```html
<div class="two-col">
  <div class="col">
    <h3>It handles</h3>
    <ul>
      <li>Orders from the 14 standing wholesale customers</li>
      <li>Any item on the price list</li>
    </ul>
  </div>
  <div class="col">
    <h3>It does not handle</h3>
    <ul>
      <li>A customer who has never ordered before</li>
      <li>A one-off discount agreed by phone</li>
    </ul>
  </div>
</div>
```

Stacks to one column on a narrow screen.

---

## Toggle

**When:** material worth keeping but not worth the reader's first pass — where a number came from, which
files the process touches. Collapsed by default, and hidden when the document is printed.

```html
<details>
  <summary>Where these numbers came from</summary>
  <div class="toggle-body">
    <ul>
      <li>Hours counted from the inbox timestamps, 17 Feb to 28 Feb</li>
      <li>Price list as of 2026-03-01</li>
    </ul>
  </div>
</details>
```

Because toggles do not print, nothing the reader must see goes inside one.

---

## Mention chip

**When:** naming a person inline.

```html
<span class="mention">Dana</span>
```

Renders as the name in a soft gray pill, with a leading `@`.

---

## Inline tag

**When:** a status or category marker inside flowing text.

```html
<span class="inline-tag green">Running</span>
<span class="inline-tag red">Blocked</span>
<span class="inline-tag yellow">Needs a decision</span>
<span class="inline-tag blue">Runs on its own</span>
<span class="inline-tag purple">Reference material</span>
<span class="inline-tag orange">You decide</span>
```

---

## Pull quote

**When:** one sentence that is the point of a section. Rarely, and never to restate the heading.

```html
<blockquote>
  Every order it could not price is a rule nobody had written down.
  <cite>— from the second interview, 2026-02-19</cite>
</blockquote>
```

---

## Sidebar table of contents

**When:** three or more sections.

```html
<nav class="toc" aria-label="Table of contents">
  <div class="toc-title">On this page</div>
  <ol>
    <li><a href="#what-it-does">What it does</a></li>
    <li><a href="#how-to-run-it">How to run it</a></li>
    <li><a href="#what-to-check">What to check</a></li>
    <li><a href="#when-it-goes-wrong">When it goes wrong</a></li>
  </ol>
</nav>
```

The script at the bottom of `base.html` highlights the section you are reading. Anchors must match the
section `id` values exactly. The sidebar disappears below 1100px and on print.

---

## Footer

**When:** always, as the last block inside `<main>`.

```html
<footer class="footer">
  <span>Riverside Bakery · order intake handover</span>
  <span>Last updated 2026-03-04</span>
</footer>
```
