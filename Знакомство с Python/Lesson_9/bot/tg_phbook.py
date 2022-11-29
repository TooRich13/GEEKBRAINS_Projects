import os
import pandas as pd
import sqlite3 as sql


class Phonebook:
    db_file = "Phonebook.db"
    out = ""
    def sql_cursor(input_func):
        def output_func(self, *args):
            try:
                connection = sql.connect(self.db_file)
                with connection:
                    _cursor = connection.cursor()
                    input_func(self, *args, cursor = _cursor )
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
                    input_func(self, *args, connection = _connection)
                    _connection.commit()
            except sql.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if _connection:
                    _connection.close()
        return output_func

    @sql_cursor
    def __init__(self,  cursor) -> None:

        with open("db_init.sql", "r") as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)

    @sql_cursor
    def add_contact(self, _name, _surname, _phone, cursor):

        name = _name
        surname = _surname
        phone = int(_phone)

        sql_query = '''INSERT INTO People (Name, Surname) VALUES (?, ?)'''
        cursor.execute(sql_query, (name, surname))

        sql_query = '''INSERT INTO Phones(user_id, Phone_number) VALUES(last_insert_rowid(), ?)'''
        cursor.execute(sql_query, (phone,))


    # @sql_cursor
    # def add_number(self, cursor):
    #     print("\nДобавление нового номера .........................")
    #     user_id = int(
    #         input("Введите ID контакта, которому хотите добавить номер: "))

    #     sql_query = ''' SELECT * FROM People WHERE user_id = ? '''
    #     cursor.execute(sql_query, (user_id,))
    #     records = cursor.fetchall()

    #     for row in records:
    #         name = row[1]
    #         surname = row[2]

    #     phone = int(input(
    #         f"Напишите номер, (ТОЛЬКО ЦИФРЫ: БЕЗ СИМВОЛОВ ' ' и '+') который вы хотите добавить {name} {surname}: "))

    #     sql_query = '''INSERT INTO Phones(user_id, Phone_number) VALUES(?, ?)'''
    #     cursor.execute(sql_query, (user_id, phone))

    @sql_cursor
    def print_book(self, cursor):
        print("\n___PHONEBOOK___\n")
        sql_query = ''' SELECT * FROM People LEFT JOIN Phones ON Phones.user_id = People.user_id '''
        cursor.execute(sql_query)

        records = cursor.fetchall()
        
        self.out = f"Всего номеров:   {len(records)} \n\n"
        for row in records:
            self.out += f"ID КОНТАКТА: {row[0]}    Имя: {row[1]} {row[2]}    Номер: {row[5]} \n\n"
        return self.out

    @sql_cursor
    def del_contact(self, _id, cursor):
        user_id = _id

        sql_query = ''' DELETE from People where user_id = ? '''
        cursor.execute(sql_query, (user_id,))

        sql_query = ''' DELETE from Phones where user_id = ? '''
        cursor.execute(sql_query, (user_id,))

    # @sql_cursor
    # def del_number(self, cursor):
    #     user_id = int(
    #         input("Введите ID КОНТАКТА, у которого хотите удалить НОМЕР: "))

    #     sql_query = ''' SELECT id, Phone_number FROM Phones WHERE user_id = ? '''
    #     cursor.execute(sql_query, (user_id,))

    #     records = cursor.fetchall()
    #     for row in records:
    #         print(f"ID НОМЕРА: {row[0]}   Номер: {row[1]}", end="\n\n")

    #     id = int(input("Введите ID НОМЕРА, который хотите удалить: "))
    #     sql_query = ''' DELETE from Phones where id = ? '''
    #     cursor.execute(sql_query, (id,))

    # @sql_connection
    # def export_csv(self, filemane, connection):

    #     df = pd.read_sql_query(
    #         ''' SELECT People.user_id, Name, Surname, Phone_number FROM People LEFT JOIN Phones ON Phones.user_id = People.user_id ''', connection)
    #     df.to_csv(filemane, index=False)

    # @sql_connection
    # def export_txt(self, filename, connection):
    #     df = pd.read_sql_query(
    #         ''' SELECT People.user_id, Name, Surname, Phone_number FROM People LEFT JOIN Phones ON Phones.user_id = People.user_id ''', connection)
    #     df.to_string(filename, index=False)

    # @sql_cursor
    # def import_csv(self, file_csv, cursor):
    #     print("Импорт начался")
    #     df = pd.read_csv(file_csv)
    #     user_id_list =[]
    #     for rec in range(len(df)):
    #         if df["user_id"][rec] not in user_id_list:
    #             user_id_list.append(df["user_id"][rec])
    #             sql_query = '''INSERT INTO People (Name, Surname) VALUES (?, ?)'''
    #             cursor.execute(sql_query,(df["Name"][rec], df["Surname"][rec]))

    #         sql_query = '''INSERT INTO Phones(user_id, Phone_number) VALUES(?, ?)'''
    #         cursor.execute(sql_query, (int(df["user_id"][rec]) ,int(df["Phone_number"][rec])))
    #     print("Импорт прошел")

    @sql_cursor
    def clr_db(self,cursor):
        cursor.execute('''DELETE  FROM People''')
        cursor.execute('''DELETE  FROM Phones''')


        
        
