# Eval baseline

## Canonical input

`eval/canonical_spec.py` — the Catalyte AI end-to-end system map, the chart this skill was
extracted from. 21 nodes across 8 of the 9 symbol kinds, 24 edges, 2 declared feedback edges,
one labelled decision, a `vars` dict that names the client in two forms, and `short` names
for the four nodes a connector caption refers to.

It is a good canonical input because it exercises every part of the pipeline: a decision with
labelled exits, two loops closed by connectors, supply nodes that ALAP has to pull down beside
their consumers, a long edge that needs dummy nodes, and boxes whose text only just fits.

## Run

```bash
cd ~/.claude/skills/wei-flowchart/scripts
python3 render_to.py ../eval/canonical_spec.py /tmp/wf_eval.svg
python3 check_map.py ../eval/canonical_spec.py
```

No virtualenv. The toolkit is standard library only — `html`, `pathlib`, `random`, `sys`,
`collections`. If a run ever needs a dependency, that is itself a regression.

## Acceptance criteria

| Signal | Required | Why this number |
|---|---|---|
| `render_to.py` nodes / edges | 21 / 24 | the spec is the fixture; a change here means the fixture moved |
| dummies | 3 | ALAP working. ASAP layering gives 15 — a jump means phase 2 regressed |
| crossings | **0** | median + transpose + 24 seeded restarts. 1 means the restart loop broke |
| connector pairs | 2 | both feedback edges honoured. 3 means DFS is cutting edges the caller declared forward |
| viewBox | `0 0 729 1034` | exact. Width drift means the slot clamp or canvas sizing changed, and width is what sets on-page text size |
| `check_map.py` first line | `check_map self-test: all four fire, none false-positive` | the checks are still checks |
| `check_map.py` verdict | `CLEAN - 22 edges, 21 boxes, 0 layout crossings` | 22 drawn = 24 spec minus 2 connector pairs |

Any deviation is a regression until proven otherwise. If a change to `scripts/` is deliberate,
re-render, LOOK AT THE PAGE, and update the numbers here in the same commit — never update the
baseline to match output nobody looked at.

### Why the width moved, 2026-08-09

`710` -> `729`, +2.7%, and every glyph shrinks by that same ratio. Deliberate: the outbound
connector caption used to be centred on its circle, which put half of it back over its own
box, and the halo whites out glyphs but not the space between two words -- so the box border
printed through the gap in `to Foundry`. The caption now shifts right by exactly enough to
clear the box by 3px, which costs width only for captions wide enough to have overlapped.
The cost lands next to the 2.6% this skill already accepted for the under-the-circle
decision, and the canonical was re-rendered and LOOKED AT before this number was changed.
Height is unchanged, so the one-page claim below still holds (the drawing got wider, not
taller, so at a fixed page width it is now shorter).

## Known-good render

Recorded 2026-08-08 on Opus 5, python 3.14.5, macOS. Re-verified 2026-08-09 after the three
connector/title fixes: 21/24, 3 dummies, 0 crossings, 2 pairs, CLEAN, and the rendered page
checked by eye -- both inbound captions fully on-canvas, both outbound captions clear of
their boxes. The same spec rendered into a formal PDF
occupies exactly one page with no clipping, no line-on-line collision, and no text outside its
symbol.

## Negative controls

`check_map.py` self-tests on every run: three charts broken on purpose (a segment through a box,
an arrowhead landing on nothing, two edges crossing) plus one clean chart that must not
false-positive. If any of the four assertions stops firing, the checker has silently become
decoration — that has happened twice to an earlier version of it.
