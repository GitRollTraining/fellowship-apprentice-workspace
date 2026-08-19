---
style: template
role: template
produces: engagements/<client-slug>/verification/persona-preflight.md
---

# Persona Preflight Template

Copy the block below to `engagements/<client-slug>/verification/persona-preflight.md`. This is internal
evidence and must not be included in the client package.

--- COPY FROM HERE ---

---
persona: library/personas/non-technical-owner.md
status: blocked
package: ""
package-sha256: ""
primary-owner-facing-artifact: ""
primary-owner-facing-sha256: ""
run-at: YYYY-MM-DDTHH:MM:SSZ
supersedes: none
---

# Non-technical owner preflight

## Run identity

| Field | Value |
|---|---|
| Engagement | |
| Package/version | |
| Fresh agent/context identifier | |
| Persona file SHA-256 | |
| Runner | |

## Client-readable inputs

List every document supplied to the persona. Pin the exact packaged bytes, then supply only the
client-visible view produced by the intended renderer/application. Include canonical deployment,
operations, known-defect and client-verification instructions when present. Do not expose invisible
comments/claim anchors or let the persona search the package or workspace for unlisted context.

| Packaged path | Packaged SHA-256 | Client-view render/export method | Supplied-view SHA-256 | Why the client reads it |
|---|---|---|---|---|
| `owner-account.pdf` | | direct PDF view | | Primary explanation |
| `package-manifest.md` | | intended Markdown renderer; comments invisible | | Package navigation |
| `deliverable/deployment.md` | | intended Markdown renderer | | Canonical deployment instructions |
| `deliverable/operations.md` | | intended Markdown renderer | | Canonical operating instructions |

## Allowed prior knowledge

Only direct owner statements and owner corrections belong here. Do not include Fellow conclusions,
requirements, specification content, implementation facts or validation results.

| Heard ID or correction | Owner's words supplied to the persona | Durable session/confirmation pointer |
|---|---|---|
| H1 | | |

## Prohibited-context check

| Material | Supplied to persona? | Result |
|---|---|---|
| Fellow conclusions (`C*`) | no | pass / blocked |
| PRD, automation approach or specification | no | pass / blocked |
| Unpresented implementation source, configuration or internal technical context | no | pass / blocked |
| Source map or Validator reports | no | pass / blocked |
| Previous preflight or owner answers | no | pass / blocked |

## Cold-reader answers

| Question | Persona answer | Supporting owner-facing passage | Answerable without guessing? |
|---|---|---|---|
| What was delivered, what starts it and what result appears? | | | yes / no |
| Walk one real instance | | | yes / no |
| What will it not do; where does a person act? | | | yes / no |
| What shows success or failure? | | | yes / no |
| First recovery or escalation action | | | yes / no |
| Where to start; who owns credentials, maintenance and cost? | | | yes / no |

## Unanswerable or ambiguous material

| Owner-facing location | Word, pointer or missing instruction | Consequence for operation/check/recovery | Required repair |
|---|---|---|---|
| | | | |

## Verdict

**Canonical verdict:** the frontmatter `status` field (`pass`, `blocked` or `superseded`). Change it
there only; do not maintain a second verdict in the body.

**Reason:**

**Next action:** proceed to real-owner check / return to Output Phraser

Any packaged byte, render/export method or supplied client-visible view change invalidates this
preflight.

--- COPY ENDS HERE ---
