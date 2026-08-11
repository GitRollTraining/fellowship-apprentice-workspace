#!/usr/bin/env python3
"""Change-point still extractor.

Pass 1 (OPTIONAL, and OFF in the shipped pipeline — run_session.sh passes --no-mask):
accumulate per-pixel change frequency at compare resolution -> churn mask (pixels
changing in > mask-thr of frames, e.g. video-call participant tiles, clocks). It was
dropped because intermittent tiles learn a mask of about 0% area; the 3 s minimum still
already filters floor churn.

Pass 2: masked byte-hash early-exit + masked histogram total-variation distance ->
stable runs -> one representative frame per run (last = settled) + forced samples
inside long transitions (scroll fix) -> full-res PNG pass -> stills.json
(+ mask.png for downstream dedupe when the mask is enabled).
"""
import argparse, hashlib, json, os, subprocess, sys
import numpy as np

def ffprobe_dims(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True).stdout.strip()
    w, h = out.split("\n")[0].split(",")[:2]
    return int(w), int(h)

def hhmmss(t):
    t = int(t)
    return f"{t//3600:02d}{t%3600//60:02d}{t%60:02d}"

def frames(video, fps, cw, ch):
    cmd = ["ffmpeg", "-v", "error", "-i", video,
           "-vf", f"fps={fps},scale={cw}:{ch}:flags=area,format=gray",
           "-f", "rawvideo", "-"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    fsz = cw * ch
    while True:
        buf = proc.stdout.read(fsz)
        if len(buf) < fsz:
            break
        yield np.frombuffer(buf, np.uint8).reshape(ch, cw)
    proc.wait()

def tv_hist(a, b, keep):
    ha = np.bincount(a[keep] >> 2, minlength=64).astype(np.float64)
    hb = np.bincount(b[keep] >> 2, minlength=64).astype(np.float64)
    return 0.5 * np.abs(ha / ha.sum() - hb / hb.sum()).sum()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("outdir")
    ap.add_argument("--fps", type=float, default=1.0)
    ap.add_argument("--thr", type=float, default=0.02)
    ap.add_argument("--min-still", type=float, default=3.0)
    ap.add_argument("--trans-max", type=float, default=15.0)
    ap.add_argument("--trans-step", type=float, default=5.0)
    ap.add_argument("--dump-scores", default=None)
    ap.add_argument("--t-offset", type=float, default=0.0)
    ap.add_argument("--src", default=None)
    ap.add_argument("--no-extract", action="store_true")
    ap.add_argument("--append", action="store_true")
    ap.add_argument("--start-index", type=int, default=1)
    ap.add_argument("--no-mask", action="store_true")
    ap.add_argument("--mask-thr", type=float, default=0.5,
                    help="pixel changes in > this fraction of frames -> masked")
    ap.add_argument("--mask-cap", type=float, default=0.4,
                    help="if masked area exceeds this fraction, disable mask + warn")
    ap.add_argument("--mask-stride", type=int, default=3,
                    help="pass-1 samples every Nth frame")
    a = ap.parse_args()

    src = a.src or os.path.basename(a.video)
    w, h = ffprobe_dims(a.video)
    cw = 480
    ch = max(2, int(round(h * cw / w / 2)) * 2)
    os.makedirs(os.path.join(a.outdir, "stills"), exist_ok=True)

    # ---- pass 1: churn mask ----
    keep = np.ones((ch, cw), bool)
    if not a.no_mask:
        prev = None
        freq = np.zeros((ch, cw), np.int32)
        n1 = 0
        for i, f in enumerate(frames(a.video, a.fps, cw, ch)):
            if i % a.mask_stride:
                continue
            if prev is not None:
                freq += (np.abs(f.astype(np.int16) - prev.astype(np.int16)) > 10)
                n1 += 1
            prev = f.copy()
        if n1 >= 10:
            churn = freq / n1 > a.mask_thr
            # dilate 1px to swallow tile borders
            d = churn.copy()
            d[1:, :] |= churn[:-1, :]; d[:-1, :] |= churn[1:, :]
            d[:, 1:] |= churn[:, :-1]; d[:, :-1] |= churn[:, 1:]
            area = d.mean()
            if area > a.mask_cap:
                print(f"WARN: churn mask area {area:.0%} > cap {a.mask_cap:.0%} — mask DISABLED", file=sys.stderr)
            else:
                keep = ~d
                import cv2
                cv2.imwrite(os.path.join(a.outdir, "mask.png"),
                            (d * 255).astype(np.uint8))
                print(f"mask: {area:.1%} of frame masked (n1={n1})", file=sys.stderr)

    # ---- pass 2: masked diffs ----
    diffs = []
    prev_hash = None
    prev = None
    n = 0
    for f in frames(a.video, a.fps, cw, ch):
        fm = f[keep]
        hsh = hashlib.sha1(fm.tobytes()).digest()
        if prev is None:
            d = 1.0
        elif hsh == prev_hash:
            d = 0.0
        else:
            d = tv_hist(prev, f, keep)
        prev = f
        prev_hash = hsh
        diffs.append(d)
        n += 1
    if n == 0:
        sys.exit("no frames decoded")

    step = 1.0 / a.fps
    t_of = lambda idx: idx * step

    if a.dump_scores:
        with open(a.dump_scores, "w") as fh:
            for idx, d in enumerate(diffs):
                fh.write(f"{t_of(idx):.1f}\t{d:.5f}\n")

    runs = []
    cur = 0
    for idx in range(1, n):
        if diffs[idx] > a.thr:
            runs.append((cur, idx - 1))
            cur = idx
    runs.append((cur, n - 1))

    stills = []
    pend = []
    def flush_trans():
        if not pend:
            return
        z0, z1 = pend[0][0], pend[-1][1]
        if (z1 - z0 + 1) * step > a.trans_max:
            t = z0 * step + a.trans_step / 2
            while t < (z1 + 1) * step:
                ridx = min(int(t / step), z1)
                stills.append(("transition", ridx,
                               max(z0, ridx - int(a.trans_step / 2 / step)),
                               min(z1, ridx + int(a.trans_step / 2 / step))))
                t += a.trans_step
        pend.clear()

    for (s, e) in runs:
        if (e - s + 1) * step >= a.min_still:
            flush_trans()
            stills.append(("still", e, s, e))
        else:
            pend.append((s, e))
    flush_trans()
    stills.sort(key=lambda x: x[2])

    jpath = os.path.join(a.outdir, "stills.json")
    existing = json.load(open(jpath)) if (a.append and os.path.exists(jpath)) else []

    out = []
    for k, (kind, rep, s, e) in enumerate(stills):
        t0 = t_of(s) + a.t_offset
        t1 = t_of(e) + step + a.t_offset
        rep_t = t_of(rep)
        name = f"{a.start_index + k:03d}_{hhmmss(t0)}.png"
        if not a.no_extract:
            subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-ss", f"{rep_t:.3f}",
                 "-i", a.video, "-frames:v", "1", "-q:v", "2",
                 os.path.join(a.outdir, "stills", name)], check=True)
        out.append({"file": f"stills/{name}", "t0": round(t0, 2),
                    "t1": round(t1, 2), "src": src, "kind": kind,
                    "rep_t": round(rep_t + a.t_offset, 2)})

    json.dump(existing + out, open(jpath, "w"), indent=1)
    ns = sum(1 for s_ in out if s_["kind"] == "still")
    print(f"frames={n} runs={len(runs)} stills={ns} transition-samples={len(out)-ns} -> {jpath}")

if __name__ == "__main__":
    main()
