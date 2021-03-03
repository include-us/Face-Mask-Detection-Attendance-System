import sqlite3 as db
import os
from sqlite3 import Error
import datetime
import tkinter as tk
from tkinter import messagebox

class database:
    def __init__(self):
        self.con=db.connect('databases//users_info.db')
        self.curr=self.con.cursor()
    def add_user(self,id,name,year,dept,barcode):
        try:
            command="INSERT INTO users VALUES('"+str(id)+"','"+name+"','"+str(year)+"','"+dept+"','"+barcode+"')"
            self.curr.execute(command)
            self.con.commit()
            messagebox.showinfo("SUCCESS","USER ADDED")
        except:
            messagebox.showerror("Error","Couldnt add the user")
    def delete_user(self,id):
        try:
            self.curr.execute("DELETE FROM users WHERE id=?",id)
            self.con.commit()
        except:
            messagebox.showerror("Error","Failed to delete user")
