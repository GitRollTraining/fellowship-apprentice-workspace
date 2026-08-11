#!/usr/bin/env python3
"""Render a spec to an SVG file.  Usage: render_to.py <spec.py> [out.svg]

Kept separate from render.py so the drawing code has no opinion about where output lands.
"""
import importlib.util
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from render import render

spec_path = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else spec_path.with_suffix(".svg")
m = importlib.util.spec_from_file_location(spec_path.stem, spec_path)
mod = importlib.util.module_from_spec(m)
m.loader.exec_module(mod)

svg, res = render(mod.SPEC)
assert "\n\n" not in svg, "blank line inside <svg> - pandoc would flatten it to literal text"
out.write_text(svg, encoding="utf-8")
print(f"{out.name}: {len(mod.SPEC['nodes'])} nodes, {len(mod.SPEC['edges'])} edges, "
      f"{len(res['dummies'])} dummies, {res['crossings']} crossings, "
      f"{len(res['back_edges'])} connector pair(s), "
      f"viewBox {svg.split('viewBox=')[1].split(chr(34))[1]}")
