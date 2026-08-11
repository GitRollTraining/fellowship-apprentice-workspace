#!/usr/bin/env python3
"""Render a graph spec to inline SVG: ISO 5807 symbols, layered placement.

The caller declares WHAT connects to what. Nothing in the spec says where a box goes --
that is the whole point. Three hand-placed layouts failed before this, each one fixing the
previous one's crossings and introducing new ones.

    spec = {
      "title": str,
      "nodes": [{"id", "kind", "title", "subs": [str, ...]}],
      "edges": [(src, dst) or (src, dst, "label")],
      "feedback": [(src, dst), ...],     # edges the author knows close a loop
    }

Four things this file does that a naive layered renderer does not, each earned from a
defect seen in a rendered PDF rather than imagined:

  variable row heights   a row is only as tall as its tallest box needs. Uniform rows made
                         the map 1106px tall against 668 wide, and a 1.66 aspect does not
                         fit a portrait page -- the last row broke onto page 3.
  priority slots         dummy nodes and high-degree nodes claim their median position
                         first, so the spine runs straight instead of wandering a slot per
                         layer while supply boxes push it around.
  labels on the jog      a decision's exit labels were both written at the diamond's
                         bottom-centre, one on top of the other, unreadable.
  a reserved lane        connector circles sat exactly where horizontal jogs run, so a
                         circle and a merge line drew through each other.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import shapes
from layout import layout

NW = 196                  # node width
HMIN, HMAX = 40, 56       # row height bounds
HGAP, VGAP = 26, 34       # slot gap, layer gap
PAD = 14
JOG, LANE = 0.34, 0.70    # fraction of the gap: horizontal jogs, connector circles
STROKE = shapes.STROKE
LABEL_PX = 9.5
# a label that lands on a line stays readable if it carries its own background
HALO = 'stroke="#ffffff" stroke-width="3" paint-order="stroke"'


def _needed_height(nd):
    """How tall this box has to be for its own text. Measured at HMAX, which is the
    worst case for a stadium (its usable width shrinks as it gets taller)."""
    _, usable, _ = shapes.outline(nd.get("kind", "process"), 0, 0, NW, HMAX)
    title = nd["title"]
    tl = [ln for t in ([title] if isinstance(title, str) else title)
          for ln in shapes.wrap(t, shapes.TITLE_PX, True, usable)]
    sl = [ln for s in nd.get("subs", []) for ln in shapes.wrap(s, shapes.SUB_PX, False, usable)]
    pad = 24 if nd.get("kind") == "datastore" else 12   # a cylinder's caps eat its box
    return max(HMIN, min(HMAX, len(tl) * 15 + len(sl) * 13 + pad))


def _slots(res, by_layer):
    """Horizontal position. Order within a layer is FIXED by crossing reduction; this only
    chooses position, and never swaps -- that separation is what keeps chains vertical
    without reintroducing crossings.

    Nodes claim their median position in PRIORITY order: dummy nodes first, because a
    straight dummy chain is a straight long edge, then by degree.
    """
    width = max(len(v) for v in by_layer.values())
    slot = {}
    for L, ns in by_layer.items():
        start = (width - len(ns)) / 2
        for i, n in enumerate(ns):
            slot[n] = start + i
    nbr, deg = {n: [] for n in slot}, {n: 0 for n in slot}
    for s, t in res["edges"]:
        nbr[s].append(t)
        nbr[t].append(s)
        deg[s] += 1
        deg[t] += 1
    prio = {n: (2 if n in res["dummies"] else 1, deg[n]) for n in slot}

    for sweep in range(8):
        keys = sorted(by_layer) if sweep % 2 == 0 else sorted(by_layer, reverse=True)
        for L in keys:
            ns = by_layer[L]
            placed = set()
            for n in sorted(ns, key=lambda z: prio[z], reverse=True):
                i = ns.index(n)
                ps = sorted(slot[m] for m in nbr[n])
                if not ps:
                    continue
                want = ps[len(ps) // 2] if len(ps) % 2 else (ps[len(ps)//2 - 1] + ps[len(ps)//2]) / 2
                lo = max([slot[ns[j]] + (i - j) for j in range(i) if ns[j] in placed],
                         default=-1e9)
                hi = min([slot[ns[j]] - (j - i) for j in range(i + 1, len(ns)) if ns[j] in placed],
                         default=1e9)
                slot[n] = min(max(want, lo), hi)
                placed.add(n)
            # keep the whole chart inside the widest layer's span. Without this clamp the
            # priority pulls spread a 3-slot graph across 4 slots, and every glyph on the
            # page shrinks by the same ratio -- SVG text size is font-size / viewBox width.
            for i in range(1, len(ns)):          # restore the minimum gap, keeping order
                slot[ns[i]] = max(slot[ns[i]], slot[ns[i - 1]] + 1)
            over = slot[ns[-1]] - (width - 1)
            if over > 0:
                for n in ns:
                    slot[n] -= over
            under = -slot[ns[0]]
            if under > 0:
                for n in ns:
                    slot[n] += under
    lo = min(slot.values())
    return {n: s - lo for n, s in slot.items()}, width


def _fill(text, vars_):
    # shapes.label() takes a LIST title to force a line break. Everything upstream of it
    # assumed a str, so declaring one crashed here before it could ever be drawn.
    if isinstance(text, (list, tuple)):
        return [_fill(t, vars_) for t in text]
    for k, v in vars_.items():
        text = text.replace("{" + k + "}", v)
    return text


def render(spec):
    # One substitution point for the parties a chart names. A map that hardcodes its client
    # is a map that cannot be reused for the next one, and renaming a party by hand across
    # four nodes is how one of them gets missed.
    vars_ = spec.get("vars", {})
    if vars_:
        spec = dict(spec, nodes=[
            dict(n, title=_fill(n["title"], vars_),
                 subs=[_fill(x, vars_) for x in n.get("subs", [])])
            for n in spec["nodes"]],
            title=_fill(spec["title"], vars_),
            edges=[e[:2] + (_fill(e[2], vars_),) if len(e) > 2 else e for e in spec["edges"]])
    nodes = {n["id"]: n for n in spec["nodes"]}
    edges = [(e[0], e[1]) for e in spec["edges"]]
    elabel = {(e[0], e[1]): e[2] for e in spec["edges"] if len(e) > 2}
    for s, t in edges:
        assert s in nodes and t in nodes, f"edge names an unknown node: {s} -> {t}"

    feedback = [tuple(e) for e in spec.get("feedback", ())]
    res = layout(list(nodes), edges, feedback)
    by_layer = {L: res["order"][L] for L in res["order"]}
    slot, width = _slots(res, by_layer)

    # geometry: each row as tall as it needs, no taller
    rowh = {L: max((_needed_height(nodes[n]) for n in ns if n in nodes), default=HMIN)
            for L, ns in by_layer.items()}
    ytop, y = {}, PAD + 30
    for L in sorted(by_layer):
        ytop[L] = y
        y += rowh[L] + VGAP
    H = int(y - VGAP + PAD)
    # from the ACTUAL slots, not the widest layer: the priority pass moves nodes past
    # their layer's own span, and sizing from layer count clipped the right-hand column
    # clean off the page.
    W = int(PAD * 2 + max(slot.values()) * (NW + HGAP) + NW)

    xs = {n: PAD + slot[n] * (NW + HGAP) for n in slot}
    ys = {n: ytop[res["layer"][n]] for n in slot}
    hs = {n: rowh[res["layer"][n]] for n in slot}

    geom = {n: (xs[n], ys[n], NW, hs[n]) for n in nodes}
    segs = []
    body = [f'<text x="{PAD}" y="{PAD + 13}" font-size="13" font-weight="600" '
            f'fill="{STROKE}">{spec["title"]}</text>']
    for n, nd in nodes.items():
        kind = nd.get("kind", "process")
        svg, usable, dy = shapes.outline(kind, xs[n], ys[n], NW, hs[n], nd.get("shade", False))
        body.append(svg)
        body.append(shapes.label(kind, xs[n], ys[n], NW, hs[n],
                                 nd["title"], nd.get("subs", []), usable, dy))

    # every drawn segment joins adjacent layers, because dummies split the long ones
    nxt = {}
    for s, t in res["edges"]:
        nxt.setdefault(s, []).append(t)
    for s in sorted({a for a, _ in res["edges"]} - res["dummies"]):
        for t in nxt[s]:
            chain, cur = [s], t
            while cur in res["dummies"]:
                chain.append(cur)
                cur = nxt[cur][0]
            chain.append(cur)
            pts = []
            for i, n in enumerate(chain):
                cx = xs[n] + NW / 2
                pts.append((cx, ys[n] + hs[n] if i == 0 else
                            ys[n] if i == len(chain) - 1 else ys[n] + hs[n] / 2))
            body.append(_path(pts))
            segs.append((chain[0], chain[-1], _points(pts)))
            lab = elabel.get((chain[0], chain[-1]))
            if lab:
                body.append(_edge_label(pts, lab))

    # a declared feedback edge becomes a labelled pair of ISO connector circles.
    # Both sit OFF the box centre-line: a box that has a feedback edge usually has a real
    # edge too, and drawing both from the same point put the circle on top of the line.
    # The OUT circle sits beside its box, not under it. Under it, a feedback edge leaving
    # the bottom row pushed the drawing into the page footer -- and the source of a feedback
    # edge is very often in the bottom row, because that is where a loop turns around.
    # The circle is ISO's connector. The LETTER inside it is not -- a bare "A" is a code, and
    # a code never stands alone: the first reader of this map asked what A and B were. Each
    # end now carries its destination in words, so the pairing needs no lookup.
    # The inbound caption is right-anchored, so it grows the canvas LEFTWARD. Nothing
    # tracked that, and viewBox started at 0, so it was silently clipped off the page.
    minx = 0
    for s, t in feedback:
        ox, oy = xs[s] + NW + 13, ys[s] + hs[s] / 2
        ix, iy = xs[t] + NW * 0.28, ys[t] - VGAP * LANE
        body.append(f'<path d="M {xs[s]+NW} {oy:.0f} H {ox-8:.0f}" '
                    f'stroke="{STROKE}" stroke-width="1.4" fill="none"/>')
        body.append(_dot(ox, oy))
        # under the circle, not after it: a caption set alongside pushed the canvas 16% wider,
        # and every glyph on the page shrinks by exactly that ratio
        cap = f"to {_short(nodes[t])}"
        # Centred on the circle, half the caption sits back over the box, and the halo
        # whites out glyphs but NOT the space between two words -- so the border printed
        # through the gap in "to Foundry". Shift right by just enough to clear the box
        # by 3px: the circle is 13px out, so the caption's left edge lands at ox-10.
        shift = max(0.0, _tw(cap) / 2 - 10)
        body.append(f'<text x="{ox+shift:.0f}" y="{oy+16:.0f}" font-size="{LABEL_PX}" '
                    f'text-anchor="middle" {HALO} fill="{STROKE}">{cap}</text>')
        W = max(W, int(ox + shift + _tw(cap) / 2 + PAD))
        body.append(f'<path d="M {ix:.0f} {iy+8:.0f} V {ys[t]:.0f}" '
                    f'stroke="{STROKE}" stroke-width="1.4" fill="none"/>')
        body.append(_dot(ix, iy))
        # LEFT of the dot, right-aligned. A real edge always lands on the box CENTRE, so the
        # strip left of the connector is the one place in a tight gap nothing else occupies --
        # set to the right, this caption printed straight through the merge line into the box.
        body.append(f'<text x="{ix-9:.0f}" y="{iy+3:.0f}" font-size="{LABEL_PX}" '
                    f'text-anchor="end" {HALO} fill="{STROKE}">from {_short(nodes[s])}</text>')
        minx = min(minx, int(ix - 9 - _tw(f"from {_short(nodes[s])}") - PAD))
        body.append(_head(ix, ys[t]))

    res["geometry"], res["segments"] = geom, segs
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d 0 %d %d" width="100%%" '
            'font-family="Helvetica, Arial, sans-serif">\n%s\n</svg>'
            % (minx, W - minx, H, "\n".join(body))), res


def _points(pts):
    """The polyline actually drawn, as a list of corners -- the same arithmetic _path uses.
    Checking the drawing means checking THESE, not re-parsing the SVG string back out."""
    out = [(pts[0][0], pts[0][1])]
    for i in range(1, len(pts)):
        (x0, y0), (x1, y1) = pts[i - 1], pts[i]
        if abs(x1 - x0) >= 0.5:
            jy = y0 + (y1 - y0) * JOG
            out += [(x0, jy), (x1, jy)]
        out.append((x1, y1))
    return out


def _path(pts):
    d = [f"M {pts[0][0]:.0f} {pts[0][1]:.0f}"]
    for i in range(1, len(pts)):
        (x0, y0), (x1, y1) = pts[i - 1], pts[i]
        if abs(x1 - x0) < 0.5:
            d.append(f"V {y1:.0f}")
        else:
            d += [f"V {y0 + (y1 - y0) * JOG:.0f}", f"H {x1:.0f}", f"V {y1:.0f}"]
    return (f'<path d="{" ".join(d)}" stroke="{STROKE}" stroke-width="1.4" fill="none"/>'
            + _head(pts[-1][0], pts[-1][1]))


def _edge_label(pts, text):
    """On the horizontal jog if there is one, so a decision's two exits cannot collide."""
    (x0, y0), (x1, y1) = pts[0], pts[1]
    if abs(x1 - x0) < 0.5:
        return (f'<text x="{x0 + 7:.0f}" y="{y0 + (y1 - y0) * 0.78:.0f}" '
                f'font-size="{LABEL_PX}" {HALO} fill="{STROKE}">{text}</text>')
    jy = y0 + (y1 - y0) * JOG
    anchor = "end" if x1 < x0 else "start"
    ax = (x0 + x1) / 2
    return (f'<text x="{ax:.0f}" y="{jy - 5:.0f}" font-size="{LABEL_PX}" '
            f'text-anchor="middle" {HALO} fill="{STROKE}">{text}</text>')


def _head(x, y):
    return (f'<polygon points="{x:.0f},{y:.0f} {x-4:.0f},{y-8:.0f} {x+4:.0f},{y-8:.0f}" '
            f'fill="{STROKE}"/>')


def _dot(cx, cy):
    """The connector mark. Small and unlabelled -- the words beside it carry the meaning."""
    return (f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="4.5" fill="#ffffff" stroke="{STROKE}" '
            f'stroke-width="1.4"/>')


def _short(node):
    """What a connector caption calls this node. The SPEC says so via "short" -- guessing it
    from the title produced "to client", which reads as a typo."""
    name = node.get("short", node["title"])
    return name if isinstance(name, str) else " ".join(name)


def _tw(text):
    return shapes.width_of(text, LABEL_PX, False)
