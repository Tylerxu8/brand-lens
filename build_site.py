"""Rebuild the entire static site from the database into site/."""
import shutil
from datetime import date

import db
from generate_briefs import build_context  # or wherever build_context lives
from render import render_brief_html, render_index, write_page


def build_site():
    conn = db.get_connection()
    today = date.today().isoformat()

    brands = db.all_brands(conn)
    for brand in brands:
        context = build_context(conn, brand["slug"], brand["name"])
        context["generated_at"] = today
        html = render_brief_html(context)
        path = write_page(brand["slug"], html)
        print(f"wrote {path}")

    index_html = render_index(brands, today)
    write_page("index", index_html)
    print("wrote site/index.html")

    shutil.copy("static/style.css", "site/style.css")
    print("copied stylesheet")

    return len(brands)


if __name__ == "__main__":
    count = build_site()
    print(f"built site for {count} brand(s)")