import sqlite3
from contextlib import contextmanager

DB_NAME = "database.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    with get_db() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS player (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                energy INTEGER DEFAULT 0)''')

def create_player(energy):
    with get_db() as cursor:
        cursor.execute("INSERT INTO player (energy) VALUES (0)", (energy,))