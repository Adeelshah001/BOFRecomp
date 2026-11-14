#!/usr/bin/env python3
"""
DC Compact Comics - Solicitations & Catalog Updater
Manages, updates, and sorts DC Compact Comics based on original inside issue release years.
"""

import json
import os
import sys
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "compact_comics.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    # Sort by original issue year descending (newest to oldest), then by release date descending
    data.sort(key=lambda x: (int(x.get("originalIssueYear", 0)), str(x.get("compactReleaseDate", ""))), reverse=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} titles to {DATA_FILE} (sorted newest to oldest by inside issue year).")

def add_title(title, original_year, collected_issues, compact_date, creators, genre, status="Upcoming", page_count=200, isbn="", description="", era="Modern"):
    data = load_data()
    slug = title.lower().replace(":", "").replace("'", "").replace("&", "and").replace(" ", "-")
    
    # Check if exists
    for item in data:
        if item.get("id") == slug or item.get("title").lower() == title.lower():
            print(f"Updating existing title: {title}")
            item.update({
                "originalIssueYear": int(original_year),
                "collectedIssues": collected_issues,
                "compactReleaseDate": compact_date,
                "status": status,
                "creators": creators,
                "genre": genre,
                "pageCount": int(page_count),
                "isbn": isbn,
                "description": description,
                "era": era
            })
            save_data(data)
            return

    new_item = {
        "id": slug,
        "title": title,
        "originalIssueYear": int(original_year),
        "originalIssueSpan": str(original_year),
        "collectedIssues": collected_issues,
        "compactReleaseDate": compact_date,
        "status": status,
        "creators": creators,
        "genre": genre,
        "pageCount": int(page_count),
        "isbn": isbn,
        "description": description,
        "era": era
    }
    data.append(new_item)
    save_data(data)
    print(f"Added new title: {title} ({original_year})")

def list_titles():
    data = load_data()
    print(f"\n=== DC COMPACT COMICS (Sorted: Newest to Oldest by Inside Issue Year) ===")
    print(f"Total Titles: {len(data)}\n")
    print(f"{'Inside Year':<12} | {'DC Compact Date':<15} | {'Status':<10} | {'Title'}")
    print("-" * 75)
    for item in data:
        print(f"{item.get('originalIssueYear', 'N/A'):<12} | {item.get('compactReleaseDate', 'N/A'):<15} | {item.get('status', 'N/A'):<10} | {item.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        list_titles()
    else:
        # Load, re-sort, and verify
        items = load_data()
        save_data(items)
        list_titles()
