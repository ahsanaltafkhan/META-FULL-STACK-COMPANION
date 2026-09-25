CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    score INTEGER NOT NULL
);

INSERT INTO students (name, score)
VALUES ('Ahsan', 91), ('Ali', 82);

SELECT * FROM students;
SELECT name, score FROM students WHERE score >= 85;
