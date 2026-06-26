import sqlite3
from pathlib import Path

APP_DIR = Path.home() / "AppData" / "Local" / "WarhammerTracker"
DB_PATH = APP_DIR / "warhammer_tracker.db"

def get_connection():
    APP_DIR.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS units (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                army TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 1,
                built_status TEXT NOT NULL,
                painted_status TEXT NOT NULL,
                storage_box TEXT,
                notes TEXT
            )
        """)

        conn.commit()

def add_unnit(name, army, quantity, built_status, painted_status, storage_box, notes):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO units (
                name,
                army,
                quantity,
                built_status,
                painted_status,
                storage_box,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, army, quantity, built_status, painted_status, storage_box, notes))

        conn.commit()

def get_all_units():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, army, quantity, build_status, painted_status, storage_box, notes
            FROM units
            ORDER BY army, name
        """)

        return cursor.fetchall()