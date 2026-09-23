import pathlib

from flask import Flask, Response, render_template
from weasyprint import HTML

from resume_data import build_context

app = Flask(__name__)


def _localize_static(html_string):
    """Point /static/ references at the files on disk so WeasyPrint reads them
    directly instead of going through HTTP (works offline and in render.py)."""
    static_uri = pathlib.Path(app.static_folder).resolve().as_uri() + "/"
    return html_string.replace('"/static/', '"' + static_uri)


def render_pdf(variant=None):
    """Render the résumé (optionally a variant) to PDF bytes. Used by the
    /download route and by render.py for tailored PDFs."""
    html_string = render_template("home.html", **build_context(variant))
    return HTML(string=_localize_static(html_string)).write_pdf()


@app.get("/")
def home():
    return render_template("home.html", **build_context())


@app.get("/download")
def download():
    return Response(
        render_pdf(),
        mimetype="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=Arstanbek_Usenov_CV.pdf"
        },
    )
