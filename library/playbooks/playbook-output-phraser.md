---
style: procedural
role: playbook
status: draft — authored, not yet run on a client engagement
serves: D-05, D-29
---

# Output Phraser

Run this playbook only after Validator A has passed the exact candidate deliverable. It turns that
validated candidate and its source chain into owner-facing material and a candidate handoff package a
non-technical reader can understand and judge.

The Output Phraser changes presentation, not behaviour. It issues no release verdict, does not approve
its own claims and does not mark the engagement `handed-over`. Discovery to Deliverable invokes the
persona, real owner, Validator B and operational acceptance after this playbook returns its candidate
package.

## What this playbook does not claim

This procedure has not been run on a Fellow or client engagement. Readability is not correctness, a
persona is not the owner, and a clean render is not an accepted handoff. The separate gates exist so
none of those can silently stand in for another.

This playbook does not concatenate the implementation into the owner account. A delivery may contain
multiple skills, scripts, integrations or services whose installable structure matters. Flattening
those files into a PDF destroys that structure, risks omissions and creates a stale second copy. The
owner account explains; the exact Validator-A-passed `deliverable/` tree travels beside it.

## Entry gate and inputs

Paths are relative to `engagements/<client-slug>/`.

Do not begin unless all of these are available and current:

| Input | Authority it supplies |
|---|---|
| `verification/deliverable-report.md` with `status: pass` | Behavioural release gate |
| `verification/deliverable-manifest.tsv` | Exact delivery bytes that passed |
| Confirmed current-state process and `interview/discovery-record.md` | Owner vocabulary, real instances and present process |
| Signed `spec/requirements.md` | Accepted future behaviour, scope and observable result |
| `spec/specification.md` and current Decision Register | Delivery shape, interfaces and package boundary |
| `deliverable/` | Exact client-operated implementation and canonical instructions |
| `deliverable/known-defects.md`, if present | Limitations that must remain visible |
| Applicable `DP-*` position | What the package may contain and send |

Recompute the deliverable manifest using Validator A's recorded command. Any mismatch returns to
Validator A. Do not phrase a candidate whose evidence has already been invalidated.

## Outputs

Create or update:

```text
handover/
  owner-account.md OR owner-account.html
  owner-account.pdf                    # when the markdown route is selected
  package-manifest.md
  <client>-handover-v<n>.zip           # default transport
verification/
  handoff-source-map.md
```

Start the owner account and package manifest from `library/templates/handover.md` and
`library/templates/handoff-package-manifest.md`. Start the source map from
`library/templates/handoff-source-map.md`.

The authoring source remains in the engagement. The default client zip contains only the rendered
owner account, `package-manifest.md` and the exact `deliverable/` tree. It never contains the source
map, validation reports, evidence, interview files, PRD, specification, Decision Register or progress
log.

## Procedure

### 1. Freeze the phrasing basis

Record the A report, delivery-manifest hash, signed PRD version, confirmed-process version, relevant
Decision Register review date and package version in `verification/handoff-source-map.md`.

List every material claim the owner-facing output must make before writing prose:

- what starts the automation and what finished result it produces;
- what it does not do and which cases stay human;
- human approvals and high-stakes boundaries;
- what the owner checks, including visible failure signals;
- what to do when a dependency or run fails;
- who owns installation, routine operation, credentials and maintenance;
- ongoing dependencies or costs; and
- every accepted limitation or known defect.

Give each claim an `HC-*` identifier and map it to an authoritative file and precise source pointer.
One source may support several claims; one claim may require several sources. A missing source blocks
phrasing. Do not fill the gap with plausible model knowledge.

### 2. Choose one owner-facing format

Use the explanation register through `library/skills/explain/` for all routes. Then choose one authoring
source:

| Route | Use when | Existing capability |
|---|---|---|
| Markdown to formal PDF | The account is mainly prose and tables or will be printed | `library/templates/handover.md` and `library/renderers/` |
| Single-file HTML, optionally printed to PDF | A short account genuinely needs status, hierarchy or an embedded diagram | `library/templates/brief-design/` |

Do not maintain equivalent markdown and HTML sources. A second source is a drift surface, not a backup.

Use `library/skills/flowchart/` for a future-state operating or recovery diagram when sequence,
branching, handoff or a loop materially affects what the owner must do. Do not add a diagram merely to
decorate parallel facts. The current-state confirmation diagram is owned by the Interview runbook and
is not recreated here unless the final account needs to contrast current and future states explicitly.

### 3. Write for judgement, not reassurance

Use the owner's words and one real instance from confirmed discovery. The account must let the owner,
without the Fellow beside them:

- say what the delivered system does and does not do;
- identify when a human must decide or approve;
- start at the correct deployment or operating instruction;
- tell a correct result from a failure;
- take or escalate the first recovery action; and
- identify who owns credentials, maintenance and ongoing cost.

Summarise canonical `deliverable/deployment.md` and `deliverable/operations.md` only enough to route the
reader. Link or point to the exact files. Do not copy a second full install or recovery procedure into
the owner account.

Expose every known limitation in language the owner can act on. “See known defects” without saying
what the limitation changes is not disclosure.

### 4. Attach the invisible trace layer

Immediately after frontmatter in markdown, or near the beginning of HTML/SVG source, include:

```html
<!-- handoff-source-map: ../verification/handoff-source-map.md -->
```

Place an invisible claim anchor before each material block, for example:

```html
<!-- claim: HC-001 -->
```

