--SELECT * FROM person;
--SELECT first_name, last_name FROM person;
--SELECT gender FROM person;
--SELECT DISTINCT gender FROM person;
--SELECT * FROM person WHERE gender = "Female";
--SELECT * FROM person WHERE date_of_birth > date("1999-01-01");

-- SELECT * FROM person
--   WHERE date_of_birth > "1999-01-01"
--     AND date_of_birth < "2003-01-01"
--     AND gender = "Female";

-----ORDER
--SELECT * FROM person ORDER BY last_name 
--SELECT * FROM person ORDER BY last_name DESC;
--SELECT * FROM person ORDER BY gender DESC, last_name, first_name;
--SELECT * FROM person ORDER BY date_of_birth;
--SELECT * FROM person ORDER BY date_of_birth DESC;


----GRUPAVIMAS
--SELECT gender, count(gender) AS count FROM person GROUP BY gender;

-- SELECT gender, count(gender) AS count FROM person
--     WHERE date_of_birth >= "1988-01-01"          --WHERE filtruoja iki grupavimo
--     GROUP BY gender
--     HAVING count > 1;                              -- HAVING filtruoja po grupavimo

--SELECT first_name || " " || last_name AS vardas FROM person;



