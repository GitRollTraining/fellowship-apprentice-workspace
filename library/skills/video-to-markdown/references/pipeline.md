# Pipeline reference — video to markdown

Loaded on demand by `SKILL.md`. Scripts live in this skill's `scripts/` directory.

## Dependencies

- System: `ffmpeg`, `ffprobe`, `python3` (3.10 or newer), `curl`.
- Python packages: `numpy` (histogram diffs, required by the screenshot pass), `opencv-python-headless` (the dedupe helper and the disabled churn-mask branch only), `mlx-whisper` (local transcription, Apple Silicon only; its first run downloads a model of about 1.6 GB).
- `library/` is read-only, so the virtual environment goes outside it. From the repository root:

  ```bash
  python3 -m venv .venv && .venv/bin/pip install numpy opencv-python-headless mlx-whisper
  export VIDEO2MD_PYTHON="$PWD/.venv/bin/python"
  ```

  `run_session.sh` uses `VIDEO2MD_PYTHON` when it is set and falls back to `python3` on the path. Either way it stops with a one-line message if that interpreter cannot import numpy, rather than failing halfway through a long run.
- Not on Apple Silicon: leave `mlx-whisper` out of the install line, and either set a transcription API key (below) or work from a recording that carries its own caption track.
- Optional hosted transcription. `transcribe_timed.py` reads the first key it finds among `OPENAI_TRANSCRIPTION_KEY`, `TRANSCRIBE_API_KEY`, `OPENAI_API_KEY`, `OPENAI_KEY`, `GROQ_API_KEY` — from the environment, or from a `.env` file in the current directory or any parent directory, or from a file named by `--env-file`. `TRANSCRIBE_BASE_URL` and `TRANSCRIBE_MODEL` override the endpoint and the model. Probe a new key on a 15 s clip before committing it to a long run.

## Probe (before anything)

```bash
# usable duration = last packet timestamp (headers lie on truncated files)
ffprobe -v error -select_streams v -show_entries packet=pts_time -of csv=p=0 "$V" | tail -1
# subtitle stream? (free, often speaker-attributed transcript)
ffprobe -v error -select_streams s -show_entries stream=index -of csv=p=0 "$V"
# real frame rate (screen recorders often write 60; do not assume 25)
ffprobe -v error -select_streams v -show_entries stream=r_frame_rate -of csv=p=0 "$V"
```

Any `.mkv`, or any container that crashed mid-write, gets remuxed before frame extraction, because seeks land off-target on damaged containers [gotcha F11]:

```bash
ffmpeg -i in.mkv -c copy -movflags +faststart out.mp4
```

## Config (frozen, validated across three real sessions)

| Parameter | Value | Why |
|---|---|---|
| Compare stream | 480 px wide grayscale, 1 fps, area-scaled | below about 480 px, changes in dense text vanish |
| Distance | 64-bin histogram total-variation, byte-hash early exit | robust to small churn; cheap |
| Change threshold | 0.02 | 0.05 lost a 12-screen registration workflow; 0.02 over-captures about 1.5x, which is acceptable because under-capture is unrecoverable |
| Minimum still | 3 s | 2 s admitted churn fragments (over 400 screenshots an hour, above the band) |
| Transition backstop | a zone changing for more than 15 s is sampled every 5 s | covers rapid application-switching bursts and live-video interludes such as a webcam view |
| Representative frame | END of the stable run | the settled state; catches the outcome of gradual typing |
| Density band | 12 to 360 screenshots per video-hour | observed on real sessions: 173 to 336 |

## Engine matrix (transcription)

| Situation | Path |
|---|---|
| Embedded subtitle stream | extract the srt, then `srt_to_transcript.py` (merges rolling same-speaker cells, `--max-seg 15`); keeps speaker names |
| API key live | `transcribe_timed.py` default: 300 s WAV chunks across 3 workers, verbose JSON, per-chunk offset, 3-attempt retry, hallucination filters |
| No key, dead key, or chunks failing in auto mode | local engine over the whole file, same filters and merge — automatic fallback |
| Code-switched audio flipping language | re-run with `--language` forced to the dominant language |

Hallucination filters: drop a segment when `no_speech_prob > 0.6`, or `avg_logprob < -1.0`, or `compression_ratio > 2.4`. Sample both what was kept and what was dropped afterwards; a huge drop count is a diagnostic, not a success signal.

## Session timeline model

A session is an ordered list of usable media segments, concatenated: session time is a position in the video over `[0, usable_dur]`, then in the continuation audio over `[usable_dur, usable_dur + wav_dur]`. Wall-clock holes from a crashed recording are NOT on the timeline — they get a header note. A continuation audio file is transcribed with `--t-offset <video usable duration> --append`, and its sections carry no screenshots.

