---
style: descriptive
role: template
serves: D-06, D-28
---

# Specification template

Destination: `engagements/<client-slug>/spec/specification.md`, one file per process specified. Copy
the block below out of this file; `library/` is read-only.

This template uses one `deliverable/skill.md` as the default delivery shape because that is the expected
common case. It does not require the final deliverable to be a single skill. Adapt or extend the
specification and deliverable structure when the agreed solution contains multiple skills, scripts,
integrations, services or a larger system; preserve the same traceability, boundary, acceptance and
review requirements.

The required chain, in this order:

| Artifact | File | Who reads it |
|---|---|---|
| The discovery record — what was heard, kept apart from what was concluded from it | `interview/discovery-record.md` | You, and anyone checking your work without you |
| The signed PRD — future behaviour, user stories, requirements and acceptance criteria | `spec/requirements.md` | The owner, the assessment engine, and you when you design |
| The automation decision brief — technical recommendation, Fellow decision and residual risk | `spec/automation-approach.md` | You, and anyone checking the design trade-offs |
| The specification — what will be built | `spec/specification.md` | The assessment engine, and you when you build |
| The deliverable — the thing that runs | `deliverable/skill.md` by default; the agreed package otherwise | The business |

Writing straight from the record or PRD to the deliverable skips the specification, which is the graded
build contract.
The assessment engine — the instrument that grades a fellow's work at a gate — reads the specification
as the evidence for nine of the twenty-five technical competencies. A competency is something a fellow
can be watched doing on a real task, producing an artifact you can point at. One of the nine has an
evidence entry that reads, in full, "the specification file".

## What this template owes, and what it does not

| Owed here | Owed elsewhere |
|---|---|
| The default document shape: which sections, in what order, what belongs in each, and the traceability chain that carries each statement back through the signed PRD to its source | The procedure for confirming the current process, obtaining PRD sign-off, resolving automation trade-offs and deciding when the work may advance |

That procedure is in `library/playbooks/playbook-discovery-to-deliverable.md`.

**Filling this shape does not prove that procedure was followed.** A specification can be correctly shaped, complete in
every section, every cell filled, and still assert a threshold, a deadline or a rule the owner never
gave. Nothing in this file detects that. The traceability column below makes the invention visible to a
reader who checks the pointer; it does not stop you writing it.

## Section order, and what each section becomes

The order is taken from the skeleton the deliverable is built from —
`library/skills/create-skill/references/skeleton.md`. Section for section, so building `skill.md` is
transcription rather than a second act of authorship.

| Section here | Where it lands in `skill.md` |
|---|---|
| The title, and the paragraph under it | The title, and the paragraph under it |
| Trigger | The `description:` line in the frontmatter; the title supplies `name:` |
| Inputs | The `Inputs` section, and the `argument-hint:` line in the frontmatter |
| Steps | The `Workflow` section |
| Exceptions | The `Gotchas` section |
| Boundaries | No single section. See below |
| Fixed values | The `Constants` section |
| Output | The `Output` section |
| Wording | The `Style` section, which is omitted entirely when nothing is prescribed |
| How the owner checks it | The `Eval` section |
| Open questions | Nowhere. They stay here |

For a larger agreed solution, keep this default as the behavioural core and add a component table rather
than inventing a new template family:

| Component | Responsibility | Interface or handoff | PRD/spec responsibilities | Operator and deployment | Recovery or rollback | Verification |
|---|---|---|---|---|---|---|
| `<service, skill, script or integration>` | `<what this component alone owns>` | `<input/output or dependency>` | `<US/R/AC IDs and spec section>` | `<who runs and maintains it, and where>` | `<how a failed change is contained or reversed>` | `<test or check>` |

Extend the example only as the solution requires. It is a reminder about component boundaries,
deployment, ownership, recovery and test evidence, not a complete system-architecture method.

## Where the mapping is not one to one

Four places. Each is a decision, not an oversight.

1. **Boundaries have no section in the skeleton.** What must not be automated, who approves, and what
   may not leave the business constrain what the deliverable is allowed to do rather than describing
   what it does. In `skill.md` they land in three places: a stop condition among the gotchas, an
   approval step in the workflow, and a named value among the constants. Keep them as one section here
   anyway. They are elicited as one thing, and splitting them across three sections of the deliverable
   is how a boundary goes missing.
2. **Open questions travel nowhere.** A current-state ambiguity stays in `interview/ambiguities.md`, a
   desired-behaviour question stays in `spec/requirements.md`, and a technical question stays in
   `spec/automation-approach.md` and the Decision Register. An open question written into `skill.md`
   becomes an instruction with a hole in it that nothing marks.
3. **A section that outgrows the page moves to a companion file.** The skeleton's rule is that detail
   running past five to ten lines belongs in `references/<name>.md` beside the `SKILL.md`, not in it.
   Exceptions overflow first, into `references/gotchas.md`. The specification is not subject to that
   rule — write it in full here and split at the build.
4. **The last section of `skill.md` is fixed boilerplate.** It points at
   `library/reference/agent-quality-guidelines.md` and `library/reference/skill-architecture.md`. The
   specification supplies nothing for it.

## The traceability column

Every behavioural table ends with a `Trace` column. It names the signed PRD item and its origin, for
example `R-004 <- H17`. A technical choice also names the current decision, for example
`R-004; AA-003`. Pure display or routing wording that asserts no business fact may say `authored`.

