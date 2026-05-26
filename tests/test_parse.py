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