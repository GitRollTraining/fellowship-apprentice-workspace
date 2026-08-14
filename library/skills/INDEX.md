<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# skills

Skills are bounded, reusable agent capabilities that are not tightly coupled to the AI Fellowship
engagement lifecycle, directory structure or required artifacts. A skill may be used during an
engagement, but it remains meaningful and usable outside one.

The curated skills are reached through the `.claude/skills` symlink at the repository root. The
original nine are copies rather than links: each was taken from a source repository at a recorded
commit and patched where it named something that does not exist here. `choose-automation-approach` was
authored for this workspace. `CANON.md` records both kinds explicitly.

**Vendored copies are not always byte-identical to their sources.** Where one carries a deliberate
patch, the provenance record outside this tree holds both hashes, so the divergence is recorded rather
than silent.

## Inventory

| Skill | You reach for it when | What it does |
|---|---|---|
| `choose-automation-approach/` | you are choosing how an automation reaches systems, runs and acts | Runs an adaptive interview and recommends a proportionate deployment, integration, credential and high-stakes-control design while preserving the Fellow's overrides and accepted trade-offs. |
| `create-skill/` | you are writing the deliverable | Runs a guided interview and scaffolds a SKILL.md with frontmatter, gotchas, and an eval baseline — the direct mechanism for engagement step 4, build an agent-executable skill.md. |
| `digest-doc/` | the business hands you a document | Turns a document the business already has in writing into a sourced fact-sheet, which is how coverage and boundary elicitation starts |
| `drive-portal/` | the process runs through an old web form | Generic operating procedure for driving legacy/government web forms through the Chrome browser extension (popups, framesets, derived fields) — exactly what a beginner needs if the owner's process to automate involves filling an old or government web portal, feeding both process reconstruction and the resulting skill.md. |
| `explain/` | you are writing for the owner | Shapes plain-language explanation for a reader unfamiliar with a field — usable both while the fellow makes sense of an unfamiliar business domain during the interview/reconstruction steps and when writing handover material the owner (unfamiliar with AI) can actually read. |
| `flowchart/` | you are rebuilding a process end to end | Builds a validated process/flow diagram as self-tested inline SVG (ISO 5807 symbols, automatic layout) — a direct fit for step 2, reconstructing the owner's process into steps/branches/exceptions, and for illustrating the resulting specification. |
| `interview-recording/` | the session is recorded and needs to become a record | Turns a recorded interview into a transcript with speakers attributed, and reduces it to key points, decisions and open questions. |
| `kb-restructure/` | the engagement directory has outgrown its shape | Renames and re-nests an engagement directory as it grows without breaking what points at it |
| `video-to-markdown/` | the owner recorded their screen doing the work | Turns a screen recording of a business owner demonstrating their process into a transcript-with-stills markdown document, directly serving step 2 (reconstruct the process) when the process is screen-based. |
| `youtube-transcript/` | the owner points you at a video | Turns a YouTube (or any yt-dlp-supported) URL into a clean transcript, useful when a business owner points to an existing explainer/tutorial video as part of their process during step 1-2 research. |

## Freshness

| File set | Cut at | Class | Status |
|---|---|---|---|
| original nine skills | 2026-08-11 | Instruction | current at the commit recorded per file |
| `choose-automation-approach/` | 2026-08-13 | Instruction | authored for this workspace; eval baseline included |
