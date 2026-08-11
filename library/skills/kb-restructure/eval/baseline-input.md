# Baseline Input — kb-restructure

Canonical input: a planted fixture tree with at least one inbound reference per proven failure class, then a simulated move of the target file. `eval/run-eval.sh` builds it mechanically; this file is the spec. Plants marked (R1) were promoted permanently from the round-01 adversarial discovery hunt.

## Fixture

Target of the mutation: `alpha/beta/file.md` (moved to `alpha/file.md` mid-eval).

| Plant | Failure class exercised |
|---|---|
| `docs/note.md` containing `see alpha/beta/file.md` | plain content ref |
| `.claude/logs/2026-01-01.md` containing `log: alpha/beta/file.md` | hidden-dir ref (plain search skips dot-dirs) |
| `docs/INDEX.md` containing `\| row \| alpha/beta/file.md \|` | INDEX manifest row |
| `.archive/old.md` containing `old alpha/beta/file.md` | historical ref — must be FOUND; classification decides leave-vs-fix |
| `secret.md`, gitignored via `.gitignore`, containing `gitignored ref alpha/beta/file.md` | gitignored ref (plain search skips) |
| `docs/link.md` → symlink to `../alpha/beta/file.md` | symlink, raw target text carries the needle; breaks silently after the move |
| `alpha/rel-link.md` → symlink to `beta/file.md` (R1) | symlink whose raw text LACKS the needle but physically resolves into it — caught only by target resolution |
| `docs/blob.bin`: needle + NUL bytes (R1) | binary file carrying the path — `--binary` required or rg skips it |
| `vendor/node_modules/pkg.md` containing the needle (R1) | must be EXCLUDED — vendored noise, pruned at any depth |
| `alpha/sib.md` containing `[see](./beta/file.md)` (R1) | relative-literal ref — invisible to the full-path scan BY DESIGN; caught by the playbook's basename alias scan |
| `docs/case.md` containing `Alpha/Beta/file.md` (R1) | case-variant ref — live on case-insensitive filesystems; caught only with `REFSCAN_ICASE=1` |

## Eval cases

1. **refscan, full-path needle, no policy file** — every content/symlink plant found with expected hints; `vendor/node_modules/`, `alpha/sib.md`, `docs/case.md` absent.
2. **refscan, policy patterns file** containing `^\.claude/logs/` — the hidden-dir hit's hint flips `content` → `historical`; nothing else changes (policy injection works).
3. **symcheck, after the move** — both symlinks break (`docs/link.md`, `alpha/rel-link.md`); exact set in baseline-output. Clean tree + exit 0 before the move.
4. **alias scan (R1)** — `refscan.sh "file.md" <fixture>` (basename needle) finds `alpha/sib.md` and `docs/case.md`: the documented cover for relative-literal and wrapped refs. Over-reporting is expected; triage is classification's job.
5. **ICASE (R1)** — `REFSCAN_ICASE=1` with the full-path needle returns EXACTLY the case-1 set plus `docs/case.md` (set equality); the default run lacks it.
6. **invalid policy regex (R1)** — a policy file with one bad ERE line aborts with exit 2 naming the line; no silent hint degradation.
7. **trailing-slash root (R1)** — `refscan.sh <needle> <fixture>/` output identical to case 1 (paths stay root-relative).
8. **node_modules-named symlink (R1)** — separate mini-fixture: a broken SYMLINK named `node_modules` is still reported by symcheck (only directories are pruned), with root-relative output under a trailing-slash root too.

## Acceptance criteria

- Case 1 output (sorted) matches `eval/baseline-output.md` exactly — no missed plant, no phantom hit, exclusions absent.
- Cases 2–8 as specified above; exit codes: refscan 0 on success / 2 on usage or bad policy; symcheck 0 clean / 1 broken / 2 usage.
- Both scripts run on a plain POSIX system with only `rg`, `bash`, `find` — no workspace-specific assumptions.
