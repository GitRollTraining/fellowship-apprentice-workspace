# Gotchas — interview recording

Every item below was measured on a real recording, not anticipated at design time.

## Speaker labels are the part that fails, not the words

On one consumer voice recorder, automatic speaker separation failed on **every** recording tested: one
label for a two-person conversation; three labels where the third fired in a single block out of
sixty-six; two labels for three people. The *text* was competitive throughout. Only the attribution was
broken.

So grade the labels before trusting them (workflow step 4), and when they fail, keep the transcript and
reconstruct attribution from content. Discarding a usable transcript over its labels pays twice for the
same words.

## Never split long audio into chunks

**Trigger:** a recording over an hour, and an instinct to cut it into pieces so it uploads faster.
**Wrong default:** split it, transcribe the pieces, concatenate the results.
**Correct behavior:** the whole file in one request. Speaker labels are assigned per request, so a chunk
boundary renumbers every speaker and destroys identity across the join — the owner is `Speaker A` before
the cut and `Speaker B` after it, and nothing in the output says so. Expect several minutes on a long
file.

## A truncated download reports success

**Trigger:** the audio was copied off a device or pulled over a link.
**Wrong default:** trust the duration a player shows.
**Correct behavior:** a partial copy keeps the original container header, so it claims the full duration
while holding a fraction of the audio. Check before paying for it:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 audio.local.m4a
```

Compare that against how long the session actually ran. You were there; you are the reference.

## A polished transcript is not a re-diarization

**Trigger:** the service offers a cleaned-up or polished version of the same transcript, described as
keeping speakers and timestamps.
**Wrong default:** reach for it to fix bad labels.
**Correct behavior:** measured on a two-person control recording, the polished block returned the same
fifty-one utterances under the same single collapsed label, with about 1.5 KB of wording smoothed away —
wording the refine step exists to preserve. It cannot turn a failed label check into a passing one. Take
the raw transcript and do the cleaning yourself.

## Never count words in a language written without spaces

A transcript in a language with no inter-word spacing under-reports by roughly an order of magnitude
under `wc -w`. A forty-minute session once appeared as "522 words" and was written up as suspiciously
compressed; it was dense continuous speech. Use `wc -m`.

## The script an engine returns is an artifact of the engine

The same speaker's recordings have come back in one written script on one date and a different one on
another. Every engine measured has some form of this. Preserve the export verbatim, note the mismatch,
and infer nothing about the speaker from it.

## Translation instead of preservation

**Trigger:** the conversation switches between two languages, which is common.
**Wrong default:** "translate it to English for readability."
**Correct behavior:** preserve the code-switching verbatim in both `original.md` and `refined.md`. An
English gloss goes in `[brackets]` only where a term is genuinely ambiguous. Section headings may be in
your working language.

## The audio and any identity-grade numbers are the only never-commit items

**Trigger:** the owner reads an account, card or identity number aloud, or the audio file is sitting in
the session directory.
**Wrong default:** commit everything, because the repository is yours.
**Correct behavior:** keep the audio out of git (workflow step 2, verified with `git check-ignore`, never
assumed). In the committed transcript replace the digits with `[redacted — account number]`; if you need
the digits, keep them beside the file under the same stem plus `.local.md`, covered by the same ignore
rule. A number in a git history is a number you cannot take back.

## Ask about recording before the session, not at the start of it

Consent obtained in the doorway is consent under pressure, and a refusal there costs you the session you
travelled to. Ask when you book it, and confirm it out loud once the recorder is running.

What a no-recording session costs, stated so you can decide rather than discover: you cannot audit
questioning you have no record of, so the self-audit is impossible; the ambiguity list has to be built
live; and every pointer in your write-up resolves to your own notes rather than to something the owner
could check without you. Treat it as a first pass to be repeated.

## This workspace asks before every network call

`.claude/settings.json` puts `curl` in `ask`, so the upload in workflow step 3 raises a prompt. That is
the gate working as designed — approve it when you recognise the command, and read it when you do not. A
first engagement should never be able to send something to the internet by accident.

## The service's request fields are the one thing here that rots

Everything else in this skill is a file operation or a text pass, and both are stable for years. A
speech-to-text vendor changes field names, model names and prices on its own schedule. If an upload
returns a 4xx on a key you know is good, read the service's current documentation before changing
anything else. Keep the key in your shell environment; a key committed to git is a key you must rotate.

## The raw transcript is not a deliverable

Nothing raw reaches the reader (`library/sops/working-standards.md`, rule 2). `original.md` is evidence,
not output. What the owner sees is written for the owner; `breakdown.md` is what you work from.
