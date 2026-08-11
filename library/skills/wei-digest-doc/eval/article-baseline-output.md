# Baseline Output — wei-digest-doc (article family)

Expected output for `article-baseline-input.md`. Update only when drift is intentional and approved.

## Output

Canonical committed digest: `agent-operations/research/2026-07-23_hpd_parsing_paper.md` (produced by this skill's first live article run; verified against the arXiv HTML with passing spot-checks).

Structural expectations (allowed variation: wording, row order; not allowed: missing sections, dropped conditions, unsourced facts):

- Frontmatter per article-schemas common block; `sensitivity: PUBLIC`; `source_type` pins v1 2026-07-21.
- Sections: Identity / Premise / Method / Training & data / Results / Scope & limits / Relevance to this workspace / Sources / Cross-references.
- Signature facts that MUST appear (spot-check set):
  1. Abstract-vs-Table-2 discrepancy flagged: abstract "2.62× the fastest existing" is actually PPS vs own baseline; table-derived vs-fastest gain is 1.62× TPS (DeepSeek-OCR-2, 2,932.1 TPS).
  2. 4,752.1 TPS / 2.68 PPS under batch size 512, A800, OmniDocBench v1.6; autoregressive baseline 1,554.8 TPS / 1.02 PPS (3.06× TPS).
  3. Overall 94.91 — best among unified parsers (HunyuanOCR-1.5 94.74); pipeline parsers higher (PaddleOCR-VL-1.6 96.3, MinerU2.5-Pro 95.75).
  4. Backbone InternVL3.5-1B = 0.3B InternViT encoder + ~0.8B decoder adapted from Qwen3-0.6B; up to 24 tiles at 448×448.
  5. <FORK>/<CHILD> token mechanism; shared-prefix KV cache reuse; P-MTP average accepted length 6.6 tokens/step.
  6. Three-stage training: 2.8M full-page samples (Stage 1), 100K branch-specific (Stage 2), 600 hard cases for RL (Stage 3); pseudo-labels from PaddleOCR-VL-1.5 + MinerU-2.5 Pro.
  7. Length-bucket scaling confined to longest bucket: up to 18.04× fewer decoding steps, 3.67× request throughput (BS=512), 5.80× lower single-request latency (BS=1).
  8. Decoder latency up to ~500× encoder latency for long outputs (motivating profile, §3.1).

## Last Verified

- Date: 2026-07-23
- Model: Fable 5
- By: agent (first live article run), pending user review
