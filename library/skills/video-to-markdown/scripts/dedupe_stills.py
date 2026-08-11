#!/usr/bin/env python3
"""Merge consecutive near-identical stills (same src). Conservative: BOTH
histogram TV-distance AND changed-pixel ratio must be tiny. Keeps the LATER
rep frame (most settled), extends span back to the earlier t0."""
import argparse, json, os, sys
import cv2
import numpy as np

def load_gray(path, w=480):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        sys.exit(f"unreadable: {path}")
    h = int(img.shape[0] * w / img.shape[1])
    return cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)

def metrics(a, b, mask=None):
    if a.shape != b.shape:
        b = cv2.resize(b, (a.shape[1], a.shape[0]))
    if mask is not None:
        if mask.shape != a.shape:
            mask = cv2.resize(mask.astype("uint8"), (a.shape[1], a.shape[0])) > 0
        a = a.copy(); b = b.copy()
        a[mask] = 0; b[mask] = 0
    ha = np.bincount(a.ravel() >> 2, minlength=64).astype(np.float64)
    hb = np.bincount(b.ravel() >> 2, minlength=64).astype(np.float64)
    hist = 0.5 * np.abs(ha / ha.sum() - hb / hb.sum()).sum()
    ratio = float((np.abs(a.astype(np.int16) - b.astype(np.int16)) > 8).mean())
    return hist, ratio

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir")
    ap.add_argument("--hist-thr", type=float, default=0.008)
    ap.add_argument("--ratio-thr", type=float, default=0.02)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    jpath = os.path.join(a.outdir, "stills.json")
    stills = json.load(open(jpath))
    mpath = os.path.join(a.outdir, "mask.png")
    mask = None
    if os.path.exists(mpath):
        mask = cv2.imread(mpath, cv2.IMREAD_GRAYSCALE) > 127
        print(f"using churn mask ({mask.mean():.1%} masked)")
    stills.sort(key=lambda s: s["t0"])
    imgs = {s["file"]: load_gray(os.path.join(a.outdir, s["file"])) for s in stills}

    out = []
    dropped = []
    for s in stills:
        if out and out[-1]["src"] == s["src"]:
            h, r = metrics(imgs[out[-1]["file"]], imgs[s["file"]], mask)
            same = h < a.hist_thr and r < a.ratio_thr
            print(f"{out[-1]['file']} vs {s['file']}: hist={h:.4f} ratio={r:.4f}"
                  f" -> {'MERGE' if same else 'keep'}")
            if same:
                prev = out[-1]
                dropped.append(prev["file"])
                merged = dict(s)
                merged["t0"] = prev["t0"]
                if prev.get("kind") == "still":
                    merged["kind"] = "still"
                out[-1] = merged
                continue
        out.append(dict(s))

    print(f"stills {len(stills)} -> {len(out)} (merged {len(dropped)})")
    if not a.dry:
        json.dump(out, open(jpath, "w"), indent=1)
        for f in dropped:
            os.remove(os.path.join(a.outdir, f))

if __name__ == "__main__":
    main()
