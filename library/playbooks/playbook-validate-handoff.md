---
style: procedural
role: playbook
status: draft — authored, not yet run on a client engagement
serves: D-04, D-05, D-09
---

# Validate Handoff (Validator B)

Run this playbook after the Output Phraser has assembled the owner-facing material, the mandatory
persona preflight has passed, and the real owner has accepted the explanation. It answers a different
question from Validator A: **is the final handoff package a faithful, comprehensible and safe rendering
of the already-validated deliverable?**

Validator B does not re-implement or routinely rerun Validator A. It verifies that A's passed candidate
is unchanged and then validates the presentation and package boundary.

The artifact contracts now exist, but this playbook has not been run on a Fellow or client handoff. Do
not treat a complete procedure as evidence that it catches the failures a real owner will expose.

## Inputs and output

Paths are relative to `engagements/<client-slug>/`.

| Required input | Why it is required |
|---|---|
| Passed `verification/deliverable-report.md` | Establishes the behavioural gate |
| `verification/deliverable-manifest.tsv` | Pins the exact delivery files Validator A passed |
| Current `deliverable/` | Supplies the package's operational contents |
| Owner-facing output and `handover/package-manifest.md` | Supply the explanation and navigation the owner accepted |
| `verification/handoff-source-map.md` | Links every material `HC-*` claim to its authority and render chain |
| Passed `verification/persona-preflight.md` | Shows the package was tested under the constrained reader context |
| Accepted `verification/owner-acceptance.md` | Establishes the hard real-owner gate against exact bytes |
| `handover/<client>-handover-v<n>.zip` by default | The exact archive or package that will be sent |
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
Compare the packaged `deliverable/` paths and hashes with Validator A's manifest after removing only the
package-root and `deliverable/` path prefixes. A complete match is required; “equivalent content” is not
the same candidate.

### 3. Verify claim fidelity and limitation visibility

Use `verification/handoff-source-map.md` to trace every material `HC-*` owner-facing claim to the signed PRD, confirmed
process, validated deliverable, known-defects file or another named authority. Check especially:

- what the solution does and does not do;
- required human approvals and high-stakes boundaries;
- inputs, outputs and failure behaviour;
- operating assumptions, costs and dependencies; and
- known defects and accepted limitations.

The Output Phraser may simplify language and presentation. It may not introduce a capability, guarantee,
number, obligation or workaround that is absent from the source chain. An untraceable material claim is
blocking.

Confirm every material source block has an invisible claim anchor and the authoring source has an
invisible map pointer. Confirm the recorded source, rendered-output and package hashes match current
bytes. The pointer is trace infrastructure, not a substitute for checking each row.

### 4. Verify usability and rendering

Run the applicable deterministic renderers, link checkers, schema checks and client verification command.
Record each command, runtime, exit code and output. Then visually inspect every rendered page, chart and
diagram for clipping, overlap, unreadable text, missing glyphs, broken hierarchy and placeholder content.

Confirm deployment and operations instructions are present and reachable from the owner-facing account.
When a proportionate client-verification command exists, confirm it is also present and reachable; when
it does not, confirm the owner account states why one is impractical. Visual inspection supplements
deterministic checks; it never replaces them. Search rendered text for `handoff-source-map` and `HC-*`;
either appearing to the owner is blocking.

### 5. Verify comprehension evidence

Confirm `verification/persona-preflight.md` says `pass` against the exact package hash and that every
client-readable input named in the report matches its packaged hash. Confirm its prohibited-context
table is clean. Confirm `verification/owner-acceptance.md` says `accepted` and names the same package and
primary owner-facing hashes, with durable evidence and no unresolved operating question.

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
ARCHIVE=handover/<client>-handover-v<n>.zip
EXPECTED_ROOT=<client>-handover-v<n>
unzip -t "$ARCHIVE" || exit 1
python3 - "$ARCHIVE" "$EXPECTED_ROOT" <<'PY' || exit 1
import re
import stat
import sys
import zipfile

archive, expected_root = sys.argv[1:]
if not expected_root or "/" in expected_root or "\\" in expected_root:
    raise SystemExit("unsafe expected package root")

