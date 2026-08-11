#!/usr/bin/env python3
"""WebVTT subtitle file to plain text. Standard library only.

    python3 clean_vtt.py captions.vtt > transcript.txt
    cat captions.vtt | python3 clean_vtt.py

Removes cue numbers, cue timings, positioning and karaoke tags, HTML entities,
and the rolling repeats automatic captions produce (each cue restates the tail
of the one before it). Emits one line of speech per line, in the order spoken.

Exits non-zero when the input holds no caption text, so an empty result is a
loud failure rather than an empty file.
"""

import html
import re
import sys

TIMING = re.compile(r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s+-->")
TAG = re.compile(r"<[^>]*>")
HEADER = re.compile(r"^(WEBVTT|NOTE|STYLE|REGION)\b|^(Kind|Language|X-TIMESTAMP-MAP)\s*[:=]")
WHITESPACE = re.compile(r"\s+")

WINDOW = 4  # how many recent lines a repeat is checked against


def clean(raw, window=WINDOW):
    lines = raw.splitlines()
    out = []
    for i, line in enumerate(lines):
        line = WHITESPACE.sub(" ", html.unescape(TAG.sub("", line))).strip()
        if not line or TIMING.match(line) or HEADER.match(line):
            continue
        # a bare number directly above a timing line is a cue index, not speech
        if line.isdigit() and i + 1 < len(lines) and TIMING.match(lines[i + 1].strip()):
            continue
        if line in out[-window:]:
            continue
        out.append(line)
    return out


if __name__ == "__main__":
    raw = (
        open(sys.argv[1], encoding="utf-8", errors="replace").read()
        if len(sys.argv) > 1
        else sys.stdin.read()
    )
    text = "\n".join(clean(raw))
    if not text.strip():
        sys.exit("clean_vtt.py: no caption text found — is this a WebVTT file?")
    print(text)
