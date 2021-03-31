import tkinter as tk
from tkinter import messagebox
from windows.admin_login import administrator
from facemask.facemask import mask


class opening_panel(object):
    def administrator(self):
        object1 = administrator()
        object1.admin_panel()

    def activate(self):
        print("ACTIVATED")
        mask().detect_mask()

    def open_panel(self):
        self.window = tk.Tk()
        self.window.configure(background="turquoise")  # background color
        self.window.geometry("700x533")
        self.window.title("Face Mask Detection And Attendance System")
        # labels added
        lab5 = tk.Label(self.window, text="", bg="turquoise",
                        fg="dark slate gray", font=("times", 36, 'bold'))
        lab1 = tk.Label(self.window, text="Face Mask Detection",
                        bg="turquoise", fg="dark slate gray", font=("times", 36, 'bold'))
        lab2 = tk.Label(self.window, text="&", bg="turquoise",
                        fg="dark slate gray", font=("times", 36, 'bold'))
        lab3 = tk.Label(self.window, text="Attendance System", bg="turquoise",
                        fg="dark slate gray", font=("times", 36, 'bold'))
        lab4 = tk.Label(self.window, text="", bg="turquoise",
                        fg="dark slate gray", font=("times", 36, 'bold'))
        self.btn_admin = tk.Button(
            self.window,
            text="Administrator",
            font=("simplified arabic fixed", 15, 'bold'),  # font
            width=60,
            height=4, bg="old lace",  # bg color
            command=self.administrator
        )
        self.btn_activate = tk.Button(
            self.window,
            text="Activate System",
            font=("simplified arabic fixed", 15, 'bold'),  # fonts
            width=60,
            height=4, bg="old lace",  # bg col
            command=self.activate
        )
        lab5.grid(row=1, column=2)
        lab1.grid(row=2, column=2)
        lab2.grid(row=3, column=2)
        lab3.grid(row=4, column=2)
        lab4.grid(row=5, column=2)
        self.btn_admin.grid(row=7, column=2)
        self.btn_activate.grid(row=8, column=2)
        self.window.mainloop()
