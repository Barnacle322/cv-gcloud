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
    "headline": None,  # optional line under the name, e.g. "Full-Stack Developer"
    "summary": None,  # optional paragraph at the top of the main column
    "email": "arstan.usenov@gmail.com",
    "linkedin": "https://www.linkedin.com/in/arstanbek-usenov-a68a78225/",
    "telegram": "https://t.me/Barnacle/",
}

EDUCATION = [
    {
        "years": "Sep 2026 - May 2028",
        "program": "Computer Information Technology Diploma",
        "place": "BCIT, Vancouver, CA",
    },
    {
        "years": "May 2023 - Jun 2023",
        "program": "Hero Training",
        "place": "Draper University, US",
    },
    {
        "years": "Sep 2021 - Jul 2022",
        "program": "Engineering Stream",
        "place": "Twente Pathway College, NL",
    },
    {
        "years": "Oct 2019 - Jun 2020",
        "program": "Java Backend Course",
        "place": "IT-Academy, KG",
    },
    {
        "years": "May 2019 - Jul 2019",
        "program": "Python Core Course",
        "place": "IT-Academy, KG",
    },
]

LANGUAGES = [
    {"name": "English", "level": "Advanced(C1) - IELTS 8.0"},
    {"name": "Russian", "level": None},
]

SKILLS = [
    {
        "category": "Programming Languages",
        "text": "Python, JavaScript, TypeScript, Java, SQL, Rust",
    },
    {
        "category": "Frameworks",
        "text": "Flask, FastAPI, Django, React, Vue.js, pinia, TailwindCSS, "
        "Express, Python-Telegram-Bot",
    },
    {
        "category": "Libraries",
        "text": "SQLAlchemy, Pydantic, Celery, authlib, alembic, pytest, "
        "asyncio, httpx, Pillow, uv, Poetry, Selenium, Babel",
    },
    {
        "category": "APIs & Auth",
        "text": "REST, GraphQL, JWT, OAuth2, WebSockets",
    },
    {
        "category": "Tools",
        "text": "Git, GitHub Actions, pgModeler, Postman, DBeaver",
    },
    {
        "category": "Web3 / Blockchain",
        "text": "Solana, Anchor, Web3.py, Ethers.js, Viem, MetaMask SDK, Privy",
    },
    {
        "category": "Infrastructure",
        "text": "Docker, CI/CD, Google Cloud, AWS, DigitalOcean, Hetzner, "
        "Cloudflare, Coolify, Dokploy",
    },
    {
        "category": "Technologies",
        "text": "PostgreSQL, Redis, Typesense, Algolia, Meilisearch, Supabase, "
        "Google Gemini, Stripe, Polar, Twilio, SendGrid, Resend, Mailchimp, "
        "Sentry, Doppler, Posthog, Google Analytics",
    },
    {
        "category": "Creative",
        "text": "Figma, Premiere Pro, Photoshop, Lightroom, Audition, "
        "DaVinci Resolve, Canva, Mixxx, MuseScore",
    },
]

EXPERIENCES = [
    {
        "id": "rw",
        "title": "Full-Stack Engineer",
        "company": "RW Community",
        "start": datetime.date(2026, 4, 1),
        "end": None,
        "end_note": "platform shipped; ongoing maintenance",
        "location": "Remote",
        "bullets": [
            "Architected and shipped a full-stack membership platform for a private members' club in Hong Kong with FastAPI, Vue 3 + TypeScript (PWA), and PostgreSQL — covering registration, tiered memberships, event booking, guest passes, and a points economy.",
            "Integrated Suprema BioStar 2 biometric door access over a WireGuard VPN, syncing membership state with face, QR, NFC, and mobile credentials so physical access reflects payment and tier status in real time.",
            "Designed a ledger-based points engine with per-batch expiry, tiered purchase bonuses, and referral rewards; shipped dual payment rails through Stripe with Celery-driven renewal reminders and reporting.",
        ],
    },
    {
        "id": "atlabyte",
        "title": "Intern Mentor & Software Engineer",
        "company": "Atlabyte",
        "start": datetime.date(2026, 1, 1),
        "end": datetime.date(2026, 4, 1),
        "location": "Bishkek",
        "bullets": [
            "Held a hybrid role spanning mentorship, engineering, and peer tutoring — supporting entry-level developers shipping into cybersecurity, e-commerce, and anti-fraud product tracks.",
            "Wired up internal tooling (CRM and team messaging integrations) into the development workflow to tighten the team's iteration cycle.",
            "Ran pairing, code reviews, and structured tutoring sessions to ramp junior engineers onto production codebases.",
        ],
    },
    {
        "id": "kasu",
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
        "id": "globalify",
        "title": "Chief Technology Officer",
        "company": "Globalify",
        "start": datetime.date(2023, 6, 1),
        "end": datetime.date(2025, 6, 1),
        "location": "Remote",
        "bullets": [
            "Designed and engineered a new SaaS product to commence the company's expansion into the global market.",
            "Directed a 5-member team, delivering 2 new SaaS products allowing the company to expand into new markets.",
            "Established a deployment infrastructure designed to cut deployment time by 50% and increase the reliability of the system.",
        ],
    },
    {
        "id": "wiot",
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
        "id": "cec",
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
        "id": "bilimkana",
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
        "id": "developstoday",
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
        "id": "eso",
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


def _enrich(exp, today):
    end = exp["end"]
    end_label = end.strftime("%B %Y") if end else "Present"
    if exp.get("end_note"):
        end_label += " ({})".format(exp["end_note"])
    date_range = "{} - {}".format(exp["start"].strftime("%B %Y"), end_label)
    days = ((end or today) - exp["start"]).days
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
    headline, summary, location, skills (full list of {category, text}),
    experiences (see _apply_experience_variant), education (full list),
    show_days (bool, default False for variants), filename (PDF name)."""
    variant = variant or {}
    today = today or datetime.date.today()

    profile = dict(PROFILE)
    for key in ("headline", "summary", "location"):
        if key in variant:
            profile[key] = variant[key]

    experiences = EXPERIENCES
    if "experiences" in variant:
        experiences = _apply_experience_variant(EXPERIENCES, variant["experiences"])

    return {
        "profile": profile,
        "education": variant.get("education", EDUCATION),
        "languages": LANGUAGES,
        "skills": variant.get("skills", SKILLS),
        "experiences": [_enrich(e, today) for e in experiences],
        "show_days": variant.get("show_days", not variant),
    }
