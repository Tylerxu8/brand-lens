import pytest
import sqlite3
import db


@pytest.fixture
def full_page_html():
	return """
	<html>
	  <head>
	    <title>Bbrand Lens</title>
	    <meta name="description" content="A tool for evaluating brand presence">
	    <meta property="og:title" content="Brand Lens - OG">
	    <link rel="canonical" href="https://example.com/canonical">
	  </head>
	  <body>
	    <h1>Welcome to Brand Lens</h1>
	    <h1>Second h1, should be ignored</h1>
	  </body>
	</html>
	"""

@pytest.fixture
def db_conn():
	conn = sqlite3.connect(":memory:")
	conn.executescript(db.SCHEMA)
	yield conn
	conn.close()