seen = set()
seen_folded = {}
file_count = 0
with zipfile.ZipFile(archive) as package:
    for entry in package.infolist():
        raw = entry.filename
        path = raw[:-1] if raw.endswith("/") else raw
        if not path or "\\" in raw or raw.startswith(("/", "//")) or re.match(r"^[A-Za-z]:", raw):
            raise SystemExit(f"unsafe archive path: {raw!r}")
        parts = path.split("/")
        if any(part in ("", ".", "..") for part in parts):
            raise SystemExit(f"non-canonical archive path: {raw!r}")
        if parts[0] != expected_root:
            raise SystemExit(f"path outside expected package root: {raw!r}")
        if len(parts) == 1 and not entry.is_dir():
            raise SystemExit(f"package root is a file, not a directory: {raw!r}")
        if any(part.startswith(".") or part in {"__MACOSX", "Thumbs.db", "desktop.ini"} for part in parts):
            raise SystemExit(f"hidden or operating-system residue: {raw!r}")
        if path in seen:
            raise SystemExit(f"duplicate archive path: {raw!r}")
        folded = path.casefold()
        if folded in seen_folded:
            raise SystemExit(f"case-colliding archive paths: {seen_folded[folded]!r}, {raw!r}")
        mode = entry.external_attr >> 16
        file_type = stat.S_IFMT(mode)
        if stat.S_ISLNK(mode):
            raise SystemExit(f"symlink in archive: {raw!r}")
        if file_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
            raise SystemExit(f"special file in archive: {raw!r}")
        if not entry.is_dir() and file_type == stat.S_IFDIR:
            raise SystemExit(f"directory metadata on file entry: {raw!r}")
        seen.add(path)
        seen_folded[folded] = raw
        if not entry.is_dir():
            file_count += 1
if file_count == 0:
    raise SystemExit("archive contains no files")
print(f"CLEAN: {file_count} files under {expected_root}/")
PY
shasum -a 256 "$ARCHIVE" || exit 1
```

This check is fail-closed: a path-policy finding exits non-zero before extraction. Record the exact
final archive hash in the report. Extract only after the integrity and path checks pass, into a fresh
directory whose location is permitted by the Data & Credential Boundary. Clean it on success or
failure; use a sentinel so cleanup cannot target an unrelated directory. For example:

```bash
# Set VALIDATION_TMP_PARENT to an approved directory when the system temp area is not permitted.
if [[ -n "${VALIDATION_TMP_PARENT:-}" ]]; then
  mkdir -p "$VALIDATION_TMP_PARENT" || exit 1
  EXTRACT="$(mktemp -d "$VALIDATION_TMP_PARENT/handoff-check.XXXXXX")" || exit 1
else
  EXTRACT="$(mktemp -d)" || exit 1
fi
: > "$EXTRACT/.validator-b-owned" || {
  rmdir -- "$EXTRACT" 2>/dev/null || true
  exit 1
}
cleanup_extract() {
  if [[ -n "${EXTRACT:-}" && -f "$EXTRACT/.validator-b-owned" ]]; then
    rm -rf -- "$EXTRACT"
  else
    printf 'refusing to clean unowned extraction path: %s\n' "${EXTRACT:-<unset>}" >&2
    return 1
  fi
}
on_extract_signal() {
  cleanup_extract || true
  trap - EXIT HUP INT TERM
  exit 130
}
trap cleanup_extract EXIT
trap on_extract_signal HUP INT TERM
if unzip -q "$ARCHIVE" -d "$EXTRACT"; then
  :
else
  EXTRACT_STATUS=$?
  cleanup_extract || true
  trap - EXIT HUP INT TERM
  exit "$EXTRACT_STATUS"
fi
run_client_checks() {
  # Replace this fail-closed sentinel with the selected deterministic open, render or verification
  # commands, rooted at "$EXTRACT/$EXPECTED_ROOT". Leaving it unchanged must not produce a pass.
  false
}
if run_client_checks; then
  cleanup_extract || { trap - EXIT HUP INT TERM; exit 1; }
  trap - EXIT HUP INT TERM
else
  CLIENT_CHECK_STATUS=$?
  cleanup_extract || true
  trap - EXIT HUP INT TERM
  exit "$CLIENT_CHECK_STATUS"
fi
```

### 7. Issue the verdict and return to the orchestrator

Write the report against the final package hash. Append the run and disposition to `progress-log.md`.
Return the verdict to Discovery to Deliverable. Validator B does not change engagement status itself;
this report says only whether the unchanged package is release-ready for client deployment and an
independent owner run. Discovery to Deliverable may mark `handed-over` only after a later
`verification/operational-acceptance.md` says `accepted` for the same package and B-report hashes. A
rejection or later invalidation returns to the owning stage and leaves the engagement running.

## Invalidation and disagreement

Invalidate B when any package byte, owner-facing output, source-map entry, comprehension record or
delivery-boundary decision changes. A delivery-file change invalidates both A and B. A presentation-only
change invalidates B and normally the persona and owner checks, but not A while the delivery manifest is
unchanged. Invalidating or superseding B also invalidates any operational acceptance tied to its report
hash. If the engagement had already been marked `handed-over`, supersede that acceptance and return both
`notes.md` and the Decision Register to `running` before distributing changed bytes.

Resolve disagreement by comparing the package, source chain and recorded acceptance. If a checker is
wrong, repair it, retain a minimal failing fixture and issue a superseding report. If a material claim
cannot be traced or the owner's acceptance is ambiguous, the verdict remains `blocked`.

## Information the client receives

Do not place `verification/handoff-report.md`, the Validator A report or internal evidence in the package.
The client receives the owner-facing account, the agreed delivery components, canonical deployment and
operations instructions, visible known limitations, and a client-runnable smoke or health check when
practical. Internal quality evidence remains available for authorised review without becoming part of
the operating deliverable.
