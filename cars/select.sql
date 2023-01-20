-- SELECT * FROM cars;
-- SELECT * FROM cars WHERE year BETWEEN 2000 AND 2008;
-- SELECT * FROM cars WHERE color IN ("Violet", "Pink", "Fuscia");
-- SELECT * FROM cars WHERE color LIKE "violet";
-- SELECT * FROM cars WHERE model LIKE "X%";
-- SELECT * FROM cars WHERE model LIKE "%a";
-- SELECT * FROM cars WHERE model LIKE "__";
-- SELECT * FROM cars WHERE model LIKE "X_";
-- SELECT * FROM cars WHERE make LIKE "__n%";
-- SELECT * FROM cars WHERE color IS NULL;
-- SELECT * FROM cars WHERE color IS NOT NULL;
-- INSERT INTO cars (make, model, year, price)
--     VALUES ("Tesla", "Model Y", 2022, 55555);
-- SELECT * FROM cars WHERE make="Ford" AND year > 2000;
-- SELECT * FROM cars WHERE make="Ford" OR year > 2010 ORDER BY make, year;
-- SELECT * FROM cars WHERE make="Ford" 
--     OR year BETWEEN 2004 AND 2006 ORDER BY year, make;
-- SELECT * FROM cars WHERE color 
--     NOT IN ("Violet", "Pink", "Fuscia", "Puce", "Red", "Crimson");
-- SELECT * FROM cars 
--     WHERE (make = "Ford" OR make = "Volvo")
--     AND price BETWEEN 20000 AND 60000;
-- SELECT * FROM cars WHERE make = "tOyOta" COLLATE NOCASE;
-- SELECT "Gamintas: " || make from cars;
-- SELECT make || ", " || model as car, year, color FROM cars;
-- SELECT make, model, 2023-year as age FROM cars;
-- SELECT make, model, year, price, ROUND(price / 1.21, 2) AS price_ex_vat FROM cars;
-- SELECT min(year), max(year), avg(year) FROM cars;
-- SELECT min(price), max(price), avg(price) FROM cars;
-- SELECT make, model, min(price) FROM cars WHERE make="Toyota";
SELECT make, model, year, min(price) AS pigiausia, count(make) AS c
    FROM cars
    WHERE year > 1990
    GROUP BY make
    HAVING c>1
    ORDER BY pigiausia;
-- SELECT sum(price), count(price) as kiekis FROM cars;
