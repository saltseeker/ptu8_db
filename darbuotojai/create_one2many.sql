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

CREATE TABLE skills (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE coders_skills (
    coder_id INTEGER,
    skill_id INTEGER,
    FOREIGN KEY (coder_id) REFERENCES coders (id),
    FOREIGN KEY (skill_id) REFERENCES skills (id)
);

CREATE TABLE passwords (
    id INTEGER PRIMARY KEY NOT NULL,
    coder_id INTEGER UNIQUE,
    pwd VARCHAR(200),
    FOREIGN KEY (coder_id) REFERENCES coders (id)
);

SELECT f_name, skills.name FROM coders 
    JOIN coders_skills ON coder_id = coders.id
    JOIN skills ON skill_id = skills.id;

SELECT f_name, l_name, pwd FROM coders JOIN passwords ON coder_id = coders.id;

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

INSERT INTO "skills" ("name") VALUES ('Python');
INSERT INTO "skills" ("name") VALUES ('JS');
INSERT INTO "skills" ("name") VALUES ('CSS');
INSERT INTO "skills" ("name") VALUES ('Go');
INSERT INTO "skills" ("name") VALUES ('AWS');
INSERT INTO "skills" ("name") VALUES ('Linux');

INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('1', '2');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('1', '3');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('2', '2');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('2', '3');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('3', '1');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('3', '4');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('4', '1');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('4', '6');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('5', '4');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('5', '5');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('6', '5');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('6', '6');

INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('1', '12345');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('2', 'verisykret');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('3', 'qwerty');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('4', 'uauauai');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('5', 'slaptazodis');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('6', 'barzda');
