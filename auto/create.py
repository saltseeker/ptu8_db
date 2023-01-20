import sqlite3

conn = sqlite3.connect('data/automobiliai.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS auto (
            id INTEGER PRIMARY KEY NOT NULL,
            marke VARCHAR(50) NOT NULL,
            modelis VARCHAR(100) NOT NULL,
            spalva VARCHAR(100) NOT NULL,
            pagaminimo_metai INTEGER NOT NULL,
            kaina DECIMAL(10,2)
        )
    """)

while True:
    print("===[MENU]===")
    print("1. Suvesti duomenis i lentele")
    print("2. Paieska")
    print("Kad iseiti spauskite enter")
    choice = input("Pasirinkite: ")
    if choice == "":
        break
    if choice == "1":
        i_marke = input("Iveskite marke: ")
        i_modelis = input("Iveskite modeli: ")
        i_spalva = input("Iveskite spalva: ")
        i_metai = input("Iveskite metus: ")
        i_kaina = input("Iveskite kaina: ")

        c.execute("INSERT INTO auto (marke, modelis, spalva, pagaminimo_metai, kaina) VALUES (?,?,?,?,?)", (i_marke, i_modelis, i_spalva, i_metai, i_kaina))
        conn.commit()
        print("Sekmingai ivesti duomenys")

    if choice == "2":
        paieska_marke = input("Iveskite marke: ")
        paieska_modelis = input("Iveskite modeli: ")
        paieska_spalva = input("Iveskite spalva: ")
        paieska_metai_nuo = input("Iveskite metus nuo: ")
        paieska_metai_iki = input("Iveskite metus iki: ")
        paieska_kaina_nuo = input("Iveskite kaina nuo: ")
        paieska_kaina_iki = input("Iveskite kaina iki: ")
        paieska_marke = f"%{paieska_marke}%"
        paieska_modelis = f"%{paieska_modelis}%"
        paieska_spalva = f"%{paieska_spalva}%"
        select = "SELECT * FROM auto WHERE marke LIKE ? AND modelis LIKE ? and spalva LIKE ?"
        args = [paieska_marke, paieska_modelis, paieska_spalva]
        if paieska_metai_nuo:
            select += " AND pagaminimo_metai >= ?"
            args.append(paieska_metai_nuo)
        if paieska_metai_iki:
            select += " AND pagaminimo_metai <= ?"
            args.append(paieska_metai_iki)
        if paieska_kaina_nuo:
            select += " AND kaina >= ?"
            args.append(paieska_kaina_nuo)
        if paieska_kaina_iki:
            select += " AND kaina <= ?"
            args.append(paieska_kaina_iki)
        with conn:
            c.execute(select,args)
            while True:
                auto = c.fetchone()
                if auto:
                    print(auto)
                else:
                    print("tik tiek")
                    break

                    