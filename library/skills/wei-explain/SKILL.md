---
name: wei-explain
description: Use when the reader is unfamiliar with a field and needs to reach competence, not merely asking how something works. Applies the explanation register; explanation and digest stay separate.
argument-hint: <source-document-or-topic>
---

# Explain — unfamiliar-field material

> Shapes an explanation for a reader who is new to the field. The rules live in
> `@references/explanation-style.md`. This skill routes to them and copies none of them, so there
> stays exactly one home. Read the reference before writing — do not work from this summary.

## Inputs

- `<source-document-or-topic>` — what to explain: a document, a codebase, an API, a paper. If
  missing, ask.

No flags. Everything else is inferred from the source and the reader.

## Workflow

1. Read `@references/explanation-style.md` in full.
2. Confirm the trigger: the READER is unfamiliar with the field. If they know the field, stop and
   write a digest instead.
3. Pick ONE anchor object; carry it through every finding. Never switch metaphor per point.
4. Convert relative metrics into countable objects. Do the arithmetic the source never performed.
5. Pair every number with its null.
6. Write the explanation as its OWN artifact. If a digest is also wanted, produce a second file and
   cross-link the two.

## Gotchas

- **Substituting a friendlier synonym for a defined term.** Wrong default: rename `competency` to
  "behaviour" so it reads easier. That does not remove a lookup — it creates a translation problem
  between this document and every other one in the programme. Correct: keep the real term, spend one
  clause defining it in plain words.
- **Merging the explanation into the digest.** Wrong default: one file with explanation sections
  inside a fact-sheet. The descriptive fact-sheet layer forbids exactly what explanation requires.
  Correct: two artifacts, cross-linked, never merged.
- **Firing on any request containing "explain".** Wrong default: treating "explain this regex" as an
  explanation-register task. The trigger is unfamiliarity with a FIELD, not a request for detail.
  Correct: for a reader who already knows the domain, answer normally and do not invoke this.
- **Carrying the anchor past its shelf life.** Wrong default: forcing the analogy onto every point
  until it asserts something the source does not support. Correct: retire it at that moment, and say
  in the text that it is being retired.
- **Treating the analogy as licence to stop sourcing.** Wrong default: an anchor makes prose feel
  self-evident, so citations get dropped. Correct: analogies are a presentation layer over sourced
  facts; every number keeps its citation and every inference is marked as inferred.

## Style

- Style directive: explanation register — one carried anchor, deliberate build-up, analogy permitted.
  Overrides the descriptive fact-sheet default for this artifact only; a companion digest stays
  strictly descriptive.
- Tested on: Opus 5
- Model floor: Sonnet 4. Choosing an anchor and knowing when to retire it is judgment; smaller models
  carry the analogy past the point where it starts inventing claims.

## Eval

- Acceptance: the reader can restate the result and its surprise unprompted — the success test
  defined in the reference.
- Baselines and applied instances are recorded with the reference, not duplicated here.

## Quality Guidelines

Adhere to:
- `@references/agent-quality-guidelines.md` (runtime behavior)
- `@references/skill-architecture.md` (structural principles)
