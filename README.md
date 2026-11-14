# DC Compact Comics — Live Dashboard

> Interactive live dashboard for all released and upcoming DC Compact Comics, sorted newest to oldest based on the original publication year of their inside issues (1982–2021).

🔗 **Live Website:** [https://dc-compact-live-dashboard.vercel.app](https://dc-compact-live-dashboard.vercel.app)

---

## Features

- **Inside Issue Chronology:** Automatically sorted from newest (2021) to oldest (1982) by original material publication date.
- **Where to Buy:** Direct purchase links for every title to **Amazon**, **Penguin Random House**, and **Indigo (Chapters)** via validated ISBNs.
- **Dual Views:** Switch seamlessly between **Card Matrix** and **Chronological Stream**.
- **Instant Search & Filtering:** Filter by Era (Modern, 90s Dark Age, Copper/Bronze Age), publication status (Released vs. Upcoming), and real-time text query.
- **Automated Daily Sync:** GitHub Actions workflow runs daily at 06:00 UTC to check for new DC and Penguin Random House solicitations, auto-committing updates to trigger instant Vercel redeployments.

---

## Tech Stack

- **Frontend:** Vanilla HTML5, Tailwind CSS, JavaScript (zero external dependencies)
- **Deployment:** Vercel (Edge Serverless Function via `/api/comics`)
- **Automation:** GitHub Actions cron workflow (`.github/workflows/update-solicitations.yml`)
- **CLI / Scraper:** Python 3 (`update_compact_comics.py`)
