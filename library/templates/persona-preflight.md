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

List every document supplied to the persona, using the exact packaged bytes. Include canonical
deployment, operations, known-defect and client-verification instructions when present. Do not let the
persona search the package or workspace for unlisted context.

| Packaged path | SHA-256 | Why the client reads it | Supplied exactly? |
|---|---|---|---|
| `owner-account.pdf` | | Primary explanation | yes / no |
| `package-manifest.md` | | Package navigation | yes / no |
| `deliverable/deployment.md` | | Canonical deployment instructions | yes / no |
| `deliverable/operations.md` | | Canonical operating instructions | yes / no |

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

**Status:** `pass` / `blocked` / `superseded`

**Reason:**

**Next action:** proceed to real-owner check / return to Output Phraser

Any supplied client-readable or package byte change invalidates this preflight.

--- COPY ENDS HERE ---
