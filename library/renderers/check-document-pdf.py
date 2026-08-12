#!/usr/bin/env python3
"""Check a markdown document and its rendered PDF for silent render failures.

    python3 library/renderers/check-document-pdf.py <path/to/doc.md> [...]

Exits non-zero if any check fails. Run it after `build-document-pdf.py`; the
build reports success whether or not the tables actually rendered, so a clean
build is not evidence the document is correct.

Each check exists because that failure was observed, not imagined:

  1. table separator present  - an edit deleted a `|---|---|` row, so pandoc
     stopped seeing a table and emitted the pipes as plain prose. The build
     succeeded, the page count was unchanged, and the section was unreadable.
  2. table rows not ragged    - a regex aimed at one table stripped the leading
     index cell from two rows of another. Those rows silently rendered one
     column to the left: the name became the index, the sentence became the name.
  3. no pipes in the PDF text - the decisive downstream signal for check 1. A `|`
     surviving into the text layer means some table did not become a table.
  4. no replacement glyphs    - a font without the character renders a blank or a
     box. Seven arrows vanished this way while every word count still matched.

Uses pdftotext (poppler) when it is on PATH. Without it the two source-side checks
still run, and the script says so rather than pretending the render was inspected.
"""
import re
from collections import Counter
import subprocess
import sys
from pathlib import Path

SEPARATOR = re.compile(r"\|(\s*:?-+:?\s*\|)+")


def check_markdown(md_path):
    """Table structure, read off the source. Returns a list of failure strings."""
    failures = []
    lines = md_path.read_text(encoding="utf-8").split("\n")
    header_cols = None
    fenced = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            header_cols = None
            continue
        if fenced:                                    # a pipe inside a code block is not a table
            continue
        if not line.startswith("|"):
            header_cols = None
            continue
        if header_cols is None:                       # this line opens a table
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not SEPARATOR.fullmatch(nxt.strip()):
                failures.append(
                    f"{md_path.name}:{i + 1} table header has no separator row "
                    f"-> renders as plain text: {line[:60]}"
                )
            header_cols = line.count("|")
            continue
        if SEPARATOR.fullmatch(line.strip()):
            continue
        if line.count("|") != header_cols:
            failures.append(
                f"{md_path.name}:{i + 1} row has {line.count('|') - 1} columns, "
                f"header has {header_cols - 1}: {line[:60]}"
            )
    return failures


def check_pdf(pdf_path):
    """Rendered output. Returns (failures, page_count)."""
    if not pdf_path.exists():
        return [f"{pdf_path.name} does not exist - was it built?"], 0
    try:
        text = subprocess.run(
            ["pdftotext", str(pdf_path), "-"], capture_output=True, text=True, check=True
        ).stdout
    except FileNotFoundError:
        # poppler is genuinely optional: say so and let the two source-side checks stand, rather
        # than dying with a traceback and reporting nothing at all.
        print("    [skipped] pdftotext not installed - the two source-side checks still ran")
        return [], 0
    # Pipes that came from a fenced block in the source are not tables - a document that SHOWS a
    # markdown table as a code sample is supposed to print pipes. Budget them: count each fenced
    # pipe line in the source, then let each one explain at most one pipe line in the PDF.
    # Matching by content alone does not work, because a separator row like |---|---|---| is
    # byte-identical whether it is a live table or a code sample.
    budget = Counter()
    md = pdf_path.with_suffix(".md")
    if md.exists():
        fenced = False
        for ln in md.read_text(encoding="utf-8").split("\n"):
            if ln.lstrip().startswith("```"):
                fenced = not fenced; continue
            if fenced and "|" in ln:
                budget[ln.strip()[:40]] += 1
    failures = []
    for marker, why in (("|", "a table did not render"),
                        ("�", "a glyph is missing from the font")):
        hits = [ln for ln in text.split("\n") if marker in ln]
        if marker == "|":
            left, unexplained = budget.copy(), []
            for ln in hits:
                key = ln.strip()[:40]
                if left[key] > 0:
                    left[key] -= 1
                else:
                    unexplained.append(ln)
            hits = unexplained
        if hits:
            failures.append(
                f"{pdf_path.name}: {len(hits)} line(s) contain {marker!r} - {why}"
                f"\n      first: {hits[0][:70]}"
            )
    pages = len(re.findall(r"\f", text)) or 1
    return failures, pages


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    all_failures = []
    for arg in argv:
        md = Path(arg)
        pdf = md.with_suffix(".pdf")
        failures = check_markdown(md)
        pdf_failures, pages = check_pdf(pdf)
        failures += pdf_failures
        status = "FAIL" if failures else "ok"
        print(f"[{status}] {md.name} -> {pages} page(s)")
        for f in failures:
            print(f"    {f}")
        all_failures += failures
    print(f"\n{len(all_failures)} failure(s)")
    return 1 if all_failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
