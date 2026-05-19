import datetime
import mimetypes
import os
from urllib.parse import urlparse

from flask import Flask, Response, render_template, request
from weasyprint import HTML, default_url_fetcher

app = Flask(__name__)


def get_dates():
    today = datetime.date.today()
    bilimkana = (datetime.date(2023, 6, 1) - datetime.date(2022, 9, 1)).days
    developstoday = (datetime.date(2023, 2, 1) - datetime.date(2022, 8, 8)).days
    eso = (datetime.date(2022, 8, 8) - datetime.date(2021, 9, 14)).days
    cec = (datetime.date(2023, 7, 1) - datetime.date(2023, 3, 1)).days
    globalify = (datetime.date(2025, 6, 1) - datetime.date(2023, 6, 1)).days
    kasu = (today - datetime.date(2025, 4, 1)).days
    wiot = (datetime.date(2023, 12, 1) - datetime.date(2023, 6, 1)).days

    return {
        "bilimkana": bilimkana,
        "developstoday": developstoday,
        "eso": eso,
        "cec": cec,
        "globalify": globalify,
        "kasu": kasu,
        "wiot": wiot,
    }


def _static_url_fetcher(url):
    parsed = urlparse(url)
    if parsed.path.startswith("/static/"):
        file_path = os.path.join(app.root_path, parsed.path.lstrip("/"))
        if os.path.isfile(file_path):
            mime_type = (
                mimetypes.guess_type(file_path)[0] or "application/octet-stream"
            )
            with open(file_path, "rb") as f:
                return {
                    "string": f.read(),
                    "mime_type": mime_type,
                    "redirected_url": url,
                }
    return default_url_fetcher(url)


@app.get("/")
def home():
    return render_template("home.html", dates=get_dates())


@app.get("/download")
def download():
    html_string = render_template("home.html", dates=get_dates())
    pdf_bytes = HTML(
        string=html_string,
        base_url=request.url_root,
        url_fetcher=_static_url_fetcher,
    ).write_pdf()
    return Response(
        pdf_bytes,
        mimetype="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=Arstanbek_Usenov_CV.pdf"
        },
    )
