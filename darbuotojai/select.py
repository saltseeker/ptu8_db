


import sqlite3


conn = sqlite3.connect('data/darbuotojai.db')
c = conn.cursor()


with conn:
    ########pakeicia darbuotoja
    #c.execute("UPDATE darbuotojai SET vardas='Sandra', pavarde='Krisiunaite' WHERE id = 3; ")
    ###### istrinam darbuotoja
    #c.execute("DELETE FROM darbuotojai WHERE id=2;")


    c.execute("SELECT * FROM darbuotojai;")
    #darbuotojai = c.fetchall()
    while True:
        darbuotojas = c.fetchone()
        if darbuotojas:
            print(darbuotojas)
        else:
            break

# if darbuotojai:
#     print(darbuotojai)
