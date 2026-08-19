# Design Tokens

Color, type, spacing and the other primitives. They are declared in `:root` in `base.html`, which is the
canonical copy. Never override a token, never substitute a near value.

## Color

Every value is tinted away from pure neutral, warm rather than blue.

### Surfaces

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#ffffff` | Page background |
| `--bg-subtle` | `#f7f6f3` | Callout backgrounds, two-column blocks, chart panels |
| `--bg-hover` | `#efeeeb` | Hover states |
| `--rule` | `#e9e9e7` | Borders, dividers |
| `--gray-soft` | `#ebeced` | Default status pill |

### Text

| Token | Hex | Use |
|---|---|---|
| `--text` | `#37352f` | Body and headings — warm dark gray |
| `--text-soft` | `#787672` | Subtitles, ledes, secondary labels |
| `--text-muted` | `#9b9a97` | Tertiary — list markers, section numbers, fine print |

### Accent hues (six)

Each hue has a base and a soft variant. Soft for backgrounds, base for text, borders and rules.

| Hue | Base | Soft | Meaning |
|---|---|---|---|
| `--accent` | `#0f6b58` | `--accent-soft` `#ddeee6` | Positive — done, agreed, working |
| `--warn` | `#a8574a` | `--warn-soft` `#fbecea` | Negative — a risk, a blocker, something that broke |
| `--blue` | `#337ea9` | `--blue-soft` `#ddebf1` | A step the agent runs; also links |
| `--purple` | `#6940a5` | `--purple-soft` `#e8deee` | Reference material the process reads |
| `--orange` | `#c96c3f` | `--orange-soft` `#faebdd` | A point where a person decides; the featured block |
| (yellow) | `--yellow-text` `#8a6500` | `--yellow-soft` `#fdecc8` | Warning — the yellow text only reads on the soft background |

### The three-way mapping, fixed

Wherever the system marks which part of a process an item belongs to — the badge on a scope item, the
left border on a structure-diagram box — the hue is fixed:

- a step the agent runs → `--blue`
- reference material the process reads (a price list, a customer list, a template) → `--purple`
- a point where a person decides → `--orange`

The same three colors mean the same three things in every brief. Do not remap them per document.

## Typography

```css
--sans: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

Use the system stack exactly as shown. The brief makes no font-network request, opens offline and does
not disclose the client opening the file to a third-party font host. Nothing in the system depends on a
specific glyph existing.

### Type scale

| Element | Size | Weight | Tracking |
|---|---|---|---|
| Title (page) | `40px` | `700` | `-0.02em` |
| Section heading | `28px` | `700` | `-0.015em` |
| Subsection (h2) | `20px` | `600` | `-0.01em` |
| Minor heading (h3) | `16px` | `600` | normal |
| Body | `16px` / `1.55` | `400` | normal |
| Lede | `15px` | `400` | normal, color `--text-soft` |
| Properties and footer | `12-14px` | varies | wider tracking on labels |
| Small uppercase labels | `10.5-11px` | `600` | `0.05-0.14em`, uppercase |

### Font features

For numbers in tables and charts:

```css
font-feature-settings: "tnum";  /* tabular numerals, so columns of figures line up */
```

## Spacing

There is no spacing scale. Use one-off values that fit the rhythm. The common ones:

| Use | Value |
|---|---|
| Page padding | `64px 56px 120px` (top / sides / bottom) |
| Between top-level sections | `60px 0 12px` margin |
| Subsection | `30px 0 8px` |
| Component margins | `18-22px 0` |
| Tight stacks such as list items | `4-8px` |

Below 720px wide the page padding drops to `40px 24px 80px`.

## Radius

| Token | Value | Use |
|---|---|---|
| `--radius` | `4px` | Pills, tags, small chips |
| `--radius-lg` | `6px` | Callouts, charts, diagram panels, two-column cards |

Never `9999px` — a fully rounded pill is the wrong register here. Never a sharp `0` either. The 4-6px
range is the whole range.

## Shadows

**None.** Separation comes from a `1px solid var(--rule)` border and from background contrast.

## Sidebar position

Right side, fixed:

```css
right: max(24px, calc((100vw - 740px) / 2 - 220px));
```

Hidden below a 1100px viewport.

## Print

Page padding `24px 36px`. Body drops to `13px`. The sidebar, the collapsible toggles and every hover
state are hidden. Background colors are forced to print (`print-color-adjust: exact`), so status pills,
callout fills and chart bars survive the PDF. Each heavy component — `callout`, `arch`, `featured`,
`cost-chart`, `scope`, and each `two-col .col` — carries `break-inside: avoid`.
