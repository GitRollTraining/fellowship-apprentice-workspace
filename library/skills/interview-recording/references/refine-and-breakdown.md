# Refine and breakdown

Loaded by workflow step 5. Two outputs from one input: a transcript a person can read, and a one-page
reduction of what was said.

## Frontmatter, on the raw transcript and both derived files

```yaml
---
doc: original          # original | refined | breakdown
session: 2026-08-11
client: <client-slug>
participants: [owner name, your name]
method: speech-to-text, speaker labels requested
audio: audio.local.m4a
---
```

## Refine, into the permitted refined transcript path

Input: `original.local.md`. Output: tracked `refined.md`, ignored `refined.local.md` or a
client-system record, exactly as `EW-001` permits. Goal: a readable transcript with every turn
attributed and the language intact.

1. **Clean the artifacts.** Remove duplicated lines, filler stutters that obscure the meaning, obvious
   mis-segmentation. Do not paraphrase and do not summarise — a refined transcript is still a transcript.
   If you find yourself improving a sentence, stop: refine makes what was said readable, and the
   reduction is a separate file.
2. **Attribute the speakers.** Sources, in order: the attendee list from your pre-session note; role and
   topic cues, since the person who describes approving the purchase is the owner; language cues. Prefix
   each turn `**Name:**`. Where you are genuinely unsure write `**[unclear]:**` — never put a name on a
   turn to make the file look finished.
3. **Say which of the two happened.** One line at the top: the engine's labels held, or you reconstructed
   attribution from content. A reader who cannot tell the difference cannot tell a quotation from an
   inference.
4. **Preserve the language.** Keep code-switching exactly as spoken; no translation. Gloss in `[brackets]`
   only where a term is genuinely ambiguous. Keep the engine's garbles with `[sic: what it wrote]` — a
   trade term the engine mangled is a term you must ask about, and repairing it silently deletes the
   question.

If the source was already a clean human transcript, refine is light: labels and artifact cleanup only.

## Reduce, into the permitted breakdown path

Input: the permitted refined transcript path. Output: tracked `breakdown.md`, ignored
`breakdown.local.md` or a client-system record, exactly as `EW-001` permits. Style: descriptive
fact-sheet. Three sections, in this order, none omitted.

```markdown
# {session title} — breakdown

## Key Points
- {one fact, one sentence, with a pointer into the transcript}

## Decisions
1. {what was settled, and by whom} — {pointer}

## Open Questions
- {what is still ambiguous, and what would settle it} — {pointer}
```

Filled, from a first session with the owner of a small bakery:

```markdown
## Key Points
- Wholesale orders arrive by text message and are copied by hand into the order book [00:07:41].
- The owner approves any ingredient purchase over 500 dollars; below that the baker orders directly
  ["anything under five hundred, he just orders it", 00:22:10].

## Decisions
1. The reconstruction covers the wholesale order only, not retail counter sales — the owner ruled retail
   out of scope [00:03:12].
2. The owner will send last month's order book photographs before the next session [00:41:55].

## Open Questions
- What happens to a text order arriving after the 4 pm cut-off. The owner gave two different answers ten
  minutes apart [00:14:05, 00:24:30]. Settled by: one dated past instance, asked next session.
```

Rules:

- One sentence per point. No narrative, no persuasion, no adjective that grades the business.
- **Every point carries a pointer into the permitted refined transcript** — a timestamp, a short
  quotation, or both. A
  breakdown you cannot trace back is a set of claims you authored (`library/sops/working-standards.md`,
  rule 1: facts are sourced, the agent does not author them).
- Names, not roles, wherever the transcript gives you a name.
- **A commitment made in the room is a decision.** Record who owes what, and by when.
- **What the owner stated goes in Key Points. What you concluded from it goes in neither section** — that
  belongs in the discovery record, where heard and concluded are kept apart (interview playbook step 15).
- Empty section, write `_None identified._` and keep the heading. A deleted Open Questions heading reads
  as "nothing was ambiguous", which after a first interview is never true.

## What this feeds

Open Questions is where the ambiguity list starts (playbook step 17, filed at `interview/ambiguities.md`),
and Key Points is the raw material for the discovery record (step 15, `interview/discovery-record.md`).
Neither of those files is this skill's job — see `library/playbooks/playbook-interview.runbook.md` for the
full destination table.
