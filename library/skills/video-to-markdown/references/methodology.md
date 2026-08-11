# Methodology — video to markdown

The measurements behind every frozen config value, the detector comparison, the failure registry, the quality protocol and the re-tuning playbook. Purpose: change a config value WITHOUT re-running the original experiment, because the evidence is recorded here.

The build run's own working files — round logs, contact sheets, excerpt corpus, prior-art notes — are not part of this repository, so the numbers stated below are the record. Re-deriving any of them means re-running the recipe in § 6 on your own recordings.

## 1. Mechanism

### Screenshot detection (per video file)

1. Decode at 1 fps, scale to 480 px wide grayscale (area interpolation).
2. Hash the frame's bytes and compare with the previous frame — identical bytes exit early. Exactly-static screens are the common case: 62% of frames on one walkthrough excerpt.
3. Distance is the total-variation distance between 64-bin grayscale histograms, in the range 0 to 1.
4. A distance above the threshold (0.02) marks a change point; a run of unchanged frames lasting at least the minimum still (3 s) becomes a span `[t0, t1]`.
5. The representative frame is the END of the stable run — the settled state, which catches the outcome of typing and a page that finished loading. Prior art for lecture slides uses the FIRST stable frame; END was chosen because interfaces settle late (spinners, skeletons, form fills).
6. A zone changing continuously for longer than 15 s emits forced samples every 5 s, tagged `transition`. This is the backstop covering rapid application-switching bursts and live-video interludes.
7. Extraction seeks decode-accurately on a remuxed mp4, never on a damaged `.mkv` [gotcha F11].

Lineage: the mechanics (downscale, byte-hash early exit, grayscale histogram, a default skip threshold of 0.02, a maximum-skip safety valve) are adopted from the open-source ScreenPipe frame comparison; the policy was re-derived on our own corpus. ScreenPipe's own code comment records that downscaling to 320 px caused hash collisions on dense text, "making scrolling through log files invisible" — hence the 480 px floor.

### Timeline model

A session is an ordered set of usable media segments, concatenated: video over `[0, dur]`, continuation audio over `[dur, dur + wav]`. Usable duration is the LAST PACKET timestamp, never the container header [gotcha F5]. Wall-clock holes from a crashed recording get a header note, not timeline space.

### Transcription

The engine matrix is in `pipeline.md` § Engine matrix: an embedded caption track first (free, speaker-attributed, and an independent source to cross-check against), then a hosted transcription API (300 s WAV chunks across 3 workers, verbose JSON, per-chunk offset, three attempts per chunk), then a local model as automatic fallback. Hallucination filters drop a segment when `no_speech_prob > 0.6`, `avg_logprob < -1.0`, or `compression_ratio > 2.4`; the thresholds come from the transcription vendors' own documentation. Drop COUNTS are a diagnostic: 2687 drops on one file turned out to be the language-flip failure, not noise.

### Assembly

