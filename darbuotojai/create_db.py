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


#### pridedam darbuotoju

    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Giedrius', 'Isora', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Airida', 'Juraitiene', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Egle', 'Motiejunaite', 6666.66);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Daiva', 'Reinike', 9999.99);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Kestutis', 'Bauzys', 7777.77);")

    darbuotojai = [
        ('Egidijus', 'Jankunas', 0),
        ('Gedimimas', 'Zakas', 10033.31),
        ('Ignas', 'Rocys', 1231.33),
        ('Kevinas', 'Karpus', 3452.32),
    ]
    c.executemany("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES (?, ?, ?)", darbuotojai)
    
