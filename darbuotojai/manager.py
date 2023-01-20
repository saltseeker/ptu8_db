import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
<<<<<<< HEAD
    print("Iveskite nieko kad iseiti")
    paieska = input("Ko ieskom: ")
=======
    print("Įveskite nieko kad išeiti")
    paieska = input("Ko ieškom?: ")
>>>>>>> c3cc311d3c4d897077cc9d174076df5106fbadcf
    if paieska == "":
        break
    else:
        paieska = f"%{paieska}%"
        with conn:
<<<<<<< HEAD
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'" )  ###veikia 'OR 1=1 -- 
=======
            # c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
>>>>>>> c3cc311d3c4d897077cc9d174076df5106fbadcf
            c.execute("SELECT * FROM darbuotojai WHERE pavarde LIKE ? OR vardas LIKE ?", (paieska, paieska))
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
<<<<<<< HEAD
                    print("...daugiau nieko nera")
=======
                    print("...daugiau nieko nėra")
>>>>>>> c3cc311d3c4d897077cc9d174076df5106fbadcf
                    break
