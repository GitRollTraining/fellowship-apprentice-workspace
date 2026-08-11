---
name: wei-create-skill
description: Scaffold new Claude Code skill following architecture principles (three-tier disclosure, gotchas, eval). Use when user asks to create, build, or author a new skill or SKILL.md.
argument-hint: <skill-name-slug> [scope=user|project]
---

# Create Skill

> Opinionated wrapper for new-skill creation. Loads canonical architecture refs, runs an interview, scaffolds SKILL.md + companion refs, runs antipattern checklist before declaring done.

## Inputs

- `<skill-name-slug>` — kebab-case slug, will be the directory name and the `name:` field
- `[scope]` — `user` (default; writes to `~/.claude/skills/`) or `project` (writes to current workspace `.claude/skills/`)

If args missing, ask user.

## Workflow

1. **Load principles.** Read both reference docs:
   - `@references/skill-architecture.md` — structural principles, antipattern checklist, applicability matrix
   - `@references/agent-quality-guidelines.md` — runtime principles (delegate, build-verify, doom loops)

2. **Decide the scope — do not just accept the default.** Settled criterion (2026-07-26, amended 2026-07-27; full audit in itsweikuo `.claude/references/skill-promotion-audit.md`):

   > **User-level iff the skill's operative destinations and config are external to any KB, or resolved at runtime from the invoking workspace. Project-level iff it names a division path that exists in only one workspace and you are not adding routing, or its content forks a same-named skill elsewhere.**

   Three things that decide it, and one that does not:
   - **Destination decides, not subject matter.** A skill that drives Spotify or Gmail still belongs project-level if its *state* is a division path. Ask where it writes, not what it is about.
   - **A one-workspace path is a fixable defect, not a verdict.** Add a routing table (step 2b) and the skill becomes promotable. This is the usual right answer.
   - **A fork is a hard block.** Two divergent contents cannot share one name at user level; one would silently replace the other. Check with `diff -r` before deciding.
   - **Cloud routines cannot see user-level skills.** A scheduled agent runs on a fresh clone with no `~/.claude/` at all. If a routine will invoke this skill, it must be project-level. Check `infra/scheduled-agents/`.

   **Check the name in all three scopes before writing** — `~/.claude/skills/`, and each workspace's `.claude/skills/`. A collision is either duplication to consolidate or a fork that blocks user scope.

2a. **Cross-workspace skills pick a SHARING PATTERN, not just a scope** (2026-08-01). When the skill is — or turns out to be — used from both operations and itsweikuo, decide in this order:

   | Pattern | When | Rule |
   |---|---|---|
   | **Fork** | Policy genuinely differs per workspace (`wei-knowledge-curator`, `sensitive-content-handling`) | Project-level in each; never symlink or overwrite; BLOCKS promotion |
   | **Symlink, owner-consumed** | Content is one workspace's policy/data, consumed verbatim by the other (`wei-archive-sweep`, shared rules) | Owner keeps it in git; consumer symlinks; register in itsweikuo `scripts/link-shared-rules.sh`; never edit through the symlink |
   | **Promote with routing** | Procedure portable; only destinations/config are workspace-specific (`wei-digest-doc`, `wei-deck`) | User-level + routing table (2b) |

   **Executing a promotion — of a new skill or an existing one — follows `~/.claude/references/skill-promotion-sop.md`**: blockers, deletion audit, three-repo choreography, reference sweep, cross-workspace smoke test. MANDATORY read when the skill has an **environment** — templates, asset libraries, venvs, scripts, anything outside `.claude/skills/` (SOP §4: ONE home + same-relative-path symlinks + owning-root resolution; never copies, never absolute paths).

