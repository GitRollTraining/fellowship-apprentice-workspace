# Root blocks — setup

The exact text step 3 adds at the repository root. Copy each block byte for byte, including the two
marker lines. The start marker is how a later run knows the block is already there.

## `AGENTS.md` (Codex reads this at the start of every session)

If the file does not exist, create it containing only the block. If it exists and does not contain
the start marker, append a blank line and then the block.

```markdown
<!-- apprentice-workspace: start -->
## Apprentice workspace

This repository holds an AI Fellowship apprentice workspace in `apprentice-workspace/`. Before you
read, file or write anything there, read `apprentice-workspace/AGENTS.md` and follow it: it says where
each kind of work goes and what must never be edited. The skills, playbooks and templates it names
come from the installed `apprentice-workspace` plugin.
<!-- apprentice-workspace: end -->
```

## `CLAUDE.md` (Claude Code reads this at the start of every session)

If the file exists and does not contain the start marker, append a blank line and then the block.

If the file does not exist, create it with this first line, a blank line, and then the block:

```markdown
@AGENTS.md
```

That first line keeps Claude Code reading the repository's `AGENTS.md`, which it stops doing on its
own once any `CLAUDE.md` exists.

The block:

```markdown
<!-- apprentice-workspace: start -->
## Apprentice workspace

@apprentice-workspace/AGENTS.md
<!-- apprentice-workspace: end -->
```

The `@` line makes Claude Code load the workspace rules into every session in this repository.
