# DC Compact Comics — Live Dashboard

A clean, live dashboard cataloging all released and upcoming **DC Compact Comics**, sorted from newest to oldest based on the original publication year of their inside issues (1982–2021).

🔗 **Live Website:** [https://dc-compact-live-dashboard.vercel.app](https://dc-compact-live-dashboard.vercel.app)

---

## Preview

<!-- Replace this image path or URL with your screenshot when ready -->
![DC Compact Comics Live Dashboard Screenshot](https://placehold.co/1200x630/0d0f14/3b82f6?text=DC+Compact+Comics+Dashboard+Preview)

---

## Features

- **Inside Issue Chronology:** Strictly sorted from newest (2021) to oldest (1982) by the original publication year of the inside material.
- **Where to Buy:** Direct purchase links for every book to **Amazon**, **Penguin Random House**, and **Indigo (Chapters)** via verified ISBNs.
- **Dual Views:** Switch between **Card Matrix** (grid) and **Chronological Stream** (timeline).
- **Instant Search & Era Filters:** Real-time search across titles, creators, and collected issues, with era toggles (Modern, 90s, Copper/Bronze).
- **Daily Automated Updates:** Daily GitHub Actions workflow checks for new solicitations and automatically triggers Vercel redeployments.

---

## Tech Stack

- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript (zero build step)
- **API:** Vercel Serverless Function (`/api/comics`)
- **Automation:** GitHub Actions cron (`.github/workflows/update-solicitations.yml`)
- **Scraper:** Python 3 (`update_compact_comics.py`)

---

<p align="center">
  <sub>Made with Rohail &amp; Adeel with Google Antigravity</sub>
</p>
