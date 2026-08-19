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
source-map: verification/handoff-source-map.md
persona-preflight: verification/persona-preflight.md
owner-acceptance: verification/owner-acceptance.md
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
| Source map | `verification/handoff-source-map.md` and hash |
| Persona-preflight record | `verification/persona-preflight.md` and hash |
| Owner-acceptance record | `verification/owner-acceptance.md` and hash |
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

| Handoff Claim ID | Owner-facing location and invisible anchor | Authority | Check | Result |
|---|---|---|---|---|
| HC-001 | | | | |

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
| Source-map pointer and `HC-*` absent from rendered prose | | | | | |
| Page/diagram visual inspection | | n/a | | | |
| Deployment/operations reachability | | | | | |
| Client-visible verification | | | | | |

## Comprehension gates

| Gate | Exact package/output version | Result | Evidence or unresolved questions |
|---|---|---|---|
| Persona preflight and prohibited-context check | | pass / blocked | |
| Real owner comprehension and acceptance | | accepted / rejected | |

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

**Canonical verdict:** the frontmatter `status` field (`pass`, `blocked` or `superseded`). Change it
there only; do not maintain a second verdict in the body.

**Reason:**

**Blocking items:**

**Changes that invalidate this report:** any package byte, owner-facing output, source-map entry,
comprehension record or delivery-boundary decision change; any delivery-file change also invalidates
Validator A.

**Release to operational acceptance or return path:**

A `pass` releases these exact package bytes to client-authorised deployment and the independent-owner
run. It does not itself permit an engagement status change to `handed-over`.

--- COPY ENDS HERE ---
