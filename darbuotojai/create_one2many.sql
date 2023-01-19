CREATE TABLE teams (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(100)
);

CREATE TABLE coders (
    id INTEGER PRIMARY KEY NOT NULL,
    f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    email VARCHAR(200) UNIQUE,
    age INTEGER CHECK (age > 0),
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams (id)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(200) NOT NULL,
    coder_id INTEGER,
    FOREIGN KEY (coder_id) REFERENCES coders (id)
);

INSERT INTO "teams" ("name") VALUES ('Back End');
INSERT INTO "teams" ("name") VALUES ('DevOps');
INSERT INTO "teams" ("name") VALUES ('Front End');

INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Jonas', 'Jonaitis', 'jj@gmail.com', 20, 1);
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Antanas', 'Antanaitis', 'aa@gmail.com', 25, 1);
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Juozas', 'Juozaitis', 'jj@hotmail.com', 30, 2);
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Petras', 'Petraitis', 'pp@mail.lt', 29, 2);
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Virgis', 'Virgutis', 'vv@gmail.com', 21, 3);
INSERT INTO "coders" ("f_name", "l_name", "email", "age", "team_id") VALUES ('Tomas', 'Aidietis', 'ta@imone.lt', 35, 3);

SELECT * FROM coders JOIN teams ON team_id = teams.id;
SELECT f_name, l_name, name FROM teams JOIN coders ON team_id = teams.id;

INSERT INTO "tasks" ("name", "coder_id") VALUES ('Sutvarkyti DB', '5');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti dizainą', '1');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti formas', '2');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti tvarkykles', '6');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perkrauti serverius', '5');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti bibliotekas', '6');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Pakeisti logotipus', '2');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti dokumentaciją', '3');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Ištestuoti programą', '4');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti API', '4');

SELECT tasks.name as task, f_name as coder, teams.name as team FROM tasks 
    JOIN coders ON coder_id = coders.id
    JOIN teams ON team_id = teams.id;
