# fetch_many.py
# Read a list of URLs from urls.txt (one URL per line)
# For each URL:
#	- fetch it
#	- extract the title
#	- record the result (URL, title, status, timestamp)
#	- if anything goes wrong, record the error instead of crashing
# Write all results to results.json (one JSON object per line)
# Print a short summary at the end: how many succeeded, how many failed

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
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

with open("urls.txt") as f: 
	urls = [line.strip() for line in f if line.strip()]

print(f"loaded {len(urls)} urls")

results = []
for url in urls:
    print(f"fetching {url}...")
    record = fetch_one(url)
    if record["error"]:
        print(f"  -> FAILED: {record['error']}")
    else:
        print(f"  -> {record['title']}")
    results.append(record)

with open("results.json", "w") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")

successes = sum(1 for r in results if not r["error"])
failures = len(results) - successes
print(f"\nbingo. {successes} succeeded, {failures} failed.")