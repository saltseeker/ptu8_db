import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/darbuotojai.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS darbuotojai (
            id INTEGER PRIMARY KEY NOT NULL,
            vardas VARCHAR(50) NOT NULL,
            pavarde VARCHAR(100) NOT NULL,
            atlyginimas DECIMAL(10,2)
        )
    """)
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Giedrius', 'Išora', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Airida', 'Jūraitienė', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Eglė', 'Motiejūnaitė', 6666.66);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Daiva', 'Reinikė', 9999.99);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Kęstutis', 'Baužys', 7777.77);")
    darbuotojai = [
        ('Egidijus', 'Jankūnas', 0),
        ('Gediminas', 'Zakas', 10033.71),
        ('Ignas', 'Rocys', 6789.10),
        ('Kevinas', 'Karpus', 9876.54),
    ]
    c.executemany("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES (?, ?, ?)", darbuotojai)
    