#!/usr/bin/env python3
"""ISO 5807 flowchart symbols, drawn in the house style.

Shapes and their meanings are taken from the standard rather than invented:
ISO 5807:1985 "Information processing - Documentation symbols and conventions for data,
program and system flowcharts". Confirmed 2019.

  terminator   stadium / rounded      start or end of a process
  process      rectangle              an action, operation or transformation
  decision     diamond                a branch; EVERY outgoing edge must be labelled
  manual       trapezoid              a step a person performs
  predefined   rectangle, side bars   a procedure defined elsewhere (an SOP)
  document     rectangle, wavy foot   a produced report or document
  io           parallelogram          data in or out
  datastore    cylinder               a stored collection
  connector    small circle           a labelled jump elsewhere in the chart

House style, carried over from catalyte-ai_system-map: white fill, #333333 1px stroke,
Georgia serif, bold 12px title over 10.5px #333333 detail, arrows as a line plus an
explicit polygon head.
"""
import html

STROKE = "#333333"
TITLE_PX, SUB_PX = 12, 10.5
EM_BOLD, EM_REG = 0.545, 0.475
INSET = 12

KINDS = {"terminator", "process", "decision", "manual", "predefined",
         "document", "io", "datastore", "connector"}


def width_of(text, size, bold):
    return len(text) * size * (EM_BOLD if bold else EM_REG)


def wrap(text, size, bold, usable):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if width_of(w, size, bold) > usable:
            raise AssertionError(f"word {w!r} cannot fit {usable:.0f}px at {size}px")
        trial = f"{cur} {w}".strip()
        if width_of(trial, size, bold) <= usable:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def outline(kind, x, y, w, h, shade=False):
    """SVG for the symbol border. Returns (svg, usable_text_width, text_y_inset)."""
    fill = "#f2f2f2" if shade else "#ffffff"
    a = f'fill="{fill}" stroke="{STROKE}" stroke-width="1"'
    if kind == "process":
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {a}/>', w - 2 * INSET, 0
    if kind == "terminator":
        r = h / 2
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" {a}/>',
                w - 2 * INSET - r, 0)
    if kind == "decision":
        cx, cy = x + w / 2, y + h / 2
        pts = f"{cx},{y} {x+w},{cy} {cx},{y+h} {x},{cy}"
        return f'<polygon points="{pts}" {a}/>', w * 0.52, 0
    if kind == "manual":
        # trapezoid, narrower at the foot
        inset = w * 0.12
        pts = f"{x},{y} {x+w},{y} {x+w-inset},{y+h} {x+inset},{y+h}"
        return f'<polygon points="{pts}" {a}/>', w - 2 * INSET - inset, 0
    if kind == "predefined":
        bar = 9
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {a}/>'
                f'<line x1="{x+bar}" y1="{y}" x2="{x+bar}" y2="{y+h}" stroke="{STROKE}" stroke-width="1"/>'
                f'<line x1="{x+w-bar}" y1="{y}" x2="{x+w-bar}" y2="{y+h}" stroke="{STROKE}" stroke-width="1"/>',
                w - 2 * INSET - 2 * bar, 0)
    if kind == "document":
        wv = 10
        d = (f"M {x} {y} L {x+w} {y} L {x+w} {y+h-wv} "
             f"Q {x+w*0.75} {y+h} {x+w/2} {y+h-wv/2} "
             f"Q {x+w*0.25} {y+h-wv} {x} {y+h-wv} Z")
        return f'<path d="{d}" {a}/>', w - 2 * INSET, -wv / 2
    if kind == "io":
        sk = w * 0.10
        pts = f"{x+sk},{y} {x+w},{y} {x+w-sk},{y+h} {x},{y+h}"
        return f'<polygon points="{pts}" {a}/>', w - 2 * INSET - sk, 0
    if kind == "datastore":
        e = 8
        d = (f"M {x} {y+e} Q {x+w/2} {y-e/2} {x+w} {y+e} L {x+w} {y+h-e} "
             f"Q {x+w/2} {y+h+e/2} {x} {y+h-e} Z")
        return (f'<path d="{d}" {a}/>'
                f'<path d="M {x} {y+e} Q {x+w/2} {y+2*e} {x+w} {y+e}" fill="none" '
                f'stroke="{STROKE}" stroke-width="1"/>', w - 2 * INSET, e / 2)
    if kind == "connector":
        r = min(w, h) / 2
        cx, cy = x + w / 2, y + h / 2
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" {a}/>', r * 1.4, 0
    raise AssertionError(f"unknown symbol kind {kind!r}")


def label(kind, x, y, w, h, title, subs, usable, dy):
    tl = [ln for t in ([title] if isinstance(title, str) else title)
          for ln in wrap(t, TITLE_PX, True, usable)]
    sl = [ln for s in subs for ln in wrap(s, SUB_PX, False, usable)]
    block = len(tl) * 15 + len(sl) * 13
    if block > h - 8:
        raise AssertionError(f"{title!r}: {len(tl)}+{len(sl)} lines need {block}px, box is {h}px")
    out, cx = [], x + w / 2
    ty = y + (h - block) / 2 + 12 + dy
    for t in tl:
        out.append(f'<text x="{cx:.0f}" y="{ty:.0f}" font-family="Georgia, serif" '
                   f'font-size="{TITLE_PX}" font-weight="bold" fill="#000000" '
                   f'text-anchor="middle">{html.escape(t)}</text>')
        ty += 15
    for s in sl:
        out.append(f'<text x="{cx:.0f}" y="{ty:.0f}" font-family="Georgia, serif" '
                   f'font-size="{SUB_PX}" fill="{STROKE}" text-anchor="middle">{html.escape(s)}</text>')
        ty += 13
    return "".join(out)
