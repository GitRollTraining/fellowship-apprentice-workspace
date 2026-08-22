---
style: descriptive
---

# Where each setup topic is explained

Four checklist items are reading, not doing, and an apprentice will ask about all four. This page
says where each one is already explained, so you answer from programme material instead of
searching the web.

**The rule: read the house copy first.** If the answer is in the table below, use it. Search the
public internet only when the table has nothing, and say plainly that is what you did — a public
answer may describe a different tool version, or a workflow this programme does not use.

This exists because of a measured failure. On 2026-08-22 an apprentice asked what entire.io was and
why they needed it. The agent searched this repository for the trainer's notes, found nothing, and
answered from `docs.entire.io` and `git-scm.com` instead. The material it needed already existed —
in Notion and in Google Classroom — and nothing here pointed at it.

## The four topics

| Checklist item | Read this first | Original, which wins on any disagreement |
|---|---|---|
| Read: version control systems | `library/reference/setup-reading/version-control-systems.md` | <https://knowledge.kitchen/content/courses/software-engineering/notes/version-control-systems/> |
| Read: Git and GitHub | `library/reference/setup-reading/git-and-github.md` | <https://knowledge.kitchen/content/courses/software-engineering/notes/git-and-github/> |
| Codex application | Not mirrored here. Google Classroom → Getting Started → "Getting Started with GitHub and Codex" | The programme's Notion page, "Start using the Codex app" |
| Session logging on entire.io | `library/reference/setup-reading/entire-io-session-logging.md` | The programme's Notion page, "Set up AI Session Log collection", and <https://docs.entire.io> |

**Why the Codex manual is not mirrored.** It is marked internal, and this repository is public. It
is published to apprentices through Google Classroom, which is access-controlled, so point them
there rather than reproducing it. If an apprentice cannot open Classroom yet, that is a `blocked`
row on their trainer, not something to work around by searching.

## What the mirrors are, and are not

The three files under `library/reference/setup-reading/` are copies, taken on the date each one
states. They are not maintained by this programme and they are not edited here — a mirror that
somebody edits is no longer a mirror, and `library/` is read-only in any case. Each carries its
source URL and its licence at the top.

Two of them, the version-control and Git notes, are third-party course material shared under the
GNU General Public License, Version 3. Keep their attribution block intact if you quote them, and
send an apprentice to the original when they want the full course.

## What to do with a reading row

Reading cannot be verified by a command. Ask, record the answer with the date, and use `confirmed`,
which is the state for something only the apprentice can attest.

Where they say they have not read it — which is common, and is what happened in the measured run —
do not mark the row and do not lecture. Give them the path from the table, one sentence on why the
topic matters for what they are about to do, and leave the row `outstanding` so the next session
asks again.

Do not tell an apprentice to "ask their trainer" for material that is sitting in the table above.
