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
        self.admin_window.configure(background="turquoise")  # background color
        self.admin_window.geometry("370x400")
        self.admin_window.title("Database")
        lab20 = tk.Label(self.admin_window, text="", bg="turquoise",
                         fg="dark slate gray", font=("times", 15, 'bold'))
        lab21 = tk.Label(self.admin_window, text="Select an option", bg="turquoise",
                         fg="dark slate gray", font=("Simplified Arabic fixed", 15, 'bold'))
        lab22 = tk.Label(self.admin_window, text="", bg="turquoise",
                         fg="dark slate gray", font=("times", 20, 'bold'))
        self.btn_add = tk.Button(
            self.admin_window,
            text="Add Student",
            font=("times", 10, 'bold'),
            height=4,
            width=50,
            bg="old lace",
            command=self.add,
        )
        self.btn_view = tk.Button(
            self.admin_window,
            text="View Students",
            font=("times", 10, 'bold'),
            height=4,
            width=50,
            bg="old lace",
            command=self.view,
        )
        self.btn_delete = tk.Button(
            self.admin_window,
            text="Delete A Student",
            bg="old lace",
            font=("times", 10, 'bold'),
            width=50,
            height=4,
            command=self.delete,
        )
        self.btn_attendance = tk.Button(
            self.admin_window,
            text="View Attendance",
            bg="old lace",
            font=("times", 10, 'bold'),
            width=50,
            height=4,
            command=self.attendance,
        )
        lab20.grid(row=1, column=0)
        lab21.grid(row=2, columnspan=2, column=0)
        lab22.grid(row=3, column=0)
        self.btn_add.grid(row=5, column=1)
        self.btn_delete.grid(row=6, column=1)
        self.btn_view.grid(row=7, column=1)
        self.btn_attendance.grid(row=8, column=1)
        self.admin_window.mainloop()
