---
name: interview-recording
description: Use when an interview recording must become a session record: transcribe with speaker labels, refine, reduce to key points, decisions, open questions. Fires on transcribe this interview.
argument-hint: <path/to/audio> [attendee-count] [session title]
---

# Interview recording

> One recorded conversation becomes three files: the audio as captured, a transcript with each turn
> attributed to a speaker, and a one-page reduction of what was said. This is engagement step 1 feeding
> step 2 — the session happens, and this turns it into something a process can be reconstructed from.
>
> What to ask in the room is a different job, and this skill does not restate it:
> `library/playbooks/playbook-interview.md`. Which step's output goes to which directory:
> `library/playbooks/playbook-interview.runbook.md`.

## Preconditions

1. The owner has agreed to the recording and knows what happens to it afterwards. Ask before the session, not at the start of it (interview playbook, precondition 2). A session you did not record is a first pass to be repeated, not the record.
2. You know how many people will speak, and their names. The label check in step 4 takes the count as an input and cannot infer it.
3. You have a key for a speech-to-text service, exported in your shell. **You supply your own key and the service bills your own account — nothing in this repository ships an account, a key or a quota.**

## Constants

| Key | Value |
|---|---|
| Session directory | `engagements/<client-slug>/interview/session-<date>/` |
| Audio, never committed | `audio.local.<ext>` in that directory |
| Raw transcript | `original.md` — what the service returned, unedited |
| Attributed transcript | `refined.md` |
| Reduction | `breakdown.md` — key points, decisions, open questions |
| Transcription requirement | one request per recording, speaker labels requested, language detected not pinned |
| Refine and reduce protocol | `references/refine-and-breakdown.md` |
| Measured failure modes | `references/gotchas.md` |

## Workflow

1. **Capture.** One device, one continuous file, from the moment consent is confirmed out loud to the end of the conversation.
   - Do not split the session across files. A split is what breaks speaker labels later, and it cannot be repaired afterwards (gotchas).
   - Put the recorder between the two of you, away from the fridge, the extractor fan and the road.
   - Say the date, who is present and which process is being discussed into the first ten seconds. That announcement survives every later copy of the file; a filename does not.
   - Note-taking while you are the one asking is craft the interview playbook owns — see its capture section. This step is only the machine.

2. **File the audio, and keep it out of git.**
   ```bash
   D=engagements/<client-slug>/interview/session-$(date +%F)
   mkdir -p "$D"
   mv <recording> "$D/audio.local.m4a"
   git check-ignore -v "$D/audio.local.m4a"
   ```
   The last command must print a matching ignore rule. If it prints nothing, the file is tracked: add `*.local.*` to `.gitignore` and run it again. An interview recording is the client's material and a large binary, and neither belongs in a commit.

3. **Transcribe the whole file in one request, with speaker labels on.** Three requirements, whichever service you use:
   - **Speaker labels requested in the request itself.** A transcript that came back without them cannot be attributed afterwards; the information is gone.
   - **The whole file in one request.** Labels are assigned per request, so a split renumbers every speaker at the boundary.
   - **Language detected, not pinned.** Pinning one language collapses a conversation that switches between two.

   Worked example against one service that meets all three. The field names are that service's; the shape is general.
   ```bash
   cd engagements/<client-slug>/interview/session-<date>
   KEY="$SPEECH_API_KEY"

   UPLOAD=$(curl -s -X POST https://api.assemblyai.com/v2/upload \
     -H "authorization: $KEY" --data-binary @audio.local.m4a \
     | python3 -c 'import json,sys; print(json.load(sys.stdin)["upload_url"])')

   ID=$(curl -s -X POST https://api.assemblyai.com/v2/transcript \
     -H "authorization: $KEY" -H "content-type: application/json" \
     -d "{\"audio_url\":\"$UPLOAD\",\"speaker_labels\":true,\"language_detection\":true}" \
     | python3 -c 'import json,sys; print(json.load(sys.stdin)["id"])')

   # repeat until "status" reads completed; a long recording takes minutes, not seconds
   curl -s "https://api.assemblyai.com/v2/transcript/$ID" -H "authorization: $KEY" > transcript.json

   python3 - <<'PY' > original.md
   import json
   d = json.load(open("transcript.json"))
   assert d["status"] == "completed", d["status"]
   for u in d["utterances"]:
       m, s = divmod(u["start"] // 1000, 60)
       print(f'**Speaker {u["speaker"]}** [{m:02d}:{s:02d}]: {u["text"]}\n')
   PY
   ```
   Put the frontmatter block from `references/refine-and-breakdown.md` at the top of `original.md`. Keep `transcript.json` beside it; it holds word-level timings the markdown drops. Transcription is billed per audio hour — check the current price before sending a two-hour session, and do it the same day as the session, because the write-up is due while the conversation is still fresh (interview playbook step 15).

4. **Grade the labels before trusting them.**
   ```bash
   grep -oE '\*\*Speaker [A-Z]\*\*' original.md | sort | uniq -c
   ```
   - Fewer distinct labels than people who spoke, or one label carrying nearly every turn, means attribution failed. Do not throw the transcript away — the words are usually right and only the labels are wrong. Reconstruct attribution from content in step 5 and say in the file that you did.
   - A matching count is not proof. The check counts labels; it cannot hear who spoke, so it passes two speakers swapped with each other. Read a page before accepting it.

5. **Refine, then reduce.** Follow `references/refine-and-breakdown.md`. Non-negotiables: preserve the language exactly as spoken and never translate; keep what the engine garbled with a `[sic: what it wrote]` gloss rather than repairing it into something the owner did not say; mark genuine uncertainty `[unclear]`; treat any engine's speaker labels as a starting point rather than truth.

6. **Index it at the point of creation.** Add a row to `engagements/<client-slug>/interview/INDEX.md` naming the session directory, the date, the process discussed, and which of the three files exist. Record whether the labels passed step 4 — a later reader needs to know how much of the attribution is the engine's and how much is yours.

7. **Hand nothing raw onward.** `original.md` is not a deliverable; nothing raw reaches the reader (`library/sops/working-standards.md`, rule 2). You work from `breakdown.md`; what the owner reads is the owner-facing account, which the interview playbook produces at step 20.

## Gotchas

`references/gotchas.md`. The four that cost the most: **speaker labels are the part that fails, not the words**; **never split long audio**, because a chunk boundary renumbers every speaker; **a truncated download reports success**, because the partial file keeps the original duration in its header; **the audio and any identity-grade numbers are the only never-commit items.**

## Style

Procedural. `refined.md` preserves the source language with no translation. `breakdown.md` is a descriptive fact-sheet: facts, tables, plain lists, no narrative and no persuasion. Model floor: a mid-sized model — the smallest ones garble non-English speech and attribute speakers poorly, which is exactly the work in step 5.

## Eval

No baseline ships with this skill. One would be: a short two-speaker recording whose correct transcript you already have, with acceptance criteria that the label grade in step 4 was run and recorded, that `refined.md` carries the language as spoken, and that `breakdown.md` has all three headings with `_None identified._` where a section is empty. Building that pair is a good first contribution to this library.

## Quality Guidelines

Adhere to:
- `library/reference/agent-quality-guidelines.md` (runtime behavior)
- `library/reference/skill-architecture.md` (structural principles)
