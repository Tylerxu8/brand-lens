import json
from datetime import datetime
import yaml

from fetch import fetch_one
from parse import parse_page


def process_url(url):
	record = {
		"url": url,
		"fetched_at": datetime.now().isoformat(),
		"status": None,
		"error": None,
	}
	status, html, error = fetch_one(url)
	record["status"] = status
	record["error"] = error
	if html is not None:
		record.update(parse_page(html,url))
	return record

def main():
	with open("brands.yaml") as f:
		config = yaml.safe_load(f)

	brand_results = {}
	for slug, brand in config["brands"].items():
		print(f"\n=== {brand['name']} ===")
		pages = []
		for url in brand["pages"]:
			print(f"  fetching {url}...")
			record = process_url(url)
			if record["error"]:
				print(f"   -> FAILED: {record['error']}")
			else:
				print(f"   -> {record.get('title')}")
			pages.append(record)
		brand_results[slug] = {
			"name": brand["name"],
			"country": brand["country"],
			"pages": pages,
		}

	with open("results.json", "w") as f:
		json.dump(brand_results, f, indent=2)

	total_pages = sum(len(b["pages"]) for b in brand_results.values())
	total_errors = sum(1 for b in brand_results.values() for p in b ["pages"] if p["error"])
	print(f"\ndone. {len(brand_results)} brands, {total_pages} pages, {total_errors} errors.")


if __name__ == "__main__":
	main()