<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# skills

Skills are bounded, reusable agent capabilities that are not tightly coupled to the AI Fellowship
engagement lifecycle, directory structure or required artifacts. A skill may be used during an
engagement, but it remains meaningful and usable outside one.

The curated skills are reached through the `.claude/skills` symlink at the repository root. The
skills here are copies rather than links: each was taken from a source repository at a recorded
commit and patched where it named something that does not exist here. Nine arrived from
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT) on 2026-08-23 at commit `5b15a47`:
`to-spec` lost its issue-tracker publishing step and `teach` had its output directory pinned to
`training/learning/`, because neither exists or is writable here as upstream assumes. `choose-automation-approach`,
`scan-agent-skill`, `onboarding` and `workspace-help` were authored for this workspace. `CANON.md`
records both kinds explicitly.

**Vendored copies are not always byte-identical to their sources.** Where one carries a deliberate
patch, the provenance record outside this tree holds both hashes, so the divergence is recorded rather
than silent.

## Inventory

| Skill | You reach for it when | What it does |
|---|---|---|
| `choose-automation-approach/` | you are choosing how an automation reaches systems, runs and acts | Runs an adaptive interview and recommends a proportionate deployment, integration, credential and high-stakes-control design while preserving the Fellow's overrides and accepted trade-offs. |
| `command-failed/` | a command or setup step failed and you are stuck | Four things to gather before asking anyone, and three not to do. Written for the day-one case, where `diagnosing-bugs` is the deep end. |
| `create-skill/` | you are writing an agent skill | Runs a guided interview, scaffolds the skill and companions, checks the explicit authoring path and requires a client-delivered skill to be tested from its documented installed form. |
| `diagnosing-bugs/` | something is broken and you cannot say why | Runs a diagnosis loop that insists on a tight pass/fail signal before any hypothesis is tested. Written for a codebase with a test suite, so it is the deep end rather than the day-one tool. |
| `digest-doc/` | the business hands you a document | Turns a document the business already has in writing into a sourced fact-sheet, which is how coverage and boundary elicitation starts |
| `drive-portal/` | the process runs through an old web form | Generic operating procedure for driving legacy/government web forms through the Chrome browser extension (popups, framesets, derived fields) — exactly what a beginner needs if the owner's process to automate involves filling an old or government web portal, feeding both process reconstruction and the resulting skill.md. |
| `explain/` | you are writing for the owner | Shapes plain-language explanation for a reader unfamiliar with a field — usable both while the fellow makes sense of an unfamiliar business domain during the interview/reconstruction steps and when writing handover material the owner (unfamiliar with AI) can actually read. |
| `flowchart/` | you are rebuilding a process end to end | Builds a validated process/flow diagram as self-tested inline SVG (ISO 5807 symbols, automatic layout) — a direct fit for step 2, reconstructing the owner's process into steps/branches/exceptions, and for illustrating the resulting specification. |
| `grill-me/` | you are about to commit to a plan | Alias. Calls `grilling`. |
| `grilling/` | you are about to commit to a plan | Interviews you relentlessly about a decision, one question at a time with a recommended answer, until the plan survives or changes. The Verify habit turned on your own thinking before you spend a day on it. |
| `handoff/` | the session has got long and confused | Compacts the conversation into a handoff document a fresh session picks up from. This is the written re-anchor the context-engineering chapter asks for. |
| `interview-recording/` | the session is recorded and needs to become a record | Turns a recorded interview into a transcript with speakers attributed, and reduces it to key points, decisions and open questions. |
| `kb-restructure/` | the engagement directory has outgrown its shape | Renames and re-nests an engagement directory as it grows without breaking what points at it |
| `onboarding/` | you are a new apprentice and nothing is set up yet | Walks the nineteen setup items from a fresh machine to a working workspace, verifies the ones a command can verify, and records the ones only the apprentice can confirm so a later session knows what is still outstanding. |
| `scan-agent-skill/` | you are about to install, execute or hand over an agent skill | Runs a pinned, local-only security scan over the whole skill package, then requires a human disposition for findings and a manual review even when the scan is clean. The scanner installs separately; its source and dependencies are not copied into this workspace. |
| `teach/` | you need to learn something properly, over days | Builds a stateful teaching workspace under `training/learning/`: a mission, a learning record, a glossary and self-contained HTML lessons that accumulate into a course. |
| `to-questionnaire/` | the owner could not answer it in the room | Turns a decision you cannot settle into a questionnaire for someone else to fill in, so an unanswered question leaves the session as a document rather than a gap. |
| `to-spec/` | the interview is done and you have the answers | Synthesises the conversation into a specification without re-interviewing: problem, solution, seams, definition of done. |
| `video-to-markdown/` | the owner recorded their screen doing the work | Turns a screen recording of a business owner demonstrating their process into a transcript-with-stills markdown document, directly serving step 2 (reconstruct the process) when the process is screen-based. |
| `wait-what/` | that last message did not land | Stops and makes the agent re-pitch what it just said. Say it instead of nodding along. |
| `workspace-help/` | you do not know where something goes or which tool to reach for | Answers how-do-I and where-does-this-go questions by listing what is in the repository at that moment and reading its manifests, rather than from a remembered inventory that goes stale as the workspace grows. |
| `writing-for-agents/` | you are writing a document an agent will read | The authoring rules for skills, AGENTS.md and CLAUDE.md: what an agent acts on, and what it skims past. |
| `youtube-transcript/` | the owner points you at a video | Turns a YouTube (or any yt-dlp-supported) URL into a clean transcript, useful when a business owner points to an existing explainer/tutorial video as part of their process during step 1-2 research. |

## Freshness

| File set | Cut at | Class | Status |
|---|---|---|---|
| original nine skills | 2026-08-11 | Instruction | current at the commit recorded per file |
| nine skills from mattpocock/skills | 2026-08-23 | Instruction | current at upstream commit `5b15a47`; two carry a local patch |
| `choose-automation-approach/` | 2026-08-13 | Instruction | authored for this workspace; eval baseline included |
| `scan-agent-skill/` | 2026-08-14 | Instruction | authored wrapper; pins Cisco AI Skill Scanner 2.0.13 |
| `onboarding/`, `workspace-help/` | 2026-08-22 | Instruction | authored for this workspace; apprentice-facing. Both were driven end to end for the first time on 2026-08-22, in the ChatGPT desktop application in Codex mode, against a throwaway clone. The onboarding run surfaced the gap this update closes: the four reading topics were explained nowhere the agent could reach, so it answered from the public web. Neither has yet been run by an apprentice who is not also a maintainer |
