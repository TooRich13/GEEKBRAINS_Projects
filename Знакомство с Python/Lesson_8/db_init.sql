CREATE TABLE IF NOT EXISTS Person (
    User_id INTEGER UNIQUE,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Date_of_birth TEXT NOT NULL,
    role TEXT,
    PRIMARY KEY(User_id AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS Employee (
    User_id INTEGER UNIQUE ,
    Company TEXT,
    Post TEXT NOT NULL,
    Salary REAL NOT NULL,
    Education TEXT NOT NULL,
    FOREIGN KEY(User_id) REFERENCES Person(User_id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Student (
    User_id INTEGER UNIQUE,
    University TEXT NOT NULL,
    Specialty TEXT NOT NULL,
    Admission_year INTEGER NOT NULL,
    Group_id INTEGER NOT NULL,
    FOREIGN KEY(User_id) REFERENCES Person(User_id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS School_student (
    User_id INTEGER UNIQUE,
    School TEXT NOT NULL,
    Grade TEXT NOT NULL,
    Average_rating REAL NOT NULL,
    FOREIGN KEY(User_id) REFERENCES Person(User_id) ON DELETE CASCADE
)