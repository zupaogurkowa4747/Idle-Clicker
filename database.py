import sqlite3
from contextlib import contextmanager

DB_NAME = "database.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_NAME) 
    conn.row_factory = sqlite3.Row
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
                energy INTEGER DEFAULT 0,
                click_quantity INTEGER DEFAULT 1,
                all_clicks INTEGER DEFAULT 0,
                upgrade_quantity INTEGER DEFAULT 0,
                upgrade_price INTEGER DEFAULT 10,
                generators_quantity INTEGER DEFAULT 0,
                factory_price INTEGER DEFAULT 100
                )''')

def create_player(energy):
    with get_db() as cursor:
        cursor.execute("INSERT INTO player (energy) VALUES (?)", (energy,))

def load_player(player_id):
    with get_db() as cursor:
        cursor.execute("SELECT * FROM player WHERE id = ? ", (player_id,))
        result = cursor.fetchone()
        return result

def save_player(player_id, energy, click_quantity, all_clicks, upgrade_quantity, upgrade_price, generators_quantity, factory_price):
    with get_db() as cursor:
        cursor.execute("UPDATE player SET energy = ?, click_quantity = ?, all_clicks = ?, upgrade_quantity = ?, upgrade_price = ?, generators_quantity = ?, factory_price = ? WHERE id = ?",
        (energy, click_quantity, all_clicks, upgrade_quantity, upgrade_price, generators_quantity, factory_price, player_id))
