# Gotchas

Every item here was measured, most of them by looking at a rendered page after the source looked
fine. None was imagined at design time.

## The pipeline

- **A blank line anywhere inside `<svg>` makes pandoc flatten the whole diagram to literal
  text.** The markdown looks correct and the SVG is valid. Correct: assert
  `"\n\n" not in svg` before writing the document, and check it in the gate.

- **A naive "is there a script tag" checker cannot tell use from mention.** A document that
  *discusses* `<script` in prose trips a checker looking for the literal string. Correct: match
  the tag as markup, not as a substring.

- **Mermaid does not render in the formal-PDF pipeline or in a terminal.** It looks like the
  better choice because it has real graph semantics. Correct: inline SVG for a document, ASCII
  for a terminal, mermaid only when the destination is Notion, GitHub, or a rendered artifact.

## Sizing

- **On-page text size is `font-size / viewBox width`.** An SVG at `width="100%"` scales to the
  page. This inverts the obvious fix: a chart that reads as "too tight" is usually too WIDE, and
  the repair is FEWER COLUMNS, not taller rows. Measured: 866 wide to 678 wide made the type 28%
  larger with no font change.

- **Uniform row heights do not fit a portrait page.** 12 layers x a uniform row gave 1106 against
  668, and a 1.66 aspect broke the last row onto the following page. Correct: each row as tall as
  its tallest box needs.

- **Sizing the canvas from the layer count clips the drawing.** The coordinate pass moves nodes
  past their own layer's span. Correct: size from the actual slot values.

- **A feedback edge leaving the bottom row pushes the drawing into the page footer.** The source
  of a feedback edge is very often in the bottom row, because that is where a loop turns around.
  Correct: the outbound connector circle sits BESIDE its box, not under it.

- **The inbound connector caption is right-anchored, and nothing grew the canvas to hold it.**
  The outbound caption had a `W = max(W, ...)` line; its inbound twin never did, and the
  `viewBox` started at `0`, so the caption ran off the left edge of the page. Measured
  2026-08-09 on a three-box chart: `from Karma Network` had its left edge at `x=-21` against a
  canvas starting at `x=0` — the "K" was simply gone. It only bites when the feedback TARGET
  sits in the leftmost column, which is why the 21-node canonical never showed it and a 5-node
  chart did. `check_map.py` reported CLEAN throughout: no check looks outside the viewBox.
  Correct: track the leftmost overhang and emit `viewBox="{minx} 0 {W-minx} {H}"`.

## Text

- **`shapes.label()` raising is the feature, not an obstacle.** A silent overflow is invisible in
  the SVG source and survives to the printed page. When it raises, shorten the text or widen the
  box — never loosen the assertion.

- **A cylinder's caps eat its box.** The two ellipses bulge above and below the rectangle, so the
  text block needs extra reserved height or it rides the bottom curve. Same class: any symbol
  whose outline is not a rectangle has less usable height than its bounding box.

- **Two labels on a decision's exits get written at the same point** if both are placed at the
  source's centre. Correct: place each on its own horizontal jog. And when one exit runs straight
  down, its label lands exactly on the jog lane the SIBLING edge uses — offset it past the lane.

- **A label that crosses a line stays readable if it carries its own background.** `stroke="#fff"
  stroke-width="3" paint-order="stroke"` gives text a halo. Cheaper than routing around it.

- **A party named inline cannot be retargeted.** Substituting through `spec["vars"]` needs TWO
  forms of each name: one for a title or a box that stands alone, one for mid-sentence. A single
  capitalised value produces "a simulated Client project", which reads as a typo and is invisible
  until the page is rendered.

- **A letter in a connector circle is a code, and a code never stands alone.** ISO's connector
  is conventionally an "A" paired with an "A". The first reader of the map asked "what are the A
  and B?" — which is the whole failure in one question. Correct: drop the letter, keep the small
  circle, and print the destination in words at each end ("to Classroom" / "from the trainer").
  A caption costs a few pixels of canvas; a lookup costs every reader forever.

- **A connector caption set to the RIGHT of its mark prints through the merge line.** A real edge
  always lands on the box CENTRE, so in a tight vertical gap the strip to the LEFT of the
  connector is the one place nothing else occupies. Same for the outbound caption: set alongside
  the circle it pushed the canvas 16% wider — and every glyph shrinks by that exact ratio — so it
  goes UNDER the circle instead, which cost 2.6%.

