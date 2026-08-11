# For whoever maintains this toolbox

Nothing in this directory is for an apprentice. It is the record of how the toolbox was cut and the
one command that tells you whether it has drifted since.

| File | What it is |
|---|---|
| `CANON.md` | Provenance for every file under `library/`: where it came from, the commit it was taken at, its hash as shipped, and its hash at the source |
| `canon-check.sh` | Answers "what has moved upstream since the cut?" Run it on a machine that has the source repositories checked out |
| `cut-record.md` | Which candidates were considered, which were kept, and the reason for each |

## Why the provenance record exists

Four earlier attempts to share this material failed the same way, and none of them failed for lack of
a sync mechanism. They failed because nothing recorded what had been cut from what. `CANON.md` is
built to prevent that one failure. It does not sync anything and does not claim to.

## Why it lives here rather than at the repository root

An apprentice opening this repository should see the engagement structure and the tools, not the
maintenance apparatus for a library they are told not to edit. The mechanism is kept because it
guards a real failure; it is moved because it is not their business.

## Running the check

```bash
bash .maintainers/canon-check.sh
```

`GONE` on every vendored file means the source repositories are not on this machine, not that the
sources were deleted.

## The one thing that will rot

`CANON.md` column 5 is the hash as shipped and column 7 is the hash at the source. They differ
exactly where a copy carries a deliberate local patch. If someone edits a `library/` file in place,
column 5 stops matching the file and the gate that reads it fails. That is the intended behaviour:
report the file, do not repair it in place.
