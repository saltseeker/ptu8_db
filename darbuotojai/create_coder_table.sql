CREATE TABLE coder (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(200) UNIQUE,
    age INTEGER CHECK (age > 17 AND age < 75),
    experience INTEGER CHECK (experience < 40)
);



INSERt INTO coder (first_name, last_name, email, age, experience)
VALUES ("Kestutis", "Jenuskevicius", "kestas@idnow.fi", 39, 35);
INSERT INTO coder (first_name, last_name, email, age, experience)
VALUES ("Emilija", "Grybaite", "emi@midonow.fi", 19, 2);
SELECT * FROM coder;


-------pridedam project_id stulpeli
ALTER TABLE coder ADD COLUMN project_id INTEGER;

ALTER TABLE coder ADD COLUMN team_id INTEGER;
ALTER TABLE coder RENAME COLUMN team_id TO teams_id;
