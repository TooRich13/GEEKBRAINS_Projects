import os
import pandas as pd
import sqlite3 as sql


class Info():
    db_file = "Data.db"

    def sql_cursor(input_func):
        def output_func(self, *args):
            try:
                connection = sql.connect(self.db_file)
                with connection:
                    _cursor = connection.cursor()
                    input_func(self, *args, cursor=_cursor)
                    _cursor.close()
                    connection.commit()
            except sql.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if connection:
                    connection.close()
        return output_func

    def sql_connection(input_func):
        def output_func(self, *args):
            try:
                _connection = sql.connect(self.db_file)
                with _connection:
                    input_func(self, *args, connection=_connection)
                    _connection.commit()
            except sql.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if _connection:
                    _connection.close()
        return output_func

    def __init__(self):
        try:
            connection = sql.connect(self.db_file)
            with connection:
                cursor = connection.cursor()
                with open("db_init.sql", "r") as sqlite_file:
                    sql_script = sqlite_file.read()
                cursor.executescript(sql_script)
                connection.commit()
        except sql.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connection:
                connection.close()

    @sql_cursor
    def add_person(self, cursor):

        print("\nСоздание новоq записи .........................")
        name = input("Введите имя человека: ")
        surname = input(f"Введите фамилию  {name}: ")
        date = input(
            f"Введиту дату рождения {surname, name} в формате YYYY-MM-DD :  ")
        p_type = int(input(
            "Кто этот человек? Введите число:  \n1- Сотрудник \n2- Студент \n3- Школьник \n"))

        sql_query = """ INSERT INTO Person (Name, Surname, Date_of_birth, role ) VALUES (?, ?, ?, ?) """
        cursor.execute(sql_query, (name, surname, date, p_type))

        match p_type:
            case 1:
                company = input("Введите компанию сотрудника: ")
                post = input("Введите должность сотрудника: ")
                salary = float(input("Введите оклад сотрудника: "))
                ed = input("Введите образование сотрудника: ")

                sql_query = """ INSERT INTO Employee (User_id, Company, Post, Salary, Education)
                                VALUES (last_insert_rowid(), ?, ?, ?, ?)"""
                cursor.execute(sql_query, (company, post, salary, ed))

            case 2:
                university = input("Введите университет студента: ")
                spec = input("Введите специальность студента: ")
                year_adm = int(input("Введите год поступления студента: "))
                group = int(input("Введите групп студента: "))

                sql_query = """ INSERT INTO Student (
                                        User_id,
                                        University,
                                        Specialty,
                                        Admission_year,
                                        Group_id
                                )
                                VALUES (last_insert_rowid(), ?, ?, ?, ?)"""
                cursor.execute(sql_query, (university, spec, year_adm, group))
            case 3:
                school = input("Введите школу ученика: ")
                grade = input("Введите класс ученика: ")
                raiting = float(input("Введите среднюю оценку: "))

                sql_query = """ INSERT INTO School_student (
                                        User_id,
                                        School,
                                        Grade,
                                        Average_rating
                                    )
                                VALUES (last_insert_rowid(), ?, ?, ?)"""

                cursor.execute(sql_query, (school, grade, raiting))
                
                
    @sql_cursor
    def del_person(self, cursor):
        id = int(input("Введите ID Человека, о котором хотите удалить запись"))
        sql_query = ''' DELETE from Phones where id = ? '''
        cursor.execute(sql_query, (id,))

    @sql_cursor
    def print_list(self, cursor):
        print("\n___PERSON___\n")
        sql_query = ''' SELECT * FROM Person '''
        cursor.execute(sql_query)

        records = cursor.fetchall()
        print("Всего записей:  ", len(records), end="\n\n")
        for row in records:
            match row[4]:
                case "1":
                    role = "Сотрудник"
                case "2":
                    role = "Студент"
                case "3":
                    role = "Школьник"
            print(
                f"ID ЧЕЛОВЕКА: {row[0]}    Имя: {row[1]} {row[2]}    Дата рождения: {row[3]}    Роль: {role}", end="\n\n")

    @sql_cursor
    def print_person_info(self, cursor):
        id = int(input("Введите id человека, по которому холтите получить данные: "))
        sql_query = ''' SELECT *
                        FROM Person
                            LEFT JOIN Student ON Person.User_id = Student.User_id
                            LEFT JOIN Employee ON Person.User_id = Employee.User_id
                            LEFT JOIN School_student on Person.User_id = School_student.User_id
                        WHERE Person.User_id = ?   '''
        cursor.execute(sql_query,(id,))
        records = cursor.fetchall()
        for row in records:
            print(
                f"ID ЧЕЛОВЕКА: {row[0]}    Имя: {row[1]} {row[2]}    Дата рождения: {row[3]}")
            match row[4]:
                case  '1':
                    print(
                    f"Роль: Сотрудник   Компания: {row[11]}    Должность: {row[12]}    Оклад: {row[13]}   Образование {row[14]}")
                case '2':
                    print(
                    f"Роль: Студент     ВУЗ: {row[6]}    Специализация: {row[7]}    Год поступления: {row[8]}   Группа: {row[9]}")
                case '3':
                    print(
                    f"Роль: Школьник     Школа: {row[16]}    Класс: {row[17]}    Средняя оценка: {row[18]}")
            print("\n\n")
                    