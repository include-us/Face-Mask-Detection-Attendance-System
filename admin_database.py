import sqlite3 as db
import os
from sqlite3 import Error

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
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO users(id, name, year, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
# def delete_user():

con = sql_connection()
sql_table(con)
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
add_user(con,entities)