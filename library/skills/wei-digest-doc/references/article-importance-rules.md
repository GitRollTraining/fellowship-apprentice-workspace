# Importance Rules — wei-digest-doc, article family

What stays, what goes, what stays verbatim. The digest is a descriptive capture of the article's substantive content — completeness first. Decision-relevance is NOT the keep/cut filter; it is one dedicated section (relevance to this workspace) at the end.

## Keep (substantive content)

Everything that is a fact of the article:

- Identity: full title (+ alternate titles in circulation), every named author + affiliation, identifier + version history, venue/status, license, authorship disclosures (AI-drafted, funded-by)
- Claims: the problem statement, each named contribution, each named mechanism/component with the paper's own definition
- Numbers: every benchmark result, model/data/compute scale, hyperparameter the paper foregrounds, speedup/multiplier WITH its baseline and conditions
- Comparisons: what the paper compares against, at what sizes/settings, and the category system it uses for the comparison
- Provenance: code/model/dataset links, what is released vs described-only
- Limits: self-declared limitations, proposed-but-not-demonstrated items, single-benchmark caveats

## Cut

- Narrative transitions, motivation rhetoric, restatements of the abstract in the intro/conclusion (capture the factual core once)
- Related-work summaries that only survey the field — compress to a positioning table (system → contribution → limitation the paper claims) when the paper builds on them; drop entirely when incidental
- Figure/table captions that repeat body prose; qualitative-example walkthroughs beyond one line per demonstrated capability
- Math derivations — keep the objective/mechanism in one descriptive line + section source; the digest reader re-opens the paper for equations

## Must keep VERBATIM (no paraphrase)

- Numbers, percentages, multipliers, parameter counts, dataset sizes, hardware specs
- Benchmark names + versions (OmniDocBench v1.6 ≠ OmniDocBench), metric names + directions (Edit ↓, TEDS ↑)
- Model/system names and sizes exactly as written (3B-A0.5B, InternVL3.5-1B)
- Measurement conditions attached to any number: "under batch size 512", "up to", "in the longest output-length bucket", "peak". Dropping the condition inflates the claim — the #1 article digest failure mode
- Load-bearing definitional sentences and self-declarations (quote, with section source)

## Evidence tags (required, per evidence-integrity.md)

- Mechanism/design facts → `[STRUCTURAL]`
- Reported experimental numbers → `[BENCHMARK]` (they are author-reported third-party data, NOT `[CONFIRMED]`, unless independently reproduced — then say by whom)
- Workspace-relevance mappings → `[HYPOTHESIS]`
- Sensitivity default `[PUBLIC]` for open-web sources; tag inline only where a facet is non-default

## Decision-relevance section (relevance to this workspace)

One section at the end. Only here does analysis appear:

- Mapping to workspace programs, rules, preferences, or prior filings — each mapping cites the workspace file it maps to
- Untested/priced-out items stated as such ("untested here", "price the cost model first")
- Keep it factual-analytic, not advocacy; every implication traces to a sourced fact earlier in the digest

## Length policy

As long as the content requires — no percentage bands. Two tests, both must pass:

1. **No-reopen test:** a reader deciding whether the technique/finding matters to a workspace program never opens the source (equation-level review excepted).
2. **No-padding test:** every line is a fact, a sourced flag, or a table row. Delete any line that restates another.

## Sourcing

- Every fact row/bullet ends with its source: `§N`, `§N.M`, `Table N`, `Fig. N`, or `p.N` (cite the rendering actually read)
- Frontmatter `source_url:` + `source_type:` carry the canonical URL + version; `retrieved:` the fetch date
- Facts not found in the source do not enter the digest — no outside knowledge except in relevance/cross-references (labeled as such)
