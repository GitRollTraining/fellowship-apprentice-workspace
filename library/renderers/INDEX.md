<!-- upstream: library/INDEX.md -->
---
style: descriptive
---

# renderers

Turning finished markdown into one file a business owner opens. A written specification the owner
cannot read is not a handover.

Start at `make-the-handover-file.md`; it is the runbook and it names the order.

## Prerequisites

```bash
brew install pandoc poppler        # Linux: apt-get install pandoc poppler-utils
pip3 install playwright && python3 -m playwright install chromium
```

No LaTeX and no office suite. `poppler` is optional: without it two of the four checks are skipped
and the other two still run.

## Inventory

| Item | What it is |
|---|---|
| `build-document-pdf.py` | Turns one markdown file into an A4 PDF a business owner can open; this is the whole answer to turning finished work into a file the owner opens |
| `check-document-pdf.py` | Proves the PDF actually rendered - catches a table that silently became prose and a character that silently vanished, neither of which changes the page count or the exit code |
| `make-the-handover-file.md` | The runbook that joins the two scripts: strip, concatenate, build, check, and read it yourself before the owner does of the specification instead of raw markdown. |

A clean build is not evidence the document rendered correctly. Run the checker: a table can
silently become plain prose without changing the page count or the build's exit code.

## Freshness

| File set | Last updated | Class | Status |
|---|---|---|---|
| all 3 files | 2026-08-11 | Instruction | first cut |
