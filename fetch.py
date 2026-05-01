import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.youtube.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string if soup.title else "(no title)"

result = {
	"url": url,
	"title": title,
	"fetched_at": datetime.now().isoformat(),
}

with open("result.json", "a") as f:
	f.write(json.dumps(result) + "\n")

print ("saved:", result)