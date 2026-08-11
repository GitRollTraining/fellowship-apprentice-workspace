# SKILL.md Skeleton

Copy-paste this template into `{target-dir}/SKILL.md`, then fill the `{{placeholders}}`. Do not include this file's `# SKILL.md Skeleton` heading in the output — it's metadata for the creator, not the skill.

## Standard Skeleton

```markdown
---
name: {{slug}}
description: {{one-sentence purpose, action-oriented, ≤200 chars, tells router when to fire}}
argument-hint: {{<required-arg> [optional-arg=default]}}
---

# {{Skill Display Name}}

> {{One paragraph: what this skill does, when to use it. Plain prose.}}

## Inputs

- `<{{required-arg}}>` — {{description}}
- `[{{optional-arg}}]` — {{description, default}}

If args missing, ask user.

## Workflow

1. {{Step one — terse imperative.}}
2. {{Step two — terse imperative.}}
3. {{Step three — for sub-protocol >5 lines, write "see `references/{detail}.md`" and put detail in ref.}}
4. {{...}}

## Gotchas

- **{{Trigger condition}}.** {{Wrong default behavior.}} {{Correct behavior.}}
- **{{Trigger condition}}.** {{Wrong default behavior.}} {{Correct behavior.}}

(If gotchas exceed ~10 items, extract to `references/gotchas.md` and link from this section.)

## Constants

| Key | Value |
|---|---|
| Skill location | `~/.claude/skills/{{slug}}/` (or `{workspace}/.claude/skills/{{slug}}/` for project skills) |
| Companion refs | `references/{{ref-name}}.md` |

## Output

{{Define expected output structure or template. Brief. If template is multi-line and static, extract to `references/output-template.md` and link.}}

## Style

{{Optional. Include only if voice is prescribed.}}
- Style directive: {{caveman | prose | JSON-only | terse procedural}}
- Tested on: {{Sonnet 4.6, Opus 4.7}}
- Model floor: {{Sonnet 4 (Haiku produces stilted output for caveman, etc.)}}

## Eval

{{Optional. Required for high-stakes skills (silent-revert risk, lost data, wrong file written).}}
- Canonical input: `eval/baseline-input.md` (or inline if short)
- Baseline output: `eval/baseline-output.md`
- Acceptance: {{regex / structural check / human review note}}

## Quality Guidelines

Adhere to:
- `@references/agent-quality-guidelines.md` (runtime behavior)
- `@references/skill-architecture.md` (structural principles)
```

## Companion Ref Skeletons

### `references/gotchas.md` (when ≥3 known gotchas exist)

```markdown
# Gotchas — {{Skill Name}}

Domain-specific failure modes. Each entry: trigger / wrong default / correct behavior.

## {{Gotcha 1 short title}}

**Trigger:** {{when this fires}}
**Wrong default:** {{what the agent does without this gotcha encoded}}
**Correct behavior:** {{what the agent must do instead}}
**Why:** {{optional — historical incident, regulatory constraint, hard-won learning}}

## {{Gotcha 2 short title}}

...
```

NO frontmatter. Plain markdown.

### `references/output-template.md` (when output template is multi-line)

```markdown
# Output Template — {{Skill Name}}

Copy this structure. Replace `{{placeholders}}`. Do not deviate.

## Template

{{Multi-line template here, e.g., a markdown report structure or JSON schema example.}}

## Required Sections

- {{Section 1}} — {{purpose}}
- {{Section 2}} — {{purpose}}

## Optional Sections

- {{Section}} — {{when to include}}
```

NO frontmatter. Plain markdown.

### `references/{sub-protocol}.md` (when a body step grows past 5-10 lines)

```markdown
# {{Sub-Protocol Name}} — {{Skill Name}}

Detailed steps for {{which body step references this ref}}. Loaded on demand.

## Steps

1. {{Detailed step}}
2. {{Detailed step}}
...

## Gotchas Specific to This Sub-Protocol

- {{Sub-protocol-only gotcha}}

## Failure Modes

- {{What goes wrong + how to recover}}
```

NO frontmatter. Plain markdown.

### `eval/baseline-input.md` and `eval/baseline-output.md` (high-stakes skills)

```markdown
# Baseline Input — {{Skill Name}}

Canonical input the skill should handle correctly.

## Input

{{Verbatim input — exact text the skill receives}}

## Acceptance Criteria

- {{Output must contain X}}
- {{Output must NOT contain Y}}
- {{Structural check: e.g., "valid JSON matching schema in references/schema.md"}}
- {{Human review note: e.g., "voice should feel 'Notion-warm', not stilted"}}
```

```markdown
# Baseline Output — {{Skill Name}}

Expected output for `baseline-input.md`. Update only when drift is intentional and approved.

## Output

{{Exact expected output, or output structure with allowed variation noted}}

## Last Verified

- Date: {{YYYY-MM-DD}}
- Model: {{Sonnet 4.6 / Opus 4.7}}
- By: {{user / agent}}
```

NO frontmatter on either eval file. Plain markdown.

## Filling Notes

- **Description field:** action-oriented. "Use when X" or "When the user asks Y" pattern fires the picker reliably. Avoid "This skill is for...". Avoid examples.
- **Workflow steps:** numbered, terse imperatives. If a step needs >5 lines of detail, the detail belongs in a ref.
- **Gotchas:** at least 1 even if you have to brainstorm one. A skill with no gotchas is usually a skill where the author hasn't yet discovered them.
- **Style section:** omit entirely if no voice is prescribed. Don't write "Style: neutral" — that's noise.
- **Eval section:** omit if low-stakes. Add later when the skill matures.

## Final Verification (run before declaring skill done)

See `references/checklist.md`.