Continue one unique `HC-*` sequence across the owner account and `handover/package-manifest.md`; both
authoring files carry the invisible map pointer and anchors. The identifiers are for internal
traceability and must not appear in rendered prose. If the final format cannot carry comments safely,
keep the pointer and anchors in its authoring source. Record the source hash and rendered-output hash in
the source map; never hand-edit a PDF to add metadata.

### 5. Render and inspect the owner-facing output

For markdown, follow `library/renderers/make-the-handover-file.md`: build the owner account alone, run
the deterministic PDF checker and inspect every page. For HTML, run the brief-design pre-send checks,
open it in a browser and inspect both screen and print output.

For every route:

- scan for placeholders, internal codes rendered as prose and broken links;
- confirm the source-map pointer and claim anchors do not render;
- inspect diagrams rather than trusting clean SVG markup; and
- record commands, exit codes and rendered hashes in the source map or progress log.

A render failure returns to the authoring source. It does not change the validated deliverable.

### 6. Write the client package manifest

`handover/package-manifest.md` is a plain-language start-here inventory. It names the package version,
the owner account, every top-level delivery component, canonical deployment and operations files,
known limitations and the client-runnable smoke or health check when one exists.

Do not render or display internal hashes, `HC-*` identifiers or verification findings in this file.
Its source does retain the required invisible map pointer and claim anchors. It helps the owner navigate
the package; Validator B holds the integrity evidence.

### 7. Assemble the default candidate zip

Resolve package contents against the current `DP-*` decision before copying anything. Use a fresh
temporary staging directory and fail if the versioned archive already exists. Before running the
example, resolve the staging location against `EW-001` and `EW-003`; use an approved ignored directory
instead of the operating-system temp area when those decisions require it. From the repository root,
adapt this example only for the selected owner-account extension:

```bash
CLIENT=<client-slug>
VERSION=v<n>
ENGAGEMENT="engagements/$CLIENT"
PACKAGE_ROOT="$CLIENT-handover-$VERSION"
ARCHIVE="$ENGAGEMENT/handover/$PACKAGE_ROOT.zip"
REPO_ROOT="$(pwd -P)"

test ! -e "$ARCHIVE" || { printf 'archive already exists: %s\n' "$ARCHIVE" >&2; exit 1; }
# Set PHRASER_TMP_PARENT to an approved directory when the system temp area is not permitted.
if [[ -n "${PHRASER_TMP_PARENT:-}" ]]; then
  mkdir -p "$PHRASER_TMP_PARENT" || exit 1
  STAGE="$(mktemp -d "$PHRASER_TMP_PARENT/output-phraser.XXXXXX")" || exit 1
else
  STAGE="$(mktemp -d)" || exit 1
fi
: > "$STAGE/.output-phraser-owned" || {
  rmdir -- "$STAGE" 2>/dev/null || true
  exit 1
}
cleanup_stage() {
  if [[ -n "${STAGE:-}" && -f "$STAGE/.output-phraser-owned" ]]; then
    rm -rf -- "$STAGE"
  else
    printf 'refusing to clean unowned staging path: %s\n' "${STAGE:-<unset>}" >&2
    return 1
  fi
}
on_stage_signal() {
  rm -f -- "$ARCHIVE"
  cleanup_stage || true
  trap - EXIT HUP INT TERM
  exit 130
}
trap cleanup_stage EXIT HUP INT TERM
trap on_stage_signal HUP INT TERM
build_archive() {
  mkdir -p "$STAGE/$PACKAGE_ROOT/deliverable" &&
    cp "$ENGAGEMENT/handover/owner-account.pdf" "$STAGE/$PACKAGE_ROOT/" &&
    cp "$ENGAGEMENT/handover/package-manifest.md" "$STAGE/$PACKAGE_ROOT/" &&
    cp -R "$ENGAGEMENT/deliverable/." "$STAGE/$PACKAGE_ROOT/deliverable/" &&
    (cd "$STAGE" && zip -X -r "$REPO_ROOT/$ARCHIVE" "$PACKAGE_ROOT")
}
if build_archive; then
  cleanup_stage || { trap - EXIT HUP INT TERM; exit 1; }
  trap - EXIT HUP INT TERM
else
  BUILD_STATUS=$?
  rm -f -- "$ARCHIVE"
  cleanup_stage || true
  trap - EXIT HUP INT TERM
  exit "$BUILD_STATUS"
fi
```

The owned staging directory is removed on success, interruption or command failure; leftover staged
client bytes are blocking and must be removed through the recorded retention route. The archive is not
approved merely because `zip` exited zero.
Discovery to Deliverable next runs the persona and real-owner checks against this exact version, then
hands the unchanged archive to Validator B.

## Exit contract

Return control to Discovery to Deliverable only when:

- the current delivery manifest still matches Validator A;
- every material owner-facing claim has an `HC-*` source-map row and invisible anchor;
- one owner-facing source rendered and passed its applicable deterministic and visual checks;
- the package manifest matches the candidate archive contents;
- the archive contains the exact `deliverable/` tree and no internal verification material; and
- `progress-log.md` records the candidate version, source/output hashes and next gate.

This exit means **ready for comprehension testing**, not passed and not handed over.

## Stop and return

Stop rather than phrase around the problem when:

- Validator A or its manifest is no longer current;
- a material claim has no authoritative source;
- making the account understandable would require changing behaviour or a signed limitation;
- the package boundary is open, provisional beyond its gate or contradicted by the requested content;
- canonical deployment or operations instructions are missing; or
- packaging would include a secret, disallowed client data or internal engagement evidence.
