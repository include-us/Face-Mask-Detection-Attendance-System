import tkinter as tk
from tkinter import Entry, messagebox
from windows.database_windows import database_methods


class admin_panel(object):
    def delete(self):
        self.handle.delete_window()

    def add(self):
        self.handle.add_window()

    def view(self):
        self.handle.view_window()

    def attendance(self):
        self.handle.attend_window()

    def admin(self):
        self.handle = database_methods()
        self.admin_window = tk.Tk()
        self.admin_window.geometry("400x200")
        self.admin_window.title("Database")
        self.btn_add = tk.Button(
            self.admin_window,
            text="Add Student",
            height=1,
            width=40,
            command=self.add,
        )
        self.btn_view = tk.Button(
            self.admin_window,
            text="View Students",
            height=1,
            width=40,
            command=self.view,
        )
        self.btn_delete = tk.Button(
            self.admin_window,
            text="Delete A Student",
            width=40,
            height=1,
            command=self.delete,
        )
        self.btn_attendance = tk.Button(
            self.admin_window,
            text="View Attendance",
            width=40,
            height=1,
            command=self.attendance,
        )
        self.btn_add.grid(row=1, column=0)
        self.btn_delete.grid(row=2, column=0)
        self.btn_view.grid(row=3, column=0)
        self.btn_attendance.grid(row=4, column=0)
        self.admin_window.mainloop()
