#!/usr/bin/env python3
"""Render a markdown document to a formal A4 PDF.

    python3 library/renderers/build-document-pdf.py <path/to/doc.md>

Writes <path/to/doc.pdf>. The markdown is the source of truth; the PDF is
compiled. Never hand-edit the PDF, and never let the two diverge.

Document STRUCTURE (which sections, in what order, at what length) is not this
script's business. This file only decides how one owner-account source looks.
The sequence that checks, builds and inspects that account is
`library/renderers/make-the-handover-file.md`; client-package assembly belongs
to `library/playbooks/playbook-output-phraser.md`.

Conventions this relies on:
  - one `# H1` at the top; it becomes the title block
  - the paragraph immediately after it becomes the small-caps subtitle line
  - optional frontmatter key `footer:` sets the running footer text
    (defaults to the H1 text); all frontmatter is stripped before rendering

Table column widths are chosen per table SHAPE, read off the header row:

  | header row                     | first column | renders as                       |
  |--------------------------------|--------------|----------------------------------|
  | absent, 3 columns              | a number     | narrow grey index, bold name     |
  | Stage / Step / Week / Phase / #| a short index| narrow plain index, then content |
  | anything else                  | a label      | bold 40%, then description       |

A label cell may carry `Canonical name — *plain gloss*`: the name stays bold and
the gloss drops to grey italic. Tables of four rows or fewer are held whole
across page breaks.

Requires: pandoc on PATH, and playwright with chromium installed for the same
python3 that runs this script. Install line: see the runbook named above.
"""
import re
import subprocess
import sys
from pathlib import Path

CSS = """
@page { size: A4; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: Georgia, "Iowan Old Style", "Times New Roman", serif;
  font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; margin: 0;
}
h1 {
  font-size: 21pt; line-height: 1.2; font-weight: normal; letter-spacing: -0.01em;
  margin: 0 0 4pt 0; padding-bottom: 10pt; border-bottom: 1.5pt solid #1a1a1a;
}
.subtitle {
  font-size: 9pt; letter-spacing: 0.09em; text-transform: uppercase;
  color: #555; margin: 8pt 0 22pt 0;
}
h2 {
  font-size: 12.5pt; font-weight: bold; margin: 20pt 0 7pt 0;
  padding-top: 8pt; border-top: 0.5pt solid #c8c8c8;
  break-after: avoid; page-break-after: avoid;
}
h2:first-of-type { border-top: none; padding-top: 0; }
h3 { font-size: 11pt; margin: 14pt 0 5pt 0; break-after: avoid; page-break-after: avoid; }
p { margin: 0 0 8pt 0; orphans: 2; widows: 2; }
strong { font-weight: bold; }
ol, ul { margin: 0 0 8pt 0; padding-left: 16pt; }
li { margin-bottom: 4pt; }
blockquote {
  margin: 0 0 10pt 0; padding-left: 12pt; border-left: 2pt solid #d0d0d0; color: #444;
}
table {
  width: 100%; border-collapse: collapse; margin: 4pt 0 12pt 0;
  font-size: 9.5pt; line-height: 1.38;
}
thead th {
  text-align: left; font-weight: bold; font-size: 8.5pt;
  letter-spacing: 0.05em; text-transform: uppercase; color: #333;
  border-bottom: 1pt solid #1a1a1a; padding: 5pt 8pt 5pt 0;
}
tbody td {
  vertical-align: top; padding: 6pt 8pt 6pt 0;
  border-bottom: 0.5pt solid #dcdcdc;
}
tbody tr { break-inside: avoid; page-break-inside: avoid; }
tbody tr:last-child td { border-bottom: 0.75pt solid #999; }
td:first-child { padding-right: 12pt; }

/* Column widths are set per table SHAPE, not blanket-applied. A blanket
   first-column rule bolds numeric columns and pads them to a third of the
   page, which is what the first render of this stylesheet got wrong. */
.t-label td:first-child { font-weight: bold; width: 40%; }
/* A label cell may carry `Canonical name — *plain gloss*`. The canonical name
   stays bold; the gloss drops back so the two are distinguishable at a glance
   and the reader can still match this document against its source record. */
.t-label td:first-child em { font-weight: normal; font-style: italic; color: #666; }
.t-narrow td:first-child, .t-narrow th:first-child { width: 7%; }
.t-caps td:first-child, .t-caps th:first-child { width: 6%; color: #777; }
.t-caps td:nth-child(2) { font-weight: bold; width: 22%; }
.t-compact { break-inside: avoid; page-break-inside: avoid; }
"""

