import requests

from fetch import fetch_one


class FakeResponse:
	def __init__(self, status_code, text):
		self.status_code = status_code
		self.text = text


def test_fetch_one_returns_status_and_html_on_success(monkeypatch):
	def fake_get(url, timeout):
		return FakeResponse(200, "<html><body>hello</body></html>")

def test_fetch_one_returns_error_when_request_raises(monkeypatch):
	def fake_get(url, timeout):
		raise requests.RequestException("network is down")

def test_fetch_one_passes_through_non_200_status(monkeypatch):
	def fake_get(url, timeout):
		return FakeResponse(404, "<html><body>not found</body></html>")


	monkeypatch.setattr(requests, "get", fake_get)

	status, html, error = fetch_one("https://example.com/")

	assert status == 404
	assert html == "<html><body>not found</body></html>"
	assert error is None