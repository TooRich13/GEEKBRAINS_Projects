
CREATE DATABASE  test_db;
USE test_db;

CREATE TABLE Students (
    Id INT,
    Name VARCHAR(20),
    Age INT,
    Address VARCHAR(20)
);

INSERT INTO Students VALUES (1, 'Boba', 99, 'Earth');

SELECT * FROM Students;