---
style: descriptive
---

# Tool inventory

Every skill, template, renderer, persona, plugin and connector in this workspace, what it is for,
and where it is. One test decided all of it: **does this help someone new to AI do an engagement?**

An engagement is: interview a business owner, confirm their current process, obtain sign-off on future
requirements, choose a proportionate automation approach, write a specification, build the agreed
deliverable, and hand it over so they can operate it without you. One agent-executable `skill.md` is the
common delivery shape, not the only one.

## What is here

| Kind | Name | Serves | Where it is | What you do with it |
|---|---|---|---|---|
| skill | `choose-automation-approach` | Automation deployment, integration and risk trade-offs | `library/skills/choose-automation-approach` | Helps a Fellow choose a proportionate runtime, access method, credential arrangement and high-stakes controls without turning every prototype into production infrastructure or hiding residual risk. |
| skill | `create-skill` | Specification writing for AI delegation | `library/skills/create-skill` | Runs a guided interview and scaffolds a SKILL.md with frontmatter, gotchas, and an eval baseline — the direct mechanism for engagement step 4, build an agent-executable skill.md. |
| skill | `digest-doc` | Coverage and boundary elicitation | `library/skills/digest-doc` | Turns a document the business already has in writing into a sourced fact-sheet, which is how coverage and boundary elicitation starts |
| skill | `drive-portal` | Operating-environment literacy | `library/skills/drive-portal` | Generic operating procedure for driving legacy/government web forms through the Chrome browser extension (popups, framesets, derived fields) — exactly what a beginner needs if the owner's process to automate involves filling an old or government web portal, feeding both process reconstruction and the resulting skill.md. |
| skill | `explain` | Owner handover explanation | `library/skills/explain` | Shapes plain-language explanation for a reader unfamiliar with a field — usable both while the fellow makes sense of an unfamiliar business domain during the interview/reconstruction steps and when writing handover material the owner (unfamiliar with AI) can actually read. |
| skill | `flowchart` | Process reconstruction in context | `library/skills/flowchart` | Builds a validated process/flow diagram as self-tested inline SVG (ISO 5807 symbols, automatic layout) — a direct fit for step 2, reconstructing the owner's process into steps/branches/exceptions, and for illustrating the resulting specification. |
| skill | `interview-recording` | Traceable synthesis | `library/skills/interview-recording` | Turns a recorded interview into a transcript with speakers attributed, and reduces it to key points, decisions and open questions. |
| skill | `kb-restructure` | Context engineering | `library/skills/kb-restructure` | Renames and re-nests an engagement directory as it grows without breaking what points at it |
| skill | `scan-agent-skill` | AI output verification and failure-mode literacy | `library/skills/scan-agent-skill` | Scans a local agent skill package with a pinned external security CLI before installation, execution or handoff. It defaults to local analyzers, uploads nothing, and treats a clean scan as evidence rather than certification. |
| skill | `video-to-markdown` | Past-instance evidence | `library/skills/video-to-markdown` | Turns a screen recording of a business owner demonstrating their process into a transcript-with-stills markdown document, directly serving step 2 (reconstruct the process) when the process is screen-based. |
| skill | `youtube-transcript` | Coverage and boundary elicitation | `library/skills/youtube-transcript` | Turns a YouTube (or any yt-dlp-supported) URL into a clean transcript, useful when a business owner points to an existing explainer/tutorial video as part of their process during step 1-2 research. |
| template | `brief-design` | Owner handover explanation | `library/templates/brief-design` | A design system for single-page HTML briefs; paired with the PDF renderer it is how a written handover becomes one file a non-technical owner opens |
| template | `engagement-decision-register` | Context engineering, autonomy calibration and gating | `library/templates/engagement-decision-register.md` | Holds the canonical current state of engagement decision areas, including unanswered future decisions, owners, controlled statuses, stage gates and revisit triggers. |
| template | `engagement-notes` | Context engineering | `library/templates/engagement-notes.md` | Generic two-mode project-notes pattern (objective, success criteria, context, decision-register pointer, materials) a fellow working alone across sessions can use to re-enter the engagement. |
| template | `engagement-progress-log` | Context engineering | `library/templates/engagement-progress-log.md` | Companion running session-log so a fellow with no reviewer keeps a verifiable record of what was done, verified, and next across multiple sessions with the owner. |
| template | `deliverable-deployment` | Client deployment | `library/templates/deliverable-deployment.md` | Gives the novice a complete canonical shape for install, configure, verify, upgrade, rollback and removal, including whole-bundle skill installation. |
| template | `deliverable-operations` | Client operation | `library/templates/deliverable-operations.md` | Gives the owner the canonical normal-run, signal, recovery, credential, maintenance, escalation and retirement path. |
| template | `deliverable-validation-report` | AI output verification | `library/templates/deliverable-validation-report.md` | Pins Validator A's candidate, contract coverage, behavioural evidence, operating checks, findings and single canonical verdict. |
| template | `handoff-package-manifest` | Owner handover navigation | `library/templates/handoff-package-manifest.md` | Plain-language start-here inventory that travels at the root of the client package. |
| template | `handoff-source-map` | Handoff traceability | `library/templates/handoff-source-map.md` | Keeps internal owner-facing claim IDs tied to authoritative sources and exact rendered/package bytes. |
| template | `handoff-validation-report` | AI output verification | `library/templates/handoff-validation-report.md` | Pins Validator B's fidelity, package-boundary, render, comprehension and archive checks. |
| template | `handover` | Owner handover explanation | `library/templates/handover.md` | What the process does, what it will not do and what to check, in the owner's vocabulary; it also carries the renderer's input contract |
| template | `index-manifest` | Context engineering | `library/templates/index-manifest.md` | Defines the INDEX manifest for governed work areas, including companion-directory inventory rules, Purpose, Inventory, Freshness and upstream pointer. |
| template | `interview-record` | Traceable synthesis | `library/templates/interview-record.md` | What was heard kept visibly apart from what was concluded, one statement per entry in the owner's own words, and a required pointer per load-bearing statement |
| template | `process-confirmation` | Grounding and confirmation | `library/templates/process-confirmation.md` | Near-direct match for reconstructing the owner's process: step-by-step, systems/data, pain points, and open items written for the owner to mark up and correct. |
| template | `process-inventory` | Coverage and boundary elicitation | `library/templates/process-inventory.md` | Extracts every workflow/process surfaced during an interview into a table plus per-item verbatim-quote evidence — the core technique for reconstructing a business owner's process from what they actually said. |
| template | `process-reconstruction` | Process reconstruction in context | `library/templates/process-reconstruction.md` | A per-step input/output, decision-rule, approval and system capture form that converts interview answers into detail the specification and agreed deliverable need. |
| template | `operational-acceptance` | Client operation | `library/templates/operational-acceptance.md` | Records client-authorised deployment and one owner-operated representative case before handed-over status. |
| template | `persona-preflight` | Handoff comprehension | `library/templates/persona-preflight.md` | Records the exact constrained context and answers from the mandatory non-technical-owner simulation. |
| template | `owner-acceptance` | Handoff comprehension | `library/templates/owner-acceptance.md` | Records the real owner's unprompted read-back and acceptance against exact candidate bytes. |
| template | `requirements-gathering` | Coverage and boundary elicitation | `library/templates/requirements-gathering.md` | Produces the PRD-like owner-sign-off artifact: desired outcomes, scope, user stories, requirements, acceptance criteria, constraints and feasibility inputs traced to confirmed discovery. |
| template | `specification` | Specification writing for AI delegation | `library/templates/specification.md` | Joins the signed PRD and current automation decisions into the traceable build contract; defaults to one skill but includes the extension shape for a larger solution. |
| renderer | `build-document-pdf` | Owner handover explanation | `library/renderers/build-document-pdf.py` | Turns one markdown file into an A4 PDF a business owner can open; this is the whole answer to turning finished work into a file the owner opens |
| renderer | `check-document-pdf` | Owner handover explanation | `library/renderers/check-document-pdf.py` | Proves the PDF actually rendered - catches a table that silently became prose and a character that silently vanished, neither of which changes the page count or the exit code |
| renderer | `make-the-handover-file` | Owner handover explanation | `library/renderers/make-the-handover-file.md` | Builds and checks the owner-account PDF while preserving the validated delivery tree as separate installable files. |
| persona | `adversarial-reviewer` | AI output verification and failure-mode literacy, Specification writing for AI delegation | `library/personas/adversarial-reviewer.md` | Nobody grades their own work, and a solo engagement has nobody else in the room |
| persona | `non-technical-owner` | Owner handover comprehension | `library/personas/non-technical-owner.md` | Cold-reads only client-visible material plus direct owner statements, exposing missing explanation without hidden implementation knowledge. |
| plugin | `claude-plugins-official` | Specification writing for AI delegation | install it: `claude-plugins-official` | Installed as a unit; 6 of its skills earn it, each named in library/sops/agent-settings.md |
| plugin | `planning-with-files` | Context engineering | install it: `planning-with-files` | Installed as a unit; 1 of its skills earn it, each named in library/sops/agent-settings.md |
| plugin | `smart-ralph` | Interview framing | install it: `smart-ralph` | Installed as a unit; 1 of its skills earn it, each named in library/sops/agent-settings.md |
| plugin | `superpowers` | Specification writing for AI delegation | install it: `superpowers` | Installed as a unit; 10 of its skills earn it, each named in library/sops/agent-settings.md |
| mcp | `claude-in-chrome` | Operating-environment literacy | connect it: claude-in-chrome | Seeing the tools the business actually uses, in the browser they use them in |
| mcp | `google-drive` | Coverage and boundary elicitation | connect it: google-drive | The small-business document reality. Connected with the client's credentials, never ours |
| mcp | `notion` | Coverage and boundary elicitation | connect it: notion | Where a business's own documentation often lives. Connected with the client's credentials, never ours |

