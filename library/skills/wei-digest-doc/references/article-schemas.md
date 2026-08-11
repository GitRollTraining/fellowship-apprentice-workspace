# Type Schemas — wei-digest-doc, article family

Section template per document type. Sections in order; omit a section only when the document genuinely has no content for it (state the omission in the report). Every fact row carries a source (`§N` for HTML/sectioned sources, `p.N` for PDFs — cite the rendering actually read). Add sections when the document contains substantive content no slot covers — schemas are floors, not ceilings.

Proven reference output: `agent-operations/research/2026-07-13_bilevel_autoresearch_paper.md` (pre-dates this family; its format is the baseline this schema codifies).

## Filing home + naming (articles have no source directory)

The spine's output rule ("source document's directory, `{doc-date}_{doc-slug}-summary.md`") assumes an in-workspace source file. Articles usually arrive as URLs, so the article family overrides it:

- **Filing home:** resolved per workspace. **`references/routing.md` is the single authority — read it, do not duplicate its table here.** Deliberately not restated in this file: two copies of a destination table drift, and the one you happen to read is then wrong. Never hardcode a destination and never accept one as a flag.
- **Naming:** follow the target directory's stated convention. `agent-operations/research/` uses `YYYY-MM-DD_slug.md` with date = filed/retrieved date. Only when the target dir declares no convention, fall back to the spine default.
- **Source archival:** do not vendor the source HTML/PDF into the workspace; the digest cites URLs. Record the version identifier (arXiv vN, report edition) so a later revision is detectable.

## Common frontmatter (all types)

```yaml
---
title: "{Canonical title}"
authors: {names (affiliations)}
source_url: {canonical URL}
source_type: {arXiv preprint (vN, YYYY-MM-DD) | industry report | white paper | vendor docs}
code: {repo/model URLs — omit if none}
retrieved: {YYYY-MM-DD}
style: descriptive
sensitivity: PUBLIC   # public web sources; paywalled/NDA-bound material escalates per evidence-integrity.md
---
```

## Type: paper (research paper — preprint, conference, journal)

| # | Section | Contents |
|---|---------|----------|
| 1 | Identity | Table: canonical title (+ alternate titles), authors + affiliations, identifier (arXiv no., versions + dates), venue/status, length, abs/PDF/code/model links, license, authorship disclosures |
| 2 | Premise | Problem statement, the gap/limitation in prior work the paper targets, positioning vs named prior systems (table when ≥3). Tag `[STRUCTURAL]` |
| 3 | Method | Core technique: components, design choices, named mechanisms with the paper's own terms (defined on first use). Tag `[STRUCTURAL]` |
| 4 | Training & data | For papers shipping models: backbone, parameter split, data scale per stage, training stages, hardware, key hyperparameters |
| 5 | Results | Tables: headline numbers WITH comparison baseline, benchmark name + version, and measurement conditions (batch size, hardware). Separate what-beats-what by category the paper itself uses. Tag `[BENCHMARK]` |
| 6 | Scope / limits | Demonstrated vs proposed-only, benchmark coverage, reproduction status (vendor-reported unless independently reproduced), self-declared limitations, internal inconsistencies found during verification |
| 7 | Relevance to this workspace | Decision-relevance lives HERE and only here. Tag `[HYPOTHESIS]`; each item traces to a sourced fact above |
| 8 | Sources | URL list with sensitivity tags |
| 9 | Cross-references | Workspace files: sibling digests, rules/preferences the paper's findings map to |

## Type: report (industry report, white paper, long-form vendor/analyst article)

| # | Section | Contents |
|---|---------|----------|
| 1 | Identity | Table: title, publisher/author, date, edition/version, URL, length, paywall status |
| 2 | Thesis | The report's central claims, stated as the report's claims (attributed), not as fact |
| 3 | Findings & data | Tables: figures with methodology notes (sample size, survey window, who funded it). Tag `[BENCHMARK]`; vendor self-reports flagged as such |
| 4 | Framework / taxonomy | Any named model, maturity curve, or category system the report introduces — captured faithfully, it is often the citable artifact |
| 5 | Scope / limits | Methodology gaps, conflicts of interest, undated/unbylined pages, marketing load |
| 6 | Relevance to this workspace | Decision-relevance, `[HYPOTHESIS]`-tagged, only here |
| 7 | Sources | URL list |
| 8 | Cross-references | Workspace files |

## Absorbed from `wei-summarize-article` (retired 2026-07-27)

That skill covered the same job — article in, digest out — with a caveman-voice TL;DR and a `--save`
flag. It was folded in here and removed. Three of its behaviors were kept, three were dropped as
defects. Do not reintroduce the dropped ones.

### Kept

**1. Input flexibility.** Beyond a path or URL, accept **pasted text** (use as-is) and a **mixed
batch** of several articles in one message — digest each separately, one output file each. The spine
step 1 classify still runs per article.

**2. A jargon section.** Research papers and vendor reports introduce terms the rest of the digest
then uses. Immediately after the summary section, when the document introduces terms a reader would
not already know:

```markdown
## Jargon and new ideas

| Term | Plain-language meaning | First use |
|---|---|---|
| {term} | {short definition, no jargon inside the definition} | p.N |
```

Omit the section entirely when the document introduces nothing new. It is not a glossary of every
technical word — only terms load-bearing for the digest's own claims.

**3. Context-aware implications.** The implications section frames against the invoking workspace,
read at runtime, not assumed: check the workspace root's `CLAUDE.md` / `CONTEXT.md` for the active
priorities and workstreams. If neither exists, use a generic "Strategic implication" framing and
**do not invent an organization**. Resolve once per session, not per article.

### Dropped, deliberately

**1. Caveman voice.** Deactivated workspace-wide 2026-07-21. All output here is descriptive
fact-sheet per `descriptive-style.md`. The retired skill's own saved outputs are flagged
`caveman digest` in `notes/article-summaries/INDEX.md`; those are historical and stay as they are.

**2. The `--save` flag, and inline-only as the default.** The old default printed to chat and wrote
nothing unless `--save` was typed, so a digest of a paid fetch and a full read vanished when the flag
was forgotten. **Writing the file is the default and is not optional** — preference #17 rule 1. The
destination comes from `references/routing.md`, not from the command line.

**3. "No tagging."** The old skill deliberately skipped confidence tags because its output was for
human read only. A filed digest is knowledge-base content, so `evidence-integrity.md` applies
normally.

### Edge cases inherited (all still apply)

| Case | Handling |
|---|---|
| Fetch fails / paywall | Report the exact failure ("WebFetch returned 403") and ask for pasted content. **Never guess the content.** A 200 is not a fetch — check the body is the article, not a JS shell or consent wall |
| Article under ~300 words | Skip the jargon section if no new terms; skip implications if not substantive. Do not pad to fill the schema |
| Opinion or narrative piece, no hard claims | Key-facts bullets become "main arguments". Stay terse, keep the page citations |
| Non-English source | Digest in English; preserve original-language proper nouns and key terms verbatim, English gloss in parentheses on first use |
| No number where one is expected | Say so explicitly. **Never fabricate a statistic** |
