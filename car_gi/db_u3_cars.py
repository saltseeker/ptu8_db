import sqlite3
import os
from tabulate import tabulate
from data.demodata import demodata


def add_search_param(search_row, search_param):
    if search_row == "":
        return search_param
    else:
        return f' AND {search_param}'


def get_between_param(nuo, iki, name):
    if nuo != "" and iki != "":
        search_param = f'"{name}" BETWEEN "{nuo}" AND "{iki}"'
    if nuo != "" and iki == "":
        search_param = f'"{name}" >= "{nuo}"'
    if nuo == "" and iki != "":
        search_param = f'"{name}" <= "{iki}"'
    return search_param


def escape_input(input_text):
    param = input(f'{input_text}: ')
    for s in ["%", "-", "?", "=", "'", '"']:
        param = param.replace(s, "")
    return param


create_car_tbl_query = """
    CREATE TABLE IF NOT EXISTS "car" (
        "id"                INTEGER NOT NULL,
        "marke"             VARCHAR(50) NOT NULL,
        "modelis"           VARCHAR(50) NOT NULL,
        "spalva"            VARCHAR(50) NOT NULL,
        "pagaminimo_metai"  INTEGER NOT NULL,
        "kaina"             FLOAT NOT NULL,
        PRIMARY KEY ("id")
    )
"""

insert_query = """
    INSERT INTO "car" ("marke", "modelis", "spalva", "pagaminimo_metai", "kaina")
        VALUES (?, ?, ?, ?, ?);
"""

conn = sqlite3.connect("car_gi/data/db_u3.db")
c = conn.cursor()

with conn:
    c.execute(create_car_tbl_query)

    c.execute('SELECT * FROM "car"')
    if len(c.fetchall()) < 1:
        inp = input("Duomenų bazė tuščia. Įveskite TAIP jei norite ją užpildyti demonstraciniais duomenimis: ")
        if inp.lower() == "taip":
            c.executemany(insert_query, demodata)


clear_cmd = "cls" if os.name == "nt" else "clear"
while True:
    os.system(clear_cmd)
    print("===[ Automobilių DB ]===\n")
    print("[1] Pridėti įrašą")
    print("[2] Atlikti paiešką")
    print("[0] Baigti darbą...")

    inp = input("\nĮveskite pasirinkimą: ")
    os.system(clear_cmd)

    if inp == "1":
        print("===[ Naujas įrašo įtraukimas ]===\n")
        marke = escape_input("Markė")
        modelis = escape_input("Modelis")
        spalva = escape_input("Spalva")
        pagaminimo_metai = escape_input("Pagaminimo metai")
        kaina = float(input("Kaina: "))

        with conn:
            c.execute(insert_query, (marke, modelis, spalva, pagaminimo_metai, kaina))

        input("\nNaujas įrašas įtrauktas. Spauskite ENTER mygtuką...")

    if inp == "2":
        search_param_row = ""

        print("===[ Įrašo paieška ]===\n")
        print("Norėdami praleisti parametrą spauskite ENTER")

        id = escape_input("ID")
        if id != "":
            search_param_row += add_search_param(search_param_row, f'"id" == "{id}"')

        marke = escape_input("Markė")
        if marke != "":
            search_param_row += add_search_param(search_param_row, f'"marke" == "{marke}"')

        modelis = escape_input("Modelis")
        if modelis != "":
            search_param_row += add_search_param(search_param_row, f'"modelis" == "{modelis}"')

        spalva = escape_input("Spalva")
        if spalva != "":
            search_param_row += add_search_param(search_param_row, f'"spalva" == "{spalva}"')

        print("Pagaminimo metai:")
        metai_nuo = escape_input(" Nuo")
        metai_iki = escape_input(" Iki")
        if metai_nuo != "" or metai_iki != "":
            search_param_row += add_search_param(search_param_row, get_between_param(metai_nuo, metai_iki, "pagaminimo_metai"))

        print("Kaina:")
        kaina_nuo = escape_input(" Nuo")
        kaina_iki = escape_input(" Iki")
        if kaina_nuo != "" or kaina_iki != "":
            search_param_row += add_search_param(search_param_row, get_between_param(kaina_nuo, kaina_iki, "kaina"))

        if search_param_row == "":
            select_query = f'SELECT * FROM "car"'
        else:
            select_query = f'SELECT * FROM "car" WHERE {search_param_row}'

        # print(select_query)
        with conn:
            c.execute(select_query)
            result = c.fetchall()
            if len(result) < 1:
                print(
                    f"\nPagal nurodytus kriterijus įrašų nerasta")
            else:
                print(
                    f"\nPagal nurodytus kriterijus surasta {len(result)} įrašų: \n")
                print(tabulate(result, headers=["ID", "Markė", "Modelis", "Spalva", "Pagaminimo metai", "Kaina"]))

        input("\nSpauskite ENTER mygtuką...")

    if inp == "0":
        break

