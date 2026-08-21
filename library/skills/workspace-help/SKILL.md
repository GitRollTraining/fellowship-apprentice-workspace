---
name: workspace-help
description: Answer an apprentice's "how do I ...?" and "where does this go?" questions about this workspace by listing what is actually in it right now and reading its manifests, never from a remembered inventory. Use whenever someone asks where a file belongs, what a playbook or skill is for, what they are allowed to edit, or which tool to reach for. Do not use it to run a playbook or to set anything up.
---

# Workspace help

Answer the question the apprentice actually asked, from what is in the repository **at this moment**.

## The one rule this skill exists to enforce

**List, then answer. Never answer from a remembered inventory.**

This workspace grows. Skills are added, playbooks change state, templates arrive. Any answer that
recites a set of files someone wrote down once is correct on the day it was written and quietly
wrong afterwards — and it stays confident while being wrong, which is worse than saying nothing.

So every answer below starts with a command that lists the thing. Run it. Read what comes back.
Answer from that. If the output disagrees with anything in this file, **the output is right**.

There is a second-order version of the same trap: reading only a manifest. A manifest is a file
someone maintains by hand, so a new playbook can sit in the directory with no row describing it.
**List the directory and read the manifest, then reconcile the two.** A file with no manifest row is
a real answer — say it exists and that it is undocumented, rather than omitting it.

## Input

The apprentice's question, in their own words. Nothing else. Do not make them name a directory or a
file — not knowing the name is usually why they are asking.

## Workflow

### 1. Work out which class of question it is

| They asked | Go to |
|---|---|
| "I'm new — where do I even start" | Filing first, then Skills. Show them the tree and the four top-level directories before naming any tool |
| "what can this thing do", "which skill should I use" | Skills |
| "how do I run an engagement", "what is a playbook" | Playbooks |
| "where do I put this" | Filing |
| "is there a template for" | Templates |
| "am I allowed to edit that" | Permissions |
| "what have I got so far" | Their own work |
| "what does <word> mean" | Terms |
| "how many X are there" | Counts — count them, never quote a number from prose |
| "what personas / renderers are there" | Personas, references, renderers |

The commands for each are in `references/enumeration.md`. Run the one that matches, from the
repository root.

### 2. Answer from the output, briefly

Name the thing and give its path. One or two sentences on what it is for. Stop there unless they
ask for more — and when they do ask, go as deep as they want.

Give a path the first time you name any file. "The interview playbook" is not something an
apprentice can open; `library/playbooks/playbook-interview.md` is.

### 3. When you point at a playbook, say two things first

**The word means two different things**, and this repository's own manifest says the conflict has
never been reconciled. Say which one you mean the first time it comes up in a conversation:

> In this workspace a playbook is a step-by-step procedure you actually run on a client engagement,
> not the read-it-yourself reference document the course calls a playbook.

**Three files in this repository define the word, and they do not agree.** When you have to pick,
`library/playbooks/INDEX.md` wins: it is the manifest governing the directory the files live in.
`library/reference/terminology.md` says a playbook is run *across* engagements, which reads as the
opposite of the manifest's *engagement-bound*; both are defensible and the difference is real, so
say which one you are using rather than blending them. Do not silently prefer the glossary because
it is shorter.

**And say what state it is in**, from the file you just read — never from a sentence remembered
here. Read the `status:` line in the playbook's own frontmatter, fall back to the State column in
`library/playbooks/INDEX.md`, and repeat what it says.

The shape of the sentence, with the state filled in from what you actually read:

> `<name>` is `<the state its own frontmatter or the manifest gives>`. Expect gaps, and report them
> rather than fixing the library yourself.

A count of how many have been run belongs in neither this file nor your answer. If the apprentice
asks how many, count them — the recipe is under Counts in `references/enumeration.md`.

Then check one more thing the manifest does not tell you: **does this playbook need a real client?**
Most of them do, and an apprentice in week one does not have one. `references/enumeration.md` shows
how to find the answer in the file rather than guessing it.

### 4. Define a term the moment you use it

The glossary at `library/reference/terminology.md` is real and is reachable from none of the three
files a new apprentice reads. Assume they have never seen it.

When a house term comes up, spend one clause defining it and carry on. **Define it; do not swap it
for a friendlier word** — a substitute means every other file in the workspace now disagrees with
you. The workspace's own writing standard says the same thing.

## What this skill does not do

**It writes nothing.** No record, no notes, no file. It reads and answers. If the apprentice needs
something written, that is theirs to write, in one of the trees they are allowed to write.

**It does not run playbooks or set anything up.** For a first-time machine and workspace setup, that
is `/onboarding`. For starting a client engagement, that is
`library/playbooks/playbook-environment-setup.md`.

**It does not repair the library.** If the answer turns out to be that a file is wrong, say so and
tell them to report it. Editing anything under `library/` is denied by the permission list and
breaks a provenance record that hashes every file in that tree.

## Gotchas

- **Reciting an inventory.** The single failure this skill is built to prevent. If you find yourself
  about to say "there are eleven skills", stop and run the listing instead. There were eleven once.
- **Reading the manifest instead of the directory.** A file with no row is invisible that way. List
  both and reconcile.
- **Trusting a count written in prose.** Several counts in this repository disagree with the files
  they describe, today, before anything else changes. Count the files yourself.
- **Routing a beginner into a 21-step procedure that needs a business owner.** Check what the
  playbook requires before naming it as their next step.
- **Answering "what is in my engagement" from a manifest.** Those manifests describe the empty shape
  the directory ships with. Use the filesystem.
- **Using a code without the thing.** Write the thing, and bracket the code after it if it helps.
  A reader who has to look something up to parse your sentence has been handed homework.

## Quality guidelines

Adhere to:

- `library/reference/agent-quality-guidelines.md` for runtime behavior.
- `library/reference/skill-architecture.md` for structural principles.
