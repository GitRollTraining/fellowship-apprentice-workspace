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
| `brief-design.md` | A design system for single-page HTML briefs; paired with the PDF renderer it is how a written handover becomes one file a non-technical owner opens |
| `engagement-notes.md` | Generic two-mode project-notes pattern (objective, success criteria, context, decisions, materials) a fellow working alone across sessions can use to keep external state on the engagement. |
| `engagement-progress-log.md` | Companion running session-log so a fellow with no reviewer keeps a verifiable record of what was done, verified, and next across multiple sessions with the owner. |
| `handover.md` | What the process does, what it will not do and what to check, in the owner's vocabulary; it also carries the renderer's input contract |
| `index-manifest.md` | Defines the INDEX.md manifest the toolbox mandates in every directory - Purpose, Inventory, Freshness, upstream pointer |
| `interview-record.md` | What was heard kept visibly apart from what was concluded, one statement per entry in the owner's own words, and a required pointer per load-bearing statement |
| `process-confirmation.md` | Near-direct match for reconstructing the owner's process: step-by-step, systems/data, pain points, and open items written for the owner to mark up and correct. |
| `process-inventory.md` | Extracts every workflow/process surfaced during an interview into a table plus per-item verbatim-quote evidence — the core technique for reconstructing a business owner's process from what they actually said. |
| `process-reconstruction.md` | A per-step input/output schema-plus-sample, decision-criteria, human-approval-point, and systems-table capture form that converts interview answers directly into the granular detail a spec and an agent-executable skill.md need. |
| `requirements-gathering.md` | Questionnaire pattern (systems access, data sources, technical environment, dependencies) helps the fellow pin down exactly what the owner's process touches before building the skill. |
| `specification.md` | The shape the specification is written into, ordered so that specification to skill.md is a mechanical step rather than a second act of authorship |
| `brief-design/` | A design system for a single-page HTML brief: tokens, components, composition rules and a starter file |

## Freshness

| File set | Last updated | Class | Status |
|---|---|---|---|
| all 12 items | 2026-08-11 | Instruction | first cut |
