---
style: procedural
role: playbook
status: draft — authored, blocked on the Output Phraser artifacts
serves: D-04, D-05, D-09
---

# Validate Handoff (Validator B)

Run this playbook after the Output Phraser has assembled the owner-facing material, the mandatory
persona preflight has passed, and the real owner has accepted the explanation. It answers a different
question from Validator A: **is the final handoff package a faithful, comprehensible and safe rendering
of the already-validated deliverable?**

Validator B does not re-implement or routinely rerun Validator A. It verifies that A's passed candidate
is unchanged and then validates the presentation and package boundary.

This draft cannot run end to end until the Output Phraser, source map and comprehension artifacts are
defined. Those missing inputs are explicit dependencies, not permission to omit the gate.

## Inputs and output

Paths are relative to `engagements/<client-slug>/`.

| Required input | Why it is required |
|---|---|
| Passed `verification/deliverable-report.md` | Establishes the behavioural gate |
| `verification/deliverable-manifest.tsv` | Pins the exact delivery files Validator A passed |
| Current `deliverable/` | Supplies the package's operational contents |
| Owner-facing outputs under `handover/` | Supplies the explanation the owner accepted |
| Handoff source map | Links material owner-facing claims to their authoritative sources |
| Passed persona-preflight record | Shows the package was tested from the intended reader's perspective |
| Real-owner acceptance record | Establishes the hard comprehension and acceptance gate |
| Final staged package | The exact archive or package that will be sent |
| Current `DP-*` delivery-boundary decision | Defines what may leave the workspace |

Create `verification/handoff-report.md` from
`library/templates/handoff-validation-report.md`. Keep it outside the staged package.

The default package is a versioned zip. If the signed specification selects another format, preserve
the same inventory, path-safety, integrity and reproducibility checks for that format.

## Verdicts

Use exactly one verdict:

- `pass`: the staged package matches the A-passed candidate, contains exactly the authorised owner-facing
  material, renders correctly and has recorded owner acceptance;
- `blocked`: any required check fails, cannot be run or lacks evidence; or
- `superseded`: a newer report explicitly replaces this report.

There is no conditional pass.

## Procedure

### 1. Re-establish Validator A integrity

Confirm the A report says `pass`. Recompute the current deliverable manifest with Validator A's recorded
command and compare it byte-for-byte with `verification/deliverable-manifest.tsv`.

If any hash or path differs, stop. Return to Validator A; do not decide that a delivery change was “only
wording.” Validator B may avoid rerunning behavioural cases only while the A-passed bytes are unchanged.

### 2. Freeze the package inventory

List every staged path and classify it as:

- owner-facing account;
- delivery component;
- deployment, operations, known-defect or client-verification instruction; or
- package manifest.

Reject any unclassified path. The package must not contain internal verification reports or evidence,
interview records, hidden files, editor residue, caches, temporary files, source-control metadata or
unauthorised client data. Reject symlinks unless the delivery specification explicitly requires and
constrains them.

`deliverable/deployment.md` and `deliverable/operations.md` remain canonical delivery files. Handover
material may summarise or point to them, but must not maintain a second conflicting set of instructions.

### 3. Verify claim fidelity and limitation visibility

Use the handoff source map to trace every material owner-facing claim to the signed PRD, confirmed
process, validated deliverable, known-defects file or another named authority. Check especially:

- what the solution does and does not do;
- required human approvals and high-stakes boundaries;
- inputs, outputs and failure behaviour;
- operating assumptions, costs and dependencies; and
- known defects and accepted limitations.

The Output Phraser may simplify language and presentation. It may not introduce a capability, guarantee,
number, obligation or workaround that is absent from the source chain. An untraceable material claim is
blocking.

### 4. Verify usability and rendering

Run the applicable deterministic renderers, link checkers, schema checks and client verification command.
Record each command, runtime, exit code and output. Then visually inspect every rendered page, chart and
diagram for clipping, overlap, unreadable text, missing glyphs, broken hierarchy and placeholder content.

Confirm deployment, operations and client-verification instructions are present and reachable from the
owner-facing account. Visual inspection supplements deterministic checks; it never replaces them.

### 5. Verify comprehension evidence

Confirm the mandatory persona preflight passed against the exact owner-facing bytes in the staged package.
Confirm the real owner acceptance record names the same version and records unresolved questions or
rejection, if any.

Owner acceptance is a hard status gate. If the owner cannot explain the operating boundary, does not
accept the package or requests a material correction, return to the Output Phraser. The engagement remains
running. A change to owner-facing content requires the relevant preflight and owner confirmation to be
repeated; a change to a delivery file also returns to Validator A.

### 6. Verify archive safety and integrity

For a zip package, run a non-extracting integrity check and inspect the path list before extracting into a
new temporary directory. At minimum reject:

- absolute paths;
- `..` traversal segments;
- paths outside the intended package root;
- unexpected duplicate or case-colliding paths; and
- hidden operating-system residue such as `__MACOSX/` or `.DS_Store`.

For example:

```sh
unzip -t <client>-handover-v<n>.zip
zipinfo -1 <client>-handover-v<n>.zip
shasum -a 256 <client>-handover-v<n>.zip
```

Record the exact final archive hash in the report. Extract only after the path list passes, then rerun
the client-visible open, render or verification path from the extracted copy.

### 7. Issue the verdict and update status

Write the report against the final package hash. Append the run and disposition to `progress-log.md`.
Mark the engagement `handed-over` only when Validator B says `pass` and the owner acceptance record still
applies to the package version. A rejection or later invalidation returns the work to the owning stage
and leaves the engagement running.

## Invalidation and disagreement

Invalidate B when any package byte, owner-facing output, source-map entry, comprehension record or
delivery-boundary decision changes. A delivery-file change invalidates both A and B. A presentation-only
change invalidates B and normally the persona and owner checks, but not A while the delivery manifest is
unchanged.

Resolve disagreement by comparing the package, source chain and recorded acceptance. If a checker is
wrong, repair it, retain a minimal failing fixture and issue a superseding report. If a material claim
cannot be traced or the owner's acceptance is ambiguous, the verdict remains `blocked`.

## Information the client receives

Do not place `verification/handoff-report.md`, the Validator A report or internal evidence in the package.
The client receives the owner-facing account, the agreed delivery components, canonical deployment and
operations instructions, visible known limitations, and a client-runnable smoke or health check when
practical. Internal quality evidence remains available for authorised review without becoming part of
the operating deliverable.
