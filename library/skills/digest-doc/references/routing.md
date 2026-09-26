# Routing — where a digest gets filed

Filing destinations are not hardcoded in the skill. They are resolved from the workspace you are in,
at runtime, and there is deliberately **no `--dest` flag** — configuration lives in the workspace, not
in something you have to remember to type.

> **This file is a local patch.** Upstream it carries a two-row table naming GitRoll's own
> repositories, which is no use to you. The rows below are this workspace's.

## Step 0 — resolve the workspace

```bash
git rev-parse --show-toplevel          # -> the root of the repository you work in
```

If that fails you are not inside a repository. **Stop and report** — do not guess a root and do not
fall back to the current directory. Every destination below is inside that root's
`apprentice-workspace/` folder. A digest filed into the wrong place is worse than no digest, and
on an engagement it can put one client's material into another client's directory.

## Destinations

A digest of a document the client gave you goes **beside the source document**, which is already
resolved from the input path — no table needed. The table is for a digest with no source directory,
which in practice means something you read on the web.

| What you digested | Where it goes | Naming | INDEX to update |
|---|---|---|---|
| A document this client gave you | beside the source, in `apprentice-workspace/engagements/<client-slug>/interview/` or `process/` | keep the source document's slug, suffix `-digest` | that directory's `INDEX.md` |
| Something you read to understand this client's field | `apprentice-workspace/engagements/<client-slug>/interview/` | `{YYYY-MM-DD}_{title-slug}.md` | that directory's `INDEX.md` |
| Something you read that is useful on every engagement | `apprentice-workspace/reference/` | `{YYYY-MM-DD}_{title-slug}.md` | `apprentice-workspace/reference/INDEX.md` |
| Coursework reading, before you have a client | `apprentice-workspace/training/<module-id>/` | `{YYYY-MM-DD}_{title-slug}.md` | that module's `INDEX.md` |

**The judgement call, and it is the only one here:** is this about *this client* or about *the work*?
If you would want it on the next engagement, it is not client material and it belongs in
`apprentice-workspace/reference/`. If you are unsure, file it with the client — moving it out later is
easy, and un-mixing two clients' material is not.

## Never

Do not file a digest into `library/`. It is the plugin's library and read-only: every file in it is
hashed in a provenance manifest kept in the plugin's own repository, and the next plugin update
overwrites a write there.
