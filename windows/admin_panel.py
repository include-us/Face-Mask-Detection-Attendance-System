import tkinter as tk
from tkinter import Entry, messagebox

class admin_panel(object):
    def admin(self):
        self.admin_window = tk.Tk()
        self.admin_window.geometry("400x200")
        self.btn_add=tk.Button(
            self.admin_window,
            text="Add Student",
            height=1,
            width=40,
        )
        self.btn_view=tk.Button(
            self.admin_window,
            text="View Students",
            height=1,
            width=40,
        )
        self.btn_delete=tk.Button(
            self.admin_window,
            text="Delete A Student",
            width=40,
            height=1,
        )
        self.btn_attendance=tk.Button(
            self.admin_window,
            text="View Attendance",
            width=40,
            height=1,
        )
        self.btn_add.grid(row=1,column=0)
        self.btn_delete.grid(row=2,column=0)
        self.btn_view.grid(row=3,column=0)
        self.btn_attendance.grid(row=4,column=0)
        self.admin_window.mainloop()