NARROW_HEADERS = {"stage", "step", "week", "phase", "#", "no."}


def classify_tables(fragment: str) -> str:
    """Tag each table by shape so column widths suit its content.

    pandoc emits undifferentiated <table>s. Which first column is a bold label
    and which is a bare number is decidable from the header row, so decide it
    here rather than with one CSS rule that guesses wrong on half of them.
    """

    def tag(m: re.Match) -> str:
        # pandoc derives per-column <colgroup> widths from the markdown source's
        # own column widths and emits them inline, where they beat any
        # stylesheet. Drop them so the classes below actually govern layout.
        table = re.sub(r"<colgroup>.*?</colgroup>", "", m.group(0), flags=re.S)

        heads = re.findall(r"<th[^>]*>(.*?)</th>", table, re.S)
        body = table.split("<tbody>")[-1]
        rows = len(re.findall(r"<tr", body))
        first = re.sub(r"<[^>]+>", "", heads[0]).strip().lower() if heads else ""
        # pandoc omits <thead> entirely when every header cell is empty, so a
        # headerless table is identified from its first body row instead.
        cols = len(re.findall(r"<td", body.split("</tr>")[0])) if not heads else len(heads)

        if not heads and cols == 3:
            cls = "t-caps"          # numbered: index, short name, description
        elif first in NARROW_HEADERS:
            cls = "t-narrow"        # narrow index column, then content
        else:
            cls = "t-label"         # bold label column, then description

        if rows <= 4:
            cls += " t-compact"     # small tables should not straddle a break
        return table.replace("<table>", f'<table class="{cls}">', 1)

    return re.sub(r"<table>.*?</table>", tag, fragment, flags=re.S)


def footer_html(text: str) -> str:
    return (
        '<div style="width:100%;font-family:Georgia,serif;font-size:7.5pt;color:#777;'
        'padding:0 20mm;display:flex;justify-content:space-between;">'
        f"<span>{text}</span><span class=\"pageNumber\"></span></div>"
    )


def build(md: Path) -> Path:
    if not md.exists():
        sys.exit(f"no such source: {md}")
    raw = md.read_text(encoding="utf-8")

    fm = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    footer = ""
    if fm:
        hit = re.search(r"^footer:\s*(.+)$", fm.group(1), re.M)
        if hit:
            footer = hit.group(1).strip().strip("\"'")

    fragment = subprocess.run(
        ["pandoc", str(md), "-f", "markdown", "-t", "html5"],
        capture_output=True, text=True, check=True,
    ).stdout

    if not footer:
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", fragment, re.S)
        footer = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else md.stem

    # Promote the paragraph directly after the title into the subtitle line.
    fragment = re.sub(
        r"(</h1>\s*)<p>(.*?)</p>",
        lambda m: f'{m.group(1)}<p class="subtitle">{m.group(2)}</p>',
        fragment, count=1, flags=re.S,
    )
    fragment = classify_tables(fragment)

    html = md.with_name(f".{md.stem}.html")
    html.write_text(
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{fragment}</body></html>",
        encoding="utf-8",
    )

    pdf = md.with_suffix(".pdf")
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html.resolve().as_uri())
        page.pdf(
            path=str(pdf), format="A4", print_background=True,
            display_header_footer=True, header_template="<div></div>",
            footer_template=footer_html(footer),
            margin={"top": "18mm", "bottom": "16mm", "left": "20mm", "right": "20mm"},
        )
        browser.close()

    html.unlink()
    return pdf


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = build(Path(sys.argv[1]))
    print(f"wrote {out} ({out.stat().st_size:,} bytes)")
