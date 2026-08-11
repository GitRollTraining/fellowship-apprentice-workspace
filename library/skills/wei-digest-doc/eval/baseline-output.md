# Baseline Output — wei-digest-doc (govdoc family)

Expected output for `baseline-input.md`. Update only when drift is intentional and approved.

## Output

Canonical committed digest: `workforce-delivery/irs-bpa/task-orders/2032H5-26-Q-00145_full-stack-developer-training/2026-06-17_to3-pws-summary.md` (produced by this skill's first live run; verified against pws.pdf with 9 passing spot-checks).

Structural expectations (allowed variation: wording, row order; not allowed: missing sections, missing qualifiers, unsourced facts):

- Frontmatter: `class: Immutable`, `sensitivity: "[INTERNAL]"`, `style: descriptive`, `source: pws.pdf (8 pages, dated 2026-06-17)`.
- Sections: document header / background & purpose / scope / task requirements (6 goals verbatim) / program management / deliverables table (8 rows) / §5.1 ownership / PLAs (4 rows + payment basis) / security / GFP-GFI / communications / logistics / implications / cross-references.
- Signature facts that MUST appear (spot-check set):
  1. §5.1 sole-property-upon-creation, no carve-out — also flagged in implications.
  2. LMS accessible 99% of business hours.
  3. 100% of billed participants completed training; no Government-directed-withdrawal exception (delta vs TO2 flagged).
  4. §9 "generally within two (2) business days" qualifier vs §6 hard 2-day PLA — divergence noted.
  5. §8 "Access to IRS systems and/or data (as authorized)" — delta vs TO2 sanitized-only posture flagged.
  6. §2 "upskilling" purpose language inside a Task 3 document.
  7. Roster validation within 2 business days of receipt.
  8. Metrics Report vs Final Report identical descriptions quirk.

## Last Verified

- Date: 2026-07-06
- Model: Fable 5
- By: agent (first live run), pending user review
