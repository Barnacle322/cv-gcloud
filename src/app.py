import datetime
import mimetypes
import os
from urllib.parse import urlparse

from flask import Flask, Response, render_template, request
from weasyprint import HTML, default_url_fetcher

app = Flask(__name__)


EXPERIENCES = [
    {
        "title": "Full-Stack Engineer",
        "company": "RW Community",
        "start": datetime.date(2026, 4, 1),
        "end": None,
        "location": "Remote",
        "bullets": [
            "Architected and shipped a full-stack membership platform for a private members' club in Hong Kong with FastAPI, Vue 3 + TypeScript (PWA), and PostgreSQL — covering registration, tiered memberships, event booking, guest passes, and a points economy.",
            "Integrated Suprema BioStar 2 biometric door access over a WireGuard VPN, syncing membership state with face, QR, NFC, and mobile credentials so physical access reflects payment and tier status in real time.",
            "Designed a ledger-based points engine with per-batch expiry, tiered purchase bonuses, and referral rewards; shipped dual payment rails through Stripe with Celery-driven renewal reminders and reporting.",
        ],
    },
    {
        "title": "Intern Mentor & Software Engineer",
        "company": "Atlabyte",
        "start": datetime.date(2026, 1, 1),
        "end": datetime.date(2026, 4, 1),
        "location": "Remote",
        "bullets": [
            "Held a hybrid role spanning mentorship, engineering, and peer tutoring — supporting entry-level developers shipping into cybersecurity, e-commerce, and anti-fraud product tracks.",
            "Wired up internal tooling (CRM and team messaging integrations) into the development workflow to tighten the team's iteration cycle.",
            "Ran pairing, code reviews, and structured tutoring sessions to ramp junior engineers onto production codebases.",
        ],
    },
    {
        "title": "Technology Lead",
        "company": "kasu.fun",
        "start": datetime.date(2025, 4, 1),
        "end": datetime.date(2025, 6, 1),
        "location": "Remote",
        "bullets": [
            "Developed a Solana-based backend using Rust/Anchor and a Python client to power on-chain parimutuel betting and quiz mechanics.",
            "Built a full-stack web application with Python (Flask) APIs and a Vue.js frontend to enable quiz creation, participation, and leaderboard functionality.",
            "Integrated AI-driven components and external services (e.g., social media posting, dynamic image generation) to enhance user engagement and automate key workflows.",
        ],
    },
    {
        "title": "Chief Technology Officer",
        "company": "Globalify",
        "start": datetime.date(2023, 6, 1),
        "end": datetime.date(2025, 6, 1),
        "location": "Remote",
        "bullets": [
            "Designed and enigineered a new SaaS product to commence the company's expansion into the global market.",
            "Directed a 5-member team, delivering 2 new SaaS products allowing the company to expand into new markets.",
            "Established a deployment infrustructure that would cut the deployment time by 50% and increase the reliability of the system.",
        ],
    },
    {
        "title": "Chief Technology Officer",
        "company": "WIoT Technologies",
        "start": datetime.date(2023, 6, 1),
        "end": datetime.date(2023, 12, 1),
        "location": "Bishkek",
        "bullets": [
            "Led the end-to-end development and deployment of WIOT's unified IoT platform, architecting a scalable infrastructure that aggregates and visualizes device data for businesses and homes in Bishkek.",
            "Designed and implemented robust integrations with diverse IoT devices and communication protocols, ensuring seamless data collection, real-time monitoring, and centralized management for end users.",
            "Directed full-stack engineering efforts, optimizing cloud-based services and platform features to deliver high-level overviews, analytics, and actionable insights across a city-wide network of connected devices.",
        ],
    },
    {
        "title": "Course Mentor",
        "company": "CEC AUCA",
        "start": datetime.date(2023, 3, 1),
        "end": datetime.date(2023, 7, 1),
        "location": "Kyrgyzstan",
        "bullets": [
            "Mentored over 25 students, breaking down complex problems, leading to a 95% in student project completion rates.",
            "Introduced innovative coding exercises that improved creative thinking and problem-solving skills.",
        ],
    },
    {
        "title": "Teacher",
        "company": "Bilimkana-Bishkek",
        "start": datetime.date(2022, 9, 1),
        "end": datetime.date(2023, 6, 1),
        "location": "Kyrgyzstan",
        "bullets": [
            "Developed and implemented a dynamic web development curriculum, improving student engagement and understanding, with a 20% increase in final project submissions.",
            "Conducted regular assessments, adjusting teaching methods to improve learning outcomes by 70%.",
            "Led coding workshops and interactive sessions, resulting in a 25% improvement in student engagement.",
        ],
    },
    {
        "title": "Python Developer",
        "company": "DevelopsToday",
        "start": datetime.date(2022, 8, 8),
        "end": datetime.date(2023, 2, 1),
        "location": "Ukraine (Remote)",
        "bullets": [
            "Maintained scalable, asynchronous systems, increasing the project's performance.",
            "Worked on crucial features that improved the user experience.",
        ],
    },
    {
        "title": "Software Engineer",
        "company": "ESO Association",
        "start": datetime.date(2021, 9, 14),
        "end": datetime.date(2022, 8, 8),
        "location": "The Netherlands",
        "bullets": [
            "Developed modular, reusable code across multiple projects, reducing project delivery times by 20%.",
            "Collaborated with 5 internal committees, introducing a brand new platform that increased Association's engagement by 80%.",
        ],
    },
]


def get_experiences():
    today = datetime.date.today()
    enriched = []
    for exp in EXPERIENCES:
        end = exp["end"]
        date_range = "{} - {}".format(
            exp["start"].strftime("%B %Y"),
            end.strftime("%B %Y") if end else "Present",
        )
        days = ((end or today) - exp["start"]).days
        enriched.append({**exp, "date_range": date_range, "days": days})
    return enriched


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
    return render_template("home.html", experiences=get_experiences())


@app.get("/download")
def download():
    html_string = render_template("home.html", experiences=get_experiences())
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
