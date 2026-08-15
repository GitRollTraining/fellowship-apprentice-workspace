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

Validator B may add `handoff-report.md`; the post-B client deployment and independent owner run add
`operational-acceptance.md`. Evidence stored here must obey the engagement Data & Credential Boundary;
use an access-controlled pointer when the evidence itself cannot be retained safely.

Output Phraser and the comprehension gates may also create:

```text
handoff-source-map.md
persona-preflight.md
owner-acceptance.md
```

The source map traces material `HC-*` claims without exposing those internal identifiers to the client.
The persona report records its restricted prior knowledge; the owner record names the exact package and
owner-facing hashes accepted or rejected. Operational acceptance names the same B-passed package and
records whether it was deployed and operated independently in the intended client environment.

Do not put this directory, either validation report or internal evidence into the client package.

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| — | 2026-08-15 | Mutable | empty; populated by Phraser, comprehension gates, Validator A/B and operational acceptance |
