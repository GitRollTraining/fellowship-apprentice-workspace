#!/usr/bin/env python3
"""Layered graph layout - the Sugiyama framework, top to bottom.

Four phases, as in the literature:

  1. cycle removal      back edges found by DFS. They are NOT reversed; each becomes a
                        pair of ISO 5807 connector circles, which is the standard's own
                        answer to an edge that would otherwise cross the whole chart.
  2. layer assignment   longest path from the sources, so every edge points down a layer.
  3. crossing reduction alternating up/down sweeps placing each node at the MEDIAN of its
                        neighbours' positions (Di Battista et al.), best order kept.
  4. coordinates        nodes centred within their layer.

Edges spanning more than one layer get DUMMY nodes in the layers between, so every drawn
segment joins adjacent layers. That is what removes long edges structurally, rather than
routing around them afterwards -- three hand-placed layouts failed at exactly that.

Reference: Sugiyama's framework; median heuristic for crossing reduction; Brandes and Koepf
for horizontal coordinates (not implemented here - simple centring is enough at this size).
"""
import random
from collections import defaultdict


def find_back_edges(nodes, edges):
    """DFS; an edge to a node on the current recursion stack closes a cycle."""
    adj = defaultdict(list)
    for s, t, *_ in edges:
        adj[s].append(t)
    colour, back = {}, set()

    def visit(n):
        colour[n] = 1
        for m in adj[n]:
            c = colour.get(m, 0)
            if c == 1:
                back.add((n, m))
            elif c == 0:
                visit(m)
        colour[n] = 2

    for n in nodes:
        if colour.get(n, 0) == 0:
            visit(n)
    return back


def assign_layers(nodes, edges):
    """Longest path: layer(v) = 1 + max(layer(u)) over incoming u."""
    incoming = defaultdict(list)
    for s, t in edges:
        incoming[t].append(s)
    layer, changed = {n: 0 for n in nodes}, True
    for _ in range(len(nodes) + 1):
        changed = False
        for n in nodes:
            want = max((layer[u] + 1 for u in incoming[n]), default=0)
            if want != layer[n]:
                layer[n] = want
                changed = True
        if not changed:
            break
    assert not changed, "layer assignment did not converge - graph still has a cycle"
    return layer


def assign_layers_alap(nodes, edges):
    """As late as possible: layer(v) = min(layer(w)) - 1 over outgoing w, then normalised.

    ASAP (longest path from the sources) is the textbook first cut and it is wrong for this
    shape of chart. It pins every supply artifact -- a standard, a curriculum, a rubric -- at
    layer 0 because nothing feeds it, then runs a long edge down to wherever it is consumed.
    Long edges become dummy chains, dummy chains occupy slots, and the whole chart widens to
    carry lines that ALAP does not create in the first place.

    Measured on this map: ASAP gives a 5-wide layer and 15 dummies; ALAP gives 3 and 2.
    """
    outgoing = defaultdict(list)
    for s, t in edges:
        outgoing[s].append(t)
    layer = {n: 0 for n in nodes}
    for _ in range(len(nodes) + 1):
        changed = False
        for n in nodes:
            want = min((layer[w] - 1 for w in outgoing[n]), default=0)
            if want != layer[n]:
                layer[n] = want
                changed = True
        if not changed:
            break
    assert not changed, "ALAP did not converge - graph still has a cycle"
    lo = min(layer.values())
    return {n: L - lo for n, L in layer.items()}


def add_dummies(edges, layer):
    """Split every edge spanning >1 layer into a chain through dummy nodes."""
    out, dummies = [], []
    for s, t in edges:
        span = layer[t] - layer[s]
        if span <= 1:
            out.append((s, t))
            continue
        prev = s
        for k in range(1, span):
            d = f"__dummy_{s}_{t}_{k}"
            dummies.append((d, layer[s] + k))
            out.append((prev, d))
            prev = d
        out.append((prev, t))
    return out, dummies


