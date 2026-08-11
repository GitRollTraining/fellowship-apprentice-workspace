---
style: descriptive
role: playbook stub
status: STUB — not written. Contents specified, author unassigned.
serves: D-01, D-09, D-12
---

# Environment setup — STUB

**This is not a playbook.** It is the specification of one, so that whoever writes it does not have to
re-derive the scope. Written to be handed to the next developer.

**When the fellow runs it:** at the start of every engagement, before the first interview.

**What it must contain, at minimum:**

1. Numbered steps, preconditions, stop conditions and failure modes — the shape set by
   `playbook-interview.md`, which is the only executed-shape precedent in the programme.
2. Creating `engagements/<client-slug>/` with the five subdirectories, and what belongs in each.
3. Which of the per-engagement MCP servers this client needs, and the instruction for obtaining the
   client's own credentials — never ours. See `library/sops/agent-settings.md`.
4. The autonomy setting for this engagement, decided once here rather than per task [D-03].
5. A budget and iteration ceiling set before work starts, not after it overruns.

**What it must NOT contain:** anything that assumes our workspace. This playbook is the one most likely
to be written by copying ours, and ours is keyed on company division, which an apprentice does not have.

**Open question the author must rule:** whether environment setup is a playbook at all, or a one-page
checklist. It is run once per engagement, which is the weakest case for a playbook of the five.
