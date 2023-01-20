import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

with conn:
    # c.execute("UPDATE darbuotojai SET vardas='Sandra', pavarde='Krisiūnaitė' WHERE id=3;")
    # c.execute("DELETE FROM darbuotojai WHERE id=4")
    c.execute("SELECT * FROM darbuotojai;")
    # darbuotojai = c.fetchall()
    while True:
        darbuotojas = c.fetchone()
        if darbuotojas:
            print(darbuotojas)
        else:
            break

# if darbuotojai:
#     print(darbuotojai)
