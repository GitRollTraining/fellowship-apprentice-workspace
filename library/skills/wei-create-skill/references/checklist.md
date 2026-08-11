# Antipattern Checklist — Pre-Merge Gate

Run every check below against newly-created skill files. Report pass/fail. A skill that fails any check should not be declared done.

Source principles: `@references/skill-architecture.md`.

## Checks

### 1. Frontmatter on a Ref File

```bash
head -5 {skill-dir}/references/*.md 2>/dev/null | grep -B1 '^---$'
```

**Pass:** No output.
**Fail:** Any output. Remove the YAML frontmatter from the matching ref file. Frontmatter on refs promotes them to the skill picker → mis-routes.

### 2. Body Length Ceiling

```bash
wc -l {skill-dir}/SKILL.md
```

**Pass:** ≤500 lines (hard cap). Target: ≤100 lines for project dispatchers, ≤150 for self-contained skills.
**Fail (hard):** >500 lines. Extract content to refs.
**Fail (soft):** >150 lines without justification. Identify what could move to refs.

### 3. Hardcoded Absolute Paths

```bash
grep -nE '/Users/|~/Documents/' {skill-dir}/SKILL.md
```

**Pass:** No output, OR output is inside a code block as documented example.
**Fail:** Path baked into instructions. Replace with `$ARGUMENTS` / `$0` / discovery instruction / workspace-relative path.

### 4. Gotchas Section Exists

```bash
grep -niE '^## (gotchas|edge cases|what not to do)' {skill-dir}/SKILL.md
```

**Pass:** At least one match.
**Fail:** No match. Add `## Gotchas` section. Even a single gotcha is better than none — name one trigger condition + wrong default + correct behavior.

### 5. Description Field Sane

Visual inspection. Open `{skill-dir}/SKILL.md`, read the `description:` field.

**Pass:**
- ≤200 characters
- Action-oriented ("Use when X", "Scaffolds Y when Z")
- Names the trigger condition

**Fail:**
- >200 chars
- Includes examples or rules (those belong in body)
- Vague ("This skill helps with various tasks")

### 6. Voice Prescription Has Model Anchor

Visual inspection. If body contains style directives ("caveman", "terse", "JSON-only", "Notion-warm", "prose"), the `## Style` section must include:
- `Style directive:`
- `Tested on:` (specific model versions)
- `Model floor:` (minimum tier)

**Pass:** All three present, OR no voice prescription anywhere.
**Fail:** Voice prescribed but model not anchored. The first model upgrade silently drifts the output.

### 7. Eval Baseline (for High-Stakes Skills)

```bash
ls {skill-dir}/eval/ 2>/dev/null
```

**Pass:**
- `eval/baseline-input.md` exists, OR
- Skill is low-stakes (no silent-revert risk, no data loss potential, no wrong-file-write potential)

**Fail:** High-stakes skill without eval baseline. Create `eval/baseline-input.md` + `eval/baseline-output.md` with canonical input + acceptance criteria.

### 8. Refs Cited in Footer

```bash
tail -10 {skill-dir}/SKILL.md | grep -E 'agent-quality-guidelines|skill-architecture'
```

**Pass:** Both refs cited (typically in `## Quality Guidelines` footer).
**Fail:** Missing one or both. Add the standard footer:

```markdown
## Quality Guidelines

Adhere to:
- `@references/agent-quality-guidelines.md` (runtime behavior)
- `@references/skill-architecture.md` (structural principles)
```

### 9. Workflow Steps Are Imperative + Terse

Visual inspection. Each numbered workflow step:

**Pass:**
- Starts with a verb (Read, Ask, Scaffold, Run, Report)
- ≤5 lines per step
- Steps requiring >5 lines reference a ref file

**Fail:** Step is a paragraph of explanation, OR sub-protocol is inlined when it should be in a ref.

### 10. Skill Can Be Invoked

After creation, verify the skill registers correctly:

```bash
# In a fresh Claude session, check available skills include the new one
ls ~/.claude/skills/{slug}/SKILL.md
```

**Pass:** File exists, frontmatter parses (verify with `head -5` shows valid YAML between `---` delimiters).
**Fail:** Frontmatter syntax error → skill won't register. Fix YAML.

## Reporting Format

After running all checks, output:

```
Antipattern Checklist: {N pass} / 10
  [X] 1. Frontmatter on refs
  [X] 2. Body length ({lines} lines)
  [X] 3. Hardcoded paths
  [ ] 4. Gotchas section — MISSING
  [X] 5. Description sane
  [-] 6. Voice anchor — N/A (no voice prescribed)
  [-] 7. Eval baseline — N/A (low-stakes)
  [X] 8. Refs cited
  [X] 9. Workflow imperative
  [X] 10. Skill registers

Failures:
  - Check 4: Add ## Gotchas section to SKILL.md.

Skill is NOT done until all failures resolved (excluding N/A).
```

## Scope and interface (added 2026-07-27)

| # | Check | How | Fail means |
|---|---|---|---|
| S1 | Scope was decided, not defaulted | The report states which criterion branch applied | Nobody asked where the skill writes |
| S2 | No name collision in any scope | `ls ~/.claude/skills/`, and each workspace's `.claude/skills/` | Two contents, one name — one silently wins |
| S3 | User-level skill has no hardcoded division path | `grep -nE '(health\|finance\|career\|infra\|notes\|projects\|hobbies\|meetings)/' SKILL.md references/*.md`. **The grep cannot finish this check** — it cannot tell a *destination* from a *citation* or a worked example, and both are legitimate outside `routing.md`. Read each hit: a path the skill WRITES to outside `routing.md` is a violation; a path it cites as provenance or a proven-output example is fine. A hit that restates `routing.md`'s table is also a violation — two copies drift | Broken in every other workspace, silently; or a duplicated destination table that drifts |
| S4 | Every flag in `argument-hint` is justified | For each: could it be inferred from workspace, input type, or config? | Preference #17 — a flag Wei must remember is a behavior that never runs |
| S5 | Workspace resolution uses the shared probe | `grep -n 'workspace.sh' SKILL.md`; no hand-rolled "walk up to `.git/`" | Resolves the wrong root inside worktrees, without erroring |
| S6 | No routine depends on it if user-level | `grep -rn '<slug>' <workspace>/infra/scheduled-agents/` | Cloud routines run on a fresh clone and cannot see `~/.claude/` |
