---
style: descriptive
---

# What to read at runtime, per class of question

Every recipe here is read-only and runs from the repository root. Run the one that matches, and
answer from its output.

**The pattern is the same every time: list the files, read the manifest, reconcile.** The listing
finds what exists; the manifest says what it is for. Neither alone is the answer, and where they
disagree the listing wins on existence and the manifest wins on meaning.

## Skills

```bash
ls -1 library/skills/*/SKILL.md | sed 's|library/skills/||; s|/SKILL.md||'
```

For what each one is for, read the frontmatter rather than the manifest — it travels with the file:

```bash
for f in library/skills/*/SKILL.md; do
  awk '/^name: /{n=substr($0,7)} /^description: /{print n" -- "substr($0,14); exit}' "$f"
done
```

Then read `library/skills/INDEX.md` for the "You reach for it when" column, which is written as the
reader's situation rather than the skill's feature and is usually the more useful half.

**Reconcile.** A directory with a `SKILL.md` and no manifest row still exists. Say so.

Two listing traps: `find . -name SKILL.md` also catches `library/templates/brief-design/SKILL.md`,
which is a template rather than a skill; and `find -L` walks the `.claude/skills` symlink and
reports everything twice.

## Playbooks

```bash
ls -1 library/playbooks/playbook-*.md
```

State, from each file's own frontmatter — this is the authority, because it travels with the file:

```bash
for f in library/playbooks/playbook-*.md; do
  printf '%-52s %s\n' "$f" "$(awk 'FNR<=12 && /^status:/{print substr($0,9); exit}' "$f")"
done
```

A file printing no status has none in its frontmatter; fall back to the State column in
`library/playbooks/INDEX.md`, and if it is in neither, say it is undocumented.

**Does it need a real client?** This is the question that decides whether an apprentice can run it
at all, and no manifest answers it. Look in the file's own preconditions:

```bash
sed -n '/^## Preconditions/,/^## /p' library/playbooks/playbook-<name>.md
```

A precondition naming a client, an owner, or a person authorised to approve access means the
apprentice cannot run it without one. Say that plainly instead of routing them into it.

The word itself, and the warning about its two senses, is in `library/playbooks/INDEX.md` under its
own heading. Read it once and carry the one-sentence definition into the conversation.

## Filing — "where does this go?"

The table in `CLAUDE.md` is the policy, and it is the answer to most filing questions:

```bash
sed -n '/^| You are doing/,/^$/p' CLAUDE.md
```

Two rules that are easy to miss and live in the same file: the six engagement subdirectories are
named for *kinds of material*, not for a sequence, so more than one fills in the same afternoon;
and anything that must not leave the business is named `*.local.*`, which the ignore file already
excludes, with a note in the process record saying it exists.

For where a manifest sits relative to its parent:

```bash
find . -name INDEX.md -not -path './.git/*' | sort
```

## Templates

```bash
ls -1 library/templates/
```

The filenames say what they are; `library/templates/INDEX.md` says when to reach for each. For
templates the manifest is the only source of meaning, so read it — but list first, because a
template with no row still exists.

## Personas, references, renderers

```bash
ls -1 library/personas/ library/reference/ library/renderers/
```

Each has its own `INDEX.md` beside it.

## Permissions — "am I allowed to edit that?"

```bash
cat .claude/settings.json
```

Read it as three lists. `allow` runs without asking, `ask` prompts every time, `deny` refuses.

Two things to say alongside it, because the file does not:

- **A path in none of the three lists still prompts.** That is most shell commands, and it is not a
  malfunction. The reasoning is in `library/sops/agent-settings.md`: reading is free, writing inside
  your own work is free, anything leaving the machine is gated.
- **`library/` is denied for a reason**, not as friction: a provenance record outside this tree
  hashes every file in it, so an edit in place breaks that record silently.

Where the reasoning file and the live JSON disagree, the JSON is what runs.

## Their own work — "what have I got so far?"

**Do not answer this from a manifest.** The engagement subdirectory manifests describe the empty
shape the directory ships with, and they go on saying so after real work lands.

```bash
find engagements training -mindepth 1 -not -name INDEX.md
git status --short
```

## Terms

```bash
cat library/reference/terminology.md
```

Assume the apprentice has never opened it: it is named in none of `README.md`, `CLAUDE.md` or the
root `INDEX.md`, so nothing a new arrival reads points at it.

It also does not define everything this workspace says. When a term is not in it, define it from how
the files use it and say that is what you are doing.

## Counts

Do not repeat a count you read in prose. Several in this repository already disagree with the files
they describe. Count what is there:

```bash
ls -1 library/skills/*/SKILL.md | wc -l
ls -1 library/playbooks/playbook-*.md | wc -l
ls -1 library/templates/*.md | wc -l
```
