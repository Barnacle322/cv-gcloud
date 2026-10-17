"""Single source of truth for the résumé content.

`build_context()` returns what the template needs. A *variant* (a dict, usually
loaded from a JSON file — see ../variants/) can override any part of it for a
tailored PDF without touching the public page.
"""

import copy
import datetime

PROFILE = {
    "name": "Arstanbek Usenov",
    "location": "Vancouver, BC",
    "headline": "Software Developer",
    "work_status": "Eligible to work in Canada",
    "summary": "Full-stack Software Developer with about 5 years of professional "
    "experience in Python and TypeScript. Shipped production platforms "
    "end-to-end, from data model and API through frontend, payments, and "
    "deployment, for clients in Hong Kong, Kyrgyzstan, and the Netherlands. "
    "Starting the BCIT Computer Information Technology diploma (graduating 2028).",
    "email": "arstan.usenov@gmail.com",
    "linkedin": "https://www.linkedin.com/in/arstanbek-usenov/",
    "telegram": "https://t.me/Barnacle/",
}

EDUCATION = [
    {
        "years": "September 2026 - May 2028 (expected)",
        "program": "Computer Information Technology Diploma",
        "place": "British Columbia Institute of Technology (BCIT)",
    },
    {
        "years": "September 2021 - July 2022",
        "program": "Engineering Stream",
        "place": "Twente Pathway College, Netherlands",
    },
]

LANGUAGES = [
    {"name": "English", "level": "Professional - IELTS 8.0 (CLB 10)"},
    {"name": "Russian", "level": "Native"},
]

SKILLS = [
    {"category": "Languages", "text": "Python, TypeScript, JavaScript, SQL, Rust"},
    {
        "category": "Backend",
        "text": "FastAPI, Flask, Django, SQLAlchemy, Celery, pytest, REST APIs",
    },
    {"category": "Frontend", "text": "Vue 3, React, Tailwind CSS, Figma"},
    {
        "category": "Data & Infra",
        "text": "PostgreSQL, Redis, Docker, GitHub Actions, AWS, Google Cloud",
    },
    {"category": "Tooling", "text": "Git, Stripe, Sentry, Postman"},
]

# Entries shown on the public page, in order. Variants pick their own ids and
# can also use the individual roles that "teaching" and "earlier" summarize.
SITE_EXPERIENCES = [
    "rw",
    "halftone",
    "polytech",
    "kasu",
    "globalify",
    "wiot",
    "teaching",
    "earlier",
]

