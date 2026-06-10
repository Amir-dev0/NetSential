import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "database.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scanned_ports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            port INTEGER,
            status TEXT
        )
        """)

        self.conn.commit()

    def save_scan(self, target, port, status):

        self.cursor.execute("""
        INSERT INTO scanned_ports (
            target,
            port,
            status
        )
        VALUES (?, ?, ?)
        """, (target, port, status))

        self.conn.commit()

    def close(self):
        self.conn.close()