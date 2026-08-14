---
style: template
role: template
produces: engagements/<client-slug>/verification/handoff-report.md
---

# Handoff Validation Report Template

Copy the block below to `engagements/<client-slug>/verification/handoff-report.md`. Keep this internal
report outside the staged client package and final archive.

--- COPY FROM HERE ---

---
validator: handoff
status: blocked
deliverable-report: verification/deliverable-report.md
deliverable-manifest: verification/deliverable-manifest.tsv
package: ""
package-sha256: ""
run-at: YYYY-MM-DDTHH:MM:SSZ
supersedes: none
---

# Handoff Validation Report

## Run identity

| Field | Value |
|---|---|
| Engagement | |
| Package/version | |
| Validator/operator | |
| Environment | |
| Validator A status | |
| Validator A report/manifest | |
| Output Phraser result | |
| Source map | |
| Persona-preflight record | |
| Owner-acceptance record | |
| Delivery-boundary decision | |

## Validator A integrity

| Check | Expected | Observed | Evidence | Result |
|---|---|---|---|---|
| A verdict | pass | | | |
| Current deliverable manifest | exact match | | | |
| Delivery-file changes since A | none | | | |

## Package inventory

| Staged path | Classification | Authority/source | Client-visible? | Expected? |
|---|---|---|---|---|
| | owner account / delivery / operation / verification command / manifest | | yes | yes |

**Unexpected, hidden, temporary or internal paths:**

## Claim-fidelity checks

| Claim/source-map ID | Owner-facing location | Authority | Check | Result |
|---|---|---|---|---|
| 1 | | | | |

## Boundary and limitation visibility

| Item | Required presentation | Observed presentation | Evidence | Result |
|---|---|---|---|---|
| Human approvals/high-stakes actions | | | | |
| Data and credential boundary | | | | |
| Known defects/limitations | | | | |
| Costs/dependencies/ownership | | | | |

## Rendering and navigation

| Artifact/check | Command or inspection | Exit code | Observed result | Evidence | Result |
|---|---|---:|---|---|---|
| PDF/HTML/SVG rendering | | | | | |
| Links and pointers | | | | | |
| Placeholder/schema scan | | | | | |
| Page/diagram visual inspection | | n/a | | | |
| Deployment/operations reachability | | | | | |
| Client-visible verification | | | | | |

## Comprehension gates

| Gate | Exact package/output version | Result | Evidence or unresolved questions |
|---|---|---|---|
| Persona preflight | | pass / blocked | |
| Real owner acceptance | | accepted / rejected / unclear | |

## Archive safety and integrity

| Check | Command | Exit code | Observed result | Evidence | Result |
|---|---|---:|---|---|---|
| Archive integrity | | | | | |
| Absolute/traversal/duplicate paths | | | | | |
| Symlink policy | | | | | |
| Hidden/residue files | | | | | |
| Extracted-copy open/verify | | | | | |
| Final SHA-256 | | | | | |

## Verdict

**Status:** `pass` / `blocked` / `superseded`

**Reason:**

**Blocking items:**

**Changes that invalidate this report:** any package byte, owner-facing output, source-map entry,
comprehension record or delivery-boundary decision change; any delivery-file change also invalidates
Validator A.

**Status transition or return path:**

--- COPY ENDS HERE ---
