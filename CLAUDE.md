# How to work in this repository

Read this before doing anything else here. It is the agent's operating instruction and the fellow's too.

## The one rule that is not negotiable

**`library/` is read-only.** You may read it, run it and copy from it. You may not edit it. Every file
in it is recorded, with a hash, in a provenance manifest kept outside this tree; editing a file here
breaks that record silently.

If a library file is wrong, report it. Do not repair it in place.

## Where things go

| You are doing | It goes in |
|---|---|
| Anything for a specific client | `engagements/<client-slug>/` |
| Coursework, exercises, practice interviews — anything with no client | `training/<module-id>/` |
| Interview notes, transcripts, session records | `engagements/<client-slug>/interview/` |
| The reconstructed process, its boundaries, its exceptions | `engagements/<client-slug>/process/` |
| The specification you are building | `engagements/<client-slug>/spec/` |
| The `skill.md` you hand over | `engagements/<client-slug>/deliverable/` |
| The owner-facing account, and the file the owner opens | `engagements/<client-slug>/handover/` |
| Something you will reuse on the next client — a question stem, a self-audit line | `reference/` |
| Something you were told must not leave the business | keep it out of git entirely: name the file `*.local.*`, which `.gitignore` already excludes, and record in the process notes that it exists and where it is |

The five engagement subdirectories are named for the five kinds of thing an engagement produces, not
for a sequence — a session fills `interview/` and `process/` in the same afternoon, and `interview/`
receives more material after `process/` has. File as you go; an engagement you file at the end is an
engagement you reconstruct from memory.

## Every directory carries an INDEX.md

One per directory, at every depth: **Purpose** in one or two sentences, an **Inventory** table listing
every item with a one-line description, and a **Freshness** table. When you create a file or a
directory, update the parent `INDEX.md` in the same operation. A sweep to fix this later is a sweep
that does not happen.

Spoke manifests declare their parent on line 1: `<!-- upstream: path/to/parent/INDEX.md -->`.

## Naming

| Casing | Meaning |
|---|---|
| `UPPERCASE.md` | A file a workflow requires structurally — `INDEX.md`, `CLAUDE.md` |
| `lowercase.md` | Content — notes, records, research |

Directories are kebab-case. Content files are snake_case or kebab-case, consistently within a directory.

## How to write

`library/sops/working-standards.md`. Four rules, one page. The one people break first: a code never
stands alone — write the thing, and bracket the code after it if it helps with filing.

## What the agent has

Ten skills in `library/skills/` (reached through the `.claude/skills` symlink), document shapes in
`library/templates/`, the renderers that turn finished work into a file the owner opens in
`library/renderers/`, four plugins you install yourself, three MCP servers on by default and three
more you connect per engagement with the client's own credentials — never ours. The full list with
reasons: `library/reference/tool-inventory.md`.

## When you finish an engagement

`engagements/<client-slug>/` is deletable as a unit, and that is deliberate: when a client relationship
ends, the material for that client goes with it. Anything worth keeping across clients is not client
material and belongs in `reference/`.
