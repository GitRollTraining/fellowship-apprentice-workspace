---
name: flowchart
description: Build a flowchart, system map or process diagram as validated inline SVG - ISO 5807 symbols, automatic layered placement, four self-tested checks. Use whenever a document needs a diagram.
argument-hint: <target-directory>
---

# Flowchart / System Map

> Declare WHAT connects to what. The layout engine decides where every box goes. Four checks
> then prove the drawing is sound before it reaches a page.
>
> Built 2026-08-08 from a map that took four attempts. The first three were hand-placed, and
> each one fixed the previous one's crossings while introducing new ones. That is the signal
> that placement is the defect: **if you are choosing coordinates, you are doing it wrong.**

## Why inline SVG

Mermaid does not render in the formal-PDF pipeline, and it does not render in a terminal.
Inline SVG renders everywhere a browser or pandoc runs. The cost is that you must place the
boxes — which is what `scripts/` removes.

## Workflow

1. **Copy the toolkit** into the caller's working directory:
   `mkdir -p <target>/flowchart && cp library/skills/flowchart/scripts/*.py <target>/flowchart/`
   (run from the repository root; the scripts travel with this repository, not with a home directory)
2. **Write the spec** as `<target>/flowchart/<name>-spec.py` — one file, the ONLY file that states
   content. Start from `references/symbols.md` to pick a symbol per node.
3. **Render**, passing both the spec and the intended output path:
   `python3 <target>/flowchart/render_to.py <target>/flowchart/<name>-spec.py <target>/<name>.svg`.
   `render_to.py` requires the spec argument; running it with no argument is an error.
4. **Check from the repository root**, using the same target paths:
   `python3 <target>/flowchart/check_map.py <target>/flowchart/<name>-spec.py` — it must print
   `CLEAN`. From another working directory, use absolute paths for both arguments. It self-tests first:
   three charts broken on purpose, each must make a check fire.
5. **LOOK AT THE RENDERED PAGE.** Not the SVG source. Every defect in the source list of
   `references/gotchas.md` was invisible in the markup and obvious on screen.
6. Iterate on the SPEC, never on coordinates.

## The one rule

**Nothing in the spec says where a box goes.** If you find yourself adding an `x`, a `row`, or
a `col` to a node, stop — the answer is a different edge set, a declared feedback edge, or a
node that should not be on this chart.

## Spec shape

```python
SPEC = {
  "title": "...",
  "vars": {"Client": "Client", "client": "client"},   # every party the chart names
  "nodes": [
    {"id": "a", "kind": "terminator", "title": "Request arrives", "subs": []},
    {"id": "b", "kind": "manual", "title": "{Client} review", "subs": ["check one case"]},
    {"id": "c", "kind": "document", "title": "Result recorded", "subs": []},
  ],
  "edges": [("a", "b"), ("b", "c", "label on the edge")],
  "feedback": [],                    # list only edges YOU know close a loop
}
```

**Name parties through `vars`, never inline.** A chart that hardcodes its client cannot be
reused for the next one, and renaming a party by hand across four nodes is how one of them gets
missed. Carry two forms — `{Client}` for a title or a standalone box, `{client}` for
mid-sentence — because "a simulated Client project" is wrong and only shows up on the page.

`kind` is one of: `terminator` `process` `decision` `manual` `predefined` `document` `io`
`datastore` `connector`. What each means and when to reach for it: `references/symbols.md`.

**Declare every feedback edge.** Left to guess, the cycle-removal pass cuts whichever edge its
own traversal reaches first — measured once, it cut the two edges that FED a cycle and left the
return edge as forward flow, sinking a supply chain below the pipeline it supplied.

## The four checks

| Check | Catches |
|---|---|
| boxes | a drawn segment passing through a box it does not start or end at |
| landing | an arrowhead floating in space or buried inside its target |
| crossings | line against LINE — the gap that made "no crossings" mean nothing |
| fit | text too big for its symbol; raised at draw time by `shapes.label` |

Each one is exercised against a chart broken on purpose before it is trusted. A checker nobody
has watched fail is decoration — this one's ancestor reported 0 of 21 arrowheads valid on a
correct diagram, twice.

## What "good" looks like

Zero crossings is necessary and nowhere near sufficient. A drawing can pass every check and
still be unreadable. The readable ones have: a spine that runs straight down, supply nodes
sitting next to what consumes them, every decision exit labelled, and loops closed by connector
circles rather than a line drawn back across the page.

## Gotchas

25 measured failures, each found in a rendered page: `references/gotchas.md`. Read it before
the first render, not after. The three that cost the most:

- **A blank line anywhere inside `<svg>` makes pandoc flatten the whole diagram to literal
  text.** It looks fine in the markdown. Assert on it.
- **On-page text size is `font-size / viewBox width`.** Taller rows do not enlarge type; fewer
  columns do. A chart that is "too tight" is usually too WIDE.
- **A gate can pass because it errored.** `grep -P` does not exist on BSD grep; under `! grep`,
  the failure inverted into a pass and a check that never ran reported ok.

## Layout knobs

Four phases, all in `scripts/layout.py`, each with the defect that earned it in its docstring:
cycle removal, ALAP layer assignment, crossing reduction (median + transpose + seeded restarts),
coordinate assignment. Background and the research it comes from: `references/layout.md`.

## Style

- Procedural skill; prescribes chart house style, not prose voice.
- House style: white fill, `#333333` 1px stroke, Georgia serif, 12px bold title over 10.5px
  detail. Change it in `shapes.py`, once, not per chart.
- Tested on: Opus 5, 2026-08-08/09, on a 21-box 24-edge system map rendered to a formal PDF,
  and a 9-box smoke chart built from scratch.
- Model floor: Sonnet 4 for spec authoring; the scripts are deterministic.

## Output

`{target}/flowchart/` with the toolkit plus one spec file, and the explicitly named SVG output that
`check_map.py` reports CLEAN on. The SVG is pasted inline into the document that needs it.

## Eval

**The eval fixture does not ship with this copy.** Upstream it is the 21-node map this skill was
extracted from, and that map is a named client's delivery architecture, so it stays where it is.

What this costs you: there is no baseline to re-run after a change to `scripts/`, so a change to the
layout or rendering code is unverified until someone builds one. A replacement is cheap — any process
diagram you have already drawn and checked by eye, saved as a spec plus its expected node and edge
counts, is a working baseline.

## Quality Guidelines

Adhere to the quality guidelines in `library/reference/agent-quality-guidelines.md` and structural
principles in `library/reference/skill-architecture.md`.
