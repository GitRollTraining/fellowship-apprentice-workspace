---
style: descriptive
---

# What to read at runtime, per class of question

Every recipe here is read-only. Set two variables once, then run the one that matches and answer
from its output:

```bash
L="$(cd "<this skill's folder>/../.." && pwd)"               # the plugin's library/
W="$(git rev-parse --show-toplevel)/apprentice-workspace"   # the apprentice's own workspace folder
```

`$L` is the plugin's library, which the apprentice reads and never edits; `$W` is their own work in
the repository in front of you. When you answer, name a library file by its `library/…` path and
say it is in the plugin.

**The pattern is the same every time: list the files, read the manifest, reconcile.** The listing
finds what exists; the manifest says what it is for. Neither alone is the answer, and where they
disagree the listing wins on existence and the manifest wins on meaning.

## Skills

```bash
ls -1 "$L"/skills/*/SKILL.md | sed "s|$L/skills/||; s|/SKILL.md||"
```

For what each one is for, read the frontmatter rather than the manifest — it travels with the file:

```bash
for f in "$L"/skills/*/SKILL.md; do
  awk '/^name: /{n=substr($0,7)} /^description: /{print n" -- "substr($0,14); exit}' "$f"
done
```

Then read `library/skills/INDEX.md` for the "You reach for it when" column, which is written as the
reader's situation rather than the skill's feature and is usually the more useful half.

**Reconcile.** A directory with a `SKILL.md` and no manifest row still exists. Say so.

One listing trap: `find "$L" -name SKILL.md` also catches `library/templates/brief-design/SKILL.md`,
which is a template rather than a skill.

## Playbooks

```bash
ls -1 "$L"/playbooks/playbook-*.md
```

State, from each file's own frontmatter — this is the authority, because it travels with the file:

```bash
for f in "$L"/playbooks/playbook-*.md; do
  printf '%-52s %s\n' "$f" "$(awk 'FNR<=12 && /^status:/{print substr($0,9); exit}' "$f")"
done
```

A file printing no status has none in its frontmatter; fall back to the State column in
`library/playbooks/INDEX.md`, and if it is in neither, say it is undocumented.

**Does it need a real client?** This is the question that decides whether an apprentice can run it
at all, and no manifest answers it. It lives in the playbook's own entry section — but **the
heading is not the same in every file**, so list the headings first and then read the one that
holds entry requirements:

```bash
grep -n '^## ' "$L"/playbooks/playbook-<name>.md | head -5
```

Headings seen carrying entry requirements include `## Preconditions`, `## Inputs`,
`## Entry gate and inputs`, `## Inputs and outputs`, `## Inputs and output` and
`## Required artifact chain`. That list is a hint, not a closed set — read what `grep` returned,
not what is written here. Then print the section you picked:

```bash
sed -n '/^## <the heading you picked>/,/^## /p' "$L"/playbooks/playbook-<name>.md
```

That range prints the following heading as its last line. Ignore it.

**If no section names entry requirements, say so** rather than concluding the playbook needs
nothing. A missing precondition section is missing documentation, not an open door.

A requirement naming a client, an owner, a signed document, or a person authorised to approve
access means the apprentice cannot run it alone. Say that plainly instead of routing them into it.

The word itself, and the warning about its two senses, is in `library/playbooks/INDEX.md` under its
own heading. Read it once and carry the one-sentence definition into the conversation.

## Filing — "where does this go?"

The table in the workspace rules, `apprentice-workspace/AGENTS.md`, is the policy, and it is the
answer to most filing questions. Every path in it is inside `apprentice-workspace/`:

```bash
sed -n '/^| You are doing/,/^$/p' "$W/AGENTS.md"
```

If `$W/AGENTS.md` does not exist, the workspace is not set up in this repository: say so and point
the apprentice at the `setup` skill.

Two rules that are easy to miss and live in the same file: the six engagement subdirectories are
named for *kinds of material*, not for a sequence, so more than one fills in the same afternoon;
and anything that must not leave the business is named `*.local.*`, which the workspace folder's
ignore file already excludes, with a note in the process record saying it exists.

For where a manifest sits relative to its parent:

```bash
find "$W" -name INDEX.md | sort
```

## Templates

```bash
ls -1 "$L"/templates/
```

That listing contains directories as well as files — a template can be a bundle with its own
`SKILL.md` and reference set, not just one markdown file. Do not filter to `*.md` and then report a
count; you will drop the bundles.

The filenames say what they are; `library/templates/INDEX.md` says when to reach for each. For
templates the manifest is the only source of meaning, so read it — but list first, because a
template with no row still exists.

## Personas, references, renderers

```bash
ls -1 "$L"/personas/ "$L"/reference/ "$L"/renderers/
```

Each has its own `INDEX.md` beside it.

## Permissions — "am I allowed to edit that?"

There is no permission file to read. The workspace used to ship `.claude/settings.json`; a plugin
cannot ship permission rules, and Codex never read that file. Answer from these three facts instead:

- **Everything in `apprentice-workspace/` is theirs** to write, and so is the rest of their own
  repository.
- **`library/` is read-only by rule, not by a setting.** It is the plugin's installed copy: a
  provenance record in the plugin's own repository hashes every file, and the next plugin update
  overwrites any edit. If a library file is wrong, they report it.
- **The agent still asks before most commands**, by its own rules. That is not a malfunction. The
  reasoning — reading is free, writing inside your own work is free, anything leaving the machine is
  gated — is in `library/sops/agent-settings.md`.

## Their own work — "what have I got so far?"

**Do not answer this from a manifest.** The engagement subdirectory manifests describe the empty
shape the directory ships with, and they go on saying so after real work lands.

```bash
find "$W/engagements" "$W/training" "$W/reference" -mindepth 1 -not -name INDEX.md
git status --short
```

## Terms

```bash
cat "$L"/reference/terminology.md
```

Assume the apprentice has never opened it: it is named in none of the plugin's `README.md`, the
workspace's `AGENTS.md` or its `INDEX.md`, so nothing a new arrival reads points at it.

It also does not define everything this workspace says. When a term is not in it, define it from how
the files use it and say that is what you are doing.

## Counts

Do not repeat a count you read in prose. Several in the library already disagree with the files
they describe. Count what is there:

```bash
ls -1 "$L"/skills/*/SKILL.md | wc -l
ls -1 "$L"/playbooks/playbook-*.md | wc -l
ls -1 "$L"/templates | grep -v '^INDEX\.md$' | wc -l
```

The template line counts directory entries rather than `*.md`, because a template can be a bundle:
`brief-design/` is a directory, and filtering to `*.md` drops it — the same mistake this file warns
about under Templates, and it returns a plausible number, which is why it survives review. It then
excludes `INDEX.md`, which is the directory's own manifest and not a template. Without that
exclusion the line returns one more than there are templates, and disagrees with the count
`library/templates/INDEX.md` gives for itself.
