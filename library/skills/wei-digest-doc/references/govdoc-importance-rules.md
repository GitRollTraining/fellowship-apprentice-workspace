# Importance Rules — wei-digest-doc, govdoc family

What stays, what goes, what stays verbatim. The digest is a descriptive capture of the document's substantive content — completeness first. Decision-relevance is NOT the keep/cut filter; it is one dedicated section (implications) at the end.

## Keep (substantive content)

Everything that is a fact of the document:

- Identifiers: solicitation/requisition/amendment numbers, form numbers, clause numbers
- Parties: offices, addresses, CO/COR names + contacts, signatories, UEI/DUNS
- Money & structure: contract type, CLINs, quantities, pricing rules, invoicing mechanics
- Time: every date, deadline (with timezone), period of performance, response-time standard
- Obligations: deliverables + due dates, PLAs, metrics, certifications, self-perform %
- Rights: IP/ownership clauses, data-rights language, government property rules
- Process: submission format, volume structure, page limits, evaluation method + factor weights + rating scales
- Scope: subject, goals (numbered lists verbatim-faithful), audience, exclusions
- For responses: every measurable promise, named person, claimed qualification, embedded asset

## Cut

- Narrative connective prose, marketing language, mission-statement rhetoric (capture the factual core in one line if it carries scope information; otherwise drop)
- FAR/IRM compliance boilerplate that is standard across sibling documents — summarize as one line ("compliance boilerplate p.18-42: FISMA, Pub 4812, IRM 10.8, 508") UNLESS a clause deviates from the sibling/prior document (then it is a delta — keep with source)
- Repetition: the same fact stated in RFQ header, schedule, and clauses appears once, with all source pages listed
- Blank/administrative pages (note their existence only when meaningful — e.g., a referenced attachment's page is blank)

## Must keep VERBATIM (no paraphrase)

- Numbers, dates, dollar figures, percentages, page limits
- Names (people, offices, systems, programs), clause/attachment identifiers
- Qualifiers and scope conditions: "unless the CO approves in writing", "no less than", "excluding Government-directed withdrawals", "where applicable". Dropping a qualifier flips a conditional obligation into an absolute — the #1 digest failure mode
- Rating-scale labels (Outstanding/Very Good/... ; High/Some/Low Confidence)
- Defined terms on first use, with the document's own definition

## Decision-relevance section (implications)

One section at the end ("{Company} implications" or "Over-commitments & delivery risks" for responses). Only here does analysis appear:

- Eligibility/fit, asset reuse/overlap, risk flags (IP, clock, staffing, ATO), win-theme hooks, open questions
- Each implication still traces to a sourced fact earlier in the digest
- Keep it factual-analytic ("§5.1 has no pre-existing-IP carve-out; LMS embedded in delivery is exposed"), not advocacy

## Length policy

As long as the content requires — no percentage bands, no line targets. Density drives length: an 8-page PWS may digest to 90 lines; a 48-page RFQ (half boilerplate) to ~160. Two tests, both must pass:

1. **No-reopen test:** a reader making a bid, delivery, or compliance decision never opens the PDF (legal review excepted).
2. **No-padding test:** every line is a fact, a sourced flag, or a table row. Delete any line that restates another.

## Sourcing

- Every fact row/bullet ends with its source: `p.N`, `p.N-M`, `§N.M`, or `rfq p.N; pws §M` when both state it
- Frontmatter `source:` names the file(s) + page count + document date
- Facts not found in the document do not enter the digest — no outside knowledge, no memory of sibling documents except in implications/cross-references (labeled as such)
