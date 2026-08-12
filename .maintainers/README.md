# For whoever maintains this toolbox

This directory contains the maintenance record for the shipped toolbox: provenance, cut decisions and
high-level design decisions that should not be mixed into Fellow-facing runtime instructions.

Start with `INDEX.md`. Nothing here is confidential: `.maintainers/` ships in every clone. The boundary
is audience and purpose, not access control.

## Structure

| Path | What it contains |
|---|---|
| `INDEX.md` | Directory manifest and freshness record |
| `CANON.md` | Provenance for every file under `library/` |
| `canon-check.sh` | Reports moved upstream or locally drifted vendored files |
| `cut-record.md` | Candidate-selection record for the original toolbox cut |
| `design/` | High-level design records for locally authored library components |

## Updating `library/`

The workspace tells a Fellow that `library/` is read-only. A maintainer may change it only as one
reviewable transaction:

1. change the library component and its parent inventory;
2. update every affected row in `CANON.md`, using `authored` for content written for this workspace;
3. update manifest counts and freshness statements;
4. run the component's validation and the provenance checks;
5. commit the library change and provenance update together.

A local edit without the provenance update is the exact drift this directory exists to prevent.

## Running the provenance check

```bash
bash .maintainers/canon-check.sh
```

Run it on a machine that has the source repositories checked out. `GONE` on vendored files means the
source path is unavailable on that machine, not that the source was deleted.

`CANON.md` column 5 is the hash as shipped and column 7 is the hash at source. They differ where a
vendored copy carries a deliberate local patch. For an `authored` row, source path, commit and source
hash are `-`.
