---
style: template
role: template
produces: engagements/<client-slug>/verification/operational-acceptance.md
---

# Operational Acceptance Template

Copy the block below to `engagements/<client-slug>/verification/operational-acceptance.md`. Complete it
only after Validator B passes. It records client-authorised deployment in the intended environment and
one safe representative run by the owner without the Fellow operating the deliverable for them.

This is internal engagement evidence. Do not place it in the client package. Validator B makes a
package release-ready; this record is the final evidence required before status becomes `handed-over`.

--- COPY FROM HERE ---

---
status: pending
package: ""
package-sha256: ""
handoff-report: verification/handoff-report.md
handoff-report-sha256: ""
deployment-environment: ""
checked-at: YYYY-MM-DDTHH:MM:SSZ
supersedes: none
---

# Operational acceptance

## Acceptance identity

| Field | Value |
|---|---|
| Engagement | |
| Package/version and SHA-256 | |
| Validator B report, status and SHA-256 | |
| Intended client runtime/environment | |
| Deployment operator and authority | |
| Owner/routine operator | |
| Fellow/facilitator | |
| Durable evidence pointer | |

## Client-authorised deployment

Follow the packaged `deliverable/deployment.md` without changing package bytes. Never record secret
values here.

| Check | Expected | Observed | Operator/evidence | Result |
|---|---|---|---|---|
| Package hash before deployment | Matches Validator B | | | pass / rejected |
| Prerequisites and permissions | As documented | | | pass / rejected |
| Install/configure/start | Instructions are complete and executable | | | pass / rejected |
| Post-install verification | Expected safe signal appears | | | pass / rejected |
| Rollback or safe-stop route | Owner can locate and explain it | | | pass / rejected |

## Independent owner run

The owner performs one safe representative case from the packaged instructions. The Fellow may observe
and ask the recorded prompts, but must not take over the operating steps or supply a missing instruction.

| Check | Owner action or answer | Expected result | Observed result/evidence | Result |
|---|---|---|---|---|
| Start one supported case | | | | pass / rejected |
| Identify the visible success/failure signal | | | | pass / rejected |
| Take or name the first recovery/escalation action | | | | pass / rejected |
| Locate credentials/maintenance ownership | | | | pass / rejected |

## Disposition

**Canonical verdict:** the frontmatter `status` field (`pending`, `accepted`, `rejected` or
`superseded`). Change it there only; do not maintain a second status in the body.

**Owner's recorded acceptance or rejection:**

**Unresolved operating issue:**

**Return path if rejected:**

- A delivery-file or canonical-instruction defect returns to Build and Validator A, then repeats every
  later gate.
- An owner-facing/package-only defect returns to Output Phraser and repeats the affected comprehension
  gates and Validator B.
- A client-environment or authorisation constraint returns to the owning PRD, automation or deployment
  decision before another attempt.

Use `accepted` only when the unchanged B-passed package was deployed in the intended environment and
the owner completed the representative run without Fellow intervention. A package-byte change or a
change to the cited B report invalidates this acceptance and requires a new Validator B report; do not
repair the archive during this check.

--- COPY ENDS HERE ---
