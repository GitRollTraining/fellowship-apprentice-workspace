---
name: video-to-markdown
description: Turn a screen recording into one markdown file — the full transcript as the spine, screenshots interleaved at the moment each screen was on display. Use on a screen recording of someone doing their work, a walkthrough, a demo, plus an optional audio-only continuation file.
argument-hint: <session-dir> [video-glob] [wav-glob|-] [title]
---

# Video to markdown

> A business owner runs their process once with a screen recorder on, talking through it. This turns that recording into one markdown file a person and an agent can both read: the transcript is the spine, and still screenshots sit at the timestamps they were on screen. It is the strongest evidence a process reconstruction can be built from, because a recording shows the steps an owner never thinks to mention.
>
> Images exist to make the speech interpretable — which page, which record, which setting, which button. The sidecar files `stills.json` and `transcript.json` make the output machine-checkable.
>
> **A session is exactly ONE video**, plus at most its verified continuation audio file. One video = one session = one output set. Never place two videos on a shared timeline.

## Inputs

- `<session-dir>` — a directory holding ONE recording. Output lands in `{session-dir}/output/`. A directory holding several videos is an intake directory, not a session directory: make one session subdirectory per video, move each video into its own, and run the workflow once per subdirectory. Never concatenate unrelated recordings with `--t-offset/--append`.
- `[video-glob]` — `*.mp4` / `*.mov` / `*.mkv` (default: the sole video file found).
- `[wav-glob|-]` — continuation audio glob, or `-` for none. A continuation is a segment recorded AFTER the video stopped, when the owner kept talking with the screen recorder off. Verify before using it: the video's start time plus its usable duration should land at about the audio file's start time.
- `[title]` — session title for the markdown header.

If arguments are missing, ask.

## Install once

Two command-line tools and three Python packages. `library/` is read-only, so the environment goes at the repository root, not in this skill directory. From the repository root:

```bash
python3 -m venv .venv && .venv/bin/pip install numpy opencv-python-headless mlx-whisper
export VIDEO2MD_PYTHON="$PWD/.venv/bin/python"
```

- `ffmpeg` and `ffprobe` must be on the path, and `python3` must be 3.10 or newer.
- Only `numpy` is needed for the screenshot pass. `opencv-python-headless` serves the optional dedupe helper; `mlx-whisper` is the local transcription engine and installs only on Apple Silicon (its first run downloads a model of about 1.6 GB).
- Not on Apple Silicon: leave `mlx-whisper` out of the line above, and either set a transcription API key (`references/pipeline.md` § Dependencies) or use a recording that already carries a caption track.
- Add `.venv/` to `.gitignore` if it is not there already.

## Workflow

1. **Pre-flight.** `ffmpeg`, `ffprobe` and `python3` present; the packages above installed; `VIDEO2MD_PYTHON` exported. An API key is optional — the local engine covers everything on Apple Silicon.
2. **Probe the media.** Take durations from the LAST PACKET timestamp, never the container header — headers lie on truncated files. Check for an embedded subtitle stream, which is a free transcript and often carries speaker names. Any `.mkv` gets remuxed `-c copy` to mp4 before any frame work. Detail: `references/pipeline.md` § Probe.
3. **Run the pipeline.** `scripts/run_session.sh <session-dir> <video-glob> <wav-glob|-> <title> [extra-note]`. It emits `output/{session.md, transcript.md, stills/, stills.json, transcript.json}`, where `transcript.md` is the clean reader transcript: text only, no timestamps, no screenshots. The screenshot detector's settings are frozen (`references/pipeline.md` § Config) — do not retune them per recording without examining a contact sheet.
4. **Verify.** Every markdown image link resolves; no uncovered gap longer than 180 s inside a video segment; screenshots per video-hour between 12 and 360; every media file appears in the transcript's source list; timestamps increase monotonically. Then READ two or three random sections plus their screenshots yourself — the automated checks alone do not qualify the output.
5. **Language check.** Sample transcript segments across the timeline. English prose where the audio is another language, or the reverse, means the transcriber flipped language mid-file: re-run that file's transcription with `--language` forced, then rebuild.
6. **Name correction.** Every business has proper nouns a transcriber garbles — a supplier, a product line, the software they run on, a member of staff. Collect them from the owner, write the list down, then run a conservative correction pass over `transcript.json`: high-confidence corrections only, anything ambiguous reported rather than changed, never a blind find-and-replace. The screenshots can settle an ambiguous name — read the screen the speech points at. Re-run `scripts/assemble.py` afterwards.
7. **Report, and treat the output as unreviewed.** State the sources and their usable durations, the screenshot counts (total and per hour), the transcription engine used per file, the number of name corrections, and a sensitivity line. A recording of a real business routinely captures customer names, invoice values, saved passwords and account balances. Keep the output directory out of version control until you have read it, and move anything the owner said must not leave the business into an untracked sidecar (repository `CLAUDE.md`, "Where things go").
8. **Digest.** Not skippable on agent judgment — session size does not exempt it; skip only if the person running it says so, and state the skip in the report. Two files: `session.md` is the complete record and is never touched; `digest.md` is the derived reader view — agent-judged screenshot consolidation (keep, merge or drop, each with a caption) over a whitelist-sanitized transcript. Run `scripts/digest_batches.py`, dispatch the verdict and sanitize sub-agents per `references/pipeline.md` § Digest (their prompts MUST embed the merge rubric, the caption discipline and the credential rule verbatim), then `digest_merge.py` → `sanitize_transcript.py` → `render_digest.py` → re-run `render_transcript.py`, which refreshes `transcript.md` from the sanitized transcript. Verify: every screenshot has exactly one verdict, kept screenshots are at most 75% of the total and at least 12 per video-hour, per-segment token preservation is at least 0.85, and `session.md` is byte-identical to before. Then audit adversarially (under-merge, caption against image, paraphrase, coverage) with fresh sub-agents until two consecutive rounds surface no new failure class. Full mechanism and the measurements behind it: `references/methodology.md`.

