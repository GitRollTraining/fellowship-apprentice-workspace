# Gotchas — video to markdown

Failure modes found while building and hardening this pipeline: three real sessions, six excerpts, three adversarial audit rounds, then a second phase for the digest layer. Each entry gives the trigger, the wrong default, and the correct behaviour.

## F5 — Container header duration lies on truncated files

**Trigger:** the recording crashed mid-write (one file's header said 5145 s; its packets ended at 1972 s).
**Wrong default:** trust `ffprobe format.duration`. Gap checks then demand screenshots inside a hole that holds no data, and the session arithmetic is off by an hour.
**Correct:** duration is the last readable packet timestamp (`ffprobe -select_streams v -show_entries packet=pts_time | tail -1`); state the unrecorded wall-clock gap in the session header.

## F8 — Segment-muxed FLAC has no duration header

**Trigger:** using `ffmpeg -f segment` to cut `.flac` chunks for upload.
**Wrong default:** ffprobe returns `N/A`, so a naive float parse crashes, or a duration-based sliver guard skips REAL chunks.
**Correct:** segment to WAV, and skip slivers by file size (16 kHz mono 16-bit is 32000 bytes per second).

## F9/F13 — Transcription API transient failures and quota death

**Trigger:** one chunk of seventeen returns 404 (transient routing), or the key is quota-dead and returns 429.
**Wrong default:** an all-or-nothing abort discards every successful chunk; a quota-dead key is retried forever.
**Correct:** three attempts with backoff per chunk; on persistent failure in auto mode, fall back to the local engine. Probe a key with a 15 s clip before burning a long run.

## F10 — Rapid application-switching bursts drop entirely

**Trigger:** the presenter flips through three or four applications in about 15 s, each visible for 1 to 8 s.
**Wrong default:** every screen is shorter than the minimum still AND the zone is shorter than a long transition backstop, so all of them are dropped — and a burst usually carries dense content. In the build run it was a note, a calendar and two chat threads.
**Correct:** transition backstop of 15 s, sampling every 5 s. The same fix covers live-video interludes, such as a webcam view or a video-call gallery, whose per-frame churn chops stable runs into fragments.

## F11 — `-ss` seeks land off-target on damaged containers

**Trigger:** input-seeking a crash-damaged or unindexed `.mkv` for frame extraction.
**Wrong default:** the extracted screenshot shows a DIFFERENT screen than the detected span. Timestamps look sane and the content is wrong — the worst failure class found, invisible to every automated check.
**Correct:** remux `-c copy` to mp4 before any frame work; when auditing, compare against decode-accurate frames (`select='eq(n,T*fps)'`), not seeks.

## F12 — Small-area changes below the threshold are invisible (accepted limitation)

**Trigger:** text typed into one field, a small dialog on a busy screen, a tiny tile flipping state.
**Wrong default:** assume every meaningful state change produces a screenshot.
**Correct:** know the limit. A whole-frame histogram distance cannot see a small-area change below the threshold. Because the representative frame is the END of a stable run, the settled outcome is still captured even when the intermediate typing is not. A candidate future fix is an additional changed-pixel-ratio trigger; it is untested.

## F14 — The transcriber flips language on code-switched audio

**Trigger:** a conversation in one language sprinkled with English technical terms; the transcriber auto-detects per window.
**Wrong default:** some windows decode as a fluent-looking English PARAPHRASE of the other language — it reads like a transcript and is not one.
**Correct:** sample each media file's transcript; if the flip is there, force `--language` to the dominant language and re-run that file. Chunked API transcription flips less than whole-file local auto-detection, but check both.

## A caption track is a rolling window, not a list of segments

**Trigger:** extracting an embedded caption track (`mov_text`) from a meeting or conferencing recording.
**Wrong default:** treat each 4 s cell as a segment, which yields choppy, duplicated text.
**Correct:** merge consecutive same-speaker cells (gap of at most 1 s, capped at about 15 to 30 s). Caption tracks carry SPEAKER NAMES, so prefer them over automatic transcription when they exist; they are also an independent source to cross-check against.

## A continuation audio file is a separate sequential segment

**Trigger:** the screen recording stops and the owner keeps talking into a voice recorder.
**Wrong default:** treat the audio as a parallel track needing cross-correlation to sync.
**Correct:** verify the start-time arithmetic (video start plus usable duration should land at about the audio file's start), transcribe it with `--t-offset <video usable duration>`, and say in the header that those sections carry no screenshots.

## Name correction must be an agent pass, never a find-and-replace

**Trigger:** the transcriber garbles proper nouns. A supplier called QuikBake comes back as "quick bake" in one place and "kwik bait" in another; the software the business runs on becomes a common noun; a member of staff becomes a different name entirely.
**Wrong default:** a blind find-and-replace from an alias list. One garble can map to several real names, and some depend on context.
**Correct:** a conservative agent pass against the list of proper nouns you collected from the owner. High-confidence corrections only; anything ambiguous is reported, not changed. The screenshots can settle an ambiguity — read the screen the speech points at.

## The credential rule does not cover money or pay figures

**Trigger:** a shared screen shows a named person's pay, a bonus, or the price a named customer was charged, which is a different thing from a login credential.
**Wrong default:** assume the credential rule (never transcribe passwords, tokens, PINs, account numbers, balances) also requires withholding pay figures from captions.
**Correct:** the credential rule's scope is login-adjacent values only. Pay and personal financial detail visible on screen form a SEPARATE, real sensitivity category that the digest pipeline does NOT redact — captions may state them factually, as they would any other on-screen content. This is a deliberate scope boundary, not an oversight; it was raised repeatedly across audit rounds and confirmed each time. Flag any digest containing a named person's pay detail for human review before it is shared, matching the treatment of credential-bearing screenshots. Do not silently redact it, and do not treat quoting it as a caption defect.

## Screenshots capture live credentials

**Trigger:** a walkthrough recording passes through a password manager, a saved-credentials page, a bank dashboard.
**Wrong default:** treat the output directory as an ordinary shareable artifact.
**Correct:** the output stays out of version control until it has been reviewed, and anything the owner said must not leave the business goes into an untracked sidecar. Say so in the run report every time.

## Frame index is not wall-clock seconds

**Trigger:** extracting probe frames by frame number for an audit.
**Wrong default:** assume 25 fps (`n = t*25`), or assume that probe N of an `fps=1/15` pass sits exactly at 15N seconds — drift accumulates over a long unseeked pass.
**Correct:** read the real frame rate (`r_frame_rate`; screen recorders often write 60), and for exact-time ground truth use decode-accurate select expressions rather than arithmetic on probe indexes.

## Digest verdict sub-agents return schema-valid garbage

**Trigger:** one batch agent in a fan-out returns 1 verdict out of 15, with the caption "test" — which passes schema validation.
**Wrong default:** trust schema-valid output and render with verdicts silently missing.
**Correct:** the completeness check in `digest_merge.py` is the gate (exit 2 plus a list of what is missing, then re-dispatch the FULL batch including the poisoned verdict). Scan results for placeholder captions before rendering.

## Digest captions drift from the pixels

**Trigger:** a verdict sub-agent captions 15 images in one pass.
**Wrong default:** accept fluent captions. The observed failure classes: on-screen qualifiers dropped from a label, a control named as the wrong type (a toggle called a checkbox), over-generalizations that contradict the visible rows, mid-word truncation at the 120-character cap, and caption ROTATION, where a caption describes the neighbouring screenshot — the worst class, because it reads perfectly plausibly.
**Correct:** prompts demand on-screen labels verbatim, endings on a complete word, and a caption written immediately after reading each image. Every audit round re-verifies caption against image at full resolution for ALL kept screenshots.

## Under-merge needs a definitional rubric, not more auditor rounds

**Trigger:** each fresh audit round flags a different set of "near-identical" pairs, because auditors redraw a subjective threshold every round — round 2 passed pairs that round 3 flagged.
**Wrong default:** keep iterating rounds and hope the count reaches zero.
**Correct:** freeze the rule. Reader-equivalence is identity of the MAIN CONTENT PANE; a sidebar scrolling or expanding, a nav or row hover, the cursor, webcam tiles and clock deltas NEVER earn a keep; a return to a screen already shown, adding nothing, merges into the first visit. Embed the rubric verbatim in the verdict prompts AND the audit prompts. Convergence then comes from the rule rather than from taste.

## Two screens that match visually can still differ in one cell

**Trigger:** two screenshots of the same spreadsheet or table look identical at a glance — same rows, same columns, same scroll position — but one has a CELL VALUE the other does not (a "Covered by" cell empty in the first, filled "Saturday relief baker" in the revisit).
**Wrong default:** merge on layout match alone, which loses the single piece of new information the revisit exists to show.
**Correct:** before merging a return to a page already shown, check whether any cell or field VALUE differs, not only the layout, scroll position or dialog state. The coverage audit — checking that content the transcript refers to is visible somewhere — is the backstop that catches this when it slips through.

## Sampling audits find violations one at a time; run a full scan instead

**Trigger:** a 20-segment random sample per round keeps finding exactly ONE new unauthorized substitution every round, three rounds running, on a transcript of 955 segments. Sampling converges slowly on a large population.
**Wrong default:** keep sampling, fix each find, and conclude "clean" after two rounds with nothing new — when 20 of 955 gives poor coverage.
**Correct:** once sampling repeatedly finds violations, run a DETERMINISTIC full scan. Diff every segment where the digest text differs from the source text, computing both the lowercased token-overlap ratio and a case-sensitive token comparison. Classify each diff as AUTHORIZED (an EXACT string match to an entry in the engagement's name list) or UNAUTHORIZED (anything else, including a confident phonetic match to a name that is on the list only in another spelling). Fix all unauthorized instances in one pass, not one per round.

**The correction that cost the most:** a first pass authorized "confident cluster match, even without exact spelling" — "Kwik" and "Quick Bait" folded into QuikBake because they sound close to spellings already listed. Two INDEPENDENT fresh audit rounds flagged that exact pattern as unauthorized, while zero rounds ever flagged any of the dozens of EXACT-match substitutions, despite equal exposure across five rounds. That asymmetry is the evidence: require an exact string match, full stop. "Clearly the same sound" is not authorization, however confident it looks.

## A case-only token change hides an unauthorized substitution

**Trigger:** a sanitize edit changes only the CASE of a token ("save" becomes "SAFE"). The tokenizer lowercases, so this looks like 100% token preservation and sails past the 0.85 guard, even though nothing on the name list authorizes it.
**Wrong default:** trust the token-preservation ratio alone.
**Correct:** `sanitize_transcript.py` also runs a case-sensitive comparison, and hard-rejects a same-length edit that differs ONLY in character case, whatever the ratio says. Even a plausible case fix — the screen may well read "SAFE" — must go through the name list or stay reported rather than applied. What an agent infers from an image is not a substitution channel.

## Manual verdict edits corrupt silently without the merge authority

**Trigger:** the orchestrator patches `verdicts.json` by hand, rebinding dictionary entries or flipping a single verdict.
**Wrong default:** ad-hoc edits. A rebound mapping never lands in the serialized list, and a flipped merge target leaves a dangling chain (139 into 138 into nothing).
**Correct:** every patch re-runs chain resolution and rebuilds the screenshot list, or simply re-runs `digest_merge.py`. The renderer's fatal check on merge targets is the backstop. Snapshot the derived artifacts to a private temporary directory after each milestone — a parallel session once deleted the lot mid-run.

## Contact-sheet thumbnails hide real differences

**Trigger:** judging duplicate screenshots, or subtle misses, from a tiled montage.
**Wrong default:** merge and prune decisions made at 384 px thumbnails ("those look identical") when the full-resolution frames differ meaningfully — dialogs, filled fields, selections.
**Correct:** contact sheets are for coverage triage only. Any keep, merge or miss decision needs the full-resolution screenshots read directly.

## Hallucination filters need adjudication, not blind trust

**Trigger:** long stretches of silence or noise; two devices recording the same room.
**Wrong default:** either no filters, so hallucinated loops enter the transcript, or silent trust in the drop count — 2687 drops on one file turned out to be the language-flip symptom, not noise.
**Correct:** filter on `no_speech_prob > 0.6`, `avg_logprob < -1.0`, `compression_ratio > 2.4`, then SAMPLE both what was kept and what was dropped. A large drop count is a diagnostic, not a success signal.

## Detector defaults from slide-extraction prior art mislead

**Trigger:** adopting scene-detection or background-subtraction parameters recommended for lecture slides.
**Wrong default:** those thresholds under-capture a walkthrough of a user interface by 4 to 10 times, because they were built for full-frame slide flips rather than partial-frame changes.
**Correct:** the frozen config here — histogram total-variation distance, threshold 0.02, at 480 px grayscale and 1 fps — was validated against a ground truth of about 22 known screens. Re-run that comparison before swapping detector families.

## Several unrelated videos in one intake directory are NOT one session

**Trigger:** the session-directory argument points at a directory holding two or more video files.
**Wrong default:** concatenate them onto one timeline with `--t-offset/--append` to keep it to "one markdown per invocation". Unrelated content gets a fake shared timeline, and the single-video contract of `run_session.sh` is bypassed by hand-driving it.
**Correct:** one video is one session is one output set. Create one session subdirectory per video, move each video in, and run the pipeline once per subdirectory. The only multi-media session is a video plus a continuation audio file, verified by the video's end landing at about the audio's start.

## The merge step truncates over-length captions mid-word

**Trigger:** a verdict sub-agent writes captions longer than 120 characters despite the caption discipline in its prompt.
**Wrong default:** trust the merge gate. `digest_merge.py` clips to 117 characters plus an ellipsis without failing, producing captions that end mid-word or on a dangling quote, pass the length check, and ship into `digest.md`.
**Correct:** after merging, scan `verdicts.json` for captions of 118 characters or more, or ending in an ellipsis. Every hit is an over-length caption that must be REWRITTEN in the result file — complete word, quoted labels intact — then re-run `digest_merge.py` and `render_digest.py`. The caption-against-image audit must also flag dangling or unclosed quotes, not only mid-word endings.
