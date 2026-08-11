<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# skills

Five agent skills, copied verbatim from the repositories that own them. Each was selected against three
tests in this order: does it serve a domain the curriculum actually teaches; is it portable; can you
install it without GitRoll's credentials.

## Inventory

| Skill | Serves | What it does |
|---|---|---|
| `wei-create-skill` | writing a specification for an agent to execute [D-06] | Authors a skill against the skill-authoring standard — the same standard your deliverable is graded by |
| `wei-explain` | explaining the finished process to the owner [D-29] | The explanation register, for a reader who is not in the field |
| `wei-flowchart` | rebuilding a process from start to finish [D-24] | A validated diagram, which is how an owner confirms a process you reconstructed |
| `wei-digest-doc` | reading what the business already has [D-27] | Turns a source document into a sourced fact-sheet |
| `kb-restructure` | keeping this workspace healthy | Renames, moves and archives files without breaking what points at them |

## How the agent finds them

`.claude/skills` is a symlink to this directory. Details, and the Windows fallback, in
`library/sops/agent-settings.md`.

## What is deliberately absent

Forty-six other skills exist in the source repositories. They were cut for one of four reasons: they are
wired to GitRoll's Notion and roadmap; they run GitRoll's meeting pipeline; they produce deliverables
that are our job rather than a fellow's; or they are personal. The full reasoning is in
`reference/tool-inventory.md`.

**One is a judgement call rather than a rule**, and it is flagged for the next developer: `wei-prep-goal`
serves autonomy calibration [D-03] and evaluation methodology [D-04] well, and its five-gate,
five-pass discipline is heavy for a first engagement. It is out on weight, not on fit.
