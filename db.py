import sqlite3
from datetime import datetime

DB_PATH = "brand_lens.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS brands (
    slug TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS pages (
    id          INTEGER PRIMARY KEY,
    brand_slug  TEXT NOT NULL REFERENCES brands(slug),
    url         TEXT NOT NULL UNIQUE,
    status      INTEGER,
    title       TEXT,
    description TEXT,
    og_title    TEXT,
    h1          TEXT,
    canonical   TEXT,
    error       TEXT,
    fetched_at  TEXT NOT NULL
);
"""


def get_connection(db_path=DB_PATH):
    return sqlite3.connect(db_path)


def init_db(db_path=DB_PATH):
    conn = get_connection(db_path)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()

def insert_brand(conn, slug, name):
    conn.execute(
        "INSERT OR IGNORE INTO brands (slug, name) VALUES (?, ?)",
        (slug, name),
    )


def upsert_page(conn, brand_slug, record):
    conn.execute(
        """
        INSERT OR REPLACE INTO pages
            (brand_slug, url, status, title, description,
             og_title, h1, canonical, error, fetched_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            brand_slug,
            record["url"],
            record.get("status"),
            record.get("title"),
            record.get("description"),
            record.get("og_title"),
            record.get("h1"),
            record.get("canonical"),
            record.get("error"),
            record.get("fetched_at") or datetime.now().isoformat(),
        ),
    )

def pages_for_brand(conn, brand_slug):
    cursor = conn.execute(
        "SELECT url, title, status FROM pages WHERE brand_slug = ?",
        (brand_slug,),
    )
    return cursor.fetchall()
