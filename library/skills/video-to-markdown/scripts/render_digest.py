#!/usr/bin/env python3
"""Render reader-facing digest.md from verdicts + sanitized transcript.

Two-file architecture: session.md = complete record (never touched);
digest.md = derived view — only KEPT stills (agent verdicts), captions under images,
sanitized transcript. Deterministic: agents judge (verdicts.json), this script executes.

Reads from a session output dir: session.md (header table + NOTE lines reused verbatim),
stills.json, verdicts.json, digest-transcript.json. Writes digest.md.
Screen numbers match session.md (gaps = consolidated frames). Interleave, destutter and
audio-only milestone headers mirror assemble.py.
"""
import argparse, datetime, json, os, re, sys

def destutter(text, prev_tail=None):  # identical to assemble.py
    text = re.sub(r'((\S{1,16})(?:\s+\2){3,})',
                  lambda m: f"{m.group(2)} {m.group(2)} […ASR repeat collapsed]", text)
    text = re.sub(r'((\S{1,12}\s\S{1,12})(?:\s+\2){2,})',
                  lambda m: f"{m.group(2)} […ASR repeat collapsed]", text)
    text = re.sub(r'(([一-鿿]{1,2})\2{3,})',
                  lambda m: f"{m.group(2)}{m.group(2)}[…ASR repeat collapsed]", text)
    if prev_tail:
        text = re.sub(r'^(?:' + re.escape(prev_tail) + r'\s+){1,}(?=' + re.escape(prev_tail) + r')', '', text)
        text = re.sub(r'^(?:' + re.escape(prev_tail) + r'\s*){2,}', prev_tail + ' ', text).lstrip()
    return text

def stutter_tail(text):
    m = re.search(r'(\S{1,16}) \1(?: \[…ASR repeat collapsed\])?\s*$', text)
    return m.group(1) if m else None

def hms(t):
    t = int(t)
    return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"

def parse_session_header(path):
    title, table, notes = None, [], []
    for line in open(path):
        line = line.rstrip("\n")
        if title is None and line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("|"):
            table.append(line)
        elif line.startswith("> NOTE:"):
            notes.append(line)
        elif line.startswith("## "):
            break
    return title, table, notes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir", help="session output dir (session.md, stills.json, verdicts.json, digest-transcript.json)")
    ap.add_argument("--out", default=None, help="default: <outdir>/digest.md")
    a = ap.parse_args()
    out_path = a.out or os.path.join(a.outdir, "digest.md")

    stills = sorted(json.load(open(os.path.join(a.outdir, "stills.json"))), key=lambda x: x["t0"])
    vd = json.load(open(os.path.join(a.outdir, "verdicts.json")))
    verd = {v["file"]: v for v in vd["stills"]}
    trans = sorted(json.load(open(os.path.join(a.outdir, "digest-transcript.json"))), key=lambda x: x["t0"])
    n_drops = len(vd.get("segment_drops", []))
    title, table, notes = parse_session_header(os.path.join(a.outdir, "session.md"))

    missing = [s["file"] for s in stills if s["file"] not in verd]
    if missing:
        sys.exit(f"FATAL: {len(missing)} stills without verdict (e.g. {missing[0]})")

    merged_into = {}
    for s in stills:
        v = verd[s["file"]]
        if v["action"] == "merge":
            tgt = v.get("into")
            if tgt not in verd or verd[tgt]["action"] != "keep":
                sys.exit(f"FATAL: merge target not a kept still: {s['file']} -> {tgt}")
            merged_into[tgt] = merged_into.get(tgt, 0) + 1

    kept = []
    for n, s in enumerate((x for x in stills if x.get("kind") != "milestone"), start=1):
        if verd[s["file"]]["action"] == "keep":
            kept.append({**s, "n": n, "caption": verd[s["file"]].get("caption", ""),
                         "absorbed": merged_into.get(s["file"], 0)})

    L = [f"# {title} (digest)\n"]
    L.append(f"> Derived reader view generated {datetime.date.today().isoformat()} by render_digest.py. "
             f"Complete record: session.md (untouched). Kept {len(kept)} of {len(stills)} stills "
             f"(agent keep/merge/drop verdicts in verdicts.json); {len(trans)} transcript segments "
             f"({n_drops} filler/artifact segments dropped, logged in verdicts.json). "
             f"Screen numbers match session.md; gaps = consolidated frames.\n")
    L.extend(table)
    L.append("")
    L.extend(notes)
    if notes:
        L.append("")

    # audio-only milestone headers at the SAME timestamps as session.md (based on ALL stills)
    if trans:
        end_t = max(x["t1"] for x in trans)
        last = max([s["t1"] for s in stills], default=0.0)
        m = last
        virt = []
        while m < end_t - 60.0:
            virt.append({"t0": m, "t1": min(m + 600.0, end_t), "kind": "milestone", "file": None})
            m += 600.0
        emit_list = sorted(kept + virt, key=lambda x: x["t0"])
    else:
        emit_list = kept

    def emit_still(s):
        if s.get("kind") == "milestone":
            L.append(f"\n## [{hms(s['t0'])}] — audio only (no screen recording)\n")
            return
        tag = " — transition sample (screen in motion)" if s.get("kind") == "transition" else ""
        L.append(f"\n## [{hms(s['t0'])} - {hms(s['t1'])}] Screen {s['n']}{tag}\n")
        L.append(f"![screen {s['n']} at {hms(s['t0'])}]({s['file']})\n")
        if s["caption"]:
            L.append(f"*{s['caption']}*\n")
        if s["absorbed"]:
            L.append(f"*(+{s['absorbed']} near-duplicate frame{'s' if s['absorbed'] > 1 else ''} consolidated)*\n")

    si, prev_tail = 0, None
    for seg in trans:
        while si < len(emit_list) and emit_list[si]["t0"] <= seg["t0"]:
            emit_still(emit_list[si]); si += 1
        cleaned = destutter(seg["text"], prev_tail)
        prev_tail = stutter_tail(cleaned)
        if cleaned:
            L.append(f"- `[{hms(seg['t0'])}]` {cleaned}")
    while si < len(emit_list):
        emit_still(emit_list[si]); si += 1

    open(out_path, "w").write("\n".join(L) + "\n")
    print(f"kept={len(kept)}/{len(stills)} segments={len(trans)} -> {out_path}")

if __name__ == "__main__":
    main()
