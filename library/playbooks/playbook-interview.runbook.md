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
| 20 Write the owner's version | owner-facing account | `handover/owner-account.md` |
| 21 Find out what they cannot answer, and fix it | what the owner could not answer, and the revision | `handover/comprehension-check.md` |

Steps 3 to 6, 9, 10, 11 and 14 are conducted in the room and produce no separate file — their output is
the session record itself.

## Which shipped tool serves which step

Machine-readable in `playbook-deps.tsv` at the task root; this is the same list with the reason.

| Step | Tool | Why this one |
|---|---|---|
| 7 Reconstruct the process | `wei-flowchart` | A process is confirmed by an owner looking at a diagram, not by reading prose back to them |
| 20 Write the owner's version | `wei-explain` | The owner is not in the field. This is the explanation register, and it is a different genre from the discovery record |
| 21 Comprehension check | `wei-explain` | The revision loop is the same register as the draft it repairs |
| 15 to 17 Write the record | `wei-digest-doc` | Reading what the business already has, and composing it into a sourced fact-sheet |
| after 21 Draft the deliverable | `wei-create-skill` | The deliverable is a `skill.md`, and this is the skill that loads the standard it will be graded against |
| after the draft | `adversarial-reviewer` persona | Nobody grades their own work, and on a solo engagement there is nobody else in the room |
| throughout | `planning-with-files` plugin | The session spans days. State that is not on disk is state that is lost |
| throughout | `kb-restructure` skill | An engagement directory that grows will need renaming and re-nesting without breaking its own references |

## Stop conditions this workspace adds

The playbook's own stop conditions still hold. Two more apply because the work is filed here:

1. **No recording agreement, and no written note of that fact.** Precondition 2 of the playbook covers
   the agreement; this adds that the absence has to be on disk in `interview/pre-session-note.md`, not
   remembered.
2. **A load-bearing statement in the discovery record with no pointer back at the session.** Step 16
   makes this a rule; filing makes it checkable. If it cannot be pointed at, it is a conclusion, and it
   belongs in the concluded half.
