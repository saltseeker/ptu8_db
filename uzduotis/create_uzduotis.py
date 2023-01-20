import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/uzduotis.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY NOT NULL,
            f_name VARCHAR(50) NOT NULL,
            l_name VARCHAR(100) NOT NULL,
            email VARCHAR(200) NOT NULL
        )
    """)
