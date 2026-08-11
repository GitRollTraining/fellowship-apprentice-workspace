#!/usr/bin/env python3
"""transcript.json + stills.json -> session.md (transcript spine, stills interleaved)."""
import argparse, datetime, json, re

def destutter(text, prev_tail=None):
    # collapse ASR loops: token (<=16 chars) or two-token phrase repeated >=4x / >=3x
    text = re.sub(r'((\S{1,16})(?:\s+\2){3,})',
                  lambda m: f"{m.group(2)} {m.group(2)} […ASR repeat collapsed]", text)
    text = re.sub(r'((\S{1,12}\s\S{1,12})(?:\s+\2){2,})',
                  lambda m: f"{m.group(2)} […ASR repeat collapsed]", text)
    # glued CJK repeats (no spaces): unit of 1-2 chars repeated >=4x
    text = re.sub(r'(([\u4e00-\u9fff]{1,2})\2{3,})',
                  lambda m: f"{m.group(2)}{m.group(2)}[…ASR repeat collapsed]", text)
    # boundary-aware: strip leading repeats of the previous bullet's trailing token
    if prev_tail:
        text = re.sub(r'^(?:' + re.escape(prev_tail) + r'\s+){1,}(?=' + re.escape(prev_tail) + r')',
                      '', text)
        text = re.sub(r'^(?:' + re.escape(prev_tail) + r'\s*){2,}', prev_tail + ' ', text).lstrip()
    return text

def stutter_tail(text):
    # trailing token that repeats at the end of this bullet (marker or bare pair)
    m = re.search(r'(\S{1,16}) \1(?: \[…ASR repeat collapsed\])?\s*$', text)
    return m.group(1) if m else None

def hms(t):
    t = int(t)
    return f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outmd")
    ap.add_argument("--title", required=True)
    ap.add_argument("--transcript", required=True)
    ap.add_argument("--stills", required=True)
    ap.add_argument("--source", action="append", default=[],
                    help="'name | duration | note' header rows")
    ap.add_argument("--note", action="append", default=[])
    a = ap.parse_args()

    trans = sorted(json.load(open(a.transcript)), key=lambda x: x["t0"])
    stills = sorted(json.load(open(a.stills)), key=lambda x: x["t0"])

    L = []
    L.append(f"# {a.title}\n")
    L.append(f"> Generated {datetime.date.today().isoformat()} by video-to-markdown pipeline. "
             f"Timestamps are relative to the start of the listed sources, concatenated in order.\n")
    if a.source:
        L.append("| Source | Duration | Note |")
        L.append("|--------|----------|------|")
        for s in a.source:
            parts = [p.strip() for p in s.split("|")]
            while len(parts) < 3:
                parts.append("")
            L.append(f"| {parts[0]} | {parts[1]} | {parts[2]} |")
        L.append("")
    for n in a.note:
        L.append(f"> NOTE: {n}")
    if a.note:
        L.append("")

    # inject milestone pseudo-stills into still-less stretches (audio-only tails):
    # a header every ~600 s keeps the document navigable without images
    if trans:
        end_t = max(x["t1"] for x in trans)
        covered = [s["t0"] for s in stills]
        virt = []
        last = max([s["t1"] for s in stills], default=0.0)
        m = last
        while m < end_t - 60.0:
            virt.append({"t0": m, "t1": min(m + 600.0, end_t), "kind": "milestone", "file": None})
            m += 600.0
        if virt:
            stills = sorted(stills + virt, key=lambda x: x["t0"])

    si = 0
    sn = 0
    def emit_still(s):
        nonlocal sn
        if s.get("kind") == "milestone":
            L.append(f"\n## [{hms(s['t0'])}] — audio only (no screen recording)\n")
            return
        sn += 1
        tag = " — transition sample (screen in motion)" if s.get("kind") == "transition" else ""
        L.append(f"\n## [{hms(s['t0'])} - {hms(s['t1'])}] Screen {sn}{tag}\n")
        L.append(f"![screen {sn} at {hms(s['t0'])}]({s['file']})\n")

    prev_tail = None
    for seg in trans:
        while si < len(stills) and stills[si]["t0"] <= seg["t0"]:
            emit_still(stills[si]); si += 1
        cleaned = destutter(seg["text"], prev_tail)
        prev_tail = stutter_tail(cleaned)
        if cleaned:
            L.append(f"- `[{hms(seg['t0'])}]` {cleaned}")
    while si < len(stills):
        emit_still(stills[si]); si += 1

    open(a.outmd, "w").write("\n".join(L) + "\n")
    print(f"segments={len(trans)} stills={len(stills)} -> {a.outmd}")

if __name__ == "__main__":
    main()
