# Gotchas — digest-doc, article family

Domain-specific failure modes. Each entry: trigger / wrong default / correct behavior.

## Abstract multipliers disagree with the results tables

**Trigger:** any headline claim ("N× the throughput of the fastest existing model") in abstract or contribution bullets.
**Wrong default:** digesting the abstract's number as authoritative.
**Correct behavior:** recompute every multiplier from the results tables; where abstract and tables disagree, record the table-derived value as the fact and the discrepancy as a flag in Scope/limits.
**Why:** real catch on first live run (HPD-Parsing, arXiv 2607.18839v1): abstract claims "2.62× the throughput of the fastest existing document parsing model", but Table 2 shows 2.62× is the PPS gain vs the paper's OWN autoregressive baseline; vs the fastest existing model (DeepSeek-OCR-2) the gain is 1.62× TPS. Abstracts are marketing surface; tables are the record.

## Benchmark conditions silently dropped

**Trigger:** any performance number (TPS, latency, accuracy).
**Wrong default:** "achieves 4,752 TPS" with no conditions.
**Correct behavior:** conditions travel with the number, verbatim: hardware, batch size, benchmark + version, bucket ("under batch size 512, on A800, OmniDocBench v1.6; up to 18.04× in the longest output-length bucket"). Same failure mode as govdoc qualifier-dropping.

## Author-reported results digested as established fact

**Trigger:** all experimental results in a paper published by the system's own authors (esp. vendor labs).
**Wrong default:** tagging results `[CONFIRMED]` or stating them as field consensus.
**Correct behavior:** tag `[BENCHMARK]`, state "authors' reported numbers, not independently reproduced" in Scope/limits. "State of the art" is the paper's claim — attribute it and record what the paper's own tables show beating it in other categories.

## Comparison tables mix categories with different conditions

**Trigger:** results tables comparing pipeline vs unified vs general-purpose systems, or models of very different sizes.
**Wrong default:** flattening to "best overall" / cherry-picking the category where the paper wins.
**Correct behavior:** preserve the paper's own category split; state per-category leaders including where the paper LOSES (e.g., best unified parser at 94.91 while pipeline parsers reach 96.3).

## Preprint versions drift under a stable URL

**Trigger:** arXiv source (vN in the URL, or version history on the abs page).
**Wrong default:** citing "the paper" with no version; digest silently describes a superseded revision later.
**Correct behavior:** record the exact version + date in Identity (`arXiv 2607.18839 — v1 2026-07-21`); frontmatter `source_type` carries it; a later revision is a new digest decision, not an in-place edit (digests are Immutable).

## HTML rendering artifacts read as content

**Trigger:** arXiv/LaTeXML HTML renders — mangled math, duplicated LaTeX source lines, truncated author lists, placeholder tokens in the author block.
**Wrong default:** transcribing render garbage as fact (a stray "YY" as an author name) or trusting a mangled equation.
**Correct behavior:** note "HTML render (LaTeXML)" as the rendering read; cross-check suspicious identity facts against the abs page or PDF; describe equations mechanically rather than reproducing possibly-corrupted symbols.

## Alternate titles / duplicate circulations

**Trigger:** the same paper circulating under a different title or as blog + paper.
**Wrong default:** filing a second digest later because grep on the other title found nothing.
**Correct behavior:** record every known alternate title in Identity so grep on either lands on the digest (proven pattern: bilevel-autoresearch digest).

## Relevance section absorbs the digest

**Trigger:** an article selected precisely because it maps to workspace concerns.
**Wrong default:** interleaving "this matters for us because..." throughout Method/Results.
**Correct behavior:** capture the article on its own terms first; ALL workspace mapping goes in the relevance section, `[HYPOTHESIS]`-tagged, each item tracing to a sourced fact.

## Sensitivity on non-public sources

**Trigger:** paywalled reports, NDA-bound analyst material, private-community posts.
**Wrong default:** `sensitivity: PUBLIC` because the digest itself contains no secrets.
**Correct behavior:** sensitivity follows the SOURCE's distribution terms: paywalled/licensed → `[INTERNAL]` minimum, quote-length discipline; NDA-bound → `[CONFIDENTIAL]` + sidecar rules (`.claude/rules/sensitive-content-handling.md`).
