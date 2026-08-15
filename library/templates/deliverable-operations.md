---
style: template
role: template
produces: engagements/<client-slug>/deliverable/operations.md
---

# Deliverable Operations Template

Copy the block below to `engagements/<client-slug>/deliverable/operations.md`. This is the canonical
routine-use and recovery authority shipped with the deliverable. Keep implementation rationale in the
specification or automation brief, and keep secret values out of this file.

--- COPY FROM HERE ---

# Operate <delivered system name>

## Ownership and supported use

| Responsibility | Owner/route |
|---|---|
| Routine operation | |
| Result checking | |
| Credentials and access | |
| Maintenance and upgrades | |
| Incident escalation | |

**Supported trigger/input:**

**Expected visible result:**

**Out of scope or stays human:**

## Normal run

1. <Exact starting action or command.>
2. <Inputs and the safe place they come from.>
3. <Human approval point, if any.>
4. <Where the result appears and who checks it.>

## Check the result

| Signal | Right looks like | Wrong or uncertain looks like | Required action |
|---|---|---|---|
| | | | |

## Failure and recovery

| Symptom | Stop/contain first | Diagnose using | Recovery | Escalate when |
|---|---|---|---|---|
| | | | | |

Do not retry an external write, send, payment, deletion or other non-idempotent action unless the
procedure first proves whether the prior attempt took effect.

## Monitoring and records

| What to check | Frequency or trigger | Where | Retention/data boundary | Owner |
|---|---|---|---|---|
| | | | | |

## Credentials and access

| Access | Owner | Stored in | Minimum permissions | Rotate/revoke when | Procedure/route |
|---|---|---|---|---|---|
| | | | | | |

Record locations and ownership only; never place a secret value here.

## Maintenance, cost and change control

| Dependency or task | Owner | Cadence/trigger | Expected cost/limit | Verification after change |
|---|---|---|---|---|
| | | | | |

Any change to delivered behaviour returns through the signed requirement, specification and validation
path. Follow `deployment.md` for upgrade, rollback and removal.

## Retirement

<State how to disable triggers, preserve or delete client data, revoke access, remove installed files
and verify that the workflow no longer runs.>

--- COPY ENDS HERE ---