- **...and centred on that circle, the outbound caption still prints through its own box.** The
  entry above moved it under the circle to stop it widening the canvas, which was right, but the
  circle sits only 13px clear of the box, so half of any caption wider than 26px lands back over
  the border. The halo whites out GLYPHS, not the space BETWEEN two words — so the border
  reappears in exactly that gap and `to Foundry` reads as `to|Foundry`. Measured 2026-08-09:
  `to Start`, 36px wide, overlapped its own box by 5px. Correct: shift right by
  `max(0, tw/2 - 10)` — zero for captions that already clear it, exactly enough for the rest.
  Cost on the canonical: 710 -> 729, +2.7%, which is the same order as the 2.6% above.

- **A LIST title is accepted by `shapes.label()` and by nothing else.** `label()` normalises
  `[title] if isinstance(title, str) else title`, so the code reads as though a two-line title
  is supported — and forcing your own break is the obvious way to control where a long name
  wraps. It was not: `_fill()` calls `.replace()`, `_needed_height()` calls `.split()`, and
  `_short()` would interpolate the raw list into a caption. Declaring one died with
  `AttributeError: 'list' object has no attribute 'replace'` before anything was drawn. A
  half-implemented capability is worse than an absent one, because the implemented half reads
  as documentation. Fixed 2026-08-09 in all three. You rarely need it: a long title wraps on
  its own, and a list only earns its place when you want one SPECIFIC break.

## Checkers

- **A checker nobody has watched FAIL is decoration.** Every check in `check_map.py` is exercised
  against a chart broken on purpose before it is trusted. Its ancestor reported 0 of 21
  arrowheads valid on a correct diagram — twice, for two different reasons.

- **An arrowhead triangle's tip is the point FARTHEST from the other two, not nearest.** The two
  base corners of an 8px-wide head sit ~8px apart and the tip ~7.2px from each. Picking the
  nearest pair, or the maximum distance sum, both return a base corner.

- **A line terminating at an arrowhead ends at the base MIDPOINT, not a corner.** Checking
  endpoint-equals-corner reads every correct arrow as dangling.

- **A gate can pass because it ERRORED.** `grep -P` does not exist on BSD grep. Under `! grep
  ...`, the command's failure inverted into a pass and a check that never ran printed `ok`.
  Correct: negative-control every gate in both directions — clean input passes, broken input
  fails — and read the gate's OUTPUT, not only its exit code.

- **"No crossings" is necessary and nowhere near sufficient.** A line-vs-box checker reported
  CLEAN on a drawing that was called unreadable, because four edges routed as five-segment
  detours that visually merged. Two consequences: check line against LINE as well, and treat
  detour count as a LAYOUT signal — a detour means the boxes are in the wrong places, not that
  the router needs work.

- **A standalone `_map.svg` beside the document goes stale silently.** The document embeds the
  SVG inline, so the document can be current while the loose preview file — the one a human
  actually opens to look at the drawing — is three versions behind. Correct: write BOTH from the
  same build step, never by hand. Measured 2026-08-09: the reviewer opened `_map.svg` and saw a
  map two rebuilds old, with boxes that had already been cut.

## Method

- **If you are choosing coordinates, you are doing it wrong.** Three hand-placed layouts each
  fixed the previous one's crossings and introduced new ones. That pattern IS the diagnosis.

- **Declare feedback edges; do not let cycle removal guess.** DFS cuts whichever edge closes the
  cycle in its own traversal order. Measured: it cut the two edges FEEDING a cycle and left the
  return edge as forward flow.

- **Cutting a feedback edge can sink its source to the bottom layer.** ALAP places a node just
  above whatever it feeds; a node whose ONLY outgoing edge is the declared feedback edge has
  nothing left to feed once that edge is cut, so it becomes a sink and drops to the last layer.
  The drawing is correct and the long inbound edge looks odd. Found by the skill's own smoke test
  on a "cannot reproduce -> ask -> back to triage" branch. Correct: either accept it (the branch
  really is a leaf that loops back), or give the node a real forward edge to whatever follows it.

- **A planned-but-not-live node dead-ends in the middle of the map** and draws the question "what
  is this?". A control that does not run belongs in its ticket, not on a map of how things work
  today.

- **Verify against the rendered page, never only the source.** The last three defects of one
  round — an orphaned sentence fragment, a letterboxed image, and nine surplus sentences — were
  all invisible in the markup and obvious on screen. A sweep verified only against source is not
  verified.
