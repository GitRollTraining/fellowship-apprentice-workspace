---
style: procedural
role: runbook
---

# Render the owner account

The two scripts in this directory turn one completed markdown owner account into an A4 PDF, then check
whether the document survived rendering. They do not package or transform the executable deliverable.

## Inputs and outputs

| Item | Path | Where it comes from |
|---|---|---|
| Owner-account source | `engagements/<client-slug>/handover/owner-account.md` | Output Phraser using `library/templates/handover.md` |
| PDF the owner reads | `engagements/<client-slug>/handover/owner-account.pdf` | `build-document-pdf.py` |
| Exact implementation the client operates | `engagements/<client-slug>/deliverable/` | Validator-A-passed candidate; this renderer does not touch it |

The markdown is the authoring source. Never hand-edit the PDF. Change the markdown, rebuild, check and
inspect again.

## Why the deliverable is not concatenated into the PDF

The old runbook stripped and joined one `deliverable/skill.md` beneath the owner account. That no longer
fits the delivery contract:

- a deliverable may contain several skills, scripts, integrations, services or supporting files;
- directory structure, exact bytes and executable formats are part of what Validator A passed;
- flattening creates a second copy that can drift from the installable files; and
- internal comments, configuration or code are not automatically appropriate owner-facing prose.

The client package therefore carries the rendered owner account and the exact `deliverable/` tree as
separate siblings. The PDF explains the work; the files perform it.

## Install once

```bash
brew install pandoc poppler
pip3 install playwright
python3 -m playwright install chromium
```

Debian or Ubuntu: install `pandoc` and `poppler-utils`, then run the same `pip3` and Playwright commands.

Verify all three dependencies:

```bash
pandoc --version | head -1
pdftotext -v
python3 -c "import playwright; print('playwright ok')"
```

Pandoc's direct PDF route normally invokes a large LaTeX installation. `build-document-pdf.py` instead
uses Pandoc for HTML and headless Chromium for PDF, which is why Playwright is required.

## 1. Check the source contract

The input contract lives in `library/templates/handover.md`. Before building, verify that the file has
exactly one first-level heading outside fences and no unfinished template marker:

```bash
ACCOUNT=engagements/<client-slug>/handover/owner-account.md
test "$(awk '/^```/{f=!f} !f && /^# /{n++} END{print n+0}' "$ACCOUNT")" -eq 1
! rg -n 'TBD|REPLACE|<client-slug>|<business name>|<v[0-9]+>' "$ACCOUNT"
```

The file must begin with frontmatter, include a quoted `footer:` value and place one subtitle paragraph
directly below the H1. Every table header needs its dashed separator row and every row needs the same
number of cells.

The internal source-map pointer and `HC-*` anchors are HTML comments. They remain in the markdown source
and must not appear in rendered prose.

## 2. Build

From the repository root:

```bash
python3 library/renderers/build-document-pdf.py "$ACCOUNT"
# wrote engagements/<client-slug>/handover/owner-account.pdf (... bytes)
```

A zero exit code proves only that a PDF was written. A missing table separator can still turn a table
into a paragraph of vertical bars without making the build fail.

## 3. Run deterministic checks

```bash
python3 library/renderers/check-document-pdf.py "$ACCOUNT"
```

Pass the markdown path; the checker derives the PDF beside it. It checks:

| Check | Failure caught |
|---|---|
| Separator row present | Pandoc would stop recognising a table |
| Rows not ragged | Cells would shift under the wrong headings |
| No vertical bars in PDF text | Downstream evidence that a table rendered as prose |
| No replacement characters | A missing glyph became a blank or box |

If `pdftotext` is available, also prove internal trace comments did not reach the text layer:

```bash
TEXT_OUT="$(mktemp)"
pdftotext "${ACCOUNT%.md}.pdf" "$TEXT_OUT"
! rg -n 'handoff-source-map|HC-[0-9]{3}' "$TEXT_OUT"
```

Record the commands and exit codes in `verification/handoff-source-map.md`.

## 4. Inspect the rendered pages

Open the PDF yourself before the owner does:

```bash
open "${ACCOUNT%.md}.pdf"      # macOS; use xdg-open on Linux
```

Inspect every page for:

- clipped, overlapping or unreadable text;
- a missing subtitle or incorrect running footer;
- tables that split badly or use an unsuitable first-column width;
- diagrams too small to read or cut across page boundaries;
- visible source-map comments, internal identifiers or placeholders;
- unexplained jargon, missing limitations or duplicated operating instructions; and
- a filename or title meaningful only inside this repository.

Visual inspection supplements the checker. It does not replace it.

## Table sizing

The renderer chooses column widths from the header row:

| Header row | First column rendering |
|---|---|
| No header, three columns | Narrow grey index, bold short name, description |
| `Stage`, `Step`, `Week`, `Phase`, `#` or `No.` | Narrow index column |
| Anything else | Bold label column at forty percent, then remaining columns |

A label may use `Canonical name — *plain gloss*`; the name stays bold and the gloss becomes grey italic.
Tables of four rows or fewer are held together across page breaks where possible.

## Troubleshooting

| Problem | Fix |
|---|---|
| `pandoc: command not found` | Install Pandoc as above |
| `ModuleNotFoundError: No module named 'playwright'` | Install Playwright for the same Python interpreter and install Chromium |
| `pdftotext: command not found` | Install Poppler; do not claim the text-layer checks ran |
| `no such source` | Run from the repository root and resolve the engagement path |
| PDF absent during check | Run the builder first against the same markdown file |
| Frontmatter printed in the body | Frontmatter did not begin on line 1 or did not close correctly |
| Two title blocks | Remove the extra H1; do not blanket-rewrite headings inside code fences |
| Vertical bars in PDF text | Repair the table separator or ragged row named by the checker |
| Blank, box or replacement glyph | Replace the unsupported character and rebuild |
| Hidden `.owner-account.html` remains | The builder crashed before cleanup; report the failed build and remove the generated residue before retrying |

Any owner-account edit invalidates its persona preflight, real-owner acceptance, Validator B report and
any operational acceptance tied to that report. Rebuild, recheck, reinspect and return to those gates.
A deliverable-file edit additionally invalidates Validator A.
