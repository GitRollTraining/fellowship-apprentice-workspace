# Symbol vocabulary — ISO 5807:1985

The standard is *Information processing — Documentation symbols and conventions for data,
program and system flowcharts*, published 1985, reviewed and confirmed 2019. It defines 19
symbols. Nine are implemented in `scripts/shapes.py`; the rest were not needed and can be added
the same way.

Using the standard set is not pedantry. It means a reader who has ever seen a flowchart already
knows what a shape means, so the diagram needs no legend of invented conventions. Where a legend
still helps — an external audience, a shape like the cylinder that is common in engineering and
not elsewhere — state what the symbol IS. Never state how not to read it.

## The nine implemented

| `kind` | Shape | Means | Reach for it when |
|---|---|---|---|
| `terminator` | stadium, fully rounded ends | start or end of a flow | the person or thing entering the process, and where they leave it |
| `process` | plain rectangle | an action, operation or transformation | the default. A step the system performs |
| `decision` | diamond | a branch | there is a condition. **Every exit must be labelled** |
| `manual` | trapezoid, narrower at the foot | an operation performed by a person | a human gate: an interview, an approval, a review |
| `predefined` | rectangle with side bars | a procedure defined elsewhere | an SOP, a written standard, a body of work with its own document |
| `document` | rectangle with a wavy foot | a produced report or document | something a named person reads: a dashboard, a passport, a rubric |
| `io` | parallelogram | data in or out | data crossing the boundary of the system |
| `datastore` | cylinder | a stored collection | a catalog, a database, a registry |
| `connector` | small circle with a letter | the flow continues at the matching circle | a loop, or any jump that would otherwise be a line drawn across the chart |

## Conventions taken from the standard

1. **Direction is top-to-bottom and left-to-right.** The layout engine enforces top-to-bottom by
   construction: layers run downward and every drawn segment joins adjacent layers.
2. **Every output path of a decision carries a label.** This is a rule, not a preference. An
   unlabelled branch is the single most common reason a reader asks "why do some go this way?"
   — which is exactly the question that produced this skill.
3. **Connectors exist to avoid crossed lines and improve readability.** They are the standard's
   own answer to a long edge, so a feedback loop drawn as a connector pair is more correct than
   one drawn as a line running the height of the page, not a compromise.

## Choosing between two plausible symbols

- **`manual` vs `process`** — ask who performs the step. If a person's judgement is what moves
  the flow on, it is `manual`. This replaces the ad-hoc habit of shading a box grey to mean
  "human gate", which requires a legend and the trapezoid does not.
- **`predefined` vs `document`** — a `predefined` is a method someone follows; a `document` is an
  artifact someone reads. A written standard is `predefined`. The rubric it produces is a
  `document`.
- **`datastore` vs `document`** — a `datastore` is queried, a `document` is read start to finish.
- **`terminator` for an external party.** ISO has no symbol for an actor. A stadium reads as
  "where the flow enters or leaves our control", which is what an external party usually is.

## House style

White fill, `#333333` 1px stroke, Georgia serif, 12px bold title over 10.5px detail, arrows as a
line plus an explicit polygon head. It lives in `shapes.py` as module constants — change it once
there, never per chart.

`shade=True` on a node fills it `#f2f2f2`. Prefer a correct symbol over a shade: a shade needs a
legend, and a legend is a lookup charged to the reader.

## Text fitting

`shapes.outline()` returns the usable text width for its symbol, which is NOT the box width —
a diamond gives about half, a trapezoid and a `predefined` less than a rectangle. `shapes.label()
raises` when the wrapped text will not fit rather than drawing over the border.

That assertion is load-bearing. A silent overflow is invisible in the SVG source and survives all
the way to the printed page.
