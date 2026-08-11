#!/usr/bin/env python3
"""Media -> transcript.json with timestamps. OpenAI-compatible /audio/transcriptions,
response_format=verbose_json (segment-level). Chunked WAV; per-chunk offset;
hallucination filters (no_speech_prob/avg_logprob/compression_ratio); tiny-segment merge.

Engine: --engine auto falls back to the local model when no API key is found. The key is
read from the environment, from a .env file in the cwd or any parent, or from --env-file.
"""
import argparse, json, os, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor

def load_env_file(path):
    if not path or not os.path.exists(path):
        return
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k and all(c.isalnum() or c == "_" for c in k):
            v = v.strip().strip('"').strip("'")
            os.environ.setdefault(k, v)


def keep_seg(s):
    return not (s.get("no_speech_prob", 0) > 0.6
                or s.get("avg_logprob", 0) < -1.0
                or s.get("compression_ratio", 1) > 2.4)

def run_local(a):
    """Local engine path: whole-file transcription, same filters/merge/output.
    Requires mlx-whisper, which installs on Apple Silicon only — on other hardware
    set a transcription API key instead (references/pipeline.md, Dependencies)."""
    try:
        import mlx_whisper
    except ImportError:
        sys.exit("local engine needs mlx-whisper (Apple Silicon only); "
                 "set a transcription API key instead — see references/pipeline.md")
    src = a.src or os.path.basename(a.media)
    with tempfile.TemporaryDirectory() as td:
        wav = f"{td}/a.wav"
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", a.media,
                        "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav],
                       check=True)
        kw = {"language": a.language} if a.language else {}
        res = mlx_whisper.transcribe(
            wav, path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
            verbose=None, **kw)
    segs, dropped = [], 0
    for s in res.get("segments", []):
        if not keep_seg(s):
            dropped += 1
            continue
        segs.append({"t0": round(s["start"] + a.t_offset, 2),
                     "t1": round(s["end"] + a.t_offset, 2),
                     "text": s["text"].strip(), "src": src})
    merged = merge_segs(segs, a)
    write_out(merged, a)
    print(f"[local] segments={len(segs)} merged={len(merged)} dropped={dropped} -> {a.out}")

def merge_segs(segs, a):
    merged = []
    for s in segs:
        if (merged and s["t0"] - merged[-1]["t1"] <= a.merge_gap
                and s["t1"] - merged[-1]["t0"] <= a.merge_max
                and s["src"] == merged[-1]["src"]):
            merged[-1]["t1"] = s["t1"]
            merged[-1]["text"] += " " + s["text"]
        else:
            merged.append(dict(s))
    return merged

