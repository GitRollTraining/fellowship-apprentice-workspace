#!/usr/bin/env python3
"""Validate a rendered chart.  Usage: check_map.py [spec.py]

 Four checks, each one earned from a defect in a printed PDF.

    boxes        no drawn segment passes through a box it does not start or end at
    landing      every arrowhead tip sits on its target box's edge, not floating or inside
    crossings    no two segments cross each other
    fit          every label fits its symbol  (asserted at draw time, in shapes.label)

The third check is here because the first three passes of this map had FOUR line-on-line
collisions while "no crossings" was reported clean -- the checker only ever tested lines
against boxes, so a defect it could not see read as an absence of defects.

Exit 0 clean, 1 with a numbered list of what is wrong and where.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

EPS = 0.6


def _seg_box(p, q, box, pad=-1.0):
    """Does segment p-q pass through the box interior (shrunk by `pad`)?"""
    x, y, w, h = box
    x0, y0, x1, y1 = x - pad, y - pad, x + w + pad, y + h + pad
    (ax, ay), (bx, by) = p, q
    t0, t1 = 0.0, 1.0
    dx, dy = bx - ax, by - ay
    for pv, qv in ((-dx, ax - x0), (dx, x1 - ax), (-dy, ay - y0), (dy, y1 - ay)):
        if abs(pv) < 1e-9:
            if qv < 0:
                return False
        else:
            r = qv / pv
            if pv < 0:
                t0 = max(t0, r)
            else:
                t1 = min(t1, r)
    return t0 < t1 - 1e-9


def _cross(a, b, c, d):
    """Do segments a-b and c-d properly cross (not merely touch at an endpoint)?"""
    def o(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)
    if len({tuple(a), tuple(b)} & {tuple(c), tuple(d)}):
        return False
    o1, o2, o3, o4 = o(a, b, c), o(a, b, d), o(c, d, a), o(c, d, b)
    return o1 != o2 and o3 != o4 and 0 not in (o1, o2, o3, o4)


def check(res):
    geom, segs = res["geometry"], res["segments"]
    bad = []

    for src, dst, pts in segs:
        for i in range(len(pts) - 1):
            for n, box in geom.items():
                if n in (src, dst):
                    continue
                if _seg_box(pts[i], pts[i + 1], box):
                    bad.append(f"edge {src}->{dst} segment {i} passes through box {n}")

    for src, dst, pts in segs:
        tx, ty = pts[-1]
        x, y, w, h = geom[dst]
        on_edge = (abs(ty - y) < EPS or abs(ty - (y + h)) < EPS) and x - EPS <= tx <= x + w + EPS
        on_side = (abs(tx - x) < EPS or abs(tx - (x + w)) < EPS) and y - EPS <= ty <= y + h + EPS
        if not (on_edge or on_side):
            bad.append(f"edge {src}->{dst} arrowhead at ({tx:.0f},{ty:.0f}) "
                       f"does not land on {dst} at ({x:.0f},{y:.0f},{w},{h})")

    flat = [(s, d, pts[i], pts[i + 1]) for s, d, pts in segs for i in range(len(pts) - 1)]
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            s1, d1, a, b = flat[i]
            s2, d2, c, e = flat[j]
            if _cross(a, b, c, e):
                bad.append(f"edge {s1}->{d1} crosses edge {s2}->{d2} "
                           f"near ({(a[0]+b[0])/2:.0f},{(c[1]+e[1])/2:.0f})")
    return bad


def _selftest():
    """A checker nobody has watched FAIL is not a checker. Build a chart that is wrong on
    purpose and assert each check fires."""
    res = {"geometry": {"a": (0, 0, 100, 40), "b": (0, 200, 100, 40), "c": (0, 100, 100, 40)},
           "segments": [("a", "b", [(50, 40), (50, 200)])]}
    assert any("through box c" in m for m in check(res)), "box check did not fire"
    res2 = {"geometry": {"a": (0, 0, 100, 40), "b": (0, 200, 100, 40)},
            "segments": [("a", "b", [(50, 40), (50, 150)])]}
    assert any("does not land" in m for m in check(res2)), "landing check did not fire"
    res3 = {"geometry": {"a": (0, 0, 100, 40), "b": (0, 200, 100, 40),
                         "c": (200, 0, 100, 40), "d": (200, 200, 100, 40)},
            "segments": [("a", "d", [(50, 40), (250, 200)]), ("c", "b", [(250, 40), (50, 200)])]}
    assert any("crosses edge" in m for m in check(res3)), "crossing check did not fire"
    assert not check({"geometry": {"a": (0, 0, 100, 40), "b": (0, 200, 100, 40)},
                      "segments": [("a", "b", [(50, 40), (50, 200)])]}), "false positive on a clean chart"
    print("  check_map self-test: all four fire, none false-positive")


if __name__ == "__main__":
    _selftest()
    import importlib.util
    spec_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "map_spec.py").resolve()
    sys.path.insert(0, str(spec_path.parent))
    m = importlib.util.spec_from_file_location(spec_path.stem, spec_path)
    mod = importlib.util.module_from_spec(m)
    m.loader.exec_module(mod)
    from render import render
    _, res = render(mod.SPEC)
    bad = check(res)
    if bad:
        print(f"FAIL - {len(bad)} defect(s):")
        for i, m in enumerate(bad, 1):
            print(f"  {i}. {m}")
        sys.exit(1)
    print(f"CLEAN - {len(res['segments'])} edges, {len(res['geometry'])} boxes, "
          f"{res['crossings']} layout crossings")
