#!/usr/bin/env python3
"""Precompute digest work batches: still batches for verdict agents + segment chunks
for sanitization agents. Writes {outdir}/.digest-work/batch-NN.json and san-NN.json;
prints a manifest. Agents read their assignment file from disk (keeps orchestrator
context clean); the RULES travel in the agent prompt, this carries only data.
"""
import argparse, json, os

def hms(t):
    t = int(t)
    return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir")
    ap.add_argument("--batch-size", type=int, default=15)
    ap.add_argument("--san-chunk", type=int, default=200)
    ap.add_argument("--excerpt-pad", type=float, default=30.0)
    a = ap.parse_args()
    outdir = os.path.abspath(a.outdir)
    wd = os.path.join(outdir, ".digest-work")
    os.makedirs(wd, exist_ok=True)

    stills = sorted(json.load(open(f"{outdir}/stills.json")), key=lambda x: x["t0"])
    trans = sorted(json.load(open(f"{outdir}/transcript.json")), key=lambda x: x["t0"])
    title = next((l[2:].strip() for l in open(f"{outdir}/session.md") if l.startswith("# ")), "session")

    numbered = []
    for n, s in enumerate(stills, start=1):
        numbered.append({"file": s["file"], "abs": os.path.join(outdir, s["file"]),
                         "t0": s["t0"], "t1": s["t1"], "span": f"{hms(s['t0'])} - {hms(s['t1'])}",
                         "n": n, "kind": s.get("kind", "still")})

    chunks, i = [], 0
    while i < len(numbered):
        chunk = numbered[i:i + a.batch_size]
        if len(numbered) - (i + a.batch_size) < 8 and i + a.batch_size < len(numbered):
            chunk = numbered[i:]  # fold a tiny tail into this batch
        chunks.append(chunk)
        i += len(chunk)

    batch_files = []
    for bi, chunk in enumerate(chunks, start=1):
        t_lo, t_hi = chunk[0]["t0"] - a.excerpt_pad, chunk[-1]["t1"] + a.excerpt_pad
        excerpt = [f"- [{hms(s['t0'])}] {s['text']}" for s in trans if s["t1"] >= t_lo and s["t0"] <= t_hi]
        ctx = numbered[numbered.index(chunk[0]) - 1] if numbered.index(chunk[0]) > 0 else None
        p = os.path.join(wd, f"batch-{bi:02d}.json")
        json.dump({"id": bi, "session_title": title, "stills": chunk,
                   "context_still": ctx, "transcript_excerpt": "\n".join(excerpt)},
                  open(p, "w"), ensure_ascii=False, indent=1)
        batch_files.append(p)

    san_files = []
    for ci in range(0, len(trans), a.san_chunk):
        chunk = trans[ci:ci + a.san_chunk]
        p = os.path.join(wd, f"san-{ci//a.san_chunk + 1:02d}.json")
        json.dump({"id": ci // a.san_chunk + 1, "session_title": title,
                   "segments": [{"t0": s["t0"], "text": s["text"]} for s in chunk]},
                  open(p, "w"), ensure_ascii=False, indent=1)
        san_files.append(p)

    print(json.dumps({"outdir": outdir, "stills": len(numbered), "segments": len(trans),
                      "batch_files": batch_files, "san_files": san_files}, indent=1))

if __name__ == "__main__":
    main()
