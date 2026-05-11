import requests


def fetch_one(url):
	"""Fetch a URL and return (status, html, error). Never raises."""
	try:
		response = requests.get(url, timeout=10)
		return response.status_code, response.text, None
	except Exception as e:
		return None, None, str(e)