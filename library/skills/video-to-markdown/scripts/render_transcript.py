#!/usr/bin/env python3
"""Render output/transcript.md — clean reader transcript: text only, no timestamps, no stills.

Prefers digest-transcript.json (sanitized, token-identical to source) when present,
else transcript.json — re-run after the digest step to pick up sanitization.
Title comes from session.md's H1. One segment per line; a `## {src}` section header
is emitted only when the session has more than one source medium (continuation wav).
"""
import argparse, json, os


def destutter(text, prev_tail=None):  # identical to assemble.py
    import re
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
    import re
    m = re.search(r'(\S{1,16}) \1(?: \[…ASR repeat collapsed\])?\s*$', text)
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir", help="session output dir holding transcript.json (+ session.md)")
    a = ap.parse_args()
    out = os.path.abspath(a.outdir)

    src_file = "digest-transcript.json" if os.path.exists(os.path.join(out, "digest-transcript.json")) \
        else "transcript.json"
    segs = sorted(json.load(open(os.path.join(out, src_file))), key=lambda s: s["t0"])

    title = "session"
    smd = os.path.join(out, "session.md")
    if os.path.exists(smd):
        for line in open(smd):
            if line.startswith("# "):
                title = line[2:].strip()
                break

    srcs = []
    for s in segs:
        if s.get("src") and s["src"] not in srcs:
            srcs.append(s["src"])
    multi = len(srcs) > 1

    lines = [f"# {title} — transcript", "",
             f"> Clean transcript: text only, no timestamps, no stills. Rendered from {src_file}; "
             f"complete record with stills and timestamps: session.md.", ""]
    cur, prev_tail = None, None
    for s in segs:
        if multi and s.get("src") != cur:
            cur = s.get("src")
            lines += [f"## {cur}", ""]
            prev_tail = None
        text = destutter(s["text"].strip(), prev_tail)
        prev_tail = stutter_tail(text)
        if text:
            lines.append(text)
    lines.append("")

    dest = os.path.join(out, "transcript.md")
    open(dest, "w").write("\n".join(lines))
    print(f"segments={len(segs)} source={src_file} -> {dest}")


if __name__ == "__main__":
    main()
