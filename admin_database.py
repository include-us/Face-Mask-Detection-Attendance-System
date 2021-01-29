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
        cursor_obj = con.cursor()
        try:
            cursor_obj.execute("CREATE TABLE users(id integer PRIMARY KEY, name text, year real, department text, position text, hireDate text)")
            con.commit()
        except:
            print("TABLE EXISTS")
    def add_user(con, entities):
        try:
            cursor_obj = con.cursor()
            cursor_obj.execute('INSERT INTO users(id, name, year, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
            con.commit()
        except:
            print("PRIMARY KEY EXISTS")
    def search_user(con,search_id):
        try:
            cursor_obj=con.cursor()
            cursor_obj.execute("SELECT name,year FROM users WHERE id= ?",str(search_id))
            rows=cursor_obj.fetchall()
            for i in rows:
                print(rows)
        except:
            print("Does not exist")
    def delete_user(con,delete_id):
        try:
            cursor_obj=con.cursor()
            cursor_obj.execute("DELETE FROM users WHERE id= 2")
            print("DELETED")
        except:
            print("CANT DELETE USER")
    def __init__(self) -> None:
        con = database.sql_connection()      