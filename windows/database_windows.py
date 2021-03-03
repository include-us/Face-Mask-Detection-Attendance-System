import tkinter as tk
from tkinter import messagebox


class database_methods(object):
    def add_window(self):
        self.window_add = tk.Tk()
        self.window_add.geometry("400x200")

        self.window_add.mainloop()

    def delete_window(self):
        self.window_delete = tk.Tk()
        self.window_delete.geometry("400x200")
        
        self.window_delete.mainloop()

    def view_window(self):
        self.window_view = tk.Tk()
        self.window_view.geometry("400x200")

        self.window_view.mainloop()

    def attend_window(self):
        self.window_attend = tk.Tk()
        self.window_attend.geometry("400x200")

        self.window_attend.mainloop()
