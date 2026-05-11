from bs4 import BeautifulSoup

def parse_page(html, url):
	"""Extract structured fields from an HTML page. Returns a dict."""
	soup = BeautifulSoup(html, "html.parser")
	record = {
		"url": url,
		"title": None,
		"description": None,
		"og_title": None,
		"h1": None,
		"canonical": None,
	}
	if soup.title and soup.title.string:
		record["title"] = soup.title.string.strip()
	desc_tag = soup.find("meta", attrs={"name": "description"})
	if desc_tag and desc_tag.get("content"):
		record["description"] = desc_tag["content"].strip()
	og_tag = soup.find("meta", attrs={"property": "og:title"})
	if og_tag and og_tag.get("content"):
		record["og_title"] = og_tag["content"].strip()
	h1_tag = soup.find("h1")
	if h1_tag:
		record["h1"] = h1_tag.get_text(strip=True)
	canonical_tag = soup.find("link", attrs={"rel": "canonical"})
	if canonical_tag and canonical_tag.get("href"):
		record["canonical"] = canonical_tag["href"]
	return record