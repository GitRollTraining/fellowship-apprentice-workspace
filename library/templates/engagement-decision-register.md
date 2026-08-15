---
style: descriptive
role: template
produces: engagements/<client-slug>/decision-register.md
---

# Engagement decision register

The canonical current-state record for decisions in one engagement. It holds decision areas before
they have answers as well as the position currently in force. It is not a chronological log, a list
of secrets or a substitute for the detailed specification.

Copy the block below to `engagements/<client-slug>/decision-register.md`. Keep the controlled-field
definitions in every copy: a register whose labels change per client cannot be read reliably by the
next Fellow or playbook.

```markdown
---
style: descriptive
---

# Decisions — {Business} — {the process being automated}

> Canonical current state. The history of a change belongs in `progress-log.md`; detailed automation
> analysis belongs in `spec/automation-approach.md`. Never record secret values here.

**Engagement:** `engagements/{client-slug}/`
**Engagement status:** not-started | running | handed-over | dropped
**Last reviewed:** {YYYY-MM-DD}

`handed-over` requires a current `verification/operational-acceptance.md` with `status: accepted` for
the unchanged Validator-B-passed package. Update this field and `notes.md` together; neither status field
is evidence by itself.

## Field definitions

### Scope

- `engagement-workspace` — the Fellow's fork, engagement files, discovery access and working limits.
- `deliverable-package` — files, data, fixtures and configuration included in the client handoff.
- `deliverable-runtime` — data and systems the installed deliverable may access, store or send.
- `automation-approach` — lifecycle path, runtime, integration, credential design and high-stakes
  controls.

### ID prefixes

- `EW` — **E**ngagement **W**orkspace decisions.
- `DP` — **D**eliverable **P**ackage decisions.
- `DR` — **D**eliverable **R**untime decisions.
- `AA` — **A**utomation **A**pproach decisions.

These prefixes correspond to the controlled `Scope` values above. The canonical workspace glossary is
`library/reference/terminology.md`.

### Status

- `candidate` — may need a decision; relevance has not yet been confirmed.
- `open` — confirmed decision area with no current answer.
- `provisional` — a temporary position is in force while more evidence is collected.
- `agreed` — the current position has been approved.
- `superseded` — no longer current; `Current position` names the replacement decision ID.
- `not-applicable` — considered and confirmed irrelevant to this engagement.

### Required before

- `data-ingest` — before client material enters the fork or engagement workspace.
- `interview` — before the first owner interview begins.
- `build` — before implementation of the deliverable begins.
- `package` — before files are assembled for client delivery.
- `deploy` — before the automation receives live access or runs unattended.
- `handover` — before the owner accepts operation and the engagement closes.
- `none` — no stage gate; retain only while the decision area remains useful.

At a stage gate, `candidate` does not pass: confirm whether it is relevant, then use `not-applicable`
or one of the states for a real decision. `open` blocks. `provisional`, `agreed` and `not-applicable`
pass. `superseded` passes only when it names a live replacement ID.

`Current position`, `Owner`, `Source` and `Revisit trigger` are free text. Use `—` when no answer exists.
`Source` is a file path or named confirmation, not a secret value.

## Register

| ID | Scope | Decision point | Status | Current position | Owner | Source | Required before | Revisit trigger |
|---|---|---|---|---|---|---|---|---|
| EW-001 | engagement-workspace | What client data may enter or leave the workspace, where may it live, may it be Git-tracked and which external discovery processors may receive it? | open | — | — | — | data-ingest | A new data category, source, destination, processor or sensitivity appears |
| EW-002 | engagement-workspace | Which identities may access client systems during the engagement, with what scope and storage mechanism? | open | — | — | — | data-ingest | A connector, identity, permission or owner changes |
| EW-003 | engagement-workspace | Who owns retention, deletion and access revocation for engagement material? | open | — | — | — | data-ingest | Retention terms change or the engagement approaches handover |
| EW-004 | engagement-workspace | Which action classes may run autonomously and which require approval? | open | — | — | — | interview | A new external or consequential action appears |
| EW-005 | engagement-workspace | What are the current time, spend and iteration ceilings, and who may raise them? | open | — | — | — | interview | Scope changes or a ceiling is approached |
| EW-006 | engagement-workspace | Which client systems or connectors are needed for discovery? | candidate | — | — | — | interview | Discovery requires a new source or operation |
| DP-001 | deliverable-package | What data, examples, fixtures, configuration and documentation may the delivered package contain? | candidate | — | — | — | package | Packaging begins or a new artifact is proposed |
| DR-001 | deliverable-runtime | What may the installed deliverable read, store or send, and across which boundaries? | candidate | — | — | — | build | A new runtime data flow or destination appears |
| AA-001 | automation-approach | What is the current lifecycle stage, intended trajectory and evidence required for promotion? | candidate | — | — | — | build | A promotion gate is reached or usage changes materially |
| AA-002 | automation-approach | Where will the automation run, who administers it and what trust boundaries does it cross? | candidate | — | — | — | build | Lifecycle, operator count or data movement changes |
| AA-003 | automation-approach | Which connector, MCP, API, browser or other access method is proportionate? | candidate | — | — | — | build | Required operations or reliability change |
| AA-004 | automation-approach | Which identity will the automation use, with what permissions, storage and revocation design? | candidate | — | — | — | deploy | Access method, ownership or permissions change |
| AA-005 | automation-approach | Which actions are high stakes, and what testing, limits, approval or recovery is proportionate? | candidate | — | — | — | deploy | Impact, detectability or reversibility changes |
```

## Maintenance rules

1. Add a decision area when it could change work; do not wait for an answer before recording the
   question.
2. A purely hypothetical `candidate` with no downstream reference may be removed. Once a row affected
   work or was cited, retain it and use `superseded` or `not-applicable`.
3. Record only credential name, type, owner, purpose, scope and storage mechanism. Never record a key,
   token, password, recovery code or cookie.
4. Update the register and append the reason to `progress-log.md` in the same working session. Never
   rewrite an old progress entry.
5. Keep detailed analysis at its source. A register row states the current position and links to the
   discovery record, specification or automation brief that supports it.