## Script reference

| Script | Role | Key flags |
|---|---|---|
| `run_session.sh DIR VGLOB WGLOB\|- TITLE [NOTE]` | the whole pipeline, one session | pass globs, never literal names (non-ASCII filenames) |
| `extract_stills.py VIDEO OUTDIR` | change-point screenshots plus `stills.json` | `--thr --min-still --trans-max --trans-step --t-offset --src --no-extract --dump-scores` |
| `transcribe_timed.py MEDIA OUT.json` | timestamped transcript | `--engine auto\|api\|local --language --chunk --t-offset --append --src --env-file` |
| `srt_to_transcript.py IN.srt OUT.json` | caption path | `--window T0 T1 --max-seg --src --t-offset --append` |
| `assemble.py OUT.md` | interleave transcript and screenshots | `--title --transcript --stills --source "name \| dur \| note" --note` (repeatable) |
| `render_transcript.py OUTDIR` | clean reader transcript into `transcript.md` (text only, no timestamps or screenshots, de-stuttered) | prefers `digest-transcript.json` over `transcript.json` — re-run it after the digest step |
| `make_sheet.sh STILLS_DIR OUT.png [COLS]` | contact sheet for coverage triage | judge at full resolution; the sheet is triage only |
| `dedupe_stills.py OUTDIR` | conservative near-duplicate merge (unused in the frozen config) | `--dry` first; no threshold separates webcam motion from a real dialog — see `gotchas.md` |
| `digest_batches.py OUTDIR` | digest step: writes screenshot batches and transcript chunks to disk as assignment files | `--batch-size 15 --san-chunk 200`; each sub-agent reads its own file, so the data stays out of the orchestrator's context |
| `digest_merge.py OUTDIR` | merges per-batch verdict results into `verdicts.json`, resolves merge chains, exits 2 on a missing verdict or a missing caption | deterministic authority over sub-agent output; re-run after ANY manual verdict edit |
| `sanitize_transcript.py SRC EDITS OUT --verdicts V` | applies whitelist edits and drops behind hard guards (token preservation at least 0.85, filler lexicon, artifact patterns) | sub-agents propose, this disposes; rejections are logged |
| `render_digest.py OUTDIR` | verdicts plus sanitized transcript into `digest.md` (kept screenshots with captions, original screen numbers) | header, table and notes are reused from `session.md` verbatim |

## Digest (step 8) — sub-agent protocol

Batches of about 15 screenshots per verdict sub-agent. Each assignment file carries absolute paths, spans, original screen numbers, the overlapping transcript excerpt, and the previous batch's last screenshot as context. Sanitize sub-agents get chunks of about 200 segments plus the engagement's name list — the proper nouns collected from the owner, which is the only authority for a name substitution.

EMBED VERBATIM in every verdict prompt: the merge rubric (identity of the MAIN CONTENT PANE decides; a change confined to a sidebar, a hover state, the cursor, a webcam tile or a clock never earns a keep; a return to a screen already shown merges into the first visit), the caption discipline (at most 120 characters, ending on a complete word; on-screen labels quoted verbatim including qualifiers; caption each screenshot immediately after reading ITS image), in-doubt-keep, and the credential rule (never transcribe a credential value; write "credentials page for X" instead). Add the structured-output schema and the isolation rules: no git, no file writes outside the named result file.

The deterministic scripts above own assembly. The audits — under-merge, caption against image, paraphrase diff, coverage — run with FRESH sub-agents until two consecutive rounds surface no new failure class. Measurements and the failure classes behind each guard: `methodology.md` § 8.

## Incidental output files

`extract_stills.py --dump-scores` leaves a `scores.tsv` (per-frame change-distance trace) in the output directory; a name-correction pass may leave a `transcript.json.bak`. Neither belongs to the output contract; both are safe to ignore or delete.

## Verification (after every run)

- Every `![](stills/...)` target exists, and no screenshot is orphaned.
- `stills.json` and `transcript.json` are monotonic, and `t1` never exceeds the session duration by more than 60 s.
- No uncovered gap longer than 180 s inside a video segment; density inside the band.
- Every media file appears in the transcript's source list.
- `transcript.md` exists and contains no image links and no `[HH:MM:SS]` stamps (`grep -cE '\!\[|\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]'` returns 0); its segment count matches its source JSON.
- MANUAL: read two or three random sections and their screenshots. When the stakes warrant it, ask "what page, what action, at minute X?" and check the answer against a decode-accurate frame.
