---
name: create-skill
description: Scaffold new Claude Code skill following architecture principles (three-tier disclosure, gotchas, eval). Use when user asks to create, build, or author a new skill or SKILL.md.
argument-hint: <skill-name-slug> [scope=user|project]
---

# Create Skill

> Opinionated wrapper for new-skill creation. Loads canonical architecture refs, runs an interview, scaffolds SKILL.md + companion refs, runs antipattern checklist before declaring done.

## Inputs

- `<skill-name-slug>` — kebab-case slug, will be the directory name and the `name:` field
- `[scope]` — in this workspace always `project`: the skill is written to `library/skills/` if it is ours, or to the engagement it belongs to if it is the client's. A skill that lives in a home directory does not travel with the work

If args missing, ask user.

## Workflow

1. **Load principles.** Read both reference docs:
   - `library/reference/skill-architecture.md` — structural principles, antipattern checklist, applicability matrix
   - `library/reference/agent-quality-guidelines.md` — runtime principles (delegate, build-verify, doom loops)

2. **Decide the scope — do not just accept the default.** In this workspace the answer is almost always `project`, so the skill travels with the repository the work is in:

   > **User-level iff the skill's operative destinations and config are external to any KB, or resolved at runtime from the invoking workspace. Project-level iff it names a division path that exists in only one workspace and you are not adding routing, or its content forks a same-named skill elsewhere.**

   Three things that decide it, and one that does not:
   - **Destination decides, not subject matter.** A skill that drives Spotify or Gmail still belongs project-level if its *state* is a division path. Ask where it writes, not what it is about.
   - **A one-workspace path is a fixable defect, not a verdict.** Add a routing table (step 2b) and the skill becomes promotable. This is the usual right answer.
   - **A fork is a hard block.** Two divergent contents cannot share one name at user level; one would silently replace the other. Check with `diff -r` before deciding.
   - **A skill in a home directory does not travel.** Anything that has to work for the person you hand the repository to must live inside the repository.

   **Check the name before writing** — `ls library/skills/` and `ls .claude/skills/`. Two skills with one name means one of them silently never runs.

2a. **Cross-repository skills pick a SHARING PATTERN, not just a scope.** When the skill is — or turns out to be — used from more than one repository, decide in this order:

   | Pattern | When | Rule |
   |---|---|---|
   | **Fork** | Policy genuinely differs per repository | Keep one copy in each; never symlink or overwrite |
   | **Symlink, owner-consumed** | Content is one repository's policy or data, consumed verbatim by the other | The owner keeps it in git; the consumer symlinks it; never edit through the symlink |
   | **Promote with routing** | Procedure portable; only destinations are repository-specific | One home plus a routing table (2b) |

   **Promotion between repositories is a GitRoll-internal procedure and its SOP does not ship here.** You will not need it: a skill you write on an engagement belongs to that engagement, and a skill worth keeping is proposed for `library/` rather than moved by hand. The one rule worth carrying out of it: a skill with an environment — scripts, templates, a virtual environment — has exactly ONE home, and everything else points at it. Never copies, never absolute paths.

