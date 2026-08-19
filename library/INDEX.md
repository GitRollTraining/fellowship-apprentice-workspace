<!-- upstream: INDEX.md -->
---
style: descriptive
---

# library — ours, and read-only

Everything here was extracted from our own working repositories, or written for this workspace.
**You do not edit it.** Where each file came from, and the hash it was cut at, is recorded outside
this tree; a hash guards nothing if the file is editable by the person it is shipped to.

If something here is wrong, say so — do not fix it locally. A local fix is invisible to everyone else
holding the same library, and it is the exact failure that stranded four earlier attempts at sharing
this material.

## Inventory

| Item | What it is | Class |
|---|---|---|
| `playbooks/` | Procedures a fellow reruns on every engagement. One worked, four stubbed | Instruction |
| `skills/` | Ten curated agent skills: nine vendored from source repositories and one authored here, all recorded in the provenance manifest | Instruction |
| `personas/` | Agent personas. One shipped, a second named | Instruction |
| `sops/` | Working standards and agent settings | Instruction |
| `templates/` | The shapes an engagement's documents are written into, and the design system for a brief | Instruction |
| `renderers/` | Turning finished markdown into one file a business owner opens, and the check that proves it rendered | Instruction |
| `reference/` | The defined terms, the curated tool cut, and the doctrine the skills route to | Instruction |

## Freshness

| File set | Cut at | Class | Status |
|---|---|---|---|
| everything under `library/` | recorded per file | Instruction | current at the cut commit recorded per row |
