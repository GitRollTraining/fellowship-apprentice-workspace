---
style: descriptive
role: template
serves: D-06, D-28
---

# Specification template

Destination: `engagements/<client-slug>/spec/specification.md`, one file per process specified. Copy
the block below out of this file; `library/` is read-only.

Three artifacts, in this order:

| Artifact | File | Who reads it |
|---|---|---|
| The discovery record — what was heard, kept apart from what was concluded from it | `interview/discovery-record.md` | You, and anyone checking your work without you |
| The specification — what will be built | `spec/specification.md` | The assessment engine, and you when you build |
| The deliverable — the thing that runs | `deliverable/skill.md` | The business |

Writing straight from the record to the deliverable skips the middle artifact, which is the graded one.
The assessment engine — the instrument that grades a fellow's work at a gate — reads the specification
as the evidence for nine of the twenty-five technical competencies. A competency is something a fellow
can be watched doing on a real task, producing an artifact you can point at. One of the nine has an
evidence entry that reads, in full, "the specification file".

## What this template owes, and what it does not

| Owed here | Owed elsewhere |
|---|---|
| The document shape: which sections, in what order, what belongs in each, and the traceability column that carries each statement back to the record | The procedure for turning a heard statement into a specified instruction without the instruction acquiring precision nobody stated |

That procedure is owed by `library/playbooks/playbook-elicitation-to-sop.md`, which is a **stub**: its
contents are specified, it is not written.

**Filling this shape does not close that stub.** A specification can be correctly shaped, complete in
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

## Where the mapping is not one to one

Four places. Each is a decision, not an oversight.

1. **Boundaries have no section in the skeleton.** What must not be automated, who approves, and what
   may not leave the business constrain what the deliverable is allowed to do rather than describing
   what it does. In `skill.md` they land in three places: a stop condition among the gotchas, an
   approval step in the workflow, and a named value among the constants. Keep them as one section here
   anyway. They are elicited as one thing, and splitting them across three sections of the deliverable
   is how a boundary goes missing.
2. **Open questions travel nowhere.** They stay in the specification and, unresolved, in
   `interview/ambiguities.md`. An open question written into `skill.md` becomes an instruction with a
   hole in it that nothing marks.
3. **A section that outgrows the page moves to a companion file.** The skeleton's rule is that detail
   running past five to ten lines belongs in `references/<name>.md` beside the `SKILL.md`, not in it.
   Exceptions overflow first, into `references/gotchas.md`. The specification is not subject to that
   rule — write it in full here and split at the build.
4. **The last section of `skill.md` is fixed boilerplate.** It points at
   `library/reference/agent-quality-guidelines.md` and `library/reference/skill-architecture.md`. The
   specification supplies nothing for it.

## The traceability column

Every table ends with a `Trace` column holding two things: which entry of the discovery record the
statement came from, and one of four words.

| Word | What it means | May it reach the deliverable |
|---|---|---|
| heard | The owner said it, and the discovery record points at the turn, the timestamp or the document it came from | Yes |
| concluded | You worked it out from what was heard, and the discovery record marks it as concluded rather than heard | Yes, once the owner has confirmed it, at which point the confirmation is itself a new heard entry with its own pointer |
| open | Nobody has settled it | No. It belongs in Open questions until it becomes one of the two above |
| authored | Wording you wrote yourself — the display name, the one-sentence trigger. It asserts no fact about the business | Yes |

Four rules govern the column.

- **Point at the discovery record entry, not at the session.** The record is what carries the session
  pointer and what keeps heard apart from concluded. Two hops, each of which resolves.
- **A pointer that does not resolve is worse than no pointer.** Step 16 of `library/playbooks/playbook-interview.md`
  makes that a fail rather than a blemish, and filing the specification here makes it checkable.
- **A row with an empty trace is a conclusion wearing a heard statement's clothes.** Mark it
  `concluded` and confirm it, or delete the row.
- **A number is the most likely thing to be invented.** Thresholds, deadlines, counts and prices carry
  the highest risk of arriving in the specification more precise than anything the owner said. Check
  each one against its pointer before the build.

## The template

```markdown
---
style: descriptive
client: <client-slug>
process: <the owner's name for the process>
status: draft
---

# <The owner's name for the process>

<One paragraph, plain words: what this process does, for whom, and what comes out of it. This paragraph
becomes the paragraph under the title of skill.md.>

## Trigger

| Field | Value | Trace |
|---|---|---|
| Fires when | <the event that starts it> | <record entry>, heard |
| Fires how often | <a count and a period, or on demand> | <record entry>, heard |
| One sentence for the router | <Use when ..., 200 characters or fewer> | authored |

## Inputs

| Input | Where it comes from | Required | If it is missing | Trace |
|---|---|---|---|---|
| <name> | <person, inbox, system, file> | yes | <ask, halt, or a named default> | <record entry>, heard |

## Steps

| # | Step | Done when | Trace |
|---|---|---|---|
| 1 | <one action, imperative> | <a result the owner can see without you> | <record entry>, heard |
| 2 | | | |

## Exceptions

| Case | How you know it is this case | What to do | Trace |
|---|---|---|---|
| <the owner's name for the case> | <the observable sign> | <the action> | <record entry>, heard |

## Boundaries

| Boundary | Statement | Trace |
|---|---|---|
| Must not be automated | <what stays a person's job, and whose> | <record entry>, heard |
| Needs approval | <what needs it, and who gives it> | <record entry>, heard |
| Must not leave the business | <what, and where it may go instead> | <record entry>, heard |

## Fixed values

| Key | Value | Trace |
|---|---|---|
| <threshold, deadline, address, name> | <the value, as the owner stated it> | <record entry>, heard |

## Output

| Field | Value | Trace |
|---|---|---|
| What comes out | <the artifact, named as the owner names it> | <record entry>, heard |
| Where it goes | <file, inbox, system, person> | <record entry>, heard |
| What good looks like | <the observable> | <record entry>, heard |

## Wording

Delete this section if nothing outside the business reads the output.

| Rule | Statement | Trace |
|---|---|---|
| Words that must appear | <the words> | <record entry>, heard |
| Words that must not appear | <the words> | <record entry>, heard |
| Greeting and sign-off | <as the owner writes them> | <record entry>, heard |

## How the owner checks it

| Check | Right looks like | Wrong looks like | Trace |
|---|---|---|---|
| <what the owner looks at> | <observable> | <observable> | <record entry>, heard |

## Open questions

| Question | Who settles it | Blocks the build |
|---|---|---|
| <the unsettled item, carried from interview/ambiguities.md> | <the owner, you, nobody yet> | yes |
```

## Before the build

- Every table has a `Trace` column and no cell in it is empty.
- No row traces to `open`. Each of those is a row in Open questions instead.
- Every step's "Done when" is observable by the owner without you in the room.
- Every exception is a case the owner named. An exception you imagined is a conclusion, and it is
  traced as one or it is cut.
- Every number has been checked against its pointer for precision the owner did not give.
- The section order matches the table above, so the build is transcription.
- The draft `skill.md` goes through the adversarial reviewer persona
  (`library/personas/adversarial-reviewer.md`) before it goes anywhere near the owner. What to do with
  each finding, by severity, belongs to `library/playbooks/playbook-elicitation-to-sop.md` and is not
  settled here.

If this file is ever rendered to a PDF, the renderer's input contract is in
`library/templates/handover.md`.
