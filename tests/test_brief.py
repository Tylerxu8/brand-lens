import json

import brief


class FakeBlock:
	def __init__(self, text):
		self.text = text


class FakeMessage:
	def __init__(self, text):
		self.content = [FakeBlock(text)]


def test_summarize_brand_parse_json_reply(monkeypatch):
	payload = {
		"value_proposition": "Clean beauty from Jeju",
		"messaging_consistency": "consistent",
		"us_presence_signal": "canonical points to US site",
		"confidence": "medium",
	}

	def fake_create(**kwargs):
		return FakeMessage(json.dumps(payload))

	monkeypatch.setattr(brief.client.messages, "create", fake_create)

	summary, error = brief.summarize_brand("Innisfree", [])

	assert error is None
	assert summary["confidence"] == "medium"
	assert summary["value_proposition"] == "Clean beauty from Jeju"


def test_summarize_brand_returns_error_on_bad_json(monkeypatch):
	def fake_create(**kwargs):
		return FakeMessage("Here is your analysis: {not valid json}")

	monkeypatch.setattr(brief.client.messages, "create", fake_create)

	summary, error = brief.summarize_brand("Innisfree", [])

	assert summary is None
	assert "parse" in error


def test_summarize_brand_returns_error_when_api_raises(monkeypatch):
	def fake_create(**kwargs):
		raise RuntimeError("rate limited")

	monkeypatch.setattr(brief.client.messages, "create", fake_create)

	summary, error = brief.summarize_brand("Innisfree", [])

	assert summary is None
	assert "api call failed" in error