import db
import brief


conn = db.get_connection()

for slug, name in conn.execute("SELECT slug, name FROM brands").fetchall():
	pages = db.page_fields_for_brand(conn, slug)
	summary, error = brief.summarize_brand(name, pages)
	if error:
		print(f"{slug}: SKIPPED - {error}")
		continue
	db.set_brief(conn, slug, summary)
	print(f"{slug}: brief stored")


conn.commit()
conn.close()