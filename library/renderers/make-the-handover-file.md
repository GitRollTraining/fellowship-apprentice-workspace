---
style: descriptive
role: runbook
---

# Make the handover file

The two scripts in this directory, run in order, turn markdown you have already written into one A4 PDF
the owner opens with a PDF reader and nothing else.

## Inputs and outputs

| Item | Path | Where it comes from |
|---|---|---|
| The owner-facing account | `engagements/<client-slug>/handover/owner-account.md` | step 20 of `library/playbooks/playbook-interview.md`, written with the `explain` skill |
| The skill you hand over | `engagements/<client-slug>/deliverable/skill.md` | written from the specification with the `create-skill` skill |
| The joined markdown | `engagements/<client-slug>/handover/handover.md` | step 2 below. This is the source of truth |
| The PDF the owner receives | `engagements/<client-slug>/handover/handover.pdf` | step 3 below |

The markdown is the source; the PDF is compiled from it. Never hand-edit the PDF. Change the markdown
and rebuild.

## Install once

```bash
brew install pandoc poppler && pip3 install playwright && python3 -m playwright install chromium
```

Debian or Ubuntu: `sudo apt install pandoc poppler-utils`, then the same `pip3` and `playwright` commands.

Verify all three:

```bash
pandoc --version | head -1 && pdftotext -v && python3 -c "import playwright; print('playwright ok')"
```

## Why `pandoc handover.md -o handover.pdf` is not the route

Pandoc's own PDF writer hands the document to a LaTeX engine, which is exactly the unusual multi-gigabyte
install this layer exists to avoid; `build-document-pdf.py` goes markdown to HTML to headless Chromium
instead, which the playwright install above already gave you.

## The sequence

Five steps: strip, join, build, check, open. Worked below on a bakery whose wholesale order intake was
the reconstructed process. Substitute your own client slug and title.

```bash
ENGAGEMENT=engagements/harbour-bakery
```

### 1. Strip the frontmatter and the internal notes

Frontmatter is consumed as metadata only at the top of a file. A second `---` block arriving in the
middle of a joined document renders as a horizontal rule with its keys printed as text underneath.
Strip each piece before joining, and strip anything you would not read aloud to the owner along with it.
Keep internal notes last, under a heading beginning `# NOTES`, and the second line below drops them.

```bash
strip() {
  awk 'NR==1 && $0=="---" {fm=1; next} fm && $0=="---" {fm=0; next} !fm' "$1" \
    | awk '/^# NOTES/{exit} {print}'
}

strip "$ENGAGEMENT/handover/owner-account.md" > /tmp/part-1.md
strip "$ENGAGEMENT/deliverable/skill.md"      > /tmp/part-2.md
```

Do not use the common one-line form `sed '1{/^---$/!q;};1,/^---$/d'`. On a file that carries no
frontmatter it prints the first line and quits, discarding the rest, and it reports no error while doing
it. Measured 2026-08-11.

### 2. Join the two pieces under one title

The renderer treats the first `# H1` as the title block, and the paragraph directly after it as the
subtitle line, which renders in small capitals. So the joined file carries exactly one `#` heading,
written by you, and a short subtitle rather than a sentence.

```bash
{
  printf -- '---\nfooter: Order intake handover\n---\n\n'
  printf '# Order intake at the bakery\n\n'
  printf 'Process handover, 11 August 2026\n\n'
  cat /tmp/part-1.md
  printf '\n'
  cat /tmp/part-2.md
} > "$ENGAGEMENT/handover/handover.md"
```

Each piece arrives with a title of its own. Demote both to `##` and rename them to say which half of the
document they open, for example "How the work is done today" and "The skill you hand over". Do this by
hand rather than with a blanket `sed 's/^# /## /'`: the skill half contains fenced code blocks, and a
blanket rule rewrites a `# comment` inside one.

Verify before building:

