---
name: wei-digest-doc
description: Digest a source document into a page-sourced fact-sheet, filed into the workspace you invoked it from. Families govdoc (RFQ, PWS, response, amendment) + article (papers, reports, web articles) live. Use on digest asks, summarize this article, solicitation PDFs, or article URLs.
argument-hint: <file-path-or-url-or-pasted-text> [--family=govdoc|article]
---

# Digest Document

> Turns a source document into a navigable descriptive fact-sheet so nobody re-reads the original except for legal review. Every fact page/section-sourced. Digest captures ALL substantive content of the document; decision-relevance ("implications") is a dedicated section at the end, NOT the keep/cut filter. Length: as long as the content requires — no size bands. Document families plug in as reference sets; the spine (classify → schema → full read → write → verify → file + index) is family-agnostic.

## Families

| Family | Status | Covers | Refs |
|--------|--------|--------|------|
| `govdoc` | LIVE | Federal procurement documents: RFQ, PWS, vendor response/quote, amendment | `references/govdoc-*.md` |
| `article` | LIVE | Research articles, industry reports, white papers filed into the workspace | `references/article-*.md` |
| books | OUT OF SCOPE | Long-form books — different mechanics (conversion, tier bands) | `wei-distill-book` (personal KB), not this skill |

New family = one schemas ref + one importance ref + one gotchas ref + eval baseline; update `--family` values in the frontmatter hint.

## Inputs

- `<file-path-or-url-or-pasted-text>` — the source document, workspace-relative or absolute; the article family also accepts a public URL, **pasted text**, and a **batch of several articles in one message** (digest each separately, one file each). If missing, ask user.
- `[--family=govdoc|article]` — document family. If omitted, infer from content; if the document fits no live family, STOP and report (propose the new family, do not force a schema).

No other arguments. The type within the family (govdoc: rfq / pws / response / amendment; article: paper / report) is always inferred from the title page + filename — state the inference in the report. Output path is always the source document's directory, named `{doc-date}_{doc-slug}-summary.md` (doc-date = issue/submission/document date from the title page, NOT today). Exception: URL-sourced articles have no source directory — filing home + naming per `references/article-schemas.md` § Filing home.

## Step 0 — establish WHERE you are, before anything else

```bash
bash ~/.claude/scripts/workspace.sh    # -> "<name>\t<root>", exit 1 if unrecognized
```