def order_within_layers(layers, edges, sweeps=8, restarts=24):
    """Median heuristic + adjacent-swap transpose, from `restarts` seeded starting orders.

    Restarts are not padding. Median-plus-transpose is hill climbing, and on this map it
    parked in a local minimum of one crossing that needed THREE simultaneous swaps to
    escape -- every single swap on the way out made the count worse, so no amount of
    sweeping found it. Seeded shuffles reach it; the seed keeps the output reproducible,
    which matters because the SVG is committed and diffed.
    """
    rng = random.Random(0)
    best, best_x = None, None
    for k in range(restarts):
        start = {L: list(ns) for L, ns in layers.items()}
        if k:
            for L in start:
                rng.shuffle(start[L])
        o, x = _one_pass(start, edges, sweeps)
        if best_x is None or x < best_x:
            best, best_x = o, x
        if best_x == 0:
            break
    return best, best_x


def _one_pass(order, edges, sweeps):
    succ, pred = defaultdict(list), defaultdict(list)
    for s, t in edges:
        succ[s].append(t)
        pred[t].append(s)
    order = {L: list(ns) for L, ns in order.items()}
    best, best_x = {L: list(v) for L, v in order.items()}, count_crossings(order, edges)
    for it in range(sweeps):
        keys = sorted(order) if it % 2 == 0 else sorted(order, reverse=True)
        for L in keys:
            ref = pred if it % 2 == 0 else succ
            pos = {n: i for k in order for i, n in enumerate(order[k])}
            def median(n):
                ps = sorted(pos[m] for m in ref[n] if m in pos)
                if not ps:
                    return pos[n]
                return ps[len(ps) // 2] if len(ps) % 2 else (ps[len(ps)//2 - 1] + ps[len(ps)//2]) / 2
            order[L] = sorted(order[L], key=median)
        transpose(order, edges)
        x = count_crossings(order, edges)
        if x < best_x:
            best_x, best = x, {L: list(v) for L, v in order.items()}
    return best, best_x


def transpose(order, edges):
    """Swap adjacent pairs while it helps. The median heuristic alone leaves local
    crossings it cannot see -- measured here, one -- because it only ever moves a node to
    its neighbours' median and never tries the swap that would beat it."""
    improved = True
    while improved:
        improved = False
        for L in sorted(order):
            for i in range(len(order[L]) - 1):
                before = count_crossings(order, edges)
                order[L][i], order[L][i + 1] = order[L][i + 1], order[L][i]
                if count_crossings(order, edges) < before:
                    improved = True
                else:
                    order[L][i], order[L][i + 1] = order[L][i + 1], order[L][i]


def count_crossings(order, edges):
    pos = {n: i for L in order for i, n in enumerate(order[L])}
    layer_of = {n: L for L in order for n in order[L]}
    by_layer = defaultdict(list)
    for s, t in edges:
        if s in layer_of and t in layer_of:
            by_layer[layer_of[s]].append((pos[s], pos[t]))
    total = 0
    for pairs in by_layer.values():
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                (a1, b1), (a2, b2) = pairs[i], pairs[j]
                if (a1 - a2) * (b1 - b2) < 0:
                    total += 1
    return total


def layout(nodes, edges, feedback=()):
    """nodes: list of ids. edges: list of (src, dst). Returns positions + metadata.

    `feedback` names the edges the AUTHOR knows close a loop. They are cut first.

    Leaving that to DFS is a real defect, not a nicety: DFS cuts whichever edge happens to
    close the cycle in its own traversal order. Measured on this map, it cut the two edges
    that FEED the weekly cycle -- a curriculum into the assignment, a rubric into the engine
    -- and left the trainer's return edge as forward flow. The supply chain then sank below
    the pipeline it supplies, and the chart went from 3 slots wide to 5.

    DFS still runs afterwards, so an undeclared cycle is caught rather than hanging.
    """
    back = set(feedback) | find_back_edges(nodes, [e for e in edges if e not in set(feedback)])
    forward = [(s, t) for s, t in edges if (s, t) not in back]
    layer = assign_layers_alap(nodes, forward)
    split, dummies = add_dummies(forward, layer)
    for d, L in dummies:
        layer[d] = L
    layers = defaultdict(list)
    for n in sorted(layer, key=lambda x: (layer[x], str(x))):
        layers[layer[n]].append(n)
    order, crossings = order_within_layers(dict(layers), split)
    return {
        "layer": layer,
        "order": order,
        "edges": split,
        "dummies": {d for d, _ in dummies},
        "back_edges": back,
        "crossings": crossings,
    }
