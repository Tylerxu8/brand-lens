import db


def test_insert_and_read_page(db_conn):
    db.insert_brand(db_conn, "innisfree", "Innisfree")
    db.upsert_page(db_conn, "innisfree", {
        "url": "https://www.innisfree.com/",
        "status": 200,
        "title": "Innisfree",
    })
    rows = db.pages_for_brand(db_conn, "innisfree")
    assert len(rows) == 1
    assert rows[0][0] == "https://www.innisfree.com/"


def test_upsert_replaces_instead_of_duplicating(db_conn):
    db.insert_brand(db_conn, "innisfree", "Innisfree")
    db.upsert_page(db_conn, "innisfree", {"url": "https://x.com/", "title": "Old"})
    db.upsert_page(db_conn, "innisfree", {"url": "https://x.com/", "title": "New"})

    rows = db.pages_for_brand(db_conn, "innisfree")
    assert len(rows) == 1                 # one row, not two
    assert rows[0][1] == "New"            # holds the latest title


def test_missing_description_stored_as_null(db_conn):
    db.insert_brand(db_conn, "innisfree", "Innisfree")
    db.upsert_page(db_conn, "innisfree", {"url": "https://y.com/", "title": "Y"})

    cursor = db_conn.execute(
        "SELECT description FROM pages WHERE url = ?", ("https://y.com/",)
    )
    assert cursor.fetchone()[0] is None