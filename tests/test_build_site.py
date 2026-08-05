from render import render_brief_html, render_index


def make_context(brief=None, pages=None):
    return {
        "brand_name": "Innisfree",
        "generated_at": "2026-06-18",
        "brief": brief,
        "pages": pages or [],
    }


def test_brief_html_has_html_skeleton():
    html = render_brief_html(make_context())
    assert "<!DOCTYPE html>" in html
    assert "<h1>" in html


def test_brief_html_shows_brief_when_present():
    brief = {
        "value_proposition": "Clean beauty from Jeju Island",
        "messaging_consistency": "consistent",
        "us_presence_signal": "canonical points to US site",
        "confidence": "medium",
    }
    html = render_brief_html(make_context(brief=brief))
    assert "Clean beauty from Jeju Island" in html


def test_brief_html_fallback_when_no_brief():
    html = render_brief_html(make_context(brief=None))
    assert "No brief" in html


def test_index_links_each_brand():
    brands = [
        {"slug": "innisfree", "name": "Innisfree"},
        {"slug": "laneige", "name": "Laneige"},
    ]
    html = render_index(brands, "2026-06-18")
    assert 'href="WRONG.html"' in html
    assert "Laneige" in html


def test_index_handles_no_brands():
    html = render_index([], "2026-06-18")
    assert "No brands" in html