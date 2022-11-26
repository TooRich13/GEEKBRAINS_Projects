SELECT *
FROM Person
    LEFT JOIN Student ON Person.User_id = Student.User_id
    LEFT JOIN Employee ON Person.User_id = Employee.User_id
    LEFT JOIN School_student on Person.User_id = School_student.User_id
WHERE Person.User_id = 4