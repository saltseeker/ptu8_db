import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
    print("Įveskite nieko kad išeiti")
    paieska = input("Ko ieškom?: ")
    if paieska == "":
        break
    else:
        paieska = f"%{paieska}%"
        with conn:
            # c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
            c.execute("SELECT * FROM darbuotojai WHERE pavarde LIKE ? OR vardas LIKE ?", (paieska, paieska))
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
                    print("...daugiau nieko nėra")
                    break
