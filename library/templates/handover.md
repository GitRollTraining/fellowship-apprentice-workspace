---
style: descriptive
role: template
serves: D-29
produces: engagements/<client-slug>/handover/owner-account.md
---

# Owner Account Template

Use this template after Validator A passes, through `library/playbooks/playbook-output-phraser.md`. It
creates the account a non-technical owner reads to understand what was delivered, what remains human,
what to check and where to go when it fails.

The account is not the implementation, specification or internal validation report. The exact
`deliverable/` tree travels beside it in the client package.

## What travels and what does not

The default handoff is one versioned zip containing:

```text
<client>-handover-v<n>/
  owner-account.pdf
  package-manifest.md
  deliverable/
    <the exact implementation that passed Validator A>
    deployment.md
    operations.md
    known-defects.md          # when present
    <client verification>    # when practical
```

Do not place interview records, requirements, specification, Decision Register, source map, persona or
owner-acceptance records, Validator reports, evidence or progress logs in that zip.

Do not concatenate delivery files into the account. A PDF cannot preserve a multi-file executable
structure and becomes a stale second copy. The account explains where to start; canonical installation,
rollback, recovery and credential instructions remain in `deliverable/deployment.md` and
`deliverable/operations.md`.

## Register: their words, not yours

Read `library/reference/explanation-style.md` through the `explain` skill before writing. These rules are
load-bearing:

1. Use the words the owner used. Define any necessary new word at first use in their terms.
2. Carry one real instance from confirmed discovery through the whole account; retire it when it would
   assert unsupported behaviour.
3. State what was expected before what happens, so the owner can judge a result.
4. Convert abstract rates into counts when the source permits and pair every number with its comparison.
5. Say limitations, human approvals and failure behaviour directly. Reassurance is not explanation.
6. Point to canonical operating files rather than reproducing them.
7. Give every material claim an internal `HC-*` source-map row and invisible comment anchor.

## Rendering contract

For a prose-and-table account, write markdown and compile it with
`library/renderers/build-document-pdf.py`; verify with `check-document-pdf.py` and inspect every page.
The markdown is the authoring source. Never hand-edit the PDF.

The file must have:

- frontmatter beginning on line 1, including a quoted `footer:` value;
- exactly one H1 title;
- one plain paragraph immediately after the H1 so the renderer has a subtitle;
- a dashed separator row under every table header and the same number of cells in every row; and
- the invisible source-map pointer immediately after frontmatter.

If the account genuinely needs a single-page visual layout or embedded diagram, use
`library/templates/brief-design/` to create one self-contained HTML source instead. Do not maintain the
same account in both markdown and HTML.

## Owner-account output

Copy and complete the block below. The `HC-*` examples are internal comments and must not appear in the
rendered PDF text.

--- COPY FROM HERE ---

```markdown
---
style: explanation
footer: "<business name> — <their name for the delivered process>"
client: <client-slug>
package-version: <v1>
---
<!-- handoff-source-map: ../verification/handoff-source-map.md -->

# <Their name for the delivered process>

<One sentence directly under the title: what was delivered and who it is for.>

<!-- claim: HC-001 -->
## What you have received

<Name the owner account, the `deliverable/` folder and the package manifest in the owner's terms. Say
that this account explains the work while the files in `deliverable/` perform it.>

| Start with | What it is for |
|---|---|
| This account | Understand the result, boundaries, checks and failure route |
| `deliverable/deployment.md` | Install, configure, upgrade, roll back or remove it |
| `deliverable/operations.md` | Run, monitor, recover, rotate access and escalate |

<!-- claim: HC-002 -->
## What it does

<Carry one real instance from the owner's work from trigger to visible result. Use only validated future
behaviour.>

| Step | What happens | What the owner sees or does |
|---|---|---|
| 1 | | |

<When sequence, branching, handoff or recovery matters to owner operation, embed the checked future-state
flowchart here. Do not add one for parallel facts.>

<!-- claim: HC-003 -->
## What it will not do

| It will not | What happens instead | Who decides or acts |
|---|---|---|
| | | |

<!-- claim: HC-004 -->
## What to check

| Check | When | Right looks like | Wrong looks like |
|---|---|---|---|
| | | | |

<!-- claim: HC-005 -->
## When it goes wrong

| What the owner sees | First action | When and where to escalate |
|---|---|---|
| | | |

<Point to the exact recovery section in `deliverable/operations.md`; do not copy the complete procedure.>

<!-- claim: HC-006 -->
## Who owns what

| Responsibility | Owner | When it needs attention |
|---|---|---|
| Installation and configuration | | |
| Routine operation and checking | | |
| Credentials and access | | |
| Maintenance, upgrades and ongoing cost | | |
| Escalation when recovery fails | | |

<!-- claim: HC-007 -->
## Known limits

<State every applicable known defect or accepted limitation in plain words, what case it changes and
what the owner should do. Point to `deliverable/known-defects.md` when present. Do not claim “none” merely
because no file exists.>

## The words used here

| Word | What it means in this business |
|---|---|
| | |
```

--- COPY ENDS HERE ---

## Before it leaves Output Phraser

- The delivery manifest still matches Validator A.
- Every `HC-*` anchor has one source-map row and every material source-map row has an anchor.
- The account makes no stronger claim than its authority and no inference looks like an owner quote.
- Deployment, operations, limitations, client verification and ownership are reachable from the account.
- Source-map comments are absent from rendered prose.
- The applicable deterministic renderer or brief checks passed, and the rendered output was inspected.
- `handover/package-manifest.md` matches the candidate zip inventory.

Passing this list means ready for the mandatory persona preflight. It is not owner acceptance or
Validator B approval.