## The plugins, skill by skill

A plugin installs as a unit, so the row above buys all of its skills. These are the ones that earn
it. Install instructions and the marketplace names are in `library/sops/agent-settings.md`.

| Plugin | Skill | 
|---|---|
| `claude-plugins-official` | `agent-development` |
| `claude-plugins-official` | `command-development` |
| `claude-plugins-official` | `mcp-integration` |
| `claude-plugins-official` | `skill-creator` |
| `claude-plugins-official` | `skill-development` |
| `planning-with-files` | `planning-with-files` |
| `smart-ralph` | `interview-framework` |
| `superpowers` | `brainstorming` |
| `superpowers` | `dispatching-parallel-agents` |
| `superpowers` | `receiving-code-review` |
| `superpowers` | `subagent-driven-development` |
| `superpowers` | `systematic-debugging` |
| `superpowers` | `test-driven-development` |
| `superpowers` | `using-superpowers` |
| `superpowers` | `verification-before-completion` |
| `superpowers` | `writing-plans` |
| `superpowers` | `writing-skills` |

## Connected per engagement, not by default

| Server | Why it is not in the base set |
|---|---|
| Slack | Real but not universal, and it needs the client's own workspace authorisation |
| Gmail | Same, and the blast radius of a mistake is higher because it can send |
| Google Calendar | Same, and rarely load-bearing for reconstructing a process |

Ship the instructions, not the connection. A connector authorised with our account against a
client's data is the wrong answer even when it works.

## Documented, deliberately not enabled

| Tool | Why |
|---|---|
| `computer-use` | Genuinely relevant to desktop automation, and it needs a per-session human grant plus native-application access. Too sharp for an unsupervised first engagement, and enabling it by default trains the habit of clicking through the grant without reading it |

## What is missing, named rather than hidden

| Gap | What it means for you |
|---|---|
| Packaging the finished deliverable into an installer a non-technical owner double-clicks | The default versioned zip preserves the exact delivery tree and gives the owner a start-here account, but it does not install the system. The private installer is still unavailable, so deployment follows the delivered instructions |
| Evidence that the finished deliverable and handoff work on a real engagement | Validator A/B, the constrained persona, real-owner comprehension and operational acceptance define the evidence chain. A novice-agent mock found and exercised wiring fixes, but none has run on a real client engagement; treat them as authored procedures, not proof that they improve outcomes |

These are the honest edges of this toolbox. The first has transport but no installer; the second has a
complete draft procedure but no real-use evidence. Nothing here pretends to close either gap further.
