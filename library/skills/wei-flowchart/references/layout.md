# Layered layout — the Sugiyama framework

The question this answers: *when a chart scales, how do nodes and edges end up in good places
without anyone choosing coordinates?*

The answer is not new. Layered graph drawing has a standard four-phase framework, usually named
after Sugiyama, and `scripts/layout.py` implements it in about 200 lines with no dependency.

Graphviz (`dot`) implements the same framework and is the right choice if it is installed. It was
not installed on the machine this was built on — `dot`, `neato`, `sfdp`, python `graphviz` and
`pydot` all absent — and installing it was not worth a Homebrew dependency for one chart. If it
is available and the chart is large, prefer it.

## Phase 1 — cycle removal

A layered drawing needs a directed acyclic graph. Real processes have loops.

**`layout.py` takes the loop edges from the CALLER**, via `spec["feedback"]`, and cuts those
first. A DFS pass still runs afterwards so an undeclared cycle is caught rather than hanging.

Why the caller decides: DFS cuts whichever edge closes the cycle in its own traversal order,
which is arbitrary. Measured on the map this came from, DFS cut the two edges that *fed* the
weekly cycle — a curriculum into an assignment, a rubric into an engine — and left the trainer's
return edge as forward flow. The supply chain sank below the pipeline it supplies and the chart
went from three slots wide to five.

Cut edges are drawn as ISO connector pairs rather than reversed arrows, which is the standard's
own device and reads better than an arrow pointing the wrong way.

## Phase 2 — layer assignment

Every edge must point down at least one layer.

Two standard choices. **ASAP** (longest path from the sources) is the textbook first cut and it
is wrong for a chart with supply nodes: anything with no incoming edge is pinned to layer 0, and
a long edge runs from there down to wherever it is consumed. Long edges become dummy chains,
dummy chains occupy horizontal slots, and the chart widens to carry lines that need not exist.

**ALAP** (as late as possible, from the sinks) places each supply artifact directly above what
consumes it. Measured on the same graph: ASAP gave a five-wide layer and 15 dummy nodes, ALAP
gave three and two.

`layout.py` uses ALAP. If a chart ever wants ASAP — a timeline where sources genuinely belong at
the top — `assign_layers()` is still there beside it.

## Dummy nodes

An edge spanning more than one layer is split into a chain through invisible dummy nodes, so
**every drawn segment joins adjacent layers**. This is what removes long edges structurally,
rather than routing around them afterwards. Three hand-placed layouts failed at exactly that: a
router that detours around obstacles produces five-segment corridors that merge into each other
visually, and the count of those detours is a better readability signal than the count of
crossings.

## Phase 3 — crossing reduction

Ordering within each layer, by the **median heuristic**: place each node at the median position
of its neighbours in the adjacent layer, sweeping down then up, keeping the best result. Gansner
et al. use a weighted median with a DFS initial ordering; the plain median is enough at this
size.

Two additions, both earned:

- **Transpose** — swap adjacent pairs while it helps. The median heuristic alone cannot see a
  crossing that a single swap would fix, because it only ever moves a node to a median.
- **Seeded restarts** — median plus transpose is hill climbing. On a 21-node graph it parked in
  a local minimum of one crossing that needed THREE simultaneous swaps to escape: every single
  swap on the way out made the count worse. 24 shuffled restarts reach zero. The seed is fixed
  because the SVG gets committed and diffed, and a layout that moves on every run is unreviewable.

## Phase 4 — coordinate assignment

Brandes and Köpf, *Fast and Simple Horizontal Coordinate Assignment* (GD 2001), is the reference
implementation. `layout.py` does something simpler that is adequate below ~40 nodes: the
**priority method**. Each node claims the median position of its neighbours, in priority order —
dummy nodes first, because a straight dummy chain is a straight long edge, then by degree. Order
within the layer is already fixed by phase 3 and is never changed here; only position is chosen.

Two constraints on top, both from observed damage:

- **Clamp the spread to the widest layer.** Without it the priority pulls spread a three-slot
  graph across four, and every glyph on the page shrinks by the same ratio, because SVG text size
  on the page is `font-size / viewBox width`.
- **Size the canvas from the ACTUAL slots**, not from the layer count. The priority pass moves
  nodes past their own layer's span, and sizing from the count clipped the right-hand column
  clean off the page.

## Vertical sizing

Rows are as tall as their tallest box needs, not uniform. Uniform rows made a 21-box map 1106
tall against 668 wide, and a 1.66 aspect does not fit a portrait page — the last row broke onto
the next one. Per-row heights brought the same content to one page with no change to type size.

## When this framework is the wrong tool

- **A chart with no direction** — an entity-relationship or a network — wants a force-directed
  layout, not layers.
- **Genuinely more than ~40 nodes** — install graphviz. The restart loop here is O(restarts x
  sweeps x crossings) and crossings is quadratic in edges.
- **A chart deeper than about 12 layers.** No layout engine fixes a portrait page holding 20
  sequential steps. Split it at a meaningful seam and join the halves with a connector pair —
  which is, again, what connectors are for.
