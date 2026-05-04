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

with open("urls.txt") as f:
	urls = [line.strip() for line in f if line.strip()]

print(f"loaded {len(urls)} urls")

results = []
successes = 0
failure = 0

for url in urls:
    print(f"fetching {url}...")
    record = {
        "url": url,
        "fetched_at": datetime.now().isoformat(),
    }
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "(no title)"
        record["status"] = response.status_code
        record["title"] = title.strip()
        record["error"] = None
        successes += 1
        print(f"  -> {title.strip()}")
    except Exception as e:
        record["status"] = None
        record["title"] = None
        record["error"] = str(e)
        failure += 1
        print(f"  -> FAILED: {e}")
    results.append(record)

with open("results.json", "w") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")

print(f"\ndone. {successes} succeeded, {failure} failed.")
print(f"results saved to results.json")