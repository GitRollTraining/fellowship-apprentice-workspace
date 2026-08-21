---
style: descriptive
role: template
produces: engagements/<client-slug>/spec/source-data-survey.md
---

# Source data survey

What you found when you opened the data the automation will actually operate on. Written before the
specification, because a rule that is in the data and was never discussed cannot be traced afterwards.

It is not analysis and it is not a proposal. It records fields, values, and the gaps between the data
and the confirmed process.

## Where it goes

- File: `engagements/<client-slug>/spec/source-data-survey.md`.
- Written at step 7 of `library/playbooks/playbook-discovery-to-deliverable.md`, before
  `spec/specification.md`.
- Anything the owner confirms from here enters the PRD. Anything they do not confirm becomes a row in
  `interview/ambiguities.md`.

## Frontmatter for the output

```yaml
---
style: descriptive
client: {client-slug}
sources: [{file, export, inbox or folder, one per line}]
read: YYYY-MM-DD
---
```

## The shape

### Sources

| Source | What it is | How many rows or items | Where it came from |
|---|---|---|---|

### Fields the automation reads

| Field | Actual values seen | What empty means | Trace |
|---|---|---|---|

`Trace` names the PRD item that needs the field, or `unstated` when nothing in the signed requirements
asks for it.

### Rules visible in the data that nobody stated

| Rule | Where it is visible | Asked the owner | Their answer |
|---|---|---|---|

A confirmed rule enters the PRD and its specification row carries
`<R-* ID>; in-data <- <source and field>`. An unconfirmed rule does not enter the specification at all.

### Where the data contradicts the confirmed process

| Confirmed statement | What the data shows | Raised on | Disposition |
|---|---|---|---|

## When there is nothing to survey

If the deliverable reads no existing data, write this file anyway with one line saying so. An absent
file and a deliberate `not applicable` look identical six weeks later.
