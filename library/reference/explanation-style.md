# Explanation Style — the explanation register

> **User-level: applies in every repository, not only the KBs.** The trigger is the reader's
> unfamiliarity with the field, so this is as relevant explaining a codebase, a library or an API as
> explaining a research paper. Pointed at from `~/.claude/CLAUDE.md`; the KB style rule
> (`descriptive-style.md` Layer 4) records only the exemption it creates and defers here.
>
> Established 2026-07-28, promoted to user level the same day. Distilled from a live walkthrough of an
> IECON 2026 paper on attention sinks under 4-bit quantization, where the reader began at "none of
> these terms make sense to me" and finished able to state the paper's result, its surprise, and its
> weakest point.

## When this applies — and when it must not

**Trigger: the reader is unfamiliar with the field.** Not the document type. A statement of work in a
domain the reader knows needs no explanation register; a research paper in a field they know needs
none either. The same document warrants explanation for one reader and not another.

**This is a distinct genre from a digest, not a variant of one.** A digest is a faithful, sourced,
compressed *record* — Layer 2 governs it, and Layer 2 forbids exactly what explanation requires
(narrative, analogy, build-up). The two must not be merged into one artifact:

| | Digest (Layer 2) | Explanation (Layer 4) |
|---|---|---|
| Job | preserve the content so nobody re-reads the source | get an unfamiliar reader to competence |
| Register | facts, tables, lists; no narrative | one carried analogy; deliberate build-up |
| Success test | no-reopen: reader never needs the original | reader can restate the result and its surprise unprompted |
| Ordering | the source's own structure | whatever order builds comprehension |

Where both are wanted, produce **two artifacts** that cross-link — never explanation sections inside
a digest. (The 2026-07-27 IECON run did embed them, under time pressure; that is the known-wrong
form, retained only because it was already in use.)

Do **not** fold these rules into a document-ingestion skill such as `wei-digest-doc`: that skill
handles RFQs, statements of work, vendor responses and amendments as well as papers, and four of
those five want the deadline and the page limit, not an anchor object.

## The three primary moves

Ranked — the first two do most of the work.

### 1. One anchor object, carried the whole way

Pick a single concrete scenario and re-express *every* subsequent finding inside it. Do not switch
metaphor per point: a new metaphor resets comprehension, a carried one accumulates it.

Worked example (attention-sink paper):

| Source concept | Anchor |
|---|---|
| 336 attention heads | 336 students in a class |
| per-head sink score | each student's exam mark |
| top-k set (k=34) | the top-34 list |
| 4-bit quantization | re-marking every exam with a blunter pen |
| rank correlation ≥ 0.980 | after re-marking, almost nobody overtook anybody |
| set overlap 0.62-0.79 | but the students on the cutoff line hopped in and out |
| terminal-layer instability | one bad grader who only marked the final exam |

### 2. Convert relative metrics into countable objects

The expensive move, and the one that buys the most. A normalized statistic is unreadable; a count is
not. This routinely requires arithmetic the source never performed — do the arithmetic and show it.

Worked example: the paper reports Jaccard set overlap (0.789) and never reports head counts.
Inverting `J = I/(2k−I)` gives `I = 2kJ/(1+J)` → **30 of 34 heads stayed**. That single conversion
did more for comprehension than any prose.

Second form of the same move: restate a bare magnitude against its span. "Mean sink score 0.65-0.80"
becomes "one token out of 4,096 absorbing two-thirds of the attention."

### 3. Every number gets its null

A figure without a comparison point is decoration. "26 of 34 heads stayed" means nothing until paired
with "a genuine scramble would leave about 3." Supply the null even when the source states it only
once and in passing.

## Supporting rules

- **State the expectation before the finding.** Results are interpretable only against what was
  expected. Open with what the authors feared or predicted, so each result lands as a confirmation or
  a denial rather than as free-floating data.
- **Name the surprise in one sentence.** "The paper went hunting for a quantization problem and found
  a domain problem." One line that reorganizes everything around it. If there is no surprise, say so
  rather than manufacturing one.
- **Lead with the inversion.** Where the truth is counterintuitive, front-load it rather than building
  to it: "the first token matters *because* it is meaningless, not despite it."
- **Tier the terminology; no definition may use an undefined word.** Three tiers, in order: (a) the
  title or headline claim decoded into plain words; (b) background field vocabulary, explicitly
  marked as **not from this source**, since the reader must know which terms the authors invented;
  (c) the source's own terms, built only from tier (b).
- **Close with a verdict table** — what was expected against what was measured, including anything
  the source did not anticipate.

## Known limits — do not force these

- **Move 2 has no exit for genuinely abstract metrics.** Forcing a picture produces a false analogy.
  The honest move is to state that the metric is abstract and give its range and direction instead.
- **The anchor object has a shelf life.** Retire it the moment it would assert something the source
  does not support. In the worked example the classroom was dropped before the calibration-transfer
  result, which has no clean classroom equivalent — continuing would have invented a claim.
- **Explanation does not license unsourced claims.** Analogies are a presentation layer over sourced
  facts; every number still carries its citation, and anything inferred during explanation is marked
  as inferred, per `evidence-integrity.md`.
- **Length is not the goal.** The register permits build-up; it does not permit padding. The
  no-padding test from `kb-sop-details.md` still applies.

## Provenance

Confirmed 2026-07-28 against a live walkthrough with a reader new to the field. Two constraints set the same day, both
load-bearing above: explanation is not digest, and this must not be folded into `wei-digest-doc`.
Session memory: `explain-with-one-anchor-object`. Applied instance (embedded form, known-wrong
container): a task directory holding the working notes the explanation was built from.
