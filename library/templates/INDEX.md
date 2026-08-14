<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# templates

The shapes an engagement's documents are written into. Copy the marked block out of a template and
into your engagement directory; do not fill one in here, because `library/` is read-only.

`handover.md` is the one to read before you write anything you intend to turn into a PDF: it carries
the input contract the renderers in `library/renderers/` actually consume, and a document that
ignores it renders wrongly without raising an error.

## Inventory

| Item | What it is |
|---|---|
| `engagement-decision-register.md` | Canonical current-state register for decision areas, owners, stage gates and the position currently in force; includes the common starter rows and controlled values. |
| `engagement-notes.md` | Generic two-mode project-notes pattern (objective, success criteria, context, decision-register pointer, materials) a fellow working alone across sessions can use to re-enter the engagement. |
| `engagement-progress-log.md` | Companion running session-log so a fellow with no reviewer keeps a verifiable record of what was done, verified, and next across multiple sessions with the owner. |
| `deliverable-validation-report.md` | Internal Validator A record: candidate manifest, acceptance evidence, behavioural cases, operating checks, findings and exact verdict |
| `handoff-package-manifest.md` | Plain client-facing start-here inventory placed at the root of the default handoff package |
| `handoff-source-map.md` | Internal `HC-*` claim-to-authority map joining owner-facing source, rendered output and candidate package hashes |
| `handover.md` | Owner-account shape: what was delivered, what it will not do, what to check and where canonical operating instructions live |
| `handoff-validation-report.md` | Internal Validator B record: passed-candidate integrity, package inventory, claim fidelity, comprehension gates, rendering and archive integrity |
| `index-manifest.md` | Defines the INDEX.md manifest the toolbox mandates in every directory - Purpose, Inventory, Freshness, upstream pointer |
| `interview-record.md` | What was heard kept visibly apart from what was concluded, one statement per entry in the owner's own words, and a required pointer per load-bearing statement |
| `process-confirmation.md` | Near-direct match for reconstructing the owner's process: step-by-step, systems/data, pain points, and open items written for the owner to mark up and correct. |
| `process-inventory.md` | Extracts every workflow/process surfaced during an interview into a table plus per-item verbatim-quote evidence — the core technique for reconstructing a business owner's process from what they actually said. |
| `process-reconstruction.md` | A per-step input/output schema-plus-sample, decision-criteria, human-approval-point, and systems-table capture form that converts interview answers directly into the granular detail a spec and an agent-executable skill.md need. |
| `persona-preflight.md` | Internal exact-input record for the constrained non-technical-owner cold-reader run |
| `owner-acceptance.md` | Internal hard-gate record of the real owner's comprehension and acceptance against exact package bytes |
| `requirements-gathering.md` | PRD-like document for owner sign-off: desired outcomes, scope, user stories, requirements, acceptance criteria, operational constraints and feasibility inputs, all traced to confirmed discovery. |
| `specification.md` | The default build-contract shape, joining the signed PRD and automation decisions to the deliverable while preserving a resolvable evidence chain. |
| `brief-design/` | A design system for a single-page HTML brief: tokens, components, composition rules and a starter file |

## Freshness

| File set | Last updated | Class | Status |
|---|---|---|---|
| all 18 items | 2026-08-15 | Instruction | Output Phraser, source-map, comprehension and package contracts added; nonexistent brief-design alias removed |
