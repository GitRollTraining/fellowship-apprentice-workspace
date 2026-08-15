---
name: digest-doc
description: "Digest a document the business already has into a page-sourced fact-sheet. One family: article - anything written down, from a supplier agreement to a printed procedure to a web page. Use on digest this, summarize this document, or a document the owner hands you."
argument-hint: <file-path-or-url-or-pasted-text>
---

# Digest Document

> Turns a source document into a navigable descriptive fact-sheet so nobody re-reads the original except for legal review. Every fact page/section-sourced. Digest captures ALL substantive content of the document; decision-relevance ("implications") is a dedicated section at the end, NOT the keep/cut filter. Length: as long as the content requires — no size bands. Document families plug in as reference sets; the spine (classify → schema → full read → write → verify → file + index) is family-agnostic.

## Families

| Family | Status | Covers | Refs |
|--------|--------|--------|------|
| `article` | LIVE | Anything the business already has in writing, and anything you read to understand their field: reports, manuals, policies, white papers, web articles | `references/article-*.md` |
| books | OUT OF SCOPE | Long-form books — different mechanics | not this skill |

New family = one schemas ref + one importance ref + one gotchas ref + eval baseline; update `--family` values in the frontmatter hint.

## Inputs

- `<file-path-or-url-or-pasted-text>` — the source document, workspace-relative or absolute; the article family also accepts a public URL, **pasted text**, and a **batch of several articles in one message** (digest each separately, one file each). If missing, ask user.
One family ships, `article`. If a document does not fit it, STOP and report - propose what the new family would need, do not force this schema onto it.

No other arguments. The type within the family (paper / report / page) is always inferred from the title page and filename — state the inference in the report. Output path is always the source document's directory, named `{doc-date}_{doc-slug}-summary.md` (doc-date = issue/submission/document date from the title page, NOT today). Exception: URL-sourced articles have no source directory — filing home + naming per `references/article-schemas.md` § Filing home.

## Step 0 — establish WHERE you are, before anything else

```bash
git rev-parse --show-toplevel          # -> the root of this apprentice workspace
```

**User-level since 2026-07-27**, so this runs in every workspace and must never assume one. Whatever
this prints is the workspace the digest is filed into. Exit 1 → **stop and report**; do not guess a
root, do not fall back to cwd. Filing routes are in `references/routing.md`; there is deliberately no
destination flag (preference #17 rule 2 — config is read from the workspace, not typed).

Do not hand-roll the check. "Walk up to a directory with `.git/`" is true in both workspaces and in
every worktree, and silently resolves the wrong root.

## Workflow

1. **Classify.** Read document page 1 (and the table of contents if present) and infer the type within the article family. A document that fits no type is a STOP, not a forced fit.
2. **Load the family spec.** Read `references/{family}-schemas.md` (section template for the type) and `references/{family}-importance-rules.md` (keep/cut/must-keep-verbatim rules). Do not digest from memory of a previous run.
3. **Read the full document** in ≤20-page chunks. No skipping: boilerplate pages get skimmed for unusual clauses (see gotchas), not skipped.
4. **Write the digest** per the type schema: YAML frontmatter (`title, solicitation/identifier, class: Immutable, sensitivity, style: descriptive, source, updated`), then schema sections. Every fact carries a `p.N` / `§N` source. Tables over prose.
5. **Verify.** Spot-check ≥5 high-stakes facts (dates, dollar figures, page limits, clause obligations, names) against the pages cited. Confirm every must-keep category (deadlines, eval factors, deliverables, IP/ownership clauses, qualifiers) appears. Fix before filing.
6. **File + index.** Resolve the output path per `references/routing.md`. **Writing the file is the default, never optional**: a digest costs a full read and often a paid fetch, so leaving it in the chat loses it. Add a row to the directory's `INDEX.md` (class Immutable, same sensitivity) in the same operation. Report: family + type used (stated vs inferred), output path, section count, verification result, any flags raised.

## Gotchas

Top four inline; full per-family list in `references/{family}-gotchas.md` — read it at step 2.

- **Dropped qualifiers flip obligations.** "Virtual unless CO approves in writing" digested as "virtual" turns a conditional into an absolute. Keep every qualifier verbatim.
- **Unusual clauses hide inside boilerplate.** A section that looks standard is where the one non-standard term hides — the clause nobody reads is exactly where an obligation gets added. Skim all boilerplate for deltas from the prior or sibling version; digest only the deltas.
- **A reply document answers "what did we commit to," not "what were we asked."** The wrong default is re-summarising the request the reply echoes back. Correct: a commitments table — promise, the requirement it answers, the page.
- **Wrong-family forcing.** A document that fits no live family — a book, a slide deck, a transcript — squeezed into the nearest schema produces a broken digest. Correct: stop, report, and propose the family rather than forcing it.

## Constants

| Key | Value |
|---|---|
| Skill location | `library/skills/digest-doc/`, reached through the `.claude/skills` symlink |
| Workspace probe | `git rev-parse --show-toplevel`. **Local patch for the apprentice workspace:** upstream this skill probes a script that recognises exactly two GitRoll repositories by git remote and exits 1 on anything else, which halted this skill at step 0 here |
| Filing routes | `references/routing.md` — per-workspace destinations, read at runtime |
| Family refs pattern | `references/{family}-schemas.md`, `references/{family}-importance-rules.md`, `references/{family}-gotchas.md` |
| article refs | `references/article-schemas.md`, `references/article-importance-rules.md`, `references/article-gotchas.md` |
| Reference outputs (proven format) | Held in GitRoll's own workspaces and not shipped here. The schemas in `references/` are the contract; follow those |

## Output

One markdown fact-sheet next to the source document (URL-sourced articles: in the topical research directory) + one INDEX.md row. Structure per the family schemas ref. Frontmatter `style: descriptive`.

## Style

- Style directive: descriptive fact-sheet (`library/sops/working-standards.md`) — no intro, no narrative, no persuasion; facts, tables and lists; no emojis.
- Tested on: a frontier model. Smaller models drop page citations, which is the whole point of the output.
- Model floor: Sonnet 4.5 — below that, qualifier preservation and page-citation accuracy degrade (untested; floor is a judgment, re-eval on first sub-Sonnet run).

## Eval

**No baseline pair ships with this copy.** Upstream, this skill is evaluated against two worked
examples; both were built from GitRoll's own federal contract documents and internal research filings,
so neither travels. Until a replacement pair exists, judge a digest against the acceptance criteria
directly: every must-keep category present, at least five spot-checked facts matching their cited
pages, every qualifier intact, and decision-relevance confined to the implications section.

Building the first apprentice-side baseline pair — one input document, one accepted output — is a good
first contribution to this library.

## Quality Guidelines

Adhere to:
- `library/reference/agent-quality-guidelines.md` (runtime behavior)
- `library/reference/skill-architecture.md` (structural principles)
