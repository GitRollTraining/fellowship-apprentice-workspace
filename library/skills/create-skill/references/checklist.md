# Antipattern Checklist — Pre-Merge Gate

Run every check below against newly-created skill files. Report pass/fail. A skill that fails any check should not be declared done.

Source principles: `library/reference/skill-architecture.md`.

Resolve the two paths once. Do not assume that an engagement authoring file is already installed under
its runtime filename:

```bash
SKILL_DIR=<workspace-relative directory containing the skill bundle>
SKILL_FILE="$SKILL_DIR/SKILL.md"       # library skill
# SKILL_FILE="$SKILL_DIR/skill.md"     # engagement deliverable
test -f "$SKILL_FILE"
```

## Checks

### 1. Frontmatter on a Ref File

```bash
find "$SKILL_DIR/references" -type f -name '*.md' -exec sh -c '
  for file do head -5 "$file"; done
' sh {} + 2>/dev/null | grep -B1 '^---$'
```

**Pass:** No output.
**Fail:** Any output. Remove the YAML frontmatter from the matching ref file. Frontmatter on refs promotes them to the skill picker → mis-routes.

### 2. Body Length Ceiling

```bash
wc -l "$SKILL_FILE"
```

**Pass:** ≤500 lines (hard cap). Target: ≤100 lines for project dispatchers, ≤150 for self-contained skills.
**Fail (hard):** >500 lines. Extract content to refs.
**Fail (soft):** >150 lines without justification. Identify what could move to refs.

### 3. Hardcoded Absolute Paths

```bash
grep -nE '^/(Users|home)/|~/[A-Z]' "$SKILL_FILE"
```

**Pass:** No output, OR output is inside a code block as documented example.
**Fail:** Path baked into instructions. Replace with `$ARGUMENTS` / `$0` / discovery instruction / workspace-relative path.

### 4. Gotchas Section Exists

```bash
grep -niE '^## (gotchas|edge cases|what not to do)' "$SKILL_FILE"
```

**Pass:** At least one match.
**Fail:** No match. Add `## Gotchas` section. Even a single gotcha is better than none — name one trigger condition + wrong default + correct behavior.

### 5. Description Field Sane

Visual inspection. Open `$SKILL_FILE`, read the `description:` field.

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
ls "$SKILL_DIR/eval/" 2>/dev/null
```

**Pass:**
- `eval/baseline-input.md` exists, OR
- Skill is low-stakes (no silent-revert risk, no data loss potential, no wrong-file-write potential)

**Fail:** High-stakes skill without eval baseline. Create `eval/baseline-input.md` + `eval/baseline-output.md` with canonical input + acceptance criteria.

### 8. Refs Cited in Footer

```bash
case "$SKILL_FILE" in
  library/skills/*)
    FOOTER="$(tail -20 "$SKILL_FILE")"
    printf '%s\n' "$FOOTER" | grep -F 'library/reference/agent-quality-guidelines.md' >/dev/null
    printf '%s\n' "$FOOTER" | grep -F 'library/reference/skill-architecture.md' >/dev/null
    ;;
  *)
    ! grep -F 'library/reference/' "$SKILL_FILE"
    ;;
esac
```

**Pass:** For a library skill, both refs are cited (typically in `## Quality Guidelines`). For an
engagement deliverable, the workspace-only footer is absent, or every cited guideline is intentionally
included in the client package at the referenced relative path.
**Fail:** A library skill is missing one or both references, or a client skill points back to an
unpackaged `library/` path. For a library skill, add the standard footer:

```markdown
## Quality Guidelines

Adhere to:
- `library/reference/agent-quality-guidelines.md` (runtime behavior)
- `library/reference/skill-architecture.md` (structural principles)
```

### 9. Workflow Steps Are Imperative + Terse

Visual inspection. Each numbered workflow step:

**Pass:**
- Starts with a verb (Read, Ask, Scaffold, Run, Report)
- ≤5 lines per step
- Steps requiring >5 lines reference a ref file

**Fail:** Step is a paragraph of explanation, OR sub-protocol is inlined when it should be in a ref.

### 10. Skill Can Be Invoked

After creation, verify the constrained frontmatter structurally. This catches the common case where a
colon in a natural-language description makes the YAML invalid, instead of merely printing five lines
and claiming they parsed:

```bash
python3 - "$SKILL_FILE" <<'PY'
import json
import pathlib
import re
import sys

path = pathlib.Path(sys.argv[1])
lines = path.read_text(encoding="utf-8").splitlines()
assert lines and lines[0] == "---", "frontmatter must begin on line 1"
end = lines.index("---", 1)
fields = {}
for line in lines[1:end]:
    match = re.fullmatch(r"([a-z][a-z-]*):\s*(.*)", line)
    assert match, f"unsupported or malformed frontmatter line: {line!r}"
    fields[match.group(1)] = match.group(2)
assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", "")), "invalid name"
description = fields.get("description", "")
assert description.startswith('"') and description.endswith('"'), "description must be JSON/YAML double-quoted"
assert isinstance(json.loads(description), str) and json.loads(description).strip(), "invalid description quoting"
assert fields.get("argument-hint", "").strip(), "missing argument-hint"
print(f"frontmatter structure clean: {path}")
PY
```

For an engagement deliverable, also follow `deliverable/deployment.md` into a disposable client-runtime
directory, preserving every companion file and installing its entry point under the runtime-required
name (commonly `<slug>/SKILL.md`). Start a fresh agent session against that copy and invoke it with one
canonical input.

**Pass:** The authoring file passes the constrained parser, and the installed copy registers and runs
from only the files the client receives. A fresh agent registration is the runtime proof; the parser is
the preflight.
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
| S2 | No name collision | Compare resolved paths and contents under `library/skills/` and `.claude/skills/`; the shipped symlink may make them the same file | Two different contents, one name — one silently wins |
| S3 | User-level skill has no hardcoded division path | Run `grep -nE '(health\|finance\|career\|infra\|notes\|projects\|hobbies\|meetings)/' "$SKILL_FILE" "$SKILL_DIR"/references/*.md`. **The grep cannot finish this check** — it cannot tell a destination from a citation or worked example. Read each hit: a path the skill writes to outside `routing.md` is a violation; provenance and proven-output examples are allowed. A duplicated routing table is also a violation | Broken in every other workspace, silently; or a duplicated destination table that drifts |
| S4 | Every flag in `argument-hint` is justified | For each: could it be inferred from workspace, input type, or config? | A flag the user has to remember is a behavior that never runs |
| S5 | Workspace resolution uses the shipped probe | `grep -n 'git rev-parse --show-toplevel' "$SKILL_FILE"` when workspace resolution is needed; no hand-rolled "walk up to `.git/`" | Resolves the wrong root inside worktrees, without erroring |
| S6 | It lives in the repository, not a home directory | `test -f "$SKILL_FILE"` and confirm the path is under `library/skills/` or the engagement's `deliverable/` | Anyone you hand the repository to gets the skill; a home directory does not travel |
