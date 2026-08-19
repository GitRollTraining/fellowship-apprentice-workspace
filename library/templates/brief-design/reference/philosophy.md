# Design Philosophy

Eight principles. Every decision in `tokens.md` and `components.md` follows from one of them.

## 1. Warm, not clinical

Body text is `#37352f`, a warm dark gray. Callout backgrounds are `#f7f6f3`. Pure black never appears —
not in text, not in a border, not in a bar fill. The page background is `#ffffff`; everything on top of
it is tinted away from pure neutral. A brief should read like a considered page, not a spec sheet.

## 2. Single column, about 740px wide

The reading width is calibrated to roughly 80 characters at 16px. Wider makes scanning harder; narrower
wastes the screen. The table-of-contents sidebar sits outside that column and disappears below 1100px.

## 3. Local system type, and typographic markers rather than icons

The local system sans stack opens without a network request, travels with no font asset and respects the
client's data boundary. Distinction comes from hierarchy and spacing, not a hidden web-font dependency.
Markers are typographic: an uppercase tracked label, a two-digit section number, a colored status pill.
No emoji and no icon set — an icon stacked above every heading is a template fingerprint, and an emoji
renders differently on the owner's machine than on yours, or prints as an empty box.

## 4. Earned callouts

Two or three per document, maximum. Each must carry information that is not in the prose beside it. The
largest regression across revisions is callout creep: every point gets boxed because it feels important,
and the boxes stop meaning anything. If a callout would only summarize what sits above it, delete the
callout.

## 5. Status pills, not status sentences

Show state with a colored pill — `Pending`, `Partial`, `Done`, `Live`. Do not write "this part is
currently pending" in prose. Pills are scannable; sentences are not. The same goes for which part of the
process an item belongs to: use a badge, not a sentence explaining it.

## 6. Draw the structure when there is structure

If the steps depend on each other, or read from something a person maintains, use the structure diagram.
If two magnitudes are being compared, use the comparison chart. A bulleted list is the wrong instrument
for a dependency: the reader cannot rebuild the shape from prose.

When the items are genuinely parallel — five unrelated checks — a list is right, and a diagram would
invent a structure that is not there.

## 7. Cut prose without mercy

After writing a section, ask: if I delete this paragraph, does the meaning survive? If yes, delete it.
Visuals replace prose; they do not accompany it. If a chart and a bulleted list say the same thing, keep
the chart and delete the list.

## 8. Print-ready by default

A brief prints clean or it is not finished. Each heavy component — `callout`, `arch`, `featured`,
`cost-chart`, `scope`, and each column of `two-col` — carries `break-inside: avoid`. The sidebar is
hidden on print, and background colors are forced to print so the pills and fills survive. Print it to
PDF before you send it; a page break through the middle of a diagram is invisible in the browser.

---

## What this style is not

| Reject | Why |
|---|---|
| Centered hero text | Reads as corporate template; left-aligned and asymmetric reads as designed |
| Gradient banners | Decorative, carries no information |
| Glass and glow effects | Decoration without purpose |
| Rounded drop shadows on cards | Generic, forgettable |
| Monospace as a way of signalling "technical" | Lazy signalling; mono is for code and file paths |
| Bouncing or elastic animation | Dated, and it spends the reader's time |
| Cards inside cards | Nesting noise; flatten it |
| An icon or emoji beside every heading | Templated, and it does not print |

If you are tempted by any of these, re-read this file.
