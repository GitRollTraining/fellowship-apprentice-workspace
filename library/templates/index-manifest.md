---
style: descriptive
role: template
produces: INDEX.md
---

# INDEX.md — the directory manifest

`CLAUDE.md` requires one `INDEX.md` in every directory, at every depth. This file gives the format and
defines the words in it.

## When it is written

| Event | What happens to the manifest |
|---|---|
| You create a directory | Create its `INDEX.md` in the same operation |
| You add, rename or delete a file | Update that directory's `INDEX.md` in the same operation |
| You move a directory | Update the upstream pointer on line 1, and the manifest of the directory it now sits under |

A manifest updated later is a manifest updated never.

## The shape

```markdown
<!-- upstream: {root-relative path to the parent INDEX.md} -->
---
style: descriptive
---

# {directory name}

## Purpose

{One or two sentences: what this directory is for and what belongs in it. Write it so that someone who
has never opened the directory can decide whether their file goes here.}

## Inventory

| Item | What it is | Class |
|---|---|---|
| `some-file.md` | {one line: what it is, not what is inside it} | Mutable |
| `some-directory/` | {one line: what it holds} | Mutable |

## Freshness

| Item | Last updated | Class | Status |
|---|---|---|---|
| `some-file.md` | 2026-05-14 | Mutable | current |
| `some-directory/` | 2026-05-14 | Mutable | empty until the first session |

## Conventions

{Only if this directory has a rule of its own: a file-naming pattern, a class most files here take, a
filing rule. Omit the whole section when there is nothing to say.}
```

## Line 1: the upstream pointer

The first line of every manifest names the manifest one level up, as an HTML comment:

    <!-- upstream: engagements/example-client/INDEX.md -->

- The path is written from the repository root, never as `../INDEX.md`. A relative path stops being
  true the moment the directory moves.
- It goes above the frontmatter, on line 1, so that one search across the repository returns the whole
  parent-child map.
- The repository's own root `INDEX.md` carries no pointer. It is the top.

## Purpose

One or two sentences. It answers "what goes in here", not "what is in here right now" — the Inventory
answers that, and it changes weekly.

## Inventory

Every file and every subdirectory appears, one row each. No exceptions.

| Column | What goes in it |
|---|---|
| Item | The file or directory name, in backticks. Directories end with `/` |
| What it is | One line, roughly eighty characters or fewer. What the item is, not a summary of its contents |
| Class | One of the four values below |

An empty directory does not need an empty table. One line is enough, and saying where the files will
come from is more useful than a row of dashes:

    Empty. Files land here as you run the interview playbook — see
    `library/playbooks/playbook-interview.runbook.md` for which step produces which file.

## Freshness

The same items, answering a different question: is this current, and should I trust it.

| Column | What goes in it |
|---|---|
| Item | Same name as in the Inventory. Rows may be grouped where one sentence is true of all of them — `all five`, `everything under library/` |
| Last updated | The date the content last meaningfully changed. Not the date you fixed a typo |
| Class | Same value as in the Inventory |
| Status | Short free text, honest. `current`, `empty`, `first draft`, `sent to the owner on 2026-05-14`, `superseded by process-ordering-v2.md`, `append-only, one line per session` |

Status is the column that earns the table. "Last updated: 2026-05-14" tells a reader nothing about
whether the file can be relied on; "first draft, not read back to the owner yet" does.

## Class — the four values

| Class | Use it for | Example in this repository |
|---|---|---|
| Mutable | The default. Content that changes as work continues | your engagement notes, a reconstructed process |
| Immutable | Frozen when created, never rewritten | an interview recording, a session record, a version of a document already sent to the owner |
| Instruction | Tells a person or an agent how to work | `CLAUDE.md`, everything under `library/` |
| Data | A structured file something reads mechanically | `.claude/settings.json`, an export from the business's own software |

Anything you cannot place is Mutable. Do not invent a fifth value; if four are genuinely not enough,
report it rather than adding one locally.

## Rules

1. Every file and subdirectory is listed. A file nobody catalogued is a file nobody finds.
2. Descriptions are one line. The manifest is a way of finding things, not documentation of them.
3. Hidden and tool-owned directories are left out: `.git/`, `.claude/`.
4. Bump the dates on the rows you touched, and only those.
5. Manifests under `library/` are read-only, like everything else there. If one is wrong, report it.
