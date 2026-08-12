#!/usr/bin/env python3
"""Merge per-batch verdict results into verdicts.json (stills part).

Deterministic authority over agent output:
  - every stills.json file must receive exactly one verdict (duplicates: first wins, logged;
    missing: listed, exit 2 so the orchestrator re-dispatches)
  - merge chains resolved to a final KEPT target (A->B->C becomes A->C)
  - merge into a dropped/unknown target, or a cycle -> flipped to keep; if the flip leaves
    a keep without caption it is listed as NEEDS-CAPTION, exit 2 (orchestrator fixes up)
  - keep captions must be non-empty and <=120 chars (violations listed, exit 2)

Input result files: JSON {"batch_id": n, "verdicts":[{file,action,into?,reason,caption?}]}.
Writes {outdir}/verdicts.json with {"stills":[...], "segment_drops":[], "sanitization_edits":[]}
(the sanitize step fills the latter two via sanitize_transcript.py --verdicts).
"""
import argparse, glob, json, os, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir")
    ap.add_argument("--results", default=None, help="glob (default {outdir}/.digest-work/result-*.json)")
    a = ap.parse_args()
    outdir = os.path.abspath(a.outdir)
    pattern = a.results or os.path.join(outdir, ".digest-work", "result-*.json")

    stills = sorted(json.load(open(f"{outdir}/stills.json")), key=lambda x: x["t0"])
    files = [s["file"] for s in stills]
    fset = set(files)

    verd, dupes, problems = {}, [], []
    for rf in sorted(glob.glob(pattern)):
        for v in json.load(open(rf))["verdicts"]:
            f = v.get("file")
            if f not in fset:
                problems.append(f"unknown still in {os.path.basename(rf)}: {f}"); continue
            if f in verd:
                dupes.append(f); continue
            verd[f] = {"file": f, "action": v.get("action"), "into": v.get("into"),
                       "reason": v.get("reason", ""), "caption": v.get("caption", "")}

    missing = [f for f in files if f not in verd]

    def resolve(f, seen):
        v = verd.get(f)
        if v is None or f in seen:
            return None
        if v["action"] == "keep":
            return f
        if v["action"] == "merge":
            return resolve(v["into"], seen | {f})
        return None  # drop

    flips, needs_caption = [], []
    for f, v in verd.items():
        if v["action"] == "merge":
            tgt = resolve(v["into"], {f})
            if tgt is None:
                v["action"], v["into"] = "keep", None
                flips.append(f)
                if not v["caption"]:
                    needs_caption.append(f)
            else:
                v["into"] = tgt
    for f, v in verd.items():
        if v["action"] == "keep":
            if not v.get("caption"):
                needs_caption.append(f)
            elif len(v["caption"]) > 120:
                v["caption"] = v["caption"][:117] + "..."
        if v["action"] != "merge":
            v.pop("into", None)

    out = {"stills": [verd[f] for f in files if f in verd], "segment_drops": [], "sanitization_edits": []}
    json.dump(out, open(f"{outdir}/verdicts.json", "w"), ensure_ascii=False, indent=1)

    kept = sum(1 for v in out["stills"] if v["action"] == "keep")
    merged = sum(1 for v in out["stills"] if v["action"] == "merge")
    dropped = sum(1 for v in out["stills"] if v["action"] == "drop")
    print(json.dumps({"stills": len(files), "verdicts": len(out["stills"]), "keep": kept,
                      "merge": merged, "drop": dropped, "dupes_ignored": dupes,
                      "merge_flipped_to_keep": flips, "missing": missing,
                      "needs_caption": sorted(set(needs_caption)), "problems": problems},
                     ensure_ascii=False, indent=1))
    if missing or needs_caption or problems:
        sys.exit(2)

if __name__ == "__main__":
    main()
