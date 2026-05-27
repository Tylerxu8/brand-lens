from parse import parse_page

def test_parse_page_extracts_title():
	html = """
	<html>
	  <head>
	    <title>Hello World</title>
	  </head>
	  <body></body>
	</html>
	"""
	record = parse_page(html, "https://example.com/")
	assert record["title"] == "Hello World"


def test_parse_page_returns_none_when_title_missing():
	html = "<html><head></head><body><h1>Hi</h1></body></html>"
	record = parse_page(html, "https://example.com/")
	assert record["title"] is None 


def test_parse_page_extracts_meta_description():
	html = """
	<html>
	  <head>
	    <meta name="description" content="A page about widgets">
	  </head>
	  <body></body>
	<html>
	"""
	record = parse_page(html, "https://example.com/")
	assert record["description"] == "A page about widgets"


def test_parse_page_returns_none_when_description_missing():
	html = "<html><head><title>X</title></head><body></body></html>"
	record = parse_page(html, "https://example.com/")
	assert record["description"] is None


def test_parse_page_extracts_og_title(full_page_html):
	record = parse_page(full_page_html, "https://example.com/")
	assert record["og_title"] == "Brand Lens - OG"


def test_parse_page_picks_first_h1(full_page_html):
	record = parse_page(full_page_html, "https://example.com/")
	assert record["h1"] == "Welcome to Brand Lens"


def test_parse_page_extracts_canonical(full_page_html):
	record = parse_page(full_page_html, "https://example.com/")
	assert record["canonical"] == "https://example.com/canonical"