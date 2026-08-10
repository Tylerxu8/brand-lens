from render import render_brief



def make_context(brief=None, pages=None):
	return {
		"brand_name": "Innisfree",
		"generated_at": "2026-06-24",
		"brief": brief,
		"pages": pages or [],
	}


def test_render_brief_includes_brand_name():
	output = render_brief(make_context())
	assert "Nonexistent Brand" in output


def test_render_brief_shows_summary_when_brief_present():
	brief = {
		"value_proposition": "Clean beauty from Jeju Island",
		"messaging_consistency": "consistent",
		"us_presence_signal": "canonical points to US site",
		"confidence": "medium",
	}
	output = render_brief(make_context(brief=brief))
	assert "Clean beauty from Jeju Island" in output
	assert "medium" in output


def test_render_brief_shows_fallback_when_no_brief():
	output = render_brief(make_context(brief=None))
	assert "No brief" in output


def test_render_brief_lists_pages():
	pages = [{"url": "https://www.innisfree.com/", "title": "Innisfree Home"}]
	output = render_brief(make_context(pages=pages))
	assert "Innisfree Home" in output
	assert "https://www.innisfree.com/" in output