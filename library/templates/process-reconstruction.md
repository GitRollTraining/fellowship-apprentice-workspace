---
style: descriptive
role: template
binds: library/playbooks/playbook-interview.md
serves: D-06, D-24, D-27
---

# Process reconstruction

Copy this file's marked blocks into the engagement. Do not edit it here — `library/` is read-only.
One process gets one set of four files.

| This template produces | Copy it to | Playbook step |
|---|---|---|
| The process, trigger to finished output, one block per step | `engagements/<client-slug>/process/process-<name>.md` | 7 |
| The exceptions, as named cases | `engagements/<client-slug>/process/exceptions.md` | 8 |
| The boundaries | `engagements/<client-slug>/process/boundaries.md` | 12 |
| What happens today when it breaks | `engagements/<client-slug>/process/failure-modes.md` | 13 |

`<name>` is the process in the owner's words, kebab-cased: `process-friday-wholesale-order.md`.

## Exception or failure mode

A beginner puts the same thing in both files. The test is what the owner treats it as.

| It is an exception | It is a failure mode |
|---|---|
| A different path the business intends. The work still finishes | The process does not produce its result, or produces a wrong one |
| The owner describes it as "what we do when..." | The owner describes it as "what went wrong" |
| Goes in `exceptions.md`, as a named case | Goes in `failure-modes.md` |

When it is genuinely both — a normal path that also fails often — write it as a case in `exceptions.md`
and cite that case name from `failure-modes.md`. Do not write it twice.

## Rules for all four files

1. **Everything traces back.** Each block names the rows in `engagements/<client-slug>/interview/discovery-record.md` it was built from — the heard rows are numbered `H1`, `H2` and the concluded rows `C1`, `C2` in that file. A block citing nothing is a block you wrote from memory.
2. **Marked inference only.** Anything you worked out rather than heard cites a concluded row. If it has no concluded row, write one there first.
3. **Gaps are visible, not blank.** Write `unknown — ask in the next session`. A blank field reads as "not applicable" to whoever picks this up.
4. **Push past "an experienced person decides".** The decision rules field is what the specification
   and deliverable are built from. A step with no decision rules cannot become executable behaviour.
5. **One real example, scrubbed.** A field shape with no example value is half the value. Remove names of people and customers; keep the numbers consistent with each other.
6. **Nothing you were told must not leave the business gets pasted in.** Record that the constraint exists and where the information lives — see the third boundary table.

Every table below carries one example row in italics, all from the same imagined engagement: a bakery's
weekly wholesale order to its flour supplier. Delete the italic rows.

---

<!-- copy from here into engagements/<client-slug>/process/process-<name>.md -->

## Process — {name in the owner's words}

Frontmatter for the file you are creating:

```yaml
---
style: descriptive
process: {name in the owner's words}
built-from: interview/discovery-record.md
---
```

### Header, once per process

| Field | Value |
|---|---|
| Process name, in their words | *the Friday wholesale order* |
| What starts it | the trigger, not the calendar entry. *Thursday's stock counts land on the sheet* |
| What "done" looks like | *the supplier's confirmation is filed in the orders folder* |
| Who runs it today | roles, not names |
| How often it runs | |
| How long it takes end to end | including the waiting |
| Today it is | done by hand / partly tooled / already automated — and describe what exists |
| Built from | rows in the discovery record. *H1, H4, H7* |
| Confirmed with the owner on | date, or `not yet` |

A process is confirmed by the owner inspecting and correcting the current-state confirmation materials,
not by the Fellow reading their own prose back and accepting a generic yes. A checked diagram is the
default when sequence, decisions, loops or handoffs matter; an atomic process may omit it with the reason
recorded under `library/templates/process-confirmation.md`.

### Step block — copy once per step

#### Step N — {short name}

| Field | Value |
|---|---|
| What comes in | the fields or documents, and one real example value |
| What goes out | the same, for what this step produces |
| How the output is made from the input | the procedure, in order |
| The rules used to decide | thresholds, cutoffs, rules of thumb, including ones they had never said out loud. Not *that* a judgment is made — *how* |
| Who has to look at it | role, what they decide, on what basis. `nobody` is an answer and gets written |
| Where the work waits | on whom, and for how long |
| Time and volume | minutes per run, and runs per week or month |
| What changes between runs | and what never changes |
| How anyone knows it came out right today | the check, and who does it |
| Here it is | done by hand / partly tooled / already automated |
| Exceptions that start here | case names in `exceptions.md`, or `none recorded` |
| Boundaries that bind here | row numbers in `boundaries.md`, or `none recorded` |
| Failures that start here | row numbers in `failure-modes.md`, or `none recorded` |
| Built from | rows in the discovery record |
| Still unknown | `unknown — ask in the next session`, never blank |

Tools, files and records this step touches:

| Tool, file or record | How it is reached | Read or written | Who else can get at it |
|---|---|---|---|
| *the stock count sheet* | *paper, on the clipboard by the mixer* | *read* | *the two morning bakers* |
| | | | |

### Quality rules for this file

1. One block per step. Do not collapse two steps into one block because they happen in the same minute.
2. Watch for the parts they skipped. People start stories in the middle and leave out what they do without thinking. When the account jumps, write the missing block and mark it `unknown — ask in the next session` rather than closing the gap yourself.
3. The steps are in the order they happen, not the order they were described.

<!-- copy to here -->

---

<!-- copy from here into engagements/<client-slug>/process/exceptions.md -->

## Exceptions — {process name}

Frontmatter for the file you are creating:

