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


    def create_metric_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpu_percent REAL,
        cpu_cores INTEGER,

        total_ram TEXT,
        used_ram TEXT,
        free_ram TEXT,
        ram_percent TEXT,

        total_disk TEXT,
        used_disk TEXT,
        free_disk TEXT,
        disk_percent TEXT,

        cpu_temperature REAL,

        battery_percent REAL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def save_system_metrics(self, metrics):

        self.cursor.execute("""
        INSERT INTO system_metrics (
            cpu_percent,
            cpu_cores,

            total_ram,
            used_ram,
            free_ram,
            ram_percent,

            total_disk,
            used_disk,
            free_disk,
            disk_percent,

            cpu_temperature,

            battery_percent
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            metrics["cpu_percent"],
            metrics["cpu_cores"],

            metrics["total_ram"],
            metrics["used_ram"],
            metrics["free_ram"],
            metrics["ram_percent"],

            metrics["total_disk"],
            metrics["used_disk"],
            metrics["free_disk"],
            metrics["disk_percent"],

            metrics["cpu_temperature"],

            metrics["battery_percent"]
        ))

        self.conn.commit()

    def create_users_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """)

        self.conn.commit()


    def create_user(self, username, password_hash):

        self.cursor.execute("""
        INSERT INTO users (
            username,
            password_hash
        )
        VALUES (?, ?)
        """, (username, password_hash))

        self.conn.commit()


    def get_user(self, username):

        self.cursor.execute("""
        SELECT username, password_hash
        FROM users
        WHERE username = ?
        """, (username,))   

        return self.cursor.fetchone()    

    def count_users(self):

        self.cursor.execute("""
        SELECT COUNT(*)
        FROM users
        """)

        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()