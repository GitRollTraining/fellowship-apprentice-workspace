# Routing — where a digest gets filed, per workspace

This skill is **user-level**, so it runs in every workspace. Filing destinations are therefore not
hardcoded in the spine: they are resolved from the workspace you were invoked from.

> Wei, 2026-07-27: *"different triggering sources should drive different behaviors for the same
> skill."* Same principle as `workspace.sh` for the transcription skills — trigger source decides.
> It is also preference #17 rule 2: configuration lives in the workspace and is read at runtime,
> never typed on the command line. There is deliberately **no `--dest` flag**.

## Step 0 — resolve the workspace

```bash
bash ~/.claude/scripts/workspace.sh    # -> "<name>\t<root>", exit 1 if unrecognized
```

Exit 1 means you are somewhere this skill has no routing for. **Stop and report** — do not guess a
root and do not fall back to the current directory. A digest written into the wrong repo is worse
than no digest, and in operations it can put client material somewhere it does not belong.

## Destinations

`govdoc` never needs this table: its output goes beside the source document, which is already
resolved from the input path.

`article` needs it, because a URL-sourced article has no source directory.

| Workspace | `article` filing home | Naming | INDEX to update |
|---|---|---|---|
| `itsweikuo` | `notes/article-summaries/` | `{YYYY-MM-DD}_{title-slug}.md`, date = filed/retrieved | `notes/article-summaries/INDEX.md` |
| `operations` | topical research dir whose INDEX declares covering scope — external AI/agent-technique intel → `agent-operations/research/`; client-facing architecture research → `engineering/ai-infra/` subtree | that directory's stated convention; `agent-operations/research/` uses `{YYYY-MM-DD}_{slug}.md` | that directory's `INDEX.md` |

In operations, if no directory fits, **propose one** rather than inventing a sibling
(`feedback_consolidate_related_research`). In itsweikuo there is one home and no such judgment call.

`govdoc` in itsweikuo: there is no federal-procurement content in the personal KB. If a govdoc
somehow arrives there, the spine's default (beside the source file) applies and you should say so in
the report rather than routing it to `notes/`.

## Adding a workspace

Add a row. Do not add a flag. If the new workspace's `article` home does not exist yet, create the
directory with an `INDEX.md` in the same operation that files the first digest, per the KB SOP's
update-at-point-of-creation rule.

## Why the table lives here and not in each workspace

Two workspaces, one table, visible in one place — and an unknown workspace fails loudly at step 0
rather than silently filing somewhere plausible. If this grows past roughly four workspaces, invert
it: have each workspace declare its own destinations in a config file this skill reads. The
runtime-resolution contract does not change, only where the rows live.
