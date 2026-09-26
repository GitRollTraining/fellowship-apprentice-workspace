# Baseline input — setup

Three starting repositories. Run the skill once in each, from the repository root, with the prompt
"Set up the apprentice workspace in this repository."

## Input

1. **Empty.** A new folder with `git init` and nothing else.
2. **Existing instructions.** A repository whose root holds `AGENTS.md` with the single line
   `Run the tests with make test.` and no `CLAUDE.md`.
3. **Second run.** Repository 1 after the first run, with one line added by hand to
   `apprentice-workspace/reference/question-bank.md`.

## Acceptance criteria

- Every file under `template/apprentice-workspace/`, including `.gitignore`, exists at the same path
  under `apprentice-workspace/` (compare the two file lists).
- Repository 1: root `AGENTS.md` holds only the AGENTS block; root `CLAUDE.md` starts with `@AGENTS.md`
  and holds the CLAUDE block.
- Repository 2: the line `Run the tests with make test.` is still the first line of `AGENTS.md`,
  followed by the AGENTS block; the new `CLAUDE.md` starts with `@AGENTS.md`.
- Repository 3: the hand-added line is still in `question-bank.md`; each root file holds the start
  marker exactly once.
- No `engagements/`, `training/` or `reference/` folder at the repository root, and no
  `apprentice-workspace/apprentice-workspace/`.
- Nothing is committed.
