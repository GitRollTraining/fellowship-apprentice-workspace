---
style: descriptive
role: runbook wrapper
binds: playbook-interview.md
serves: D-21, D-22, D-23, D-24, D-25, D-26, D-27, D-28, D-29
---

# Running the interview playbook in this workspace

`playbook-interview.md` is shipped **verbatim** from the programme record and is not edited here. It is
written to be read without any other document, and it names no tool, no directory and no file. That is
correct for a playbook and insufficient for running one. This file supplies the missing half: where each
step's output goes, and which shipped tool it uses.

For execution in this workspace, this wrapper governs artifact destinations and stage timing wherever
the verbatim record differs. In particular, steps 20 and 21 confirm the **current-state process**; they
do not create the post-build owner account or end the engagement. Keep the original wording as programme
provenance, but do not use its “finished process” language as permission to skip the PRD, build or gates.

## Read this first: what "validated" means here, and what it does not

The playbook carries `status: draft — never executed`, and that stamp is still true. **No fellow has run
it against a business owner and no result of any kind has come back from it.** Nothing below changes that.

What was validated in this round is narrower and is stated exactly:

| Checked | How | Result |
|---|---|---|
| Every step that produces an artifact has a destination directory that exists in this repo | the table below, against `structure.tsv` | pass |
| Every tool **name** the playbook needs appears in the curated cut | a set difference between `playbook-deps.tsv` and `cut.tsv` (gate G4) | pass |
| Every tool the playbook names actually **runs** for someone outside GitRoll | a first-round audit read every shipped `SKILL.md` | **five of eight failed, and were repaired**: three routed to doctrine files that were pointed at but never shipped, one copied its own scripts out of the author's home directory, and one halted at step 0 on a probe that recognised exactly two GitRoll repositories. Repaired here; **not yet re-run end to end by a person** |
| Every taught competency the playbook names maps to a domain the curriculum teaches | its inline competency names against `domains-in.tsv` | pass |

**Read the second and third rows together.** G4 compares two columns of text. It cannot open a skill, and
it never did — a name matching a name is not a tool that works. The row above it says "pass" about names;
the row below says what happened when someone actually read the files.

**Not checked, and not claimable:** that following it collects more or better than not following it. The
playbook says so on its own face, citing the one controlled study of teaching an interview method to
novices, which found no significant difference in output quality and a significant difference only in how
confident the taught group felt.

## Where each step's output goes

Paths are relative to `engagements/<client-slug>/`.

| Playbook step | Output | Destination |
|---|---|---|
| 1 Decide what the session must settle | the pre-session note | `interview/pre-session-note.md` |
| 2 Write the questions, then repair them | both versions, kept | `interview/questions-v1.md`, `interview/questions-v2.md` |
| 3 to 14 (the session) | recording, and live notes | `interview/session-<date>/` |
| 7 Reconstruct the process end to end | the reconstructed process | `process/process-<name>.md` |
| 8 Get the exceptions | named exception cases | `process/exceptions.md` |
| 12 Ask the boundary questions | what must not be automated, who approves, what may not leave | `process/boundaries.md` |
| 13 Ask what happens when it breaks | failure behaviour today | `process/failure-modes.md` |
| 15 Write the record, heard and concluded apart | the discovery record | `interview/discovery-record.md` |
| 16 Point every load-bearing statement back at the session | pointers inside the discovery record | same file |
| 17 List what is still ambiguous | ambiguity list with dispositions | `interview/ambiguities.md` |
| 18 Close the loop on the pre-session note | annotated pre-session note | `interview/pre-session-note.md` |
| 19 Audit your own questioning | the self-audit | `interview/self-audit-<date>.md` |
| between 19 and 20 Prepare current-state confirmation | owner-facing confirmation, its default checked flowchart and any new heard corrections | `process/confirmation-<process-slug>-v<n>.md`, `process/confirmation-<process-slug>-v<n>-flowchart.svg`, `interview/discovery-record.md` |
| 20 Give the owner their version of the current state | the returned or synchronously marked confirmation materials | the same versioned files under `process/` |
| 21 Find what they cannot confirm, and repair it | new heard corrections and the next confirmation version | `interview/discovery-record.md`, `process/confirmation-<process-slug>-v<n+1>.md` and its flowchart when applicable |

Steps 3 to 6, 9, 10, 11 and 14 are conducted in the room and produce no separate file — their output is
the session record itself.

## Which shipped tool serves which step

This table is the list. Every tool named here is in this repository at the path given, and the steps
are the numbered steps of `playbook-interview.md`.