2b. **If user-level and it writes anywhere in a KB, give it a routing table.** Never hardcode a division path in a user-level skill, and never accept the destination as a flag (preference #17 rule 2). Resolve the workspace at runtime:

   ```bash
   bash ~/.claude/scripts/workspace.sh    # -> "<name>\t<root>", exit 1 if unrecognized
   ```

   Then `{target-dir}/references/routing.md` maps workspace → destination. Exit 1 must **stop and report**, never fall back to cwd. Reference implementation: `~/.claude/skills/wei-digest-doc/references/routing.md`.

3. **Resolve target dir.**
   - `scope=user` → `~/.claude/skills/{slug}/`
   - `scope=project` → resolve the workspace root with `bash ~/.claude/scripts/workspace.sh`, then `{root}/.claude/skills/{slug}/`. **Do not walk up from cwd looking for `.git/`** — that predicate is true in every workspace *and* every git worktree, so it silently resolves the wrong root. If the probe exits 1, ask for an explicit root.
   - If target dir already exists, halt and ask user (overwrite vs. abort vs. rename).

4. **Run interview.** Ask the user the questions in `references/questions.md`. Capture answers — do not infer silently. Required answers:
   - One-sentence purpose / trigger condition (becomes `description`)
   - Argument contract (becomes `argument-hint`) — **and for each proposed flag, justify it against preference #17 or drop it**
   - Scope: user vs. project — decided in step 2 by the criterion, not by preference
   - If user-level and it writes into a KB: the destination per workspace (becomes `references/routing.md`)
   - Voice prescription: yes / no (if yes → ask model floor + tested-on)
   - High-stakes? (silent-revert risk, lost data, wrong file written) → if yes, eval baseline required
   - Known gotchas at creation time (>=1 if any can be named)

5. **Scaffold files.**
   - Read `references/skeleton.md` → fill placeholders w/ interview answers → write to `{target-dir}/SKILL.md`
   - Create `{target-dir}/references/` dir
   - If interview produced ≥3 known gotchas, also create `{target-dir}/references/gotchas.md` (empty markdown stub w/ heading + interview gotchas pre-filled)
   - If high-stakes, also create `{target-dir}/eval/` dir w/ `baseline.md` stub (canonical input + acceptance criteria placeholders)

6. **Run antipattern checklist.** Read `references/checklist.md` and run each grep/check against newly-written files. Report pass/fail per check.

7. **Report.** Output:
   - Files written (full paths)
   - Antipattern checklist results
   - Remaining TODOs for the user (e.g., "fill `eval/baseline.md` with canonical input")
   - Reminder: test the skill by invoking `/{slug}` with a real input before relying on it

## Gotchas

- **Description teaches instead of routing.** The `description:` field is for the skill picker to decide if the skill applies. Keep ≤200 chars, action-oriented. Do NOT include examples or rules — those go in body.
- **Slug already exists.** Do not silently overwrite. Halt + ask.
- **"Walk up to a `.git/`" resolves the WRONG root, not no root.** The failure people expect is "no repo found"; the real one is that the predicate is satisfied in every workspace *and* inside every git worktree, so it confidently returns a root that is not the one the user meant. Use `bash ~/.claude/scripts/workspace.sh`, which identifies the workspace by remote and cross-checks it against the root `CLAUDE.md`, and exits 1 rather than guessing. Outside a known workspace, ask for an explicit root.
- **Every flag you add is a behavior that will never run.** Wei invokes a given skill weeks or months apart. Preference #17: the correct behavior is the DEFAULT; configuration lives in the workspace and is read at runtime; one option rather than a menu; a flag is justified only when both branches are genuinely correct AND the choice is per-invocation. During the interview, for every proposed flag ask "could this be inferred from the workspace, the input type, or a config file?" — if yes, delete it. Two measured casualties: `--diarize` (a paid transcript came back unlabelled because the flag was not typed) and `--save` (a digest of a paid fetch evaporated for the same reason).
- **A user-level skill that hardcodes a division path is broken in every other workspace.** It will not error — it will write to a path that does not exist, or worse, one that does and means something else. Give it a routing table (step 2b).
- **A skill's environment does not promote with it.** A skill that depends on templates, asset libraries, scripts, or a venv outside `.claude/skills/` looks portable and is not. Wrong defaults: copy the assets into the skill or the consumer workspace (a second copy that silently drifts), or hardcode the owner's absolute path. Correct: the assets keep ONE home in the owning workspace; the consumer reaches them through symlinks at the SAME relative path; anything that must resolve against the owner (venv, doc-internal pointers) uses owning-root resolution (`pwd -P` through the symlink + `git rev-parse --show-toplevel`). Full taxonomy: promotion SOP §4; measured instance: `wei-deck` 2026-08-01.
- **Promotion hides a skill from cloud routines.** Scheduled agents run on a fresh clone with no `~/.claude/`. A project skill they can read becomes invisible the moment it is promoted, and nothing fails loudly. Check `infra/scheduled-agents/` before choosing user scope.
- **A provenance table is not an inventory.** Skill-provenance tables in workspace docs drift and can list skills that do not exist — two phantom rows survived in itsweikuo until 2026-07-27, and an audit that trusted the table would have "audited" a directory that was never there. Enumerate `ls .claude/skills/` and treat the table as a claim to verify.
- **User says voice doesn't matter, then prescribes one inline.** Re-read interview answers — if voice keywords ("caveman", "terse", "JSON-only", "structured prose") appear anywhere in user's purpose statement, treat as voice prescription and ask for model floor.
- **Frontmatter on a ref file.** When creating `references/*.md` from skeleton, never start them with `---`. Verify w/ `head -5 references/*.md` after write.
- **Skipping the antipattern checklist.** Step 6 is mandatory, not optional. A skill that fails its own creator's checklist should not be marked done.

## Constants

| Key | Value |
|---|---|
| Skill location (this skill) | `~/.claude/skills/wei-create-skill/` |
| Architecture ref | `@references/skill-architecture.md` (resolves to `~/.claude/references/skill-architecture.md`) |
| Quality ref | `@references/agent-quality-guidelines.md` |
| Companion refs | `references/skeleton.md`, `references/checklist.md`, `references/questions.md` |
| Workspace probe | `~/.claude/scripts/workspace.sh` — shared; never copy or re-implement it |
| Scope criterion + audit ledger | itsweikuo `.claude/references/skill-promotion-audit.md` |
| Promotion SOP (execution) | `~/.claude/references/skill-promotion-sop.md` — sharing patterns, environment taxonomy, three-repo choreography |
| Routing reference implementations | `~/.claude/skills/wei-digest-doc/references/routing.md` (destinations only); `~/.claude/skills/wei-deck/references/routing.md` (destinations + environment/owning-root) |
| User-level skill dir | `~/.claude/skills/` |
| Project-level skill dir | `{workspace-root}/.claude/skills/` |

## Output

End-of-run report:

```
Created skill: {scope}/.claude/skills/{slug}/
  SKILL.md (frontmatter + body)
  references/skeleton-companion-files-as-needed.md

Antipattern checklist: {N pass} / {M total}
  [X] Frontmatter routing-only
  [X] Body ≤500 lines (actual: {n})
  ...

Next:
  1. Test: invoke /{slug} with canonical input
  2. Fill: {any TODO refs}
  3. Iterate: refine based on first real-use feedback
```

## Style

Procedural skill. No voice prescription on output (user's new skill defines its own voice). Tested on Sonnet 4.6 + Opus 4.7. Model floor: Sonnet 4 (interview + antipattern reasoning).

## Quality Guidelines

Adhere to:
- `@references/agent-quality-guidelines.md` (runtime — delegate, build-verify, doom loops)
- `@references/skill-architecture.md` (structural — three-tier disclosure, gotchas, evals)
