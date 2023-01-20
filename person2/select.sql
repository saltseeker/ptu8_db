<<<<<<< HEAD
-- SELECT * FROM person;
-- SELECT * FROM car;
-- SELECT * FROM company;

-- ------WHERE----------

-- SELECT person.first_name, person.last_name, car.plate      -----ko reikia
--     FROM person, car                                       -----is kuriu lauku
--     WHERE person.car_id = car.id;                          -----

-- SELECT last_name, name, make FROM person, company, car          ---- ka pasirenki ir kokias lenteles naudosi
--     where person.company_id = company.id AND person.car_id = car.id
--     ORDER BY name, make;                                                                 

------JOIN-------    

-- SELECT last_name, make, model FROM person JOIN car ON  person.car_id = car.id;
-- SELECT last_name, plate, name FROM person
--     JOIN car ON person.car_id = car.id
--     JOIN company ON person.company_id = company.id
--     WHERE company_id = 5;
--    --- WHERE name LIKE "%a";


-- SELECT last_name, make, model, plate, name FROM person
--     join car ON person.car_id = car.id
--     JOIN company ON person.company_id = company.id
--     WHERE make = "Ford"
--     ORDER BY name DESC;


-- SELECT name, count(*) as count FROM person 
--     JOIN company ON company_id = company.id
--     GROUP BY name;


-- SELECT name, count(*) as count FROM person 
--     JOIN company ON company_id = company.id       ------ kur dirba daugiau uz 3
--     GROUP BY name
--     HAVING count >3;


-- SELECT plate FROM car                                       ---- apple darbuotoju masinu numeriai
--     JOIN person ON person.car_id = car.id
--     JOIN company on person.company_id = company.id
--     WHERE company.name = "Apple";



----Isrinkti varda, pavarde, auto gamintoja ir imone tik is tu imoniu,
----- kuriose dirba iki 3 darbuotoju


-- SELECT first_name, last_name, make, name FROM person
--     JOIN car ON car_id = car.id
--     JOIN company on company_id = company.id
--     where company_id IN (
--         SELECT company.id FROM company
--             JOIN person ON person.company_id = company.id
--             GROUP BY name HAVING count() <= 3 ORDER BY name
--     );



-- INSERT INTO car (make, model, plate)
--     VALUES ("Dethlefts", "A1558", "BGY 555");
-- SELECT * FROM car;


-------sujunge lenteles tuscius laukus uzpildo NULL
-- SELECT first_name, last_name, make, model, plate FROM person
--     LEFT JOIN car ON car_id = car.id;



-- SELECT first_name, last_name, make, model FROM car
--     LEFT JOIN person ON car.id = person.car_id;
=======
SELECT * FROM person;
SELECT * FROM car;
SELECT * FROM company;

-- WHERE
SELECT person.first_name, person.last_name, person.email, car.plate
    FROM person, car
    WHERE person.car_id = car.id;

SELECT last_name, name, make FROM person, company, car
    WHERE person.company_id = company.id AND person.car_id = car.id
    ORDER BY name, make;

-- JOIN
SELECT last_name, make, model FROM person JOIN car ON person.car_id = car.id;

SELECT last_name, plate, name FROM person
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE name LIKE "%a%";

SELECT last_name, make, model, plate, name FROM person
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE make = "Ford"
    ORDER BY name DESC;

SELECT name, count(*) as count FROM person 
    JOIN company ON company_id = company.id
    GROUP BY name
    HAVING count > 3;

-- išrinkti tik Apple darbuotojų automobilių numerius
SELECT plate 
    FROM car
    JOIN person     ON person.car_id = car.id
    JOIN company    ON person.company_id = company.id
    WHERE company.name = "Apple";

-- išrinkti vardą, pavardė, auto gamintoją ir įmonę tik iš tų įmonių, 
-- kuriose dirba iki 3 darbuotojų
SELECT first_name, last_name, make, name FROM person
    JOIN car ON car_id = car.id
    JOIN company on company_id = company.id
    WHERE company_id IN (
        SELECT company.id FROM company 
            JOIN person ON person.company_id = company.id
            GROUP BY name HAVING count(*) <= 3 ORDER BY name
    );

INSERT INTO car (make, model, plate) 
    VALUES ("Dethleffs", "A1558", "BGY 555");
SELECT * FROM car;

-- LEFT JOIN
SELECT first_name, last_name, make, model, plate FROM person
    LEFT JOIN car on car_id = car.id;

SELECT first_name, last_name, make, model FROM car
    LEFT JOIN person ON person.car_id = car.id;
>>>>>>> c3cc311d3c4d897077cc9d174076df5106fbadcf
