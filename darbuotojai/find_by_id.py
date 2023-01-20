import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
    print("Atskirimas kableliais, nieko kad iseiti")
    paieska = input("Iveskite ID: ")
    if paieska == "":
        break
    else:
        ids = paieska.split(',')
        with conn:
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'" )  ###veikia 'OR 1=1 -- 
            # Creating a string that looks like this:
            # SELECT * FROM darbuotojai WHERE rowid IN (?, ?, ?)
            query = "SELECT * FROM darbuotojai WHERE rowid IN ("+', '.join(['?' for x in range (len(ids))])+ ")"
            print(query)
            c.execute(query, ids)
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
                    print("...daugiau nieko nera")
                    break