def write_out(merged, a):
    existing = []
    if a.append:
        try:
            existing = json.load(open(a.out))
        except FileNotFoundError:
            pass
    json.dump(existing + merged, open(a.out, "w"), indent=1, ensure_ascii=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("media"); ap.add_argument("out")
    ap.add_argument("--src", default=None)
    ap.add_argument("--t-offset", type=float, default=0.0)
    ap.add_argument("--chunk", type=int, default=300)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--append", action="store_true")
    ap.add_argument("--merge-gap", type=float, default=0.6)
    ap.add_argument("--merge-max", type=float, default=15.0)
    ap.add_argument("--engine", choices=["auto", "api", "local"], default="auto")
    ap.add_argument("--language", default=None, help="force language (local engine), e.g. zh")
    ap.add_argument("--env-file", default=None,
                    help="path to a .env holding the API key; by default only the "
                         ".env walk-up from the current directory is used")
    a = ap.parse_args()

    # .env discovery: walk up from cwd, then the explicit --env-file if one was given
    d = os.getcwd()
    while True:
        cand = os.path.join(d, ".env")
        if os.path.exists(cand):
            load_env_file(cand)
            break
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    load_env_file(a.env_file)
    key = (os.environ.get("OPENAI_TRANSCRIPTION_KEY") or os.environ.get("TRANSCRIBE_API_KEY")
           or os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENAI_KEY")
           or os.environ.get("GROQ_API_KEY"))
    if a.engine == "local" or (a.engine == "auto" and not key):
        return run_local(a)
    if not key:
        sys.exit("no API key (TRANSCRIBE_API_KEY/OPENAI_API_KEY/OPENAI_KEY/GROQ_API_KEY)")
    url = os.environ.get("TRANSCRIBE_BASE_URL",
                         "https://api.openai.com/v1/audio/transcriptions")
    model = os.environ.get("TRANSCRIBE_MODEL", "whisper-1")
    src = a.src or os.path.basename(a.media)

    segs = []
    dropped = 0
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", a.media,
                        "-ar", "16000", "-ac", "1", "-f", "segment",
                        "-segment_time", str(a.chunk), f"{td}/c_%03d.wav"],
                       check=True)
        chunks = sorted(os.listdir(td))

        def one(ci_c):
            ci, c = ci_c
            path = f"{td}/{c}"
            # 16 kHz mono s16 wav = 32000 bytes/s; skip sub-0.5 s slivers
            if os.path.getsize(path) < 16000 + 44:
                return ci, None, f"chunk {ci}: sliver skipped ({os.path.getsize(path)} B)"
            last = ""
            for attempt in range(3):
                if attempt:
                    time.sleep(5 * (3 ** (attempt - 1)))  # 5s, 15s
                r = subprocess.run(
                    ["curl", "-sS", "--max-time", "240", "-w", "\n%{http_code}", url,
                     "-H", f"Authorization: Bearer {key}",
                     "-F", f"model={model}", "-F", "response_format=verbose_json",
                     "-F", f"file=@{path}"],
                    capture_output=True, text=True)
                if r.returncode != 0:
                    last = f"curl failed: {r.stderr[:200]}"
                    continue
                body, code = r.stdout.rsplit("\n", 1)
                if code.strip() != "200":
                    last = f"HTTP {code}: {body[:200]}"
                    continue
                return ci, json.loads(body), f"chunk {ci}: ok" + (f" (attempt {attempt+1})" if attempt else "")
            return ci, False, f"chunk {ci}: FAILED after 3 attempts: {last}"

        results = {}
        with ThreadPoolExecutor(max_workers=a.workers) as ex:
            for ci, data, msg in ex.map(one, enumerate(chunks)):
                print(msg, file=sys.stderr)
                results[ci] = data
        if any(v is False for v in results.values()):
            if a.engine == "auto":
                print("API chunks failed — falling back to local engine", file=sys.stderr)
                return run_local(a)
            sys.exit("one or more chunks failed — aborting (no partial output)")
        for ci in sorted(results):
            data = results[ci]
            if data is None:
                continue
            off = ci * a.chunk + a.t_offset
            for s in data.get("segments", []):
                if (s.get("no_speech_prob", 0) > 0.6
                        or s.get("avg_logprob", 0) < -1.0
                        or s.get("compression_ratio", 1) > 2.4):
                    dropped += 1
                    continue
                segs.append({"t0": round(s["start"] + off, 2),
                             "t1": round(s["end"] + off, 2),
                             "text": s["text"].strip(), "src": src})

    merged = []
    for s in segs:
        if (merged and s["t0"] - merged[-1]["t1"] <= a.merge_gap
                and s["t1"] - merged[-1]["t0"] <= a.merge_max
                and s["src"] == merged[-1]["src"]):
            merged[-1]["t1"] = s["t1"]
            merged[-1]["text"] += " " + s["text"]
        else:
            merged.append(dict(s))

    existing = []
    if a.append:
        try:
            existing = json.load(open(a.out))
        except FileNotFoundError:
            pass
    json.dump(existing + merged, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(f"segments={len(segs)} merged={len(merged)} dropped={dropped} -> {a.out}")

if __name__ == "__main__":
    main()
