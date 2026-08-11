# Baseline Input — wei-digest-doc (article family)

Canonical input the skill should handle correctly.

## Input

```
/wei-digest-doc https://arxiv.org/html/2607.18839v1 --family=article
```

Source: *HPD-Parsing: Hierarchical Parallel Document Parsing* (PaddleOCR team, Baidu), arXiv 2607.18839 v1, 2026-07-21, cs.CL, CC BY 4.0. Type: paper. Stable public URL; version-pinned.

## Acceptance Criteria

- Frontmatter present: `title`, `authors`, `source_url`, `source_type` naming the version (v1, 2026-07-21), `code`, `retrieved`, `style: descriptive`, `sensitivity: PUBLIC`.
- Filed in the topical research directory (`agent-operations/research/`) under that directory's naming convention (`YYYY-MM-DD_slug.md`, date = filed date), NOT next to a source file.
- Every paper-schema section present or its omission reported.
- The abstract-vs-Table-2 multiplier discrepancy caught and flagged (abstract "2.62× the fastest existing model" vs table-derived 1.62× TPS vs DeepSeek-OCR-2; 2.62× is PPS vs the paper's own autoregressive baseline).
- Benchmark conditions intact on spot-check (4,752.1 TPS under batch size 512 on A800; 18.04×/3.67×/5.80× confined to the longest output-length bucket; OmniDocBench version v1.6 stated).
- Category-honest results: best among unified parsers (94.91 vs HunyuanOCR-1.5 94.74) while pipeline parsers reach higher (PaddleOCR-VL-1.6 96.3).
- Results tagged `[BENCHMARK]` with "authors' reported numbers, not independently reproduced" in Scope/limits.
- ≥5 facts spot-checked against cited §/Table and matching.
- Decision-relevance appears ONLY in the relevance section, `[HYPOTHESIS]`-tagged.
- No fact without a `§`/`Table`/`p.` source. No emojis. No narrative prose.
- INDEX.md row added for the digest in the same operation.

## Failure modes this eval catches

1. Abstract-multiplier trust (headline number not recomputed from tables).
2. Condition dropping (peak/bucket/batch-size qualifiers cut from numbers).
3. Wrong filing (vendoring the source or inventing a directory instead of the topical research dir).
4. `[CONFIRMED]` tag on author-reported benchmarks.