2b. **If user-level and it writes anywhere in a KB, give it a routing table.** Never hardcode a division path in a user-level skill, and never accept the destination as a flag (preference #17 rule 2). Resolve the workspace at runtime:

   ```bash
   git rev-parse --show-toplevel          # -> the root of this workspace
   ```

   Then `{target-dir}/references/routing.md` maps the resolved root to a destination. A failure here must **stop and report**, never fall back to the current directory. Worked example: `library/skills/digest-doc/references/routing.md`.

3. **Resolve target dir.**
   - ours, reusable across engagements → propose it for `library/skills/{slug}/`
   - this client's only skill → `engagements/<client-slug>/deliverable/`; for a multi-skill delivery,
     use the component directory selected by the specification
   - resolve the root with `git rev-parse --show-toplevel`, and if that fails, ask for an explicit root rather than guessing
   - for a library skill, halt if the proposed skill directory already exists
   - for an engagement skill, the scaffolded `deliverable/` directory is expected to exist; halt only
     if the intended `skill.md` or a generated companion path would overwrite client work

4. **Resolve the build interview.** Read `references/questions.md`. If the caller supplied an accepted
   build contract or an answered questionnaire, bind and cite its answers first, then ask only for a
   genuinely absent answer. Otherwise ask the user each question. Do not make the user repeat an
   accepted decision, and do not infer a missing one silently. Required answers:
   - One-sentence purpose / trigger condition (becomes `description`)
   - Argument contract (becomes `argument-hint`) — **and for each proposed flag, justify it against preference #17 or drop it**
   - Scope: user vs. project — decided in step 2 by the criterion, not by preference
   - If user-level and it writes into a KB: the destination per workspace (becomes `references/routing.md`)
   - Voice prescription: yes / no (if yes → ask model floor + tested-on)
   - High-stakes? (silent-revert risk, lost data, wrong file written) → if yes, eval baseline required
   - Known gotchas at creation time (>=1 if any can be named)

5. **Scaffold files.**
   - Read `references/skeleton.md` → fill placeholders w/ interview answers → write to
     `{skill-dir}/SKILL.md` for a library skill, or `{skill-dir}/skill.md` for an engagement deliverable.
     The lowercase name is this workspace's client-content convention, not necessarily the target
     runtime's entry filename
   - Create `{skill-dir}/references/` dir
   - If interview produced ≥3 known gotchas, also create `{skill-dir}/references/gotchas.md` (empty markdown stub w/ heading + interview gotchas pre-filled)
   - If high-stakes, also create `{skill-dir}/eval/baseline-input.md` and
     `{skill-dir}/eval/baseline-output.md` from the supplied companion skeletons
   - For an engagement deliverable, remove or rewrite the skeleton's `Quality Guidelines` footer unless
     those `library/reference/` files are intentionally included in the client package. No shipped skill
     may rely on a workspace-only path the client will not receive
   - Update `deliverable/INDEX.md`. Ensure `deliverable/deployment.md` installs the complete bundle into
     the selected client runtime and names its required entry filename — commonly
     `<skill-slug>/SKILL.md` — while preserving all companion relative paths

6. **Run antipattern checklist.** Read `references/checklist.md`, set its `SKILL_DIR` and `SKILL_FILE`
   for the selected scope, and run each check against the newly written files. Report pass/fail per
   check. For an engagement skill, also test a disposable copy installed exactly as
   `deliverable/deployment.md` instructs.

7. **Report.** Output:
   - Files written (full paths)
   - Antipattern checklist results
   - Remaining TODOs for the user (e.g., "fill `eval/baseline-input.md` and
     `eval/baseline-output.md` with the canonical pair")
   - Reminder: test a library skill by invoking `/{slug}` with a real input; test an engagement skill
     from its disposable installed form before relying on it

## Gotchas

- **Description teaches instead of routing.** The `description:` field is for the skill picker to decide if the skill applies. Keep ≤200 chars, action-oriented. Do NOT include examples or rules — those go in body.
- **Slug already exists.** Do not silently overwrite. Halt + ask.
- **"Walk up to a `.git/`" resolves the WRONG root, not no root.** The failure people expect is "no repository found"; the real one is that the test succeeds inside every git worktree too, so it confidently returns a root that is not the one you meant. Prefer `git rev-parse --show-toplevel`, and when you are not certain the answer is the workspace you mean, ask rather than guess.
- **Every flag you add is a behavior that will never run.** People invoke a given skill weeks or months apart, and working memory does not carry a flag across that gap. The rule: the correct behavior is the DEFAULT; configuration lives in the workspace and is read at runtime; one option rather than a menu; a flag is justified only when both branches are genuinely correct AND the choice is per-invocation. During the interview, for every proposed flag ask "could this be inferred from the workspace, the input type, or a config file?" — if yes, delete it. Two measured casualties: `--diarize` (a paid transcript came back unlabelled because the flag was not typed) and `--save` (a digest of a paid fetch evaporated for the same reason).
- **A user-level skill that hardcodes a division path is broken in every other workspace.** It will not error — it will write to a path that does not exist, or worse, one that does and means something else. Give it a routing table (step 2b).
- **A skill's environment does not promote with it.** A skill that depends on templates, asset libraries, scripts, or a venv outside `.claude/skills/` looks portable and is not. Wrong defaults: copy the assets into the skill or the consumer workspace (a second copy that silently drifts), or hardcode the owner's absolute path. Correct: the assets keep ONE home in the owning workspace; the consumer reaches them through symlinks at the SAME relative path; anything that must resolve against the owner (venv, doc-internal pointers) uses owning-root resolution (`pwd -P` through the symlink + `git rev-parse --show-toplevel`). The rule that survives: the assets keep one home, and everything else points at it.
- **Moving a skill to a home directory hides it from everyone else.** It keeps working for you, and nothing fails loudly, so the breakage is invisible until someone else clones the repository and the skill is simply not there.
- **A provenance table is not an inventory.** A table listing which skills exist drifts, and can name skills that were never built — an audit trusting one would "audit" a directory that is not there. Enumerate `ls .claude/skills/` and treat any table as a claim to verify.
- **User says voice doesn't matter, then prescribes one inline.** Re-read interview answers — if voice keywords ("caveman", "terse", "JSON-only", "structured prose") appear anywhere in user's purpose statement, treat as voice prescription and ask for model floor.
- **Frontmatter on a ref file.** When creating `references/*.md` from skeleton, never start them with `---`. Verify w/ `head -5 references/*.md` after write.
- **Skipping the antipattern checklist.** Step 6 is mandatory, not optional. A skill that fails its own creator's checklist should not be marked done.

## Constants

| Key | Value |
|---|---|
| Skill location (this skill) | `library/skills/create-skill/`, reached through the `.claude/skills` symlink |
| Architecture ref | `library/reference/skill-architecture.md` — shipped in this repository |
| Quality ref | `library/reference/agent-quality-guidelines.md` |
| Companion refs | `references/skeleton.md`, `references/checklist.md`, `references/questions.md` |
| Workspace probe | `git rev-parse --show-toplevel`. **Local patch:** upstream this is a script recognising two GitRoll repositories by remote, which does not ship |
| Scope criterion | In this workspace: `project`. The cross-workspace promotion ledger is GitRoll-internal and does not ship |
| Promotion SOP | GitRoll-internal; does not ship. See the note in step 2a |
| Routing worked example | `library/skills/digest-doc/references/routing.md` |
| Skill directory | `library/skills/` for ours; `.claude/skills` is the symlink the agent reads |
| Project-level skill dir | `{workspace-root}/.claude/skills/` |

## Output

End-of-run report:

```
Created skill: {actual skill directory}
  {SKILL.md or skill.md} (frontmatter + body)
  references/skeleton-companion-files-as-needed.md

Antipattern checklist: {N pass} / {M total}
  [X] Frontmatter routing-only
  [X] Body ≤500 lines (actual: {n})
  ...

Next:
  1. Test: {invoke /{slug}, or install a disposable copy per deployment.md and invoke it}
  2. Fill: {any TODO refs}
  3. Iterate: refine based on first real-use feedback
```

## Style

Procedural skill. No voice prescription on output (user's new skill defines its own voice). Tested on Sonnet 4.6 + Opus 4.7. Model floor: Sonnet 4 (interview + antipattern reasoning).

## Quality Guidelines

Adhere to:
- `library/reference/agent-quality-guidelines.md` (runtime — delegate, build-verify, doom loops)
- `library/reference/skill-architecture.md` (structural — three-tier disclosure, gotchas, evals)
