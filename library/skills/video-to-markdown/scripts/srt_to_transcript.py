#!/usr/bin/env python3
"""Caption-track .srt -> transcript.json. Merges consecutive same-speaker cells
(a recorder's caption track is a rolling window, not a list of segments)."""
import argparse, json, re, sys

def ts(s):
    h, m, rest = s.split(":")
    sec, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000

def parse(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    cells = []
    for block in re.split(r"\n\s*\n", txt.strip()):
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        if len(lines) < 2 or "-->" not in lines[1]:
            continue
        t0s, t1s = [x.strip() for x in lines[1].split("-->")]
        speaker = None
        body = lines[2:]
        if body and re.fullmatch(r"\(.+\)", body[0]):
            speaker = body[0][1:-1]
            body = body[1:]
        cells.append({"t0": ts(t0s), "t1": ts(t1s),
                      "speaker": speaker, "text": " ".join(body)})
    return cells

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("srt"); ap.add_argument("out")
    ap.add_argument("--t-offset", type=float, default=0.0)
    ap.add_argument("--src", required=True)
    ap.add_argument("--window", nargs=2, type=float, default=None,
                    help="slice [T0 T1] then rebase to 0")
    ap.add_argument("--max-seg", type=float, default=30.0)
    ap.add_argument("--append", action="store_true")
    a = ap.parse_args()

    cells = parse(a.srt)
    if a.window:
        w0, w1 = a.window
        cells = [c for c in cells if c["t1"] > w0 and c["t0"] < w1]
        for c in cells:
            c["t0"] = max(0.0, c["t0"] - w0)
            c["t1"] = min(w1 - w0, c["t1"] - w0)

    segs = []
    for c in cells:
        if (segs and c["speaker"] == segs[-1]["speaker"]
                and c["t0"] - segs[-1]["t1"] <= 1.0
                and c["t1"] - segs[-1]["t0"] <= a.max_seg):
            segs[-1]["t1"] = c["t1"]
            segs[-1]["text"] += " " + c["text"]
        else:
            segs.append(dict(c))

    out = [{"t0": round(s["t0"] + a.t_offset, 2),
            "t1": round(s["t1"] + a.t_offset, 2),
            "text": (f"{s['speaker']}: " if s["speaker"] else "") + s["text"].strip(),
            "src": a.src} for s in segs if s["text"].strip()]

    existing = []
    if a.append:
        try:
            existing = json.load(open(a.out))
        except FileNotFoundError:
            pass
    json.dump(existing + out, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"cells={len(cells)} segments={len(out)} -> {a.out}")

if __name__ == "__main__":
    main()