| Step | Tool | Where it is | Why this one |
|---|---|---|---|
| 3–14 Record the session | `interview-recording` | `library/skills/` | The in-room conversation becomes a transcript a process can be reconstructed from |
| between 19 and 21 Confirm the reconstruction | `flowchart` | `library/skills/` | A checked diagram is the default confirmation view when sequence, branching, a loop or handoff gives the owner a relationship to inspect |
| 7, 8, 12, 13 Reconstruct | `process-reconstruction.md` | `library/templates/` | Per-step capture, exceptions as named cases, the three boundary questions, and what happens when it breaks |
| 15 to 17 Write the record | `interview-record.md` | `library/templates/` | Heard kept visibly apart from concluded, with a required pointer column |
| 15 to 17 Write the record | `digest-doc` | `library/skills/` | Reading what the business already has, and composing it into a sourced fact-sheet |
| between 19 and 20 Confirm the reconstruction | `process-confirmation.md` | `library/templates/` | The document the owner reads or marks up, synchronously or asynchronously, before requirements are written |
| 20 and 21 Confirm and repair current state | `process-confirmation.md` | `library/templates/` | The versioned document and default flowchart close discovery before requirements are written |
| after 21 Continue from discovery to the deliverable | `playbook-discovery-to-deliverable.md` | `library/playbooks/` | Owns PRD drafting and sign-off, automation approach, specification and build |
| Draft the PRD | `requirements-gathering.md` | `library/templates/` | Normalises confirmed discovery into future behaviour, user stories, requirements and acceptance criteria |
| Test the PRD for feasibility | `choose-automation-approach` | `library/skills/` | Makes runtime, integration, credential and high-stakes-control decisions without owning engagement bookkeeping |
| Write the technical specification | `specification.md` | `library/templates/` | Joins the signed PRD to the technical decisions in the build contract |
| Build the default single-skill deliverable | `create-skill` | `library/skills/` | Loads the standard and scaffolds `deliverable/skill.md`; larger agreed solutions adapt the build shape |
| before reviewing a delivered skill | `scan-agent-skill` | `library/skills/` | Runs pinned local security analyzers against the complete installable unit; clean is evidence, not certification |
| after the draft | `adversarial-reviewer` persona | `library/personas/` | Nobody grades their own work, and on a solo engagement there is nobody else in the room |
| after Validator A | `playbook-output-phraser.md` | `library/playbooks/` | Creates the owner-facing account, source map and candidate package without changing validated behaviour |
| after Output Phraser | `non-technical-owner` persona | `library/personas/` | Mandatory cold-reader preflight constrained to what the owner actually knew from discovery |
| after persona pass | `owner-acceptance.md` | `library/templates/` | Records the real owner's comprehension and acceptance against the exact candidate bytes |
| package release gate | `playbook-validate-handoff.md` | `library/playbooks/` | Checks fidelity, package boundary, rendering, comprehension evidence and final archive integrity |
| after Validator B | `operational-acceptance.md` | `library/templates/` | Records client deployment and one independent owner run before status becomes handed-over |
| Render the final account | `make-the-handover-file.md` | `library/renderers/` | Builds and checks only the owner account; executable delivery files remain separate and installable |
| throughout | `planning-with-files` plugin | installed, see `library/sops/agent-settings.md` | The session spans days. State that is not on disk is state that is lost |
| throughout | `kb-restructure` skill | `library/skills/` | An engagement directory that grows will need renaming and re-nesting without breaking its own references |

The last row of the interview playbook is not the last step of the engagement. After step 21 confirms
the current state, work continues through `library/playbooks/playbook-discovery-to-deliverable.md`:
signed requirements, automation approach, specification, implementation, Validator A, Output Phraser,
the constrained persona, real owner acceptance, Validator B, client-authorised deployment and one
independent owner run. The engagement ends only when operational acceptance records that the owner ran
the unchanged B-passed package in the intended environment and the orchestrator records `handed-over`.

## Stop conditions this workspace adds

The playbook's own stop conditions still hold. Two more apply because the work is filed here:

1. **No recording agreement, and no written note of that fact.** Precondition 2 of the playbook covers
   the agreement; this adds that the absence has to be on disk in `interview/pre-session-note.md`, not
   remembered.
2. **A load-bearing statement in the discovery record with no pointer back at the session.** Step 16
   makes this a rule; filing makes it checkable. If it cannot be pointed at, it is a conclusion, and it
   belongs in the concluded half.
