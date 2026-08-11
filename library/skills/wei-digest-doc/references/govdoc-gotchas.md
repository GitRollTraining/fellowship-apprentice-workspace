# Gotchas — wei-digest-doc, govdoc family

Domain-specific failure modes. Each entry: trigger / wrong default / correct behavior.

## Dropped qualifiers flip obligations

**Trigger:** any conditional phrase — "unless COR approves otherwise", "no less than", "excluding Government-directed withdrawals", "where applicable".
**Wrong default:** keep the headline claim, cut the hedge ("place of performance: virtual").
**Correct behavior:** qualifier travels with the fact, verbatim ("virtual; no on-site unless CO authorizes in writing").
**Why:** documented #1 summary failure mode; flips conditional obligations into absolutes and vice versa.

## Unusual clauses hide inside boilerplate

**Trigger:** long compliance/clauses sections that look standard (FAR flow-downs, 508, FISMA).
**Wrong default:** skip "boilerplate" wholesale.
**Correct behavior:** skim every boilerplate page for deltas vs the sibling/prior document; digest the deltas with source. One-line summarize the rest.
**Why:** TO3 PWS §5.1 grants the Government absolute ownership of ALL deliverables with no pre-existing/commercial/LMS carve-out — sibling TO2 had the carve-out. Reading it as "standard ownership language" buries an IP exposure.

## Response digests restate requirements instead of promises

**Trigger:** type `response`; responses echo RFQ requirement text back before answering it.
**Wrong default:** summarizing the echoed requirements — produces a second RFQ digest.
**Correct behavior:** extract commitments (promise → requirement answered → page), staffing names, embedded assets, over-commitments. Requirement facts cite the RFQ digest, never the response.
**Why:** the response digest's job is "what did we sign up for"; requirement restatements are already covered by the rfq/pws digest.

## Near-identical solicitation numbers

**Trigger:** any solicitation/BPA number (2032L226Q00041 = BPA vs 2032L226Q00052 = TO1 differ by two digits; 205AE9-26-Q-00072, 2032H5-26-Q-00145 follow different office formats).
**Wrong default:** typing the number from memory or from a sibling digest.
**Correct behavior:** copy character-by-character from the title page; spot-check in verification step.

## Draft artifacts in received response PDFs

**Trigger:** response PDF carries inline red RFQ-instruction text, yellow highlights, or requirement-echo blocks under headings.
**Wrong default:** digesting instruction text as if it were response content; or silently ignoring draft status.
**Correct behavior:** distinguish instruction text (red/requirement echoes) from response prose; digest only the response; FLAG the draft-artifact status in frontmatter-adjacent opening + implications ("confirm final-as-submitted version").
**Why:** TO3 Vol II arrived with red instruction text + highlights; treating it as final misrepresents what the Government received.

## Referenced attachments that are not actually present

**Trigger:** response says "Attachment 01 ... is included below" but the following page is blank; RFQ lists attachments distributed as separate files.
**Wrong default:** recording the attachment as present.
**Correct behavior:** verify the content physically exists in the PDF; if absent, record "referenced but not in this file" and flag as a missing-artifact follow-up.

## Sensitivity defaults

**Trigger:** setting frontmatter `sensitivity:`.
**Wrong default:** `[PUBLIC]` (workspace default for sourced docs).
**Correct behavior:** solicitations competed among BPA holders and all vendor responses are `[INTERNAL]` minimum. A response containing partner-private pricing or NDA-bound material escalates to `[CONFIDENTIAL]` + sidecar rules (`.claude/rules/sensitive-content-handling.md`).

## Digest date vs document date

**Trigger:** naming the output file and filling `updated:`.
**Wrong default:** today's date in the filename.
**Correct behavior:** filename uses the DOCUMENT's date (issue/submission/signature date from the title page): `{doc-date}_{slug}-summary.md`. `updated:` = date the digest was written/last edited.

## Intra-document qualifier divergence

**Trigger:** the same obligation stated in two sections with different strength (TO3 PWS: §9 responses "generally within two (2) business days" vs §6 PLA hard "Response within 2 business days").
**Wrong default:** citing one section and silently normalizing to a single standard.
**Correct behavior:** capture both statements with both sources and note the divergence — the PLA (surveilled standard) governs, but the softer clause is negotiation material.

## Compliance verdicts on draft copies

**Trigger:** running the compliance-check table on a PDF flagged with draft artifacts.
**Wrong default:** issuing Met/Not-met verdicts as if the copy were final.
**Correct behavior:** prefix the table with a basis note ("Basis: draft-artifact copy — re-verify against final-as-submitted") and rate uncertain items AT RISK, not failed.

## Sibling-document deltas are top-value facts

**Trigger:** the document has a sibling/near-twin (TO2 vs TO3; original vs amendment).
**Wrong default:** digesting the document in isolation.
**Correct behavior:** run a deliberate delta pass on high-stakes clauses (IP/ownership, PLAs + exceptions, materials/access posture, participant counts) against the sibling's digest; state each delta in implications with both sources. Real catches: TO3 dropped TO2's Government-directed-withdrawal exception on the completion PLA; TO3 §8 allows authorized IRS system/data access where TO2 was sanitized-only.

## Embedded-PWS duplication

**Trigger:** an RFQ digest already covers a PWS (embedded, or summarized together like TO3's rfq+pws fact-sheet), and a standalone PWS digest is requested.
**Wrong default:** writing a second full digest that duplicates the RFQ summary (violates one-source-of-truth).
**Correct behavior:** standalone PWS digest goes §-by-§ deeper than the combined summary; each notes the other in cross-references with scope split ("combined overview: rfq summary; §-level detail: this file"). If no deeper detail exists to add, do not create the file — report instead.
