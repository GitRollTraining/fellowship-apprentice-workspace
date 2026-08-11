# Baseline Input — wei-digest-doc (govdoc family)

Canonical input the skill should handle correctly.

## Input

```
/wei-digest-doc workforce-delivery/irs-bpa/task-orders/2032H5-26-Q-00145_full-stack-developer-training/pws.pdf --family=govdoc
```

Source: TO3 Performance Work Statement, 8 pages, dated 2026-06-17 (smallest real input; committed in the repo, stable).

## Acceptance Criteria

- Frontmatter present: `class: Immutable`, `sensitivity: "[INTERNAL]"`, `style: descriptive`, `source:` naming pws.pdf + page count + date.
- Every pws-schema section present or its omission reported.
- §5.1 absolute-IP-ownership clause captured with its no-carve-out delta vs TO2 flagged in implications.
- All qualifiers intact on spot-check (e.g., hours "unless COR approves otherwise"; travel "unless CO approves in writing").
- ≥5 facts spot-checked against cited §/page and matching (PoP 6 months, virtual, GS 11-15 + SL/SES/EX, LMS 99% business-hours availability, 100%-of-billed-participants completion PLA).
- Decision-relevance appears ONLY in the implications section.
- No fact without a `§`/`p.` source. No emojis. No narrative prose.
- INDEX.md row added for the digest in the same operation.

## Failure modes this eval catches

1. Qualifier dropping (conditional → absolute).
2. Boilerplate skip missing the §5.1 IP delta.
3. Unsourced facts / hallucinated page numbers.
