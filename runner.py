import json
from datetime import datetime
import yaml
import argparse
import csv

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
	parser = argparse.ArgumentParser(description="Fetch brand pages and produce a structured reort.")
	parser.add_argument("--input", "-i", default="brands.yaml", help="Path to brands YAML config")
	parser.add_argument("--output", "-o", default="results.json", help="Path to output JSON file")
	parser.add_argument("--limit", "-n", type=int, default=None, help="Only process the first N brands")
	parser.add_argument("--verbose", "-v", action="store_true", help="Print each page record as it's processed")
	parser.add_argument("--csv", help="Also writes a flat per-page CSV to this path")
	args = parser.parse_args()

	with open(args.input) as f:
		config = yaml.safe_load(f)

	brand_items = list(config["brands"].items())
	if args.limit is not None:
		brand_items = brand_items[: args.limit]

	brand_results = {}
	for slug, brand in brand_items:
		print(f"\n=== {brand['name']} ===")
		pages = []
		for url in brand["pages"]:
			print(f"  fetching {url}...")
			record = process_url(url)
			if record["error"]:
				print(f"   -> FAILED: {record['error']}")
			else:
				print(f"   -> {record.get('title')}")
			if args.verbose:
				print(f"   record: {record}")
			pages.append(record)
		brand_results[slug] = {
			"name": brand["name"],
			"country": brand["country"],
			"pages": pages,
		}

	if args.csv:
		rows = []
		for slug, brand in brand_results.items():
			for page in brand["pages"]:
				row = {"brand_slug": slug, "brand_name": brand["name"], "country": brand["country"]}
				row.update(page)
				rows.append(row)
		if rows:
			keys = list(rows[0].keys())
			with open(args.csv, "w", newline="") as f:
				writer = csv.DictWriter(f, fieldnames=keys)
				writer.writeheader()
				for r in rows:
					writer.writerow(r)
			print(f"csv written to {args.csv}")

	with open(args.output, "w") as f:
		json.dump(brand_results, f, indent=2)


	total_pages = sum(len(b["pages"]) for b in brand_results.values())
	total_errors = sum(1 for b in brand_results.values() for p in b["pages"] if p ["error"])
	print(f"\ndone. {len(brand_results)} brands, {total_pages} pages, {total_errors} errors.")
	print(f"output written to {args.output}")

if __name__ == "__main__":
	main()