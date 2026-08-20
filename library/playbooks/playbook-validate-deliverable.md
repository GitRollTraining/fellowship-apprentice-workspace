---
style: procedural
role: playbook
status: draft — authored, not yet run on a client engagement
serves: D-04, D-05, D-09
---

# Validate Deliverable (Validator A)

Run this playbook after the implementation and its adversarial review are complete, and before any
owner-facing document or handoff package is treated as final. It answers one question: **does the
candidate deliverable satisfy the signed PRD and technical specification within the agreed operating
boundaries?**

The result is an internal release gate. It is not a client report, and it does not replace owner
acceptance of the current-state process or PRD.

## Principle and limits

The model reasons, code computes, and the system verifies. A Fellow or agent saying “done” is an input
to verification, never evidence of completion. Use model judgement to identify risks and design cases;
use repeatable commands, observable outputs and durable evidence to decide whether those cases passed.

This draft has not been run on a client engagement. Record the first real use before claiming that it
improves delivery quality.

## Inputs and outputs

Paths are relative to `engagements/<client-slug>/`.

| Required input | Why it is required |
|---|---|
| Signed `spec/requirements.md` | Defines the accepted business behaviour and acceptance criteria |
| `spec/specification.md` | Defines components, interfaces, boundaries and verification targets |
| `spec/automation-approach.md` and `decision-register.md` | Define the current technical choices and constraints |
| `deliverable/INDEX.md` and every candidate component | Define exactly what is being validated |
| `deliverable/deployment.md` and `deliverable/operations.md` | Define how the solution is installed, operated, recovered and retired |
| `deliverable/known-defects.md`, if any | Defines disclosed non-blocking limitations |
| Representative fixtures or cases | Make observable behaviour reproducible |
| `library/reference/deliverable-review-checklist.md` | Supplies the reusable design and evidence review surface |

Create or update:

```text
verification/
  deliverable-report.md
  deliverable-manifest.tsv
  evidence/
    commands/
    fixtures/
    observed-results/
```

Start the report from `library/templates/deliverable-validation-report.md`. Evidence may link to a
stable external system when it cannot be stored safely, but the report must say how an authorised
reviewer can retrieve it. Never copy secrets or prohibited client data into evidence.

## Verdicts

Use exactly one verdict:

- `pass`: every in-scope signed requirement has sufficient evidence, and no blocking defect remains;
- `blocked`: a required check failed, could not be run, or lacks sufficient evidence; or
- `superseded`: a newer report explicitly replaces this report.

There is no conditional pass. A non-blocking limitation may coexist with `pass` only when it does not
violate signed scope or a boundary and is recorded in `deliverable/known-defects.md`.

## Procedure

### 1. Freeze and inventory the candidate

Confirm `deliverable/INDEX.md` names every component. Hash every regular file in deterministic path
order and write `deliverable-manifest.tsv` as `sha256<TAB>relative-path`. Do not follow symlinks. A
symlink in the candidate is blocking unless the signed specification explicitly requires it; in that
case, define and record a deterministic manifest representation that includes the link and target text
before validation begins. The example below is only for a regular-file candidate.

For example, from the engagement root, this Python implementation is portable across the macOS and
Linux shells supported by the workspace. It fails on symlinks, tab/newline path names and an empty
candidate instead of allowing a broken pipeline to write a plausible empty manifest:

```bash
DELIVERABLE=deliverable
VERIFICATION=verification
mkdir -p "$VERIFICATION/evidence/commands" \
  "$VERIFICATION/evidence/fixtures" \
  "$VERIFICATION/evidence/observed-results"
python3 - "$DELIVERABLE" "$VERIFICATION/deliverable-manifest.tsv" <<'PY'
import hashlib
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
if not root.is_dir():
    raise SystemExit(f"missing deliverable directory: {root}")

files = []
for path in root.rglob("*"):
    if path.is_symlink():
        raise SystemExit(f"symlink requires an explicit manifest contract: {path}")
    if path.is_file():
        rel = path.relative_to(root).as_posix()
        if "\t" in rel or "\n" in rel:
            raise SystemExit(f"path cannot be represented safely in TSV: {rel!r}")
        files.append((rel, path))

if not files:
    raise SystemExit("deliverable contains no regular files")

rows = []
for rel, path in sorted(files):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    rows.append(f"{digest}\t{rel}\n")
out.write_text("".join(rows), encoding="utf-8")
print(f"wrote {len(rows)} manifest rows to {out}")
PY
```

If this command is not supported by the engagement runtime, choose an equivalent deterministic command
and record the exact command, runtime and exit code. Assert the recorded row count equals the number of
regular candidate files. Do not silently hand-edit the manifest.

