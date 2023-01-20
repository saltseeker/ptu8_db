import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('carsuzduotis/cars1.db')
with conn:
    c = conn.cursor()
    c.execute("""
create table if not exists cars1 (
	id INTEGER PRIMARY KEY NOT NULL,
    MAkE VARCHAR(50),
	MODEL VARCHAR(50),
	COLOR VARCHAR(50),
	YEAR VARCHAR(50),
	PRICE INT
)
""")


    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Infiniti', 'QX', 'Orange', 1999, 46);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Pontiac', 'Grand Prix', 'Pink', 2002, 31);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Volvo', 'S60', 'Aquamarine', 2001, 27);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Ford', 'Explorer', 'Teal', 2010, 61);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Chevrolet', 'SSR', 'Puce', 2003, 4);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Buick', 'Regal', 'Aquamarine', 2003, 27);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Jaguar', 'X-Type', 'Pink', 2007, 20);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Mitsubishi', 'Truck', 'Maroon', 1988, 5);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Land Rover', 'Range Rover', 'Mauv', 2010, 15);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Chevrolet', 'Silverado 3500HD', 'Indigo', 2006, 1);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Volkswagen', 'Fox', 'Maroon', 1991, 26);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Mazda', 'CX-7', 'Goldenrod', 2009, 31);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Mercedes-Benz', 'SLS AMG', 'Fuscia', 2012, 82);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Chevrolet', 'Silverado 2500', 'Goldenrod', 2000, 43);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Toyota', 'Prius', 'Purple', 2005, 91);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Chevrolet', 'Corvette', 'Red', 1967, 12);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Chrysler', 'PT Cruiser', 'Fuscia', 2001, 54);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Audi', 'S4', 'Turquoise', 2002, 68);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Ford', 'Escort', 'Pink', 1991, 89);")
    # c.execute ("insert into cars1 (MAkE, MODEL, COLOR, YEAR, PRICE) values ('Ford', 'Club Wagon', 'Maroon', 1995, 43);")