EXPERIENCES = [
    {
        "id": "rw",
        "title": "Full-Stack Developer",
        "company": "RW Community",
        "start": datetime.date(2026, 4, 1),
        "end": None,
        "location": "Remote (Hong Kong client)",
        "bullets": [
            "Architected and shipped a private members' club platform (FastAPI, Vue 3 + TypeScript PWA, PostgreSQL): registration, tiered memberships, event booking, guest passes.",
            "Integrated Suprema BioStar 2 biometric access over WireGuard, syncing face, QR, NFC, and mobile credentials so door access follows payment and tier status in real time.",
            "Designed a ledger-based points engine: per-batch expiry, tiered purchase bonuses, referral rewards.",
            "Built Stripe payments with Celery-scheduled renewal reminders and reporting.",
        ],
    },
    {
        "id": "halftone",
        "title": "Co-founder & Software Developer",
        "company": "Halftone",
        "start": None,  # TODO: start date
        "end": None,
        "location": "Vancouver, BC",
        "bullets": [
            "Co-founded a two-person product design and engineering studio that handles full-cycle builds for startups, from product design through engineering and launch.",
        ],
    },
    {
        "id": "polytech",
        "title": "Software Developer (Contract)",
        "company": "Polytechnology LTD",
        "start": None,  # TODO: start date
        "end": None,
        "location": "Bishkek (Remote)",
        "bullets": [
            "Built the building management system for IVOX, the company's AV and climate systems product line, used to monitor and control equipment installed in client buildings.",
            "Developed the IVOX digital signage and hotel TV platform, which manages content on lobby and in-room displays.",
            "Built a warehouse management system for tracking equipment stock across the company's installation projects.",
        ],
    },
    {
        "id": "atlabyte",
        "title": "Intern Mentor",
        "company": "Atlabyte",
        "start": datetime.date(2026, 1, 1),
        "end": datetime.date(2026, 4, 1),
        "location": "Bishkek",
        "bullets": [
            "Ran pairing sessions and code reviews to get junior developers onto production codebases in cybersecurity, e-commerce, and anti-fraud tracks.",
        ],
    },
    {
        "id": "kasu",
        "title": "Tech Lead",
        "company": "kasu.fun",
        "start": datetime.date(2025, 4, 1),
        "end": datetime.date(2025, 6, 1),
        "location": "Remote",
        "bullets": [
            "Built Solana programs in Rust/Anchor plus a Python client for on-chain parimutuel betting and quizzes.",
            "Shipped the web app (Flask API, Vue.js frontend) for quiz creation, participation, and leaderboards, with automated social media posting and AI-generated images.",
        ],
    },
    {
        "id": "globalify",
        "title": "Tech Lead",
        "company": "Globalify",
        "start": datetime.date(2023, 6, 1),
        "end": datetime.date(2025, 6, 1),
        "location": "Remote",
        "bullets": [
            "Led a 5-person engineering team that delivered two new SaaS products for the company's expansion into new markets.",
            "Designed and built the first of these products and set up the deployment infrastructure for both.",
        ],
    },
    {
        "id": "wiot",
        "title": "Founding Engineer",
        "company": "WIoT Technologies",
        "start": datetime.date(2023, 6, 1),
        "end": datetime.date(2023, 12, 1),
        "location": "Bishkek",
        "bullets": [
            "Built WIoT's IoT platform end-to-end, collecting and visualizing device data for businesses and homes across a city-wide network in Bishkek.",
            "Integrated diverse IoT devices and communication protocols into a single platform for real-time monitoring and centralized management.",
        ],
    },
    {
        "id": "teaching",
        "title": "Teaching & Mentoring",
        "company": None,
        "start": datetime.date(2022, 9, 1),
        "end": datetime.date(2026, 4, 1),
        "location": "Bishkek, Kyrgyzstan",
        "bullets": [
            "Intern Mentor, Atlabyte (January 2026 - April 2026): ran pairing sessions and code reviews to get junior developers onto production codebases in cybersecurity, e-commerce, and anti-fraud tracks.",
            "Course Mentor, CEC AUCA (March 2023 - July 2023): mentored 25+ students through programming course projects.",
            "Web Development Teacher, Bilimkana-Bishkek (September 2022 - June 2023): designed and taught a web development curriculum, with workshops and project assessments.",
        ],
    },
    {
        "id": "cec",
        "title": "Course Mentor",
        "company": "CEC AUCA",
        "start": datetime.date(2023, 3, 1),
        "end": datetime.date(2023, 7, 1),
        "location": "Kyrgyzstan",
        "bullets": [
            "Mentored 25+ students through programming course projects.",
        ],
    },
    {
        "id": "bilimkana",
        "title": "Web Development Teacher",
        "company": "Bilimkana-Bishkek",
        "start": datetime.date(2022, 9, 1),
        "end": datetime.date(2023, 6, 1),
        "location": "Kyrgyzstan",
        "bullets": [
            "Designed and taught a web development curriculum, with workshops and project assessments.",
        ],
    },
    {
        "id": "earlier",
        "title": "Earlier Roles",
        "company": None,
        "start": datetime.date(2021, 9, 1),
        "end": datetime.date(2023, 2, 1),
        "location": None,
        "bullets": [
            "Python Developer, DevelopsToday, Remote (August 2022 - February 2023): maintained asynchronous Python backend services and shipped user-facing features.",
            "Software Developer, ESO Association, Netherlands (September 2021 - August 2022): built a shared platform used by the association's 5 internal committees.",
        ],
    },
    {
        "id": "developstoday",
        "title": "Python Developer",
        "company": "DevelopsToday",
        "start": datetime.date(2022, 8, 1),
        "end": datetime.date(2023, 2, 1),
        "location": "Remote",
        "bullets": [
            "Maintained asynchronous Python backend services and shipped user-facing features.",
        ],
    },
    {
        "id": "eso",
        "title": "Software Developer",
        "company": "ESO Association",
        "start": datetime.date(2021, 9, 1),
        "end": datetime.date(2022, 8, 1),
        "location": "The Netherlands",
        "bullets": [
            "Built a shared platform used by the association's 5 internal committees.",
        ],
    },
]


def _enrich(exp, today):
    end = exp["end"]
    end_label = end.strftime("%B %Y") if end else "Present"
    if exp.get("end_note"):
        end_label += " ({})".format(exp["end_note"])
    if exp["start"]:
        date_range = "{} - {}".format(exp["start"].strftime("%B %Y"), end_label)
        days = ((end or today) - exp["start"]).days
    else:
        date_range, days = end_label, None
    return {**exp, "date_range": date_range, "days": days}


def _apply_experience_variant(base, spec):
    """`spec` is a list; each entry is an id string or {"id": ..., overrides}.
    Order of the list = display order. Ids absent from the list are dropped.
    Overrides: title, bullets (full replacement), extra_bullets (appended)."""
    by_id = {e["id"]: e for e in base}
    out = []
    for entry in spec:
        if isinstance(entry, str):
            entry = {"id": entry}
        exp = copy.deepcopy(by_id[entry["id"]])
        if "title" in entry:
            exp["title"] = entry["title"]
        if "bullets" in entry:
            exp["bullets"] = list(entry["bullets"])
        if "extra_bullets" in entry:
            exp["bullets"] = exp["bullets"] + list(entry["extra_bullets"])
        out.append(exp)
    return out


def build_context(variant=None, today=None):
    """Return the template context. `variant` keys (all optional):
    headline, summary, location, work_status, skills (full list of {category, text}),
    experiences (see _apply_experience_variant), education (full list),
    show_days (bool, default False), filename (PDF name)."""
    variant = variant or {}
    today = today or datetime.date.today()

    profile = dict(PROFILE)
    for key in ("headline", "summary", "location", "work_status"):
        if key in variant:
            profile[key] = variant[key]

    experiences = _apply_experience_variant(
        EXPERIENCES, variant.get("experiences", SITE_EXPERIENCES)
    )

    return {
        "profile": profile,
        "education": variant.get("education", EDUCATION),
        "languages": LANGUAGES,
        "skills": variant.get("skills", SKILLS),
        "experiences": [_enrich(e, today) for e in experiences],
        "show_days": variant.get("show_days", False),
    }
