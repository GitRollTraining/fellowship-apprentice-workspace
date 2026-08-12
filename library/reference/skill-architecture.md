# Skill Architecture Guidelines

> All skills MUST follow these structural principles.
> Source: Lax Meiyappan, "What You're Actually Writing When You Write a SKILL.md" (https://internals.laxmena.com/p/what-youre-actually-writing-when, 2026-04-30)

A SKILL.md is a **loader specification**, not a long prompt. The runtime uses progressive disclosure to load content at different times. Architectural choices compound across every skill and every turn — restructuring beats rewriting.

## The Three-Tier Loader Model

| Level | What loads | When | Token budget |
|---|---|---|---|
| **1. Frontmatter** | YAML `name` + `description` (+ optional `argument-hint`, `disable-model-invocation`) | Always — every session | ~100 tokens per skill |
| **2. Body** | SKILL.md procedural instructions | When the skill triggers | ≤500 lines hard cap, ~100 lines target |
| **3. Refs + Scripts** | Reference markdown files; executable scripts | On demand — when body points to them | Effectively unlimited |

**Architectural insight:** Identical content structured across these tiers vs. dumped into Level 2 can drop context cost 3×. The tier you put content in determines when it loads, not whether it's available.

## Principle 1: Frontmatter Is for Routing Only

Frontmatter is the index card on the runtime's pinboard. The agent reads only `name` + `description` to decide whether the skill applies.

**Required:**
- `name` — slug matching directory name
- `description` — one sentence, ≤200 chars, action-oriented. Should tell the router exactly when to fire.

**Optional:**
- `argument-hint` — input contract for the user (e.g., `<file_path> [--mode=quick|deep]`)
- `disable-model-invocation` — only set explicitly if you understand why; default is false

**Anti-pattern:** Stuffing examples, rules, or workflow into the description. Description is for routing, not teaching.

## Principle 2: Body Has a Ceiling

Hard cap: 500 lines. Target: ≤100 lines for project-scoped dispatchers, ≤150 for self-contained skills.

If the body exceeds 100 lines, audit what could move out:
- Multi-line templates → ref file
- Long edge-case lists → ref file
- Worked examples → ref file (or `examples/` subdir)
- Detailed sub-protocol steps → ref file
- Domain-specific gotchas → `references/gotchas.md`

Body should contain: dispatch logic, high-level workflow, pointers to refs. Not exhaustive content.

**Anti-pattern:** Monolithic skill where body grows to absorb every edge case discovered over time. Refs exist precisely so growth is downward, not outward.

## Principle 3: Refs Have NO Frontmatter

Reference files inside a skill directory must be plain markdown. **Never add YAML frontmatter to a non-skill `.md` file.**

The runtime scans for frontmatter to populate the skill picker. A ref file with frontmatter gets promoted to routing visibility — the agent will fire it directly as if it were a standalone skill, bypassing the parent SKILL.md and loading wrong context.

**Anti-pattern:**
```markdown
---
name: my-skill-rules
description: Rules for my-skill
---
# Rules
...
```

**Correct:**
```markdown
# Rules

These rules apply when the parent SKILL.md invokes this reference.
...
```

Verify: `head -5 {ref-file}.md` should never show a `---` delimiter.

## Principle 4: Path Discovery, Not Hardcoding

Skills must work across machines and clones. Never bake absolute paths into body text.

**Use:**
- `$ARGUMENTS` / `$0` — argument placeholders
- Discovery instructions — "Locate project root by walking up from cwd until `.git/` is found"
- Workspace-relative paths — `.claude/rules/INDEX.md` (acceptable for project-scoped skills inside a known workspace)

**Avoid:**
- An absolute path into one person's home directory
- A path naming one specific project directory on one machine
- Hard assumptions about layout without a discovery step

**Project-scoped skill caveat:** If the skill lives inside a workspace (`{workspace}/.claude/skills/`), workspace-relative paths are fine. The skill is intentionally coupled to the workspace.

## Principle 5: Gotchas Section Required

The agent's defaults are statistically reasonable but fail in non-average environments. Explicit gotchas capture domain-specific deviations.

Every skill body OR a referenced `gotchas.md` must include a section labeled **`## Gotchas`** (preferred) or `## Edge Cases` / `## What NOT to Do`. Standardize on `Gotchas`.

Each gotcha should state:
1. The trigger condition
2. The wrong default behavior
3. The correct behavior

**Example:**
```markdown
## Gotchas

- **Renamed files show as DELETE + ADD in `git log --name-status`.** Default agent reads this as a directory removal. Correct: detect ADD/DELETE pairs with matching content hashes; treat as rename.

- **Concurrent edits to INDEX.md.** Sub-agents writing in parallel can clobber each other. Correct: serialize INDEX.md writes through a single agent or use file locking.
```

If the gotcha list grows past ~10 items, extract to `references/gotchas.md` and link from body.

## Principle 6: Voice & Model Tuning Explicit

Skills tuned on one model are calibrated to that model's compliance characteristics, not just its capabilities. Sonnet may apply judgment to a stylistic instruction; Opus may follow it literally; Haiku may misread it.

If the skill prescribes a voice (caveman, prose, JSON-only, terse), document the model tier:

```markdown
## Style

- **Style directive:** caveman, full level
- **Tested on:** Sonnet 4.6, Opus 4.7
- **Model floor:** Sonnet 4 minimum (Haiku produces stilted output for caveman)
```

For procedural skills (no voice prescription), this section is optional.

**Anti-pattern:** "Use caveman style" with no model anchor. The first model upgrade silently drifts the output.

## Principle 7: Eval Harness for Non-Trivial Skills

Without a paired-run baseline, model upgrades degrade output silently.

Required for skills that:
- Prescribe voice or formatting
- Have a high-severity failure mode (silent revert, lost data, wrong file written)
- Are reused across many sessions

Minimum harness:
1. **Canonical input** — one representative input the skill should handle correctly
2. **Baseline output** — saved expected output (file or inline)
3. **Acceptance criteria** — what makes the output correct (regex, structural check, or human review note)

Storage convention: `{skill-dir}/eval/` or workspace `.claude/evaluations/{skill-name}/`.

When upgrading the host model: re-run the canonical input, diff against baseline, update baseline only if drift is intentional and approved.

**Anti-pattern:** Assuming a model upgrade preserves skill behavior. The Sonnet → Opus example in the source article shows it can break it.

## Antipattern Checklist

Run this against every new skill before merging:

| Antipattern | Check |
|---|---|
| Frontmatter on a ref file | `head -5 references/*.md \| grep -B1 '^---'` should be empty |
| Body > 500 lines | `wc -l SKILL.md` |
| Body > 100 lines without justification | Could content move to refs? |
| Hardcoded absolute paths | `grep -nE '^/(Users\|home)/\|~/[A-Z]' SKILL.md` |
| No Gotchas section | `grep -i 'gotchas\|edge cases\|what not' SKILL.md` |
| Voice prescription without model tier | Search for style/tone directives without "model" / "Sonnet" / "Opus" / "Haiku" |
| No eval baseline (for high-stakes skills) | `ls eval/` or `.claude/evaluations/{skill}/` |
| Description teaches instead of routing | Description >200 chars, contains examples or rules |
| Reference that does not resolve | `ls {skill-dir}/references/{file}` — a skill's references must live inside the skill directory |

## New-Skill Skeleton

Copy-paste starter for a new SKILL.md:

```markdown
---
name: skill-name
description: One sentence, action-oriented, when this skill should fire. Under 200 chars.
argument-hint: <required-arg> [optional-arg]
---

# Skill Name

> One paragraph describing what this skill does and when to use it.

## Constants

| Key | Value | Purpose |
|---|---|---|
| {workspace} | (workspace root) | Discovered via {method} |
| {ref dir} | `references/` | This skill's reference files |

## Workflow

1. Step one — terse imperative.
2. Step two — terse imperative.
3. For complex sub-protocol, see `references/{detail}.md`.

## Gotchas

- **Trigger condition.** Wrong default. Correct behavior.
- **Trigger condition.** Wrong default. Correct behavior.

## Style

- Style directive: {voice}
- Tested on: {model versions}
- Model floor: {minimum tier}

## Output

Define the expected output structure or template. Brief.

## Eval

Canonical input + baseline at `eval/` or `.claude/evaluations/{skill-name}/`.

## Quality Guidelines

Adhere to the quality guidelines in `library/reference/agent-quality-guidelines.md` and structural principles in `library/reference/skill-architecture.md`.
```

Companion `references/` files (each WITHOUT frontmatter):

- `gotchas.md` — when gotchas exceed 10 items
- `examples.md` — worked examples
- `template.md` — multi-line output templates
- `{sub-protocol}.md` — extracted detailed steps

## Migration Tips for Existing Skills

When restructuring an existing skill toward these principles:

1. **Audit body for extraction candidates** — multi-line templates, edge-case lists, sub-protocol steps. Move to refs.
2. **Verify refs have no frontmatter** — `head -5 references/*.md`. Strip if found.
3. **Add Gotchas section** — if absent, mine the project's incident logs / post-mortems for real failure modes.
4. **Specify model tier** — if voice is prescribed.
5. **Add eval baseline** — at minimum, one canonical input + expected output.
6. **Re-run skill on canonical input** — confirm restructure didn't change behavior.

## Applicability

| Principle | New skill | Existing skill review | Plugin skill (vendored) |
|---|---|---|---|
| 1. Frontmatter routing only | REQUIRED | REQUIRED | inspect, don't modify |
| 2. Body ceiling | REQUIRED | recommended (target ≤100 lines) | inspect, don't modify |
| 3. Refs no frontmatter | REQUIRED | REQUIRED | inspect, flag if violated |
| 4. Path discovery | REQUIRED | REQUIRED | inspect, don't modify |
| 5. Gotchas section | REQUIRED | recommended | inspect |
| 6. Voice/model tuning | when voice prescribed | when voice prescribed | inspect |
| 7. Eval harness | for high-stakes skills | recommended | n/a |