`assemble.py` lays the transcript down as the spine (`- [HH:MM:SS] text` bullets), interleaves screenshots at the start of their span, and runs a de-stutter pass (a repeated token, a repeated two-token phrase, and glued repeats in scripts without spaces are collapsed, with awareness of the previous line's boundary). Milestone headers every 600 s keep audio-only tails navigable without images.

## 2. Config provenance (frozen)

| Parameter | Value | What the sweep showed |
|---|---|---|
| Compare stream | 480 px gray, 1 fps, area-scaled | below about 480 px, changes in dense text vanish; 1 fps is sufficient for interface cadence, and prior art samples 1 to 3 fps |
| Distance | 64-bin histogram total variation, byte-hash early exit | the hash exits 62% of frames on static-heavy excerpts; the histogram is robust to video-tile churn |
| Change threshold | **0.02** | 0.05 LOST a 12-screen registration workflow on the walkthrough excerpt. 0.02 over-captures by 1.5 to 2 times, accepted because under-capture is unrecoverable and consolidation is cheap (the digest layer). Score distributions: median 0.003, 0.0075 and 0.002 across three excerpts — real transitions sit well above 0.02 and churn sits well below |
| Minimum still | **3 s** | 2 s admitted churn fragments at 407 to 462 screenshots an hour, above the band. 3 s holds density at 173 to 336 an hour on real sessions |
| Transition backstop | a zone changing for more than **15 s**, sampled every 5 s | a 17 s burst of four screens (an analyst note, a calendar, two chat threads) was dropped entirely: every screen was shorter than the minimum still AND the zone was shorter than the old 120 s backstop. 15 s and 5 s covers bursts and live-video interludes both |
| Representative frame | END of the stable run | the settled state; catches gradual typing outcomes that the small-area blind spot misses mid-run |
| Density band | **12 to 360** screenshots per video-hour | observed on real sessions at this config: 173 to 336 an hour; excerpt baselines 192, 252, 234. The band is the anti-degenerate gate, not a target |

## 3. Detector comparison

Ground truth: the walkthrough excerpt has about 15 to 20 known distinct screens (a registration workflow plus admin pages), counted by examining a contact sheet by hand.

| Family | Config tested | Result | Verdict |
|---|---|---|---|
| Histogram change-point (chosen) | threshold 0.02, 1 fps, minimum still 3 s | every known screen captured, 1.5 to 2 times over-capture | **CHOSEN** — capture low, consolidate later |
| Scene detection by content | threshold 10 (the prior-art recommendation for slides is 8 to 12, against a natural-video default of 27) | **5 screenshots** on the walkthrough excerpt, losing the registration workflow; 37 on a second excerpt | rejected — built for full-frame slide flips, blind to partial-frame interface changes |
| Background subtraction (MOG2) | the slide-extraction consensus: settle below 0.1% foreground, re-arm at or above 3% | 14 screenshots on one excerpt, 5 on the walkthrough — never re-arms on subtle interface changes | rejected |
| Scene-score, freeze detection, transcript-cue hybrid | — | not reached; the chosen family passed the gates first | untested |

Caveat carried in the confidence map: the two rejected families were tested at their RESEARCHED DEFAULT parameters, not exhaustively tuned. Re-running the comparison means cutting excerpts, building contact sheets, and counting against a known-screen ground truth (§ 6).

## 4. Failure registry (what broke, how it was found, what guards it)

Full trigger, wrong-default and correct-behaviour write-ups for the ones that were found in practice: `gotchas.md`.

| Code | Failure | Found | Guard |
|---|---|---|---|
| F1 | Scroll blindness: a long stretch with no stable frame yields zero screenshots | predicted before the run | gap gate: no uncovered span longer than 180 s |
| F2 | Video-tile or webcam churn means nothing is ever "still" | predicted before the run | density lower bound plus coverage audits |
| F3 | Degenerate config: zero screenshots, or thousands | predicted before the run | density band, 12 to 360 an hour |
| F4 | Transcription chunk-boundary timestamp drift | predicted before the run | monotonic-timestamp gate plus the transcript audit |
| F5 | Container header duration lies (header 5145 s, packets ending at 1972 s — 53 minutes unrecorded) | corpus preparation | duration is the last packet timestamp, everywhere |
| F6 | Automatic churn mask is a dead end: video tiles churn intermittently, in under half of frames, so the learned mask covers about 0% | round 1 | mask DROPPED; a 3 s minimum still already filters floor churn |
| F7 | A tail sliver of audio makes the API return 400 | full-run round | skip chunks under 0.5 s, measured by file size |
| F8 | Segment-muxed FLAC has no duration header, so real chunks are skipped as slivers | full-run round | segment to WAV; skip slivers by file size |
| F9 | A transient 404 on one chunk aborted the whole run | first session run | three attempts with backoff per chunk |
| F10 | A rapid application-switching burst dropped entirely: four screens in 17 s, carrying dense content | round 2 coverage audit | transition backstop, 15 s and 5 s |
| F11 | `-ss` seeks land off-target on a crash-damaged container — screenshots showed the WRONG content with sane timestamps; the worst class, invisible to every automated gate | round 2 coverage audit | remux `-c copy` to mp4 before all frame work; audits use decode-accurate frames |
| F12 | Small-area changes below the threshold are invisible (text typed in one field, a small dialog on a busy screen) | round 2 | ACCEPTED LIMITATION; representative-frame-at-END captures the settled outcome; a changed-pixel-ratio trigger is the untested candidate fix |
| F13 | A quota-dead API key was retried forever | round 2 | probe the key with a 15 s clip before the run; automatic fallback to the local engine |
| F14 | The transcriber flipped language: windows in the second language decoded as fluent English PARAPHRASE, which reads like a transcript and is not one | transcript audit on one audio file | sample per media file; force `--language`; drops fell from 2687 to 271 once forced |

## 5. Quality protocol (how the output was judged)

Frozen BEFORE tuning, with deterministic sampling so the grader cannot cherry-pick. Fresh sub-agents grade; never the builder.

- **Minute-X question and answer.** A grader agent extracts truth frames at deterministic timestamps and writes questions; a SEPARATE blind agent answers from `session.md` and the screenshots only. The walkthrough session scored 12 of 12, including exact counts read off the screen. Bar: 80%.
- **Transcript spot-check.** Sixty-second windows are re-transcribed by an INDEPENDENT engine, compared by token overlap, with a mandatory semantic read of the worst window. The token bar was moved from 0.85 to a median of 0.75 during the run, because measured cross-engine agreement is 0.78 to 0.86 in English and 0.48 to 0.85 in Chinese even when the two are word-for-word semantically identical (script variants, hallucination loops on the checking side, speaker prefixes). Lesson: a token bar on a non-Latin script is unreliable, and the semantic read is primary.
- **Contact-sheet completeness.** A reviewer walks 1 fps thumbnail strips against the chosen screenshots and lists distinct screens that were missed. This found the dropped application-switching burst [F10] and the off-target seek [F11]. Sheets are TRIAGE ONLY; keep and merge decisions need full-resolution reads, because thumbnails hide dialogs and filled fields.
- **Readability end-test.** A fresh agent must carry out the recorded process from `session.md` alone. The first such test returned 26 findings; every pipeline-attributable one was fixed over the following rounds (milestone headers, note scope, 30-plus entity fixes, the fourth de-stutter revision). Later rounds returned 8, then 8, then 3 findings, with no new failure class after the second, and the final round found nothing.
- **Convergence rule.** Stop only after two consecutive fresh adversarial rounds surface no NEW failure class.
- **Source-versus-pipeline triage.** Most "gaps" the readability test reported were SOURCE gaps — a credential never shown on screen, an unresolved supplier contract. The pipeline SURFACING them is correct behaviour, not a defect.

## 6. Re-tuning playbook (change a parameter without re-running the experiment)

Evidence bar for any change to the frozen config: reproduce the relevant sweep on a small corpus, run the relevant audit, and log the change where a gate value moves. Never retune per recording on eyeball alone.

1. **Cut a corpus** of 10-minute excerpts (`-c copy` is fine for mp4; remux `.mkv` first): `ffmpeg -ss <T> -i <video> -t 600 -c copy exA.mp4`. Include a dense interface workflow, a static-heavy stretch, a webcam or video-call interlude, and an application-switching burst if you have one. Keep a tuning set and a held-out set.
2. **Sweep the parameter** with `extract_stills.py --thr/--min-still/--trans-max/--trans-step --dump-scores`, and compare screenshots per hour against the 12-to-360 band alongside the score distribution. Real transitions should sit at least five times above the churn floor; the frozen config's margin is a churn median of 0.002 to 0.0075 against a threshold of 0.02.
3. **Build contact sheets** for coverage triage (`make_sheet.sh`), then judge ANY keep, merge or miss call at full resolution.
4. **Run the completeness audit** with a fresh agent (1 fps thumbnails against the chosen screenshots, held-out set included) — the check that caught both F10 and F11.
5. **Spot-check with three truth-frame questions** if the change touches the choice of representative frame.
6. **Raising the threshold or the minimum still?** Re-verify the two historical casualties first: the 12-screen registration workflow (lost at threshold 0.05) and the application-switching burst (lost when the minimum still exceeds the burst's dwell time). Both regressions are silent — no automated gate catches a missing screen.
7. **Log it.** Parameter sweeps and verdicts belong in the run's own notes, and a gate value that moves needs an explicit `GATE-CHANGE: old -> new, reason` line.

Re-tuning the digest layer (batch size, merge aggressiveness): re-run the digest audits — the under-merge hunt, the over-merge coverage hunt, the verbatim paraphrase diff — on one session before changing anything fleet-wide. The reduction floor (at least 12 kept screenshots per hour) and the record-integrity hashes are the deterministic rails.

## 7. Rejected alternatives (do not re-litigate without new evidence)

| Alternative | Why rejected |
|---|---|
| Minimum still of 2 s | 407 to 462 screenshots an hour, above the band, made of churn fragments |
| Automatic churn mask (learn the video-tile zones and mask them out) | tiles churn intermittently, so the learned mask covers about 0%; the minimum still already filters it |
| Aggressive automatic deduplication by histogram or perceptual-hash threshold | NO global threshold separates webcam-motion "duplicates" from real dialog changes. At full resolution the "near-duplicates" were mostly REAL state changes — dialogs, selections, typed text — with dry-run distances spread from 0.03 to 0.5. Superseded by the agent-judged digest layer |
| Scene detection by content or adaptive scene detection | under-captures interface walkthroughs by 4 to 10 times at prior-art parameters (§ 3) |
| Background-subtraction state machines (MOG2, KNN, GMG) | never re-arm on subtle interface changes (§ 3) |
| Word-level forced alignment | segment-level accuracy of 1 to 2 s is enough to align screenshots; word timestamps add infrastructure that no gate uses |
| A whole-document agent rewrite for the digest | unauditable, with the entire document as hallucination surface. Replaced by structured per-screenshot verdicts, a deterministic renderer, and a verbatim-guarded transcript |
| Restoring blind find-and-replace for name correction | one garble can map to several real names, and some are context-dependent; an agent pass with a name list and an ambiguity report replaces it |

## 8. Digest layer

Two files. `session.md` is the complete record, hash-gated and untouched; `digest.md` is the derived reader view, regenerable at any time. Sub-agents JUDGE (structured keep, merge and drop verdicts with captions of at most 120 characters, in batches of about 15 screenshots with overlapping transcript excerpts); deterministic scripts EXECUTE (`digest_batches.py`, then the verdict sub-agents, then `digest_merge.py` to resolve merge chains, then `sanitize_transcript.py` for the whitelist-guarded transcript, then `render_digest.py`).

The transcript stays VERBATIM apart from a frozen whitelist: speaker-label formatting, punctuation and whitespace, high-confidence canonical substitutions authorized by the engagement's name list, artifact removal, and logged drops of pure filler. A per-segment content-token preservation guard of at least 0.85 makes paraphrase machine-detectable, and every violating proposal is rejected rather than repaired. Merge targets resolve along the chain to a kept screenshot; in doubt, keep; captions NEVER transcribe a credential value.

Convergence record from the walkthrough session: 15 verdict sub-agents and 2 sanitize sub-agents produced the first cut, keeping about 65%. Five fresh adversarial audit rounds — under-merge, caption against image, paraphrase diff, coverage, seven agents each — drove it to 142 of 230 kept, a 38% reduction, with the paraphrase check clean for five consecutive rounds and zero confirmed coverage losses. Every claimed loss was adjudicated and turned out to be a source gap, or an auditor missing the merge chain, or a later kept screenshot showing the same thing.

Failure classes found in this layer and now gated: degenerate batch returns that are schema-valid garbage (caught by the completeness check), caption imprecision (dropped qualifiers, a control named as the wrong type), mid-word caption truncation at the schema cap, external deletion of derived artifacts by a parallel session (fixed by snapshotting to a private temporary directory), and caption rotation within a batch — the worst class, caught only by a full-coverage caption-against-image audit.

Convergence came from FREEZING the merge rubric (main-content-pane identity; changes confined to chrome never keep; a return to a screen already shown merges) rather than from more auditor rounds. Fresh auditors redraw a subjective threshold every round until the rule is definitional.
