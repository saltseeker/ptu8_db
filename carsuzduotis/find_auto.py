import sqlite3

conn = sqlite3.connect('carsuzduotis/cars1.db')
c = conn.cursor()

continue_search = True

while continue_search:
    make = input("Enter the cars make (or leave blank to skip): ")
    model = input("Enter the cars model (or leave blank to skip): ")
    color = input("Enter the cars color (or leave blank to skip): ")
    year_from = input("Enter the starting year (or leave blank to skip): ")
    year_to = input("Enter the ending year (or leave blank to skip): ")
    price_from = input("Enter the starting price (or leave blank to skip): ")
    price_to = input("Enter the ending price (or leave blank to skip): ")

    aNd = []

    if make:
        aNd.append("MAKE = '" + make + "'")
    if model:
        aNd.append("MODEL = '" + model + "'")
    if color:
        aNd.append("COLOR = '" + color + "'")
    if year_from:
        aNd.append("YEAR >= " + year_from + "'")
    if year_to:
        aNd.append("YEAR <= " + year_to + "'")
    if price_from:
        aNd.append("PRICE >= " + price_from + "'")
    if price_to:
        aNd.append("PRICE <= " + price_to + "'")

    if aNd:
        choice = "SELECT * FROM cars1 WHERE " + " AND ".join(aNd)
        print(choice)
        c.execute(choice)
        results = c.fetchall()
        if len(results) > 0:
            for result in results:
                print(result)
        else:
            print("Car does not exist.")
    else:
        print("Please enter at least one search parameter.")

    continue_search = input("Do you want to continue searching? (y/n)") == 'y'  



