# Interview Questions — wei-create-skill

Ask these in order. Capture answers literally. Do not infer silently — if the user says "skip" or "don't know", record that and adjust scaffolding (e.g., omit Eval section if user skips eval questions).

## Block 1: Identity (required)

1. **Slug.** "What's the kebab-case slug for this skill? (e.g., `wei-meeting-prep`, `gstack-ship`)"
   - Must match pattern `[a-z][a-z0-9-]*`.
   - Will be used as directory name AND `name:` frontmatter field.
   - If args provided, confirm.

2. **One-sentence purpose.** "In one sentence (≤200 chars), describe when this skill should fire. Action-oriented. Avoid examples."
   - Becomes `description:` field.
   - Probe if vague: "What user phrasing should trigger this?"

3. **Scope.** "Is this ours and reusable across engagements — `library/skills/` — or this client's, and part of what they receive?"
   - Default: user.
   - If project, confirm workspace root path.

3b. **Cross-workspace use.** "Will this skill be used from more than one repository — now or plausibly later?"
   - If yes → decide the sharing pattern per SKILL.md step 2a (fork / symlink owner-consumed / promote-with-routing) and record which pattern and why.
   - If promote → scope is user-level with a routing table (2b); ask the destination per workspace.
   - If the skill needs anything outside `.claude/skills/` (templates, scripts, venv, asset library) → promotion SOP §4 governs; name the owning workspace of each dependency.

## Block 2: Inputs (required)

4. **Argument contract.** "What arguments does the skill take? Format: `<required> [optional=default]`. Or 'none' if interactive."
   - Becomes `argument-hint:` field.
   - If 'none', omit the field entirely.

5. **Argument discovery.** "If a required argument is missing, what should happen — ask the user, or fail fast with an error message?"
   - Default: ask the user.

## Block 3: Workflow Outline (required)

6. **High-level steps.** "List the 3-7 main steps of the workflow. Imperative, terse. Bullet form is fine."
   - Will become numbered Workflow section.
   - If any step needs >5 lines of detail, flag it for ref extraction (Block 7).

## Block 4: Voice (optional)

7. **Voice prescription?** "Does the OUTPUT have a prescribed style (caveman, JSON-only, Notion-warm prose, terse procedural, etc.)? Yes/no."
   - If no → skip questions 8-9, omit `## Style` section from skeleton.

8. **Model anchor.** (only if 7 = yes) "Which model versions did you test on? What's the minimum model tier (Haiku 4.5 / Sonnet 4 / Sonnet 4.6 / Opus 4 / Opus 4.7)?"
   - Required if voice is prescribed.
   - Risk surfaced: "Voice prescriptions drift silently across model upgrades. Without an anchor, the next model swap may break this skill."

## Block 5: Stakes (optional but pushed)

9. **High-stakes?** "Can this skill cause silent failures with real cost? Examples: writing to wrong file, losing user data, reverting changes silently, sending external messages, modifying shared infrastructure. Yes/no."
   - If yes → eval harness required (Block 6).
   - If no → eval optional.

10. **Failure mode catalog.** (only if 9 = yes) "Name 1-3 specific failure modes you want to catch in eval."
    - Used to seed `eval/baseline-input.md` acceptance criteria.

## Block 6: Eval (required for high-stakes, optional otherwise)

11. **Canonical input.** "Give a representative input the skill should handle correctly. One example."
    - Saved verbatim to `eval/baseline-input.md`.

12. **Acceptance criteria.** "What makes the output correct? List 2-4 checks."
    - Examples: "Output is valid JSON", "Output mentions all team members listed in input", "Output preserves Mandarin verbatim quotes".

## Block 7: Gotchas (encouraged, not required)

13. **Known gotchas.** "Are there 1-3 known failure modes / edge cases / domain quirks the skill should encode upfront? Each: trigger condition + wrong default + correct behavior."
    - If ≥3 → write `references/gotchas.md` with these pre-filled.
    - If 1-2 → keep inline in body's `## Gotchas` section.
    - If 0 → still create `## Gotchas` heading w/ placeholder; better to discover and add later than to skip the section.

## Block 8: Refs to Pre-Create (optional)

14. **Multi-line templates / sub-protocols?** "Does any workflow step or output have a multi-line template, complex sub-protocol, or detailed sub-checklist? If so, name them — each becomes a `references/{name}.md`."
    - Common candidates: output template, error recovery, validation checklist, prompt composition.

## Block 9: Confirm

15. **Summary review.** Read back captured answers:
    - Slug: `{slug}`
    - Description: `{description}`
    - Scope: `{scope}` → `{target dir}`
    - Args: `{argument-hint or 'none'}`
    - Workflow: {N steps}
    - Voice: `{voice or 'none'}`
    - Stakes: `{high / low}`
    - Refs to create: `{list or 'none'}`

    "Proceed with scaffolding? (y/n)"
    - If n, ask which block to revisit.
    - If y, proceed to Workflow step 4 in main SKILL.md.

## Notes for the Creator Agent

- **Don't compress questions.** Each question exists because it shapes the scaffolding output. Skipping questions = silent defaults = same drift the architecture doc warns against.
- **Push back on vague answers.** "I'll figure it out later" for description = skill won't route. Insist on a concrete sentence.
- **Be terse in your prompts.** User wants to create the skill, not narrate. Caveman tone OK for the question prose.
