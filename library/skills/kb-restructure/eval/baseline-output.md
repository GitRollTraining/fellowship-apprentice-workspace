# Baseline Output — kb-restructure

Expected output for `eval/baseline-input.md`. Update only when drift is intentional and approved.

## Case 1 — refscan, full-path needle, no policy file (sorted)

```
.archive/old.md	historical
.claude/logs/2026-01-01.md	content
alpha/rel-link.md	symlink
docs/INDEX.md	manifest
docs/blob.bin	content
docs/link.md	symlink
docs/note.md	content
secret.md	content
```

Absent by design: `vendor/node_modules/pkg.md` (pruned), `alpha/sib.md` (relative literal — alias scan's job), `docs/case.md` (case variant — ICASE's job).

## Case 2 — refscan, policy file `^\.claude/logs/` (sorted)

Identical to case 1 except:

```
.claude/logs/2026-01-01.md	historical
```

## Case 3 — symcheck after `alpha/beta/file.md` → `alpha/file.md` (sorted)

```
alpha/rel-link.md
docs/link.md
```

Exit code 1. Before the move: empty output, exit 0.

## Case 4 — alias scan `refscan.sh "file.md" <fixture>`

Superset scan; must contain at least:

```
alpha/sib.md	content
docs/case.md	content
```

## Case 5 — ICASE

`REFSCAN_ICASE=1`, full-path needle: EXACTLY the case-1 set plus `docs/case.md	content` (set equality asserted). Default run: `docs/case.md` absent.

## Case 6 — invalid policy regex

Policy file line 2 = `a[` → exit 2, stderr names `:2:`. No hit output trusted.

## Case 7 — trailing-slash root

`refscan.sh <needle> <fixture>/` — byte-identical to case 1.

## Case 8 — node_modules-named symlink (mini-fixture)

`ln -s /nonexistent <mini>/node_modules` → `symcheck.sh <mini>` and `symcheck.sh <mini>/` both print exactly `node_modules`, exit 1.

## Last Verified

- Date: 2026-07-12
- Model: n/a (scripts are deterministic; verified by `eval/run-eval.sh`)
- By: agent (round 01 build, round-1 adversarial promotions included)
