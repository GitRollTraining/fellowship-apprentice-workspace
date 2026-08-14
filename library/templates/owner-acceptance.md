---
style: template
role: template
produces: engagements/<client-slug>/verification/owner-acceptance.md
---

# Owner Acceptance Template

Copy the block below to `engagements/<client-slug>/verification/owner-acceptance.md`. This records the
real owner's comprehension and acceptance against exact candidate bytes. It is internal engagement
evidence, not a document placed in the client package.

--- COPY FROM HERE ---

---
status: pending
package: ""
package-sha256: ""
owner-facing-artifact: ""
owner-facing-sha256: ""
checked-at: YYYY-MM-DDTHH:MM:SSZ
supersedes: none
---

# Owner comprehension and acceptance

## Check identity

| Field | Value |
|---|---|
| Engagement | |
| Owner role | |
| Fellow/facilitator | |
| Route | synchronous read-back / asynchronous written response |
| Durable evidence | recording, returned document, comment or message pointer |
| Persona preflight | path, status and package hash |

## How the check was run

Give the owner the exact candidate owner-facing artifact and package version named above. Without
explaining or completing their answer, ask them to show or tell:

1. what was delivered, what starts it and what result should appear;
2. what it will not do and where a person approves or takes over;
3. how they will tell a correct result from a failure;
4. the first recovery or escalation action;
5. where deployment and normal-operation instructions live; and
6. who owns credentials, maintenance and ongoing cost.

“Does this make sense?” is not a comprehension check. Agreement without a read-back does not pass.

## Owner's result

| Prompt | Owner's answer or demonstrated location | Could answer from package without Fellow help? | Correction/request |
|---|---|---|---|
| Purpose, trigger and result | | yes / no | |
| Limits and human action | | yes / no | |
| Correct result and failure signal | | yes / no | |
| Recovery or escalation | | yes / no | |
| Deployment and operations location | | yes / no | |
| Credentials, maintenance and cost owner | | yes / no | |

## Acceptance

**Status:** `pending` / `accepted` / `rejected` / `superseded`

**Owner's recorded statement or action:**

**Unresolved questions:**

Use `accepted` only when every required answer is available from the package and the owner agrees to
receive and operate within its stated boundaries. A material correction, unanswered operating question
or refusal is `rejected` and returns to Output Phraser. It is not a softer form of acceptance.

Any owner-facing or package byte change invalidates this record and requires a new owner check. A
delivery-file change also invalidates Validator A.

--- COPY ENDS HERE ---