```bash
awk '/^```/{f=!f} !f && /^# /' "$ENGAGEMENT/handover/handover.md" | wc -l     # expect exactly 1
```

The `footer:` key sets the running footer on every page and does not appear in the body. With no
`footer:` key the footer falls back to the title text.

### 3. Build

```bash
python3 library/renderers/build-document-pdf.py "$ENGAGEMENT/handover/handover.md"
# wrote engagements/harbour-bakery/handover/handover.pdf (92,460 bytes)
```

**A clean build is not evidence the tables survived.** Deleting one dashed separator row from one table
produced a PDF the build called a success, at the same page count, in which that table had become a
paragraph of vertical bars. That is what step 4 is for.

### 4. Check

```bash
python3 library/renderers/check-document-pdf.py "$ENGAGEMENT/handover/handover.md"
# [ok] handover.md -> 6 page(s)
#
# 0 failure(s)
```

Pass the markdown path, not the PDF path; the checker derives the PDF beside it. It accepts several paths
at once and exits non-zero if anything fails, so it can gate a script. Four checks, each one present
because that failure was observed rather than imagined:

| Check | Fails when | What it catches |
|---|---|---|
| Separator row present | a table header is not followed by its dashed separator row | pandoc stops seeing a table and prints the rows as prose |
| Rows not ragged | a row has a different cell count from its header | rows render one column to the left: the name becomes the index, the sentence becomes the name |
| No vertical bars in the PDF text | a vertical bar survives into the PDF text layer | the downstream proof of the first check |
| No replacement characters | a question-mark-in-a-diamond glyph reaches the text layer | a character the serif font has no glyph for. Arrows disappear this way while every word count still matches |

### 5. Open it yourself, before the owner does

```bash
open "$ENGAGEMENT/handover/handover.pdf"      # macOS; xdg-open on Linux
```

A sweep verified only against the source is not verified. Read the pages.

## Post-render checklist

- [ ] Exactly one title block, at the top, and no second one mid-document.
- [ ] The line under the title reads as a subtitle. It renders in small capitals, so a full sentence there looks wrong.
- [ ] The footer names the document on every page.
- [ ] Every table is still a table, and its columns are split sensibly.
- [ ] No placeholder survives: a client slug, a `TBD`, an empty bracket, a figure you never confirmed.
- [ ] No internal material: the self-audit, the ambiguity list, the known-defects file, your own notes.
- [ ] Nothing the owner said must not leave the business.
- [ ] Every code is written out beside the thing it names. The owner holds no key. See `library/sops/working-standards.md` rule 4.
- [ ] Names, amounts, cut-off times and approval thresholds match the discovery record.
- [ ] The skill half is complete enough that the owner can follow it with you not in the room.
- [ ] The filename means something to the owner rather than to you.

## How the renderer sizes a table

Column widths are chosen per table shape, read off the header row.

| Header row | First column renders as |
|---|---|
| no header row at all, three columns | a narrow grey index, then a bold short name, then the description |
| Stage, Step, Week, Phase, # or No. | a narrow plain index column, then the content |
| anything else | a bold label column at 40 percent of the width, then the description |

Two further behaviours: a label cell written `Canonical name — *plain gloss*` keeps the name bold and
drops the gloss to grey italic, and a table of four rows or fewer is held whole across a page break.

If a column of bare numbers comes out bold and a third of the page wide, its header is not one of the
narrow words. Rename the header to `Step` or `#`.

## Troubleshooting

| Problem | Fix |
|---|---|
| `pandoc: command not found` | the install line above |
| `ModuleNotFoundError: No module named 'playwright'` | `pip3 install playwright && python3 -m playwright install chromium`, for the same python3 you are calling |
| `pdftotext: command not found` | `brew install poppler`, or `sudo apt install poppler-utils` |
| A script prints its own usage text and stops | wrong argument count. The builder takes exactly one markdown path; the checker takes one or more |
| `no such source: ...` | the path is wrong. Paths here are relative to the repository root |
| `handover.pdf does not exist - was it built?` | the checker ran before the builder, or against a different markdown file |
| Frontmatter keys appear in the body of the PDF | a piece was joined without being stripped. Redo step 1 |
| Two title blocks in the document | a piece kept its own `#` heading. `awk '/^```/{f=!f} !f && /^# /' ` must return 1 |
| Checker reports lines containing a vertical bar | a table lost its dashed separator row, or a row's cell count differs from its header's. The message names the file and the line |
| A row's cells are shifted one column to the left | a ragged row, same cause. The message names the line |
| A character renders as a blank or a box | the serif font has no glyph for it. Replace arrows and box-drawing characters with words or hyphens |
| A hidden `.handover.html` is left beside the markdown | the build crashed before its own cleanup. Delete it and rerun |

## Rebuilding

Any edit to the account or to the skill means all five steps again: strip, join, build, check, open. The
PDF is compiled output and there is no partial rebuild.
