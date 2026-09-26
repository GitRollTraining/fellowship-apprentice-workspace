---
name: setup
description: Set up the apprentice workspace folder, with its rules, in the repository you are working in. Use once in each new repository, or when apprentice-workspace/ is missing or incomplete.
---

# Set up the apprentice workspace in this repository

Creates `apprentice-workspace/` at the root of the repository the agent is working in: the folders for
client work, coursework and reusable notes, and the rules file that says where everything goes. Then
it adds a short block to the repository's `AGENTS.md` and `CLAUDE.md` so the agent reads those rules
in every later session. The tools themselves (skills, playbooks, templates) stay in the plugin.

Run it once per repository, and again after the plugin is updated. Running it again is safe: it only
adds what is missing, and replaces the rules file only if the apprentice agrees.

## Input

None. It works on the repository the agent is in. Do not ask the apprentice for a path unless step 1
says to.

## Workflow

1. **Find the repository root.** Run `git rev-parse --show-toplevel` in the working folder. If that
   fails, use the working folder itself, unless it is the home folder, a Desktop or Downloads folder,
   or inside the installed plugin: then stop and ask which project folder they mean. Say which
   folder you chose.
2. **Copy the template, never overwriting.** The template is `template/apprentice-workspace/` in this
   skill's own folder. Copy every file in it, including the dot-file `.gitignore`, to the same path
   under `<root>/apprentice-workspace/`, skipping any file that already exists. On macOS or Linux:
   `cp -R -n "<this skill's folder>/template/apprentice-workspace" "<root>/"`. Anywhere else, or if
   that command is not available, create each missing file with the template file's exact text.
   One exception: if `<root>/apprentice-workspace/AGENTS.md` already exists and differs from the
   template's, it is either an older copy of the plugin's rules or was edited in this repository.
   Show the apprentice the difference, and replace that one file with the template's only if they
   agree. Never replace any other file that exists.
3. **Add the root blocks.** For `<root>/AGENTS.md` and `<root>/CLAUDE.md`, follow
   `references/root-blocks.md`: add the block only if the file does not already contain
   `<!-- apprentice-workspace: start -->`, append it at the end, and never change anything else in
   the file. A new `CLAUDE.md` gets the extra first line that file specifies.
4. **Check the result.** List `<root>/apprentice-workspace/` including dot-files, and confirm: `AGENTS.md`,
   `INDEX.md`, `.gitignore`; `engagements/example-client/` with `interview/`, `process/`, `spec/`,
   `deliverable/`, `handover/`, `verification/`, each holding an `INDEX.md`; `training/onboarding/`;
   `reference/`. Confirm both root files contain the start marker. Anything missing: create it from
   the template and check again.
5. **Read the rules now.** Read `<root>/apprentice-workspace/AGENTS.md` in full and follow it for the
   rest of this session: this session started before the file existed, so nothing loaded it for you.
6. **Tell the apprentice, in three lines at most:** what was created, what already existed, and
   whether the rules file was replaced; that their work for this repository goes in
   `apprentice-workspace/`; and that a new chat will load the rules by itself. Do not commit; if they
   want the folder in git, that is a normal commit they approve.

## Gotchas

- **Replacing a file that was already there.** A client repository or a challenge fork can already
  have an `AGENTS.md`, a `CLAUDE.md` or a `.gitignore` that matters to someone else. Append the marked
  block; never rewrite, reorder or "tidy" what is there.
- **Creating `CLAUDE.md` with only the workspace block.** Claude Code reads a repository's `AGENTS.md`
  only while no `CLAUDE.md` exists, so a new `CLAUDE.md` without `@AGENTS.md` silently hides the
  repository's own instructions from it. `references/root-blocks.md` says what a new file starts with.
- **Running in the wrong folder.** The home folder is not a repository, and the plugin's own folder is
  read-only. Stop and ask rather than creating `apprentice-workspace/` there.
- **Nesting.** If the working folder is inside `apprentice-workspace/`, the root is still the
  repository root. Never create `apprentice-workspace/apprentice-workspace/`.
- **Skipping the dot-file.** A file-by-file copy that lists only visible files leaves out
  `.gitignore`, and then material named `*.local.*` is no longer kept out of git.
- **Setting up the folders at the repository root instead.** `engagements/`, `training/` and
  `reference/` belong inside `apprentice-workspace/`, even though the playbooks write them without the
  prefix.

## Quality guidelines

Adhere to:

- `library/reference/agent-quality-guidelines.md` for runtime behavior.
- `library/reference/skill-architecture.md` for structural principles.

`library/` here is the plugin's library: the folder two levels above this skill's own folder.
