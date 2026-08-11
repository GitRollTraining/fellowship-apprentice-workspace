# Type Schemas — wei-digest-doc, govdoc family

Section template per document type. Sections in order; omit a section only when the document genuinely has no content for it (state the omission in the report). Every fact row carries a source (`rfq p.N`, `pws §N`, `resp p.N`). Add sections when the document contains substantive content no slot covers — schemas are floors, not ceilings.

## Common frontmatter (all types)

```yaml
---
title: {Document title} ({solicitation number})
solicitation: {number}
class: Immutable
sensitivity: "[INTERNAL]"   # solicitations competed among BPA holders + vendor responses default INTERNAL, not PUBLIC
style: descriptive
source: {filename} ({N} pages[, dated YYYY-MM-DD])
updated: {YYYY-MM-DD}
---
```

Opening paragraph (no heading): 2-4 sentences placing the document — which vehicle/task order, which BPA task, what distinguishes it from sibling documents, what the source files are. Facts only.

## Type: rfq (solicitation; subsumes embedded PWS)

| # | Section | Contents |
|---|---------|----------|
| 1 | Solicitation header | Table: solicitation no., requisition no., issue date, offer due, issuing office + address, CO (name/email/phone), COR, method, form, set-aside, NAICS + size standard, authority, competed-among, invoicing |
| 2 | Contract type & CLIN structure | FFP/T&M, each CLIN with description/QTY/period, pricing rules |
| 3 | Subject & goals | Program subject, numbered practical-skills goals, scope boundaries (which BPA task; what's excluded) |
| 4 | Participants | Count, grades, roster mechanics, who identifies priorities |
| 5 | Period & delivery | Table: PoP, base-period dates, delivery mode, place, hours, travel, LMS, materials constraints |
| 6 | Deliverables | Table: deliverable, due, reviewer. Then ownership/IP clause + inspection/acceptance |
| 7 | Performance metrics + PLAs | Minimum metrics list; PLA table (objective, standard, surveillance) |
| 8 | Security & compliance | Requirements + which compliance boilerplate applies and how heavily |
| 9 | Key dates | Table: issued, questions due, quotes due (with timezone) |
| 10 | Submission requirements | Format rules; volume table (volume, contents, page limit) |
| 11 | Subcontracting / set-aside mechanics | Self-perform %, commitment letters, teaming rules — when present |
| 12 | Evaluation | Method, factor order + relative weights, rating scales, price-evaluation basis, award-without-exchanges language |
| 13 | Attachments | Table: attachment, type (proposal deliverable vs post-award vs reference), notes |
| 14 | {Company} implications | Decision-relevance lives HERE and only here: eligibility, reuse/overlap with existing assets, risks (IP, clock, staffing), win-theme hooks |
| 15 | Cross-references | Sibling task orders, parent BPA, glossary |

## Type: pws (standalone performance work statement)

| # | Section | Contents |
|---|---------|----------|
| 1 | Document header | Table: title, date, parent solicitation, BPA task, pages |
| 2 | Background & purpose | Stated mission context — facts only, 2-4 lines |
| 3 | Scope | Which BPA task, audience, program shape (cohorts), what's out of scope |
| 4 | Task requirements | Per PWS §4 subsection: requirement + standard. Numbered skill areas verbatim |
| 5 | Program management | Kickoff, reporting cadence, workforce-report mechanics, certifications |
| 6 | Deliverables | Table: deliverable, due, reviewer + ownership/IP clause + inspection/acceptance |
| 7 | PLAs | Table: objective, standard, surveillance + payment basis |
| 8 | Security & compliance | SBU/GFI handling, training prerequisites, 508 |
| 9 | GFP / GFI | What government furnishes, constraints |
| 10 | Logistics | PoP, place, hours, travel, communications |
| 11 | {Company} implications | Decision-relevance: delivery obligations vs our assets, risk clauses, open questions |
| 12 | Cross-references | Parent RFQ digest, sibling documents |

## Type: response (our team's quote/proposal volume)

Frame: what did WE promise. Not a restatement of requirements.

| # | Section | Contents |
|---|---------|----------|
| 1 | Submission header | Table: RFQ responded to, volume + factor(s), due date, submitted-by (prime, UEI, signatory, POC), page count, partners named |
| 2 | Commitments | Table: commitment (verbatim-faithful promise) → RFQ/PWS requirement it answers → resp page. Every measurable promise: durations, hours/week, cohort sizes, response times, platforms |
| 3 | Delivery model | Schedule shape, cohort structure, participant time commitment, modality |
| 4 | Staffing & named personnel | Names, roles, qualifications claimed, org (prime vs sub) |
| 5 | Assessment & measurement approach | Baseline/formative/post structure, what's tracked, where it surfaces |
| 6 | Embedded assets | Figures, dashboards, tools shown — what asset, whose IP, where it appears |
| 7 | Partner roles | Prime vs subcontractor split as written |
| 8 | Win themes & differentiators | Explicit claims of advantage (past performance, incumbency, credentials) |
| 9 | Over-commitments & delivery risks | Promises that bind delivery: aggressive standards, unbuilt capabilities, staffing dependencies. This is the response-type implications section |
| 10 | Compliance check | Table: RFQ submission requirement (page limit, required content, format) → met/not-met/at-risk → evidence. If the copy carries draft artifacts, open with a basis note ("Basis: draft-artifact copy — re-verify against final-as-submitted") and use AT RISK for uncertain items |
| 11 | Cross-references | RFQ digest, sibling volumes, partner docs |

## Type: amendment

| # | Section | Contents |
|---|---------|----------|
| 1 | Amendment header | Table: amendment no., signed date, CO, parent solicitation |
| 2 | Changes | Table: item changed → before → after → source page. Include deadline shifts, CLIN changes, page-limit changes, new attachments |
| 3 | Superseded documents | Which files are now non-authoritative; add `[SUPERSEDED → x]` flags to their INDEX rows |
| 4 | Q&A digest | When the amendment releases vendor Q&As: table of question topic → answer substance → Q number |
| 5 | {Company} implications | What the delta changes for bid/delivery |
| 6 | Cross-references | Parent solicitation digest |