## Gotchas

The four that cost the most. Full registry: `references/gotchas.md`.

- **Several videos in one directory are NOT one session.** Wrong default: concatenate them with `--t-offset/--append` to keep it to one invocation, which puts unrelated content on a fake shared timeline. Correct: one session subdirectory per video, one pipeline run per subdirectory. Only a verified continuation audio file shares a session with a video.
- **Container header durations lie on truncated recordings.** A crashed recorder claimed 5145 s in the header while its packets ended at 1972 s. Wrong default: trust `format.duration`. Correct: probe the last packet timestamp, and state the unrecorded gap in the markdown header.
- **`-ss` seeks land off-target on damaged or unindexed containers** — the extracted screenshot silently shows the WRONG screen while every timestamp looks sane. Wrong default: seek the original `.mkv`. Correct: remux to mp4 first, and when in doubt compare a screenshot against a decode-accurate frame.
- **The transcriber flips language on code-switched audio.** Auto-detection renders the second language as fluent-looking paraphrase in the first: it reads like a transcript and is not one. Wrong default: accept plausible text. Correct: sample each media file, then force `--language` for the dominant language and re-run.

## Constants

| Key | Value |
|---|---|
| Skill location | `library/skills/video-to-markdown/` (read-only; also reachable as `.claude/skills/video-to-markdown/`) |
| Pipeline scripts | `scripts/` in this skill directory |
| Python interpreter | `$VIDEO2MD_PYTHON` if set, otherwise whatever `python3` is on the path |
| Companion references | `references/pipeline.md`, `references/gotchas.md`, `references/methodology.md` |
| Output contract | `{session-dir}/output/{session.md, transcript.md, stills/, stills.json, transcript.json}` |
| Digest contract (step 8) | `{session-dir}/output/{digest.md, verdicts.json, digest-transcript.json}` — derived, regenerable |

## Output

Per session: `session.md` (header table of sources, durations and notes; transcript lines `- [HH:MM:SS] text`; `## [t0 - t1] Screen N` blocks with image links), `transcript.md` (clean reader transcript — text only, no timestamps, no screenshots; rendered from the sanitized transcript once the digest has run, otherwise from `transcript.json`), `stills/NNN_HHMMSS.png`, `stills.json` (`{file, t0, t1, src, kind}` spans), and `transcript.json` (`{t0, t1, text, src}`, monotonic). Timestamps are session-relative across the concatenated usable media. Audio-only stretches carry no screenshots and say so in a header note.

## Self-check

Run the pipeline on a short recording you can verify by eye — five to ten minutes of any screen work is enough — and accept it only when all of these hold:

- Every image link in `session.md` resolves, and no screenshot in `stills/` is missing from the markdown.
- Screenshot density falls inside 12 to 360 per video-hour.
- No uncovered gap longer than 180 s inside a video segment.
- Pick three timestamps at random, answer "what was on screen and what was being done here?" from `session.md` alone, then check each answer against the recording. Three of three correct is the bar.

## Quality guidelines

Adhere to `library/reference/agent-quality-guidelines.md` (runtime behaviour) and `library/reference/skill-architecture.md` (structural principles).
