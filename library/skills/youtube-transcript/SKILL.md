---
name: youtube-transcript
description: Turn a video URL into a clean markdown transcript — free captions when the video carries them, a local transcription pass when it does not. Triggers on youtube transcript, transcribe this video, get the text of that walkthrough.
argument-hint: <video-url> [output.md]
---

# Video URL to Transcript

> Turns a video URL into readable text. In an engagement this is how a training video, a recorded
> walkthrough or a supplier's how-to becomes something you can quote in a process record instead of
> watching four times.
>
> Two routes, tried in this order: captions if the video carries them, which is free and needs no
> account; a local transcription pass if it does not. Anything `yt-dlp` supports works, not only
> YouTube.

## Inputs

- `<video-url>` — the video. If it is missing, ask.
- `[output.md]` — where the transcript is written. With no path it prints to the terminal, which is
  fine for a look and not fine for anything you intend to cite.

No flags.

## Constants

| Key | Value |
|---|---|
| Skill location | `library/skills/youtube-transcript/`, reached through the `.claude/skills` symlink |
| Caption cleaner | `scripts/clean_vtt.py` — WebVTT to plain text, Python standard library only |
| Dependencies and maintenance | `references/setup.md` |
| Fallback when there are no captions | the pipeline in `library/skills/video-to-markdown/` — transcribes on this machine, no account, no cost |
| Where a transcript is filed | `engagements/<client-slug>/interview/` |

## Workflow

1. **See what the video carries before downloading anything.**

   ```bash
   yt-dlp --list-subs "<video-url>"
   ```

   Manual captions, written by a person, beat automatic captions produced by speech recognition. Both
   beat nothing. The listing labels which is which.

2. **Pull the captions.**

   ```bash
   yt-dlp --skip-download --write-subs --write-auto-subs \
     --sub-langs "en.*,en" --sub-format vtt -o "%(id)s" "<video-url>"
   ```

   Writes `<id>.<lang>.vtt` into the working directory. `--sub-langs` filters to English; when the
   owner's video is in another language, replace it with that language's code, or use `--sub-langs all`
   and pick the track from what arrives.

3. **Clean them.**

   ```bash
   python3 library/skills/youtube-transcript/scripts/clean_vtt.py <id>.en.vtt
   ```

   Cue numbers, timings, karaoke tags, HTML entities and the rolling repeats automatic captions produce
   all come out; one line of speech per line, in order. Add `> transcript.txt` to keep it. The script
   exits non-zero and says so when the file holds no caption text — that is a malformed or empty
   caption file, not an empty video.

4. **If there are no captions**, in this order:

   - **Ask the owner.** A written procedure, a caption file or an existing transcript often exists
     already, and any of the three beats a transcript you generated. Working standards rule 1: sourced,
     not generated.
   - **Transcribe locally.** Download the video into a fresh directory and run the pipeline in
     `library/skills/video-to-markdown/`. It transcribes on this machine at no cost, and interleaves
     screenshots — which is what you want anyway for a screen walkthrough, where half the information
     is which screen is open.

     ```bash
     mkdir -p <session-dir>    # one video per directory — that pipeline's contract
     yt-dlp -f "bv*[height<=1080]+ba/b" --merge-output-format mp4 \
       -o "<session-dir>/video.mp4" "<video-url>"
     ```

   - **A hosted speech-to-text service** also works. It costs money on an account of your own, and it
     sends the owner's recording to a third party. Ask the owner before doing that, not after.

5. **File it.** A transcript from a client's video is engagement material:
   `engagements/<client-slug>/interview/{date}_{slug}.md`, and update that directory's `INDEX.md` in
   the same operation. Keep the downloaded media out of the repository — commit the transcript, never
   the recording.

6. **Verify before reporting done.** The output is non-empty, opens with the `# {title}` header, and
   reads as speech rather than as timing artifacts. Read two passages yourself. Report the path and
   which route produced it — captions or local transcription.

The title for the header comes from the same tool:

```bash
yt-dlp --skip-download --print "%(title)s" "<video-url>"
```

## Gotchas

- **A transcript is working material, not a deliverable.** Working standards rule 2: nothing raw reaches
  the reader. What the owner sees is the process record you wrote from it.
- **A video is not an interview.** It shows what was recorded once, on a good day, with the exceptions
  left out. Use it to prepare better questions, never to skip asking them.
- **`yt-dlp` breaks roughly quarterly**, when the site changes its internals. Symptom: metadata or
  download fails on a URL that plays fine in a browser. Fix and cadence: `references/setup.md`.
- **Automatic captions repeat themselves.** Each cue restates the tail of the previous one, so a
  hand-cleaned file ships most lines twice. `clean_vtt.py` collapses them against a four-line window.
- **Automatic captions carry no punctuation and no casing.** Expected, not a fault. They are evidence of
  substance, not of wording — never present a line of automatic caption as a verbatim quote of the
  owner.
- **An auto-translated caption track reads fluently and is wrong in the details.** If the only English
  track was machine-translated from another language, step 1's listing says so; prefer the original
  language plus your own reading over a fluent mistranslation.
- **A private, unlisted or login-walled video will fail**, and that is the correct outcome. Ask the
  owner for the file or for access granted to them; do not drive it with credentials that are not
  yours.
- **Length costs nothing on the caption route and real time on the local one.** Captions are a text
  download at any duration. Local transcription runs against the machine, so say how long it will take
  before starting a two-hour video.

## Style

Procedural skill. The output is a transcript, so no voice is prescribed. The logic lives in `yt-dlp` and
one small script, not in the prompt.

## Output

```
# {video title}

> Source: {url}
> Method: captions (manual) | captions (automatic) | local transcription | {date}

{transcript text}
```

## Eval

**No fixture ships with this copy**, and building one takes about a minute — do it before you rely on
the skill in front of a client. Pick any public video that carries manual captions, run steps 1 to 3,
and record the expected first line and the line count. Acceptance: a non-empty transcript that opens
with the title header and contains a phrase you know is spoken in the video. Re-run it after every
`yt-dlp` upgrade, which is the one part of this skill that changes underneath you.

## Quality Guidelines

Adhere to the quality guidelines in `library/reference/agent-quality-guidelines.md` (build-verify,
review before exit) and the structural principles in `library/reference/skill-architecture.md`
(three-tier disclosure, gotchas).
