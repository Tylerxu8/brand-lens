import json
from datetime import date

import db
from render import render_brief, write_brief


def build_context(conn, slug, name):
	row = conn.execute(
		"SELECT brief FROM brands WHERE slug = ?", (slug,)
	).fetchone()

	brief_json = row[0] if row else None
	brief = json.loads(brief_json) if brief_json else None

	pages = db.page_fields_for_brand(conn, slug)

	return {
		"brand_name": name,
		"generated_at": date.today().isoformat(),
		"brief": brief,
		"pages": pages,
	}

def generate_all(conn):
	paths = []
	for slug, name in conn.execute("SELECT slug, name FROM brands").fetchall():
		context = build_context(conn, slug, name)
		markdown = render_brief(context)
		path = write_brief(slug, markdown)
		paths.append(path)
	return paths

if __name__ == "__main__":
	conn = db.get_connection()
	written = generate_all(conn)
	conn.close()
	for path in written:
		print(f"wrote {path}")