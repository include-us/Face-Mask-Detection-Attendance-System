import sqlite3 as db
import os
from sqlite3 import Error
import datetime
import sqlite3
import tkinter as tk
from tkinter import messagebox


class database:
    def __init__(self):
        self.con = db.connect('databases//users_info.db')
        self.curr = self.con.cursor()

    def add_user(self, name, year, dept):
        sid=self.curr.execute("SELECT COUNT(id) FROM users")
        sid=self.curr.fetchall()
        print(sid)
        id=int(sid[0][0])+1
        command = "INSERT INTO users VALUES('"+str(id)+"','" + \
            name+"','"+str(year)+"','"+dept+"','','0')"
        print("Called")
        try:
            self.curr.execute(command)
            self.con.commit()
            messagebox.showinfo("SUCCESS", "USER ADDED")
        except sqlite3.Error as er:
            messagebox.showerror("Error", "Couldnt add the user "+str(er))

    def delete_user(self, id):
        try:
            self.curr.execute("DELETE FROM users WHERE id=" + str(id))
            self.con.commit()
            messagebox.showinfo("SUCCESS", "USER DELETED")
        except:
            messagebox.showerror("Error", "Failed to delete user")

    def view_users(self):
        try:
            self.curr.execute("SELECT * FROM users")
            rows = self.curr.fetchall()
            return rows
        except:
            messagebox.showerror("Error While Fetching Table")
