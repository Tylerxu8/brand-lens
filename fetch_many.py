# fetch_many.py
# Read a list of URLs from urls.txt (one URL per line)
# For each URL:
#	- fetch it
#	- extract the title
#	- record the result (URL, title, status, timestamp)
#	- if anything goes wrong, record the error instead of crashing
# Write all results to results.json (one JSON object per line)
# Print a short summary at the end: how many succeeded, how many failed

import yaml
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import csv
# import traceback


def fetch_one(url):
    record = {
        "url": url,
        "fetched_at": datetime.now().isoformat(),
        "status": None,
        "title": None,
        "description": None,
        "og_title": None,
        "h1": None,
        "canonical": None,
        "error": None,
    }
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        record["status"] = response.status_code
        record["title"] = soup.title.string.strip() if soup.title else "(no title)"
        desc_tag = soup.find("meta", attrs={"name": "description"})
        record["description"] = desc_tag["content"].strip() if desc_tag and desc_tag["content"] is not None else None
        og_tag = soup.find("meta", attrs={"property": "og:title"})
        record["og_title"] = og_tag["content"].strip() if og_tag else None
        canonical_tag = soup.find("link", attrs={"rel": "canonical"})
        record["canonical"] = canonical_tag["href"] if canonical_tag else None
        h1_tag = soup.find("h1")
        record["h1"] = h1_tag.get_text(strip=True) if h1_tag else None
    except Exception as e:
        record["error"] = str(e)
    return record

with open("brands.yaml") as f:
    config = yaml.safe_load(f)

brand_results = {}
for slug, brand in config["brands"].items():
    print(f"\n=== {brand['name']} ===")
    pages = []
    for url in brand["pages"]:
        print(f"   fetching {url}...")
        record = fetch_one(url)
        if record["error"]:
            print(f"   -> FAILED: {record['error']}")
        else:
            print(f"   -> {record['title']}")
        pages.append(record)
    brand_results[slug] = {
        "name": brand["name"],
        "country": brand["country"],
        "pages": pages,
    }

with open("results.json", "w") as f:
    json.dump(brand_results, f, indent=2)


total_pages = sum(len(b["pages"]) for b in brand_results.values())
total_errors = sum(1 for b in brand_results.values() for p in b["pages"] if p["error"])
print(f"\ndone. {len(brand_results)} brands, {total_pages} pages, {total_errors} errors.")