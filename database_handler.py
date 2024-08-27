import configparser
import os
import json  # Import the json module to handle JSON data
import sqlite3

def create_table():
    conn = sqlite3.connect('config.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS config_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_database(json_data):
    conn = sqlite3.connect('config.db')
    c = conn.cursor()
    c.execute('INSERT INTO config_data (data) VALUES (?)', (json_data,))
    conn.commit()
    conn.close()

def get_latest_data():
    conn = sqlite3.connect('config.db')
    c = conn.cursor()
    c.execute('SELECT data FROM config_data ORDER BY id DESC LIMIT 1')
    row = c.fetchone()
    conn.close()
    return json.loads(row[0]) if row else None

# Example usage
if __name__ == "__main__":
    create_table()
    sample_data = {"Database": {"host": "localhost", "port": 3306}}
    save_to_database(json.dumps(sample_data))
    print(get_latest_data())
