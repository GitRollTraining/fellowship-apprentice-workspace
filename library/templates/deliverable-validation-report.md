---
style: template
role: template
produces: engagements/<client-slug>/verification/deliverable-report.md
---

# Deliverable Validation Report Template

Copy the block below to `engagements/<client-slug>/verification/deliverable-report.md`. This is an internal
verification record and must not be included in the client package.

--- COPY FROM HERE ---

---
validator: deliverable
status: blocked
prd-version: ""
specification: spec/specification.md
candidate-manifest: verification/deliverable-manifest.tsv
run-at: YYYY-MM-DDTHH:MM:SSZ
supersedes: none
---

# Deliverable Validation Report

## Run identity

| Field | Value |
|---|---|
| Engagement | |
| Candidate/version | |
| Validator/operator | |
| Environment | |
| Signed PRD | |
| Specification | |
| Automation approach | |
| Decision Register snapshot/date | |
| Manifest SHA-256 | |

## Candidate inventory

`verification/deliverable-manifest.tsv` is the canonical inventory for this run. Format each row as
`sha256<TAB>path-relative-to-deliverable`.

| Component | Responsibility/source | Operator | Included in manifest? |
|---|---|---|---|
| | | | |

## Acceptance-evidence matrix

| AC | Component | Method | Case/fixture | Expected | Observed and evidence | Result |
|---|---|---|---|---|---|---|
| AC-001 | | automated / witnessed / inspection | | | | pass / fail / not-run |

## Review findings

| ID | Severity | Location and trigger | Violated contract | Evidence | Disposition |
|---|---|---|---|---|---|
| 1 | BLOCKING / NON-BLOCKING | | | | |

## Behavioural cases

| Case | Coverage | Command/action | Exit code | Observed result | Evidence | Result |
|---|---|---|---:|---|---|---|
| Normal success | | | | | | |
| Missing/invalid input | | | | | | |
| Named exception | | | | | | |
| Human approval/high-stakes action | | | | | | |
| Dependency failure | | | | | | |
| Data/credential/authorisation boundary | | | | | | |
| Recovery/retry | | | | | | |

## Deployment and rollback

| Check | Command/action | Exit code | Observed result | Evidence | Result |
|---|---|---:|---|---|---|
| Prerequisites | | | | | |
| Clean installation | | | | | |
| Configuration/start/stop | | | | | |
| Upgrade or replacement | | | | | |
| Rollback/recovery | | | | | |
| Uninstall/residue | | | | | |

## Operations and failure recovery

| Check | Operator action | Observable signal | Evidence | Result |
|---|---|---|---|---|
| Normal operation | | | | |
| Monitoring/logging | | | | |
| Dependency failure | | | | |
| Recovery | | | | |
| Credential rotation/revocation | | | | |
| Escalation | | | | |

## Boundary and high-stakes checks

| Boundary/approval | Expected control | Observed control | Evidence | Result |
|---|---|---|---|---|
| | | | | |

## Known limitations

| Limitation | Signed scope still satisfied because | `known-defects.md` pointer | Owner-facing disclosure target |
|---|---|---|---|
| | | | |

## Verdict

**Canonical verdict:** the frontmatter `status` field (`pass`, `blocked` or `superseded`). Change it
there only; do not maintain a second verdict in the body.

**Reason:**

**Blocking items:**

**Changes that invalidate this report:** any candidate-manifest change; cited PRD/specification/decision
change; supporting fixture, oracle or command change; or a changed external constraint named above.

**Next gate or return path:**

--- COPY ENDS HERE ---
