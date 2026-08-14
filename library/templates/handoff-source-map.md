---
style: template
role: template
produces: engagements/<client-slug>/verification/handoff-source-map.md
---

# Handoff Source Map Template

Copy the block below to `engagements/<client-slug>/verification/handoff-source-map.md`. It is an internal
derivation record and must not be included in the client package.

--- COPY FROM HERE ---

---
map-version: v1
package-version: ""
owner-facing-source: handover/owner-account.md
owner-facing-source-sha256: ""
rendered-output: handover/owner-account.pdf
rendered-output-sha256: ""
deliverable-manifest: verification/deliverable-manifest.tsv
created-at: YYYY-MM-DDTHH:MM:SSZ
supersedes: none
---

# Handoff source map

## Authority snapshot

| Authority | Exact version/date | Hash or durable pointer |
|---|---|---|
| Confirmed current-state process | | |
| Discovery record | | |
| Signed PRD | | |
| Specification | | |
| Validator A report | | |
| Deliverable manifest | | |
| Decision Register | | |
| Known defects, if any | | |

## Claim map

Use `HC-001` onward. An output locator is a heading plus a short exact phrase, HTML element ID or SVG
element ID — enough to find the claim after nearby prose changes.

| Claim ID | Owner-facing artifact and locator | Claim in plain words | Authority | Exact source pointer | Transformation and limits |
|---|---|---|---|---|---|
| HC-001 | `handover/owner-account.md` — `## What it does`, “…” | | | | direct / paraphrase / calculated / inferred; state any limit |

## Invisible pointers

| Artifact | Map pointer present? | Claim anchors present? | Confirmed absent from rendered prose? |
|---|---|---|---|
| | yes / no | yes / no | yes / no |

Expected pointer in markdown, HTML or SVG authoring source:

```html
<!-- handoff-source-map: ../verification/handoff-source-map.md -->
```

Expected material-claim anchor:

```html
<!-- claim: HC-001 -->
```

## Render and package chain

| Stage | Path | SHA-256 | Produced by / command | Exit code or inspection result |
|---|---|---|---|---|
| Authoring source | | | | |
| Rendered owner-facing output | | | | |
| Candidate package | | | | |

## Completion

- [ ] Every material capability, limitation, approval, failure, recovery, ownership, dependency and cost
  claim has a row.
- [ ] Every source pointer resolves to the recorded authority version.
- [ ] Calculations and inferences are marked; no inference is presented as an owner statement.
- [ ] Every material output block has an invisible `HC-*` anchor.
- [ ] The source-map pointer and anchors are absent from rendered prose.
- [ ] Source and rendered hashes match the candidate package inputs.

--- COPY ENDS HERE ---
