<!-- upstream: engagements/example-client/INDEX.md -->
---
style: descriptive
---

# verification

## Purpose

Internal evidence for the exact candidate and handoff package that were checked. Validator A writes the
delivery manifest, report and permitted reproducible evidence here. Validator B writes the handoff
report here. This directory is part of the engagement record, not the client delivery boundary.

## Inventory

Empty. Validator A may create:

```text
deliverable-report.md
deliverable-manifest.tsv
evidence/
  commands/
  fixtures/
  observed-results/
```

Validator B may add `handoff-report.md`. Evidence stored here must obey the engagement Data & Credential
Boundary; use an access-controlled pointer when the evidence itself cannot be retained safely.

Do not put this directory, either validation report or internal evidence into the client package.

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| — | 2026-08-15 | Mutable | empty; populated by Validator A/B |
