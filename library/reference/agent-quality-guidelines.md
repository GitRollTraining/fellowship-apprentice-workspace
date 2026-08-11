# Agent & Skill Quality Guidelines

> All agents and skills MUST follow these principles.
> Reference: `@references/agent-quality-guidelines.md`

## Principle 0: Delegate to Sub-Agents

Protect the main context window by offloading discrete, independent work to sub-agents.

Use sub-agents when:
- Research or exploration may produce large outputs
- Multiple independent queries can run in parallel
- A task is self-contained and doesn't need ongoing dialogue with the user

Do not use sub-agents when:
- The task is a simple, directed search (use Glob/Grep directly)
- The result is needed immediately for a dependent next step and a tool call suffices
- Spawning an agent would add overhead without saving context

Anti-pattern: Performing broad searches or multi-file analysis in the main context, then running out of room for the actual implementation.

## Principle 1: Build-Verify Loop

Never mark work complete without verification.

Before declaring a task done:
1. Re-read the original requirement/goal
2. Run any available verification command (test suite, type check, build)
3. Compare output against the requirement — not just "does it exist" but "does it work"
4. If no automated verification exists, perform a manual checklist:
   - Files created/modified match what was requested
   - No orphaned imports, unused variables, or broken references
   - Code compiles/parses without errors

Anti-pattern: Reading your own output and deciding it "looks correct" without running it.

## Principle 2: Doom Loop Detection

Detect and break out of repetitive edit cycles.

Track which files you modify during execution. If you edit the same file 3+ times:

1. Stop editing immediately
2. Re-read the original task specification
3. State explicitly: (a) What the file should accomplish, (b) What issue has required multiple edits, (c) Whether a different approach would resolve this
4. Choose: rewrite from scratch, escalate to user, or pivot strategy

Anti-pattern: Making incremental patches to the same file hoping each one fixes the issue.

## Principle 3: Write Tests

When creating or modifying functional code:
1. Check if the project has an existing test framework and conventions
2. Write tests covering: happy path, edge cases, error conditions
3. Run tests and confirm they pass
4. If modifying existing code, run existing tests first as baseline

Skip when: Documentation changes, configuration files, one-line fixes with obvious correctness.

## Principle 4: Review & Validate Before Exit

Before finishing, answer these questions:
1. **Completeness:** Does the output address every part of the request?
2. **Correctness:** Would this work in production, not just in isolation?
3. **Wiring:** Are new components connected to the rest of the system?
4. **Simplicity:** Is this the minimum viable solution, or did scope creep occur?
5. **Side effects:** Did you modify anything outside the scope of the request?

If any answer is "no" or "unsure": fix it before completing.

## Principle 5: Reasoning Sandwich

Invest thinking time unevenly: heavy at start and end, light in the middle.

- **Start:** Carefully analyze requirements, identify ambiguities, plan approach
- **Middle:** Execute efficiently — don't over-deliberate on mechanical steps
- **End:** Carefully verify output against original requirements

## Principle 6: Context Before Action

Before writing code in an unfamiliar area:
1. Read the files you'll modify (the whole file, not just the function)
2. Check for existing patterns, conventions, and related code
3. Identify test files, configuration, and integration points
4. If a codebase snapshot or architecture doc exists, read it first

## Applicability

| Principle | Code-writing agents | Review/research agents | File-modifying skills | Plan-generating skills |
|---|---|---|---|---|
| Build-Verify Loop | REQUIRED | recommended | REQUIRED | recommended |
| Doom Loop Detection | REQUIRED | n/a | REQUIRED | n/a |
| Write Tests | REQUIRED | n/a | when applicable | n/a |
| Review & Validate | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| Reasoning Sandwich | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| Context Before Action | REQUIRED | REQUIRED | REQUIRED | recommended |
