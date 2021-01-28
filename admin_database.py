import sqlite3 as db
import os
from sqlite3 import Error
import datetime
class database:
    def sql_connection():
        try:
            con=db.connect("databases/users_info.db")
            return con
        except Error:
            print(Error)

    #-----------------TESTING ONLY PHASE----------------
    def sql_table(con):
        cursorObj = con.cursor()
        try:
            cursorObj.execute("CREATE TABLE users(id integer PRIMARY KEY, name text, year real, department text, position text, hireDate text)")
            con.commit()
        except:
            pass
    def add_user(con, entities):
        try:
            cursorObj = con.cursor()
            cursorObj.execute('INSERT INTO users(id, name, year, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
            con.commit()
        except:
            print("PRIMARY KEY EXISTS")
    # def delete_user():
    def __init__(self) -> None:
        con = database.sql_connection()
        database.sql_table(con)
        entities = (22, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
        database.add_user(con,entities)
        print("A")