### 2. Build the acceptance-evidence matrix

For every signed `AC-*`, record:

| Field | Required content |
|---|---|
| Acceptance criterion | Exact `AC-*` identifier and PRD version |
| Component | File, service, workflow or interface responsible |
| Method | `automated`, `witnessed` or `inspection` |
| Case | Fixture, precondition and action |
| Expected | Observable result from the signed PRD or specification |
| Observed | Result, command exit code and evidence pointer |
| Result | `pass`, `fail` or `not-run` |

Self-report is not a method. A witnessed result names the witness role, date, environment and durable
record. Inspection is sufficient only for properties that cannot reasonably be executed, such as the
presence of a required owner-controlled approval step.

### 3. Run the reusable deliverable review

Apply `library/reference/deliverable-review-checklist.md` to the whole candidate, not only to a
`skill.md`. Record each finding with its exact location, triggering input or state, violated contract,
evidence and severity. This review attacks assumptions and evidence; it does not substitute for the
behavioural tests in the next step.

### 4. Exercise behaviour and failure paths

Select cases proportionate to the signed workflow. At minimum cover, when applicable:

- a normal successful case;
- missing or invalid input;
- a named exception from discovery;
- every human approval or high-stakes action;
- a downstream dependency failure;
- a data, credential or authorisation boundary; and
- a recovery or retry path.

Use representative fixtures that are permitted by the Data & Credential Boundary. Preserve inputs,
commands, observed outputs and exit codes. If a required case cannot safely be executed, mark the report
`blocked`; do not convert inability to test into a pass by inspection.

A pass counts as evidence only when the check meets `library/reference/gate-evidence-standard.md`:
chosen for a failure that would otherwise be invisible, and watched going red on a known-bad input at
least once. Record that input beside the pass.

### 5. Verify deployment and rollback

From an environment that does not depend on the builder's unstated local state, follow
`deliverable/deployment.md`. Verify installation, configuration, start, stop, upgrade or replacement,
rollback and uninstall where each applies. Record prerequisites and any residue left behind.

A risky or state-changing deployment without a credible rollback or recovery path is blocking unless
the signed PRD and technical decision explicitly establish that no rollback is possible and define an
accepted alternative recovery procedure.

### 6. Verify operations and recovery

Follow `deliverable/operations.md` as an operator would. Check health signals, logs, alerts or other
monitoring, routine operation, dependency failure, recovery, credential rotation or revocation, data
retention and escalation. The instructions must be executable by the stated operator without relying
on private knowledge held only by the Fellow.

### 7. Dispose findings and issue the verdict

A finding is blocking when it demonstrates any of the following:

- a signed requirement or acceptance criterion fails or has no evidence;
- a data, credential, authorisation, safety or high-stakes boundary is crossed;
- the deliverable cannot be deployed, operated or recovered as specified;
- an in-scope case cannot be tested safely or reproducibly; or
- a claimed pass is contradicted by observed evidence.

Fix blocking implementation defects, rerun the affected checks, and rerun one case that never
triggered the defect — a fix verified only against the input that reported it is not verified.
If the signed requirement itself is wrong or infeasible, return to the PRD and technical-decision
loop; the Validator may not override it.
Move an accepted non-blocking limitation into `deliverable/known-defects.md`, then confirm the owner-facing
material will expose it before handoff.

Write the verdict only after the evidence matrix and finding disposition are complete. Append the run,
result and next gate to `progress-log.md`.

## Invalidation and disagreement

A `pass` is valid only for the exact manifest and cited source versions. Invalidate and rerun the
affected checks when any of these changes:

- a file in `deliverable/`, including deployment, operations or known-defects instructions;
- the signed PRD, specification or a relevant Decision Register position;
- a fixture, oracle or test command that supported a pass; or
- an external constraint on which the result depended.

When the Fellow and Validator disagree, inspect the evidence and contract rather than negotiating the
verdict. If the checker is wrong, fix the checker, retain a minimal failing fixture that demonstrates the
error, and issue a new report that supersedes the old one. If the requirement is wrong, return it to its
owner. If evidence is missing, the result remains `blocked`.

## Exit gate

Hand the candidate to the Output Phraser only when:

- the latest `deliverable-report.md` says `pass`;
- its manifest matches the current candidate exactly;
- every non-blocking limitation is in `known-defects.md`; and
- `progress-log.md` records the passed report and manifest.

The next playbook may change presentation, not delivery behaviour. Any later change to a delivery file
invalidates this gate.