The full chain is:

```text
session pointer -> discovery H/C row -> PRD US/R/AC item
  -> specification section -> deliverable component -> verification
```

Five rules govern it.

- **Every hop resolves.** The discovery row carries the session pointer; the PRD item carries the
  discovery or durable-confirmation source; the specification carries the PRD ID. A long chain with one
  broken hop is not traceability.
- **The signed PRD is the behavioural authority.** A specification may not point at a raw statement to
  bypass a requirement the owner rejected or changed during sign-off.
- **A Fellow conclusion cannot cross the sign-off gate alone.** A `C*` origin reaches the specification
  only through a PRD version that records the owner's confirmation.
- **Open questions do not become instructions.** Resolve them before their named gate or keep them out of
  the specification.
- **Check every number against its origin.** Thresholds, deadlines, counts and prices are the most likely
  details to acquire precision nobody stated.

## The template

```markdown
---
style: descriptive
client: <client-slug>
process: <the owner's name for the process>
status: draft
requirements: spec/requirements.md v<n>, signed-off YYYY-MM-DD
automation-approach: spec/automation-approach.md, reviewed YYYY-MM-DD
---

# <The owner's name for the process>

<One paragraph, plain words: what this process does, for whom, and what comes out of it. This paragraph
becomes the paragraph under the title of skill.md.>

## Trigger

| Field | Value | Trace |
|---|---|---|
| Fires when | <the event that starts it> | <US/R ID> <- <H row or confirmation> |
| Fires how often | <a count and a period, or on demand> | <R ID> <- <H row or confirmation> |
| One sentence for the router | <Use when ..., 200 characters or fewer> | authored |

## Inputs

| Input | Where it comes from | Required | If it is missing | Trace |
|---|---|---|---|---|
| <name> | <person, inbox, system, file> | yes | <ask, halt, or a named default> | <US/R ID> <- <source> |

## Steps

| # | Step | Done when | Trace |
|---|---|---|---|
| 1 | <one action, imperative> | <a result the owner can see without you> | <US/R ID>; <AA ID if technical> |
| 2 | | | |

## Exceptions

| Case | How you know it is this case | What to do | Trace |
|---|---|---|---|
| <the owner's name for the case> | <the observable sign> | <the action> | <R/AC ID> <- <source> |

## Boundaries

| Boundary | Statement | Trace |
|---|---|---|
| Must not be automated | <what stays a person's job, and whose> | <R ID>; <AA-005> |
| Needs approval | <what needs it, and who gives it> | <R ID>; <AA-005> |
| Must not leave the business | <what, and where it may go instead> | <R ID>; <DR-001/AA-002> |

## Fixed values

| Key | Value | Trace |
|---|---|---|
| <threshold, deadline, address, name> | <the signed value> | <R ID> <- <source> |

## Output

| Field | Value | Trace |
|---|---|---|
| What comes out | <the artifact, named as the owner names it> | <US/R ID> <- <source> |
| Where it goes | <file, inbox, system, person> | <R ID>; <AA/DR ID if technical> |
| What good looks like | <the observable> | <AC ID> <- <source> |

## Wording

Delete this section if nothing outside the business reads the output.

| Rule | Statement | Trace |
|---|---|---|
| Words that must appear | <the words> | <R ID> <- <source> |
| Words that must not appear | <the words> | <R ID> <- <source> |
| Greeting and sign-off | <as the owner writes them> | <R ID> <- <source> |

## How the owner checks it

| Check | Right looks like | Wrong looks like | Trace |
|---|---|---|---|
| <what the owner looks at> | <observable> | <observable> | <AC ID> <- <source> |

## Traceability matrix

Every signed PRD item appears once. `Disposition` is `implemented`, `deferred — owner accepted`, or
`not-applicable — <reason>`.

| PRD item | Origin | Disposition | Specification section | Deliverable component | Verification |
|---|---|---|---|---|---|
| <US/R/AC ID> | <H/C row or durable confirmation> | <controlled value> | <heading or step> | <file/component/responsibility> | <AC ID, test or check> |

## Open questions

| Question ID and source | Who settles it | Blocks before | Status |
|---|---|---|---|
| <OQ ID from PRD, or technical question from the brief> | <owner, Fellow or named role> | <specification/build/deploy/none> | <open/resolved/deferred> |
```

## Before the build

- The PRD version in frontmatter is signed off and the automation brief is current against it.
- Every behavioural table has a `Trace` column and no cell in it is empty.
- Every signed PRD item appears in the traceability matrix with a disposition.
- Every pointer resolves through the PRD to discovery evidence or durable owner confirmation.
- No open question has reached the gate it blocks.
- Every step's "Done when" is observable by the owner without you in the room.
- Every exception is a case the owner named. An exception you imagined is a conclusion, and it is
  traced as one or it is cut.
- Every number has been checked against its pointer for precision the owner did not give.
- The section order matches the table above, so the build is transcription.
- The draft `skill.md` goes through the adversarial reviewer persona
  (`library/personas/adversarial-reviewer.md`) before it goes anywhere near the owner. Finding disposition
  is defined in `library/playbooks/playbook-discovery-to-deliverable.md`.

If this file is ever rendered to a PDF, the renderer's input contract is in
`library/templates/handover.md`.
