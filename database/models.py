import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "db.sqlite3"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            telegram_id INTEGER UNIQUE,
            full_name TEXT,
            username TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()

def add_user(telegram_id: int, full_name: str, username: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id, full_name, username)
        VALUES (?, ?, ?);
        """, (telegram_id, full_name, username))
        conn.commit()
