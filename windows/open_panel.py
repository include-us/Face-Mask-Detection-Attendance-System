import tkinter as tk
from tkinter import messagebox
from windows.admin_login import administrator


class opening_panel(object):
    def administrator(self):
        object1 = administrator()
        object1.admin_panel()

    def activate(self):
        print("ACTIVATED")

    def open_panel(self):
        self.window = tk.Tk()
        self.window.geometry("400x100")
        self.window.title("Face Mask Detection And Attendance System")
        self.btn_admin = tk.Button(
            self.window,
            text="Administrator",
            width=50,
            height=1,
            command=self.administrator
        )
        self.btn_activate = tk.Button(
            self.window,
            text="Activate System",
            width=50,
            height=1,
            command=self.activate
        )
        self.btn_admin.grid(row=1, column=1)
        self.btn_activate.grid(row=2, column=1)
        self.window.mainloop()