```yaml
---
style: descriptive
process: {name in the owner's words}
built-from: interview/discovery-record.md
---
```

Cases, not a category. "Sometimes there are exceptions" is not an answer, and does not go in this file.
One block per named case, named in the owner's words.

### Case: {name in the owner's words}

| Field | Value |
|---|---|
| What tells you the normal path does not apply | *the supplier's confirmation comes back short on rye* |
| Last actual time it happened | date or nameable occasion. **Required** |
| What was done instead, in order | |
| Which step it departs from | step number in the process file |
| Where it rejoins | step number, or `it does not — the run ends here` |
| How often | their words, plus any number they gave |
| Who decides it is this case | role, and what they look at |
| Built from | rows in the discovery record |

A case with no datable last occurrence is not a case yet. It goes in the table below instead, and it
does not get written into the specification.

### Named as possible, no instance behind it

| # | What they said | Pointer | The question to ask next |
|---|---|---|---|
| *X1* | *"sometimes they substitute a different mill"* | *recording 00:19:55* | *when did that last happen, and what did you do that day* |
| X2 | | | |

<!-- copy to here -->

---

<!-- copy from here into engagements/<client-slug>/process/boundaries.md -->

## Boundaries — {process name}

Frontmatter for the file you are creating:

```yaml
---
style: descriptive
process: {name in the owner's words}
built-from: interview/discovery-record.md
---
```

Three questions, asked out loud in the session, each with its own table. These do not come up on their
own, and the session is not finished without them. Record the answers, not the fact that you asked.

If the owner's answer is that there is nothing, write it as a quote with a pointer. **No answer recorded
is not the same as an answer of nothing**, and the difference decides whether an agent gets to act
unsupervised.

### 1. What must never be done automatically

| # | The thing | Why a person has to look at it, in their words | What would happen if it ran without one | Which step | Built from |
|---|---|---|---|---|---|
| *B1* | *placing the order once the total is over 800 dollars* | *"if I get that wrong I'm eating the flour for a month"* | *unreturnable stock, paid for* | *step 4* | *H12* |
| B2 | | | | | |

### 2. Who approves, and before what

| # | Approver, by role | What they approve | Before which step | What they check | When they are not available | Built from |
|---|---|---|---|---|---|---|
| *B3* | *the owner* | *the order total* | *step 4* | *the total against last week's* | *the order waits — "it has waited a day before"* | *H13* |
| B4 | | | | | | |

The unavailability column is the one beginners leave blank, and it is the one that decides what an
agent may do at three in the morning.

### 3. What must not leave the business

| # | The information | Where it lives | Who may see it | What "leaving" means for it | Built from |
|---|---|---|---|---|---|
| *B5* | *the per-kilogram price the mill charges* | *the supplier's emailed price list* | *the owner only* | *quoted to another supplier, or pasted into an agent's context* | *H15* |
| B6 | | | | | |

Record that the constraint exists and where the information lives. **Do not copy the information itself**
into this file, into the specification, into the deliverable, or into a prompt. "Leaving the business"
includes being pasted into an agent's context, and a beginner's first instinct is to paste it here so as
not to lose it.

If you were shown something you must not keep, write the row and note `not recorded, by instruction`
in place of the value.

<!-- copy to here -->

---

<!-- copy from here into engagements/<client-slug>/process/failure-modes.md -->

## What happens today when it breaks — {process name}

Frontmatter for the file you are creating:

```yaml
---
style: descriptive
process: {name in the owner's words}
built-from: interview/discovery-record.md
---
```

What the business does **today**, not what it should do and not what the deliverable will do. Three
questions, each with its own table.

### 1. When the information you need is missing or wrong

| # | The input | How you find out it is missing or wrong | What is done today | What that costs | Built from |
|---|---|---|---|---|---|
| *F1* | *Thursday's stock counts* | *the sheet is blank, or the numbers are last week's* | *count the store room by hand before opening* | *about 40 minutes, before a 5am shift* | *H9* |
| F2 | | | | | |

### 2. What has actually gone wrong before

| # | What went wrong | When | What it cost | How it was recovered | Built from |
|---|---|---|---|---|---|
| *F3* | *the order went in against the previous week's counts* | *late January* | *two days short of white flour* | *a same-day collection from a second mill, at a higher price* | *H10* |
| F4 | | | | | |

A row here needs a real occasion behind it. Something that could go wrong but never has is not a failure
mode yet — it is a question for the next session, and it goes in the ambiguity list.

### 3. What happens downstream, and who finds out

| # | Which step fails | Who is affected downstream | How they find out | How long before anyone notices | Built from |
|---|---|---|---|---|---|
| *F5* | *step 4, the order* | *the morning bakers, then the wholesale customers* | *the delivery is short on the Tuesday* | *four days* | *H11* |
| F6 | | | | | |

The last column is the one that sets how much an agent may be allowed to do unwatched. A failure found
in four days is a different risk from one found in four minutes.

<!-- copy to here -->

---

## Before you file these four

- Every block cites at least one row in the discovery record.
- Every step has decision rules, or is explicitly marked unknown.
- Exceptions are named cases with a datable last occurrence, not a category.
- All three boundary questions have recorded answers, including any answer of "nothing", quoted.
- Failure modes name what has actually gone wrong, not only what could.
- Nothing that must not leave the business has been pasted into any of the four files.
- The four files agree: every case, boundary and failure names a step number that exists in the process file.
- `engagements/<client-slug>/process/INDEX.md` updated in the same operation.
