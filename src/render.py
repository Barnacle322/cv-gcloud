"""Render the résumé — or a tailored variant — to a PDF file.

    python render.py                              # base résumé → Arstanbek_Usenov_CV.pdf
    python render.py ../variants/teach.json       # variant → <filename from JSON or variant name>.pdf
    python render.py variant.json -o /path/out.pdf

Run from the repo root with the same deps as the site, e.g.
    DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --python 3.12 \
        --with weasyprint --with flask python src/render.py variants/teach.json

Variant JSON keys (all optional): headline, summary, location, skills,
experiences, education, show_days, filename — see resume_data.build_context.
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, render_pdf  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("variant", nargs="?", help="variant JSON file")
    parser.add_argument("-o", "--output", help="output PDF path")
    args = parser.parse_args()

    variant = None
    if args.variant:
        with open(args.variant, encoding="utf-8") as f:
            variant = json.load(f)

    output = args.output
    if not output:
        if variant and variant.get("filename"):
            output = variant["filename"]
        elif args.variant:
            stem = os.path.splitext(os.path.basename(args.variant))[0]
            output = "Arstanbek_Usenov_CV_{}.pdf".format(stem)
        else:
            output = "Arstanbek_Usenov_CV.pdf"
        output = os.path.join(
            os.path.dirname(os.path.abspath(args.variant)) if args.variant else ".",
            output,
        )

    with app.app_context(), app.test_request_context("/"):
        pdf_bytes = render_pdf(variant)

    with open(output, "wb") as f:
        f.write(pdf_bytes)
    print(output)


if __name__ == "__main__":
    main()
