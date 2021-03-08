import tkinter as tk
from tkinter import messagebox
from admin_database import database as db
from tkinter import *


class database_methods(object):
    def view_command(self):
        self.list.delete(0, END)
        self.srows = db()
        rows = self.srows.view_users()
        for row in rows:
            self.list.insert(END, row)

    # --------------------------Windows----------------------------
    def add_window(self):
        self.window_add = tk.Tk()
        self.window_add.geometry("400x200")
        self.window_add.title("Add A User")

        self.window_add.mainloop()

    def delete_window(self):
        self.window_delete = tk.Tk()
        self.window_delete.geometry("400x200")
        self.window_delete.title("Delete A User")

        self.window_delete.mainloop()

    def view_window(self):
        self.window_view = tk.Tk()
        self.window_view.geometry("500x400")
        self.window_view.title("View All Users")
        self.list = tk.Listbox(self.window_view, height=25, width=65)
        self.scroller = tk.Scrollbar(self.window_view)
        self.btn_update = tk.Button(
            self.window_view,
            text="Update",
            height=1,
            width=20,
            command=self.view_command,
        )
        self.btn_update.grid(row=30, column=0, columnspan=2)
        self.scroller.grid(row=2, column=2, rowspan=6)
        self.list.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.list.configure(yscrollcommand=self.scroller.set)
        self.scroller.configure(command=self.list.yview)

        self.window_view.mainloop()

    def attend_window(self):
        self.window_attend = tk.Tk()
        self.window_attend.geometry("400x200")
        self.window_attend.title("Check Attendance Of A User")
        
        self.window_attend.mainloop()