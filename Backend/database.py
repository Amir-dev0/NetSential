# importing the required modules
import sqlite3
from pathlib import Path

# path database.db
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "database.db"

# connecting to database
conn = sqlite3.connect(DB_PATH)

# creating  curser
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

conn.commit()
conn.close()

print("Table deleted!")