**User-level since 2026-07-27**, so this runs in every workspace and must never assume one. Whatever
this prints is the workspace the digest is filed into. Exit 1 → **stop and report**; do not guess a
root, do not fall back to cwd. Filing routes are in `references/routing.md`; there is deliberately no
destination flag (preference #17 rule 2 — config is read from the workspace, not typed).

Do not hand-roll the check. "Walk up to a directory with `.git/`" is true in both workspaces and in
every worktree, and silently resolves the wrong root.

## Workflow

1. **Classify.** Read document page 1 (+ TOC if present). Confirm or infer `--family`, then infer the type within it. Mixed govdoc documents (RFQ with embedded PWS) use type `rfq` — the rfq schema subsumes PWS sections.
2. **Load the family spec.** Read `references/{family}-schemas.md` (section template for the type) and `references/{family}-importance-rules.md` (keep/cut/must-keep-verbatim rules). Do not digest from memory of a previous run.
3. **Read the full document** in ≤20-page chunks. No skipping: boilerplate pages get skimmed for unusual clauses (see gotchas), not skipped.
4. **Write the digest** per the type schema: YAML frontmatter (`title, solicitation/identifier, class: Immutable, sensitivity, style: descriptive, source, updated`), then schema sections. Every fact carries a `p.N` / `§N` source. Tables over prose.
5. **Verify.** Spot-check ≥5 high-stakes facts (dates, dollar figures, page limits, clause obligations, names) against the pages cited. Confirm every must-keep category (deadlines, eval factors, deliverables, IP/ownership clauses, qualifiers) appears. Fix before filing.
6. **File + index.** Resolve the output path — govdoc: beside the source document; article: per `references/routing.md` for the workspace step 0 returned. **Writing the file is the default, never optional**: a digest costs a full read and often a paid fetch, so leaving it in the chat loses it. Add a row to the directory's `INDEX.md` (class Immutable, same sensitivity) in the same operation. Report: family + type used (stated vs inferred), output path, section count, verification result, any flags raised.

## Gotchas

Top four inline; full per-family list in `references/{family}-gotchas.md` — read it at step 2.

- **Dropped qualifiers flip obligations.** "Virtual unless CO approves in writing" digested as "virtual" turns a conditional into an absolute. Keep every qualifier verbatim.
- **Unusual clauses hide inside boilerplate.** Skipping "standard" sections wholesale would have missed TO3 PWS §5.1 (absolute IP ownership, no carve-out). Skim all boilerplate for deltas from the sibling/prior document; digest only the deltas.
- **Response digests answer "what did WE promise," not "what did they ask."** Wrong default: re-summarizing the requirements the response echoes back. Correct: commitments table (promise → requirement it answers → page), staffing names, embedded assets, over-commitments.
- **Wrong-family forcing.** A document that fits no live family (a book, a slide deck, a transcript) squeezed into the nearest schema produces a broken digest. Correct: stop, report, propose the family (or route to the right tool — books → `wei-distill-book` in the personal KB, transcripts → `/wei-meeting-summary`).

## Constants

| Key | Value |
|---|---|
| Skill location | `~/.claude/skills/wei-digest-doc/` — **user-level** since 2026-07-27, runs in any workspace |
| Workspace probe | `~/.claude/scripts/workspace.sh` — shared with the transcription skills, never copy it |
| Filing routes | `references/routing.md` — per-workspace destinations, read at runtime |
| Family refs pattern | `references/{family}-schemas.md`, `references/{family}-importance-rules.md`, `references/{family}-gotchas.md` |
| govdoc refs | `references/govdoc-schemas.md`, `references/govdoc-importance-rules.md`, `references/govdoc-gotchas.md` |
| article refs | `references/article-schemas.md`, `references/article-importance-rules.md`, `references/article-gotchas.md` |
| Reference outputs (proven format) | Both in the **operations** workspace — govdoc: `workforce-delivery/irs-bpa/task-orders/*/20*-summary.md`; article: `agent-operations/research/2026-07-23_hpd_parsing_paper.md`. No proven itsweikuo output yet; the first article digest filed to `notes/article-summaries/` becomes it |

## Output

One markdown fact-sheet next to the source document (URL-sourced articles: in the topical research directory) + one INDEX.md row. Structure per the family schemas ref. Frontmatter `style: descriptive`.

## Style

- Style directive: descriptive fact-sheet (`.claude/rules/descriptive-style.md`) — no intro/narrative/persuasion; facts + tables + lists; no emojis.
- Tested on: Fable 5 (2026-07-06, three-document govdoc iteration; 2026-07-23, first article run).
- Model floor: Sonnet 4.5 — below that, qualifier preservation and page-citation accuracy degrade (untested; floor is a judgment, re-eval on first sub-Sonnet run).

## Eval

- govdoc: `eval/baseline-input.md` + `eval/baseline-output.md` (TO3 PWS, 8 pages — smallest real input).
- article: `eval/article-baseline-input.md` + `eval/article-baseline-output.md` (HPD-Parsing arXiv paper, first live article run).
- Acceptance: all must-keep categories present, ≥5 spot-checked facts match cited pages, qualifiers intact, decision-relevance confined to implications section.
- New family → add its own baseline pair before first production run.

## Quality Guidelines

Adhere to:
- `@references/agent-quality-guidelines.md` (runtime behavior)
- `@references/skill-architecture.md` (structural principles)
