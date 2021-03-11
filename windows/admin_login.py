import tkinter as tk
from tkinter import Entry, messagebox
from windows.admin_panel import admin_panel
# ---------------ADMIN CREDENTIALS----------------
global admin_password
global admin_username
admin_username = "admin"
admin_password = "admin"


class administrator:
	def check(self):
		entered_password = self.entry_password.get()
		entered_username = self.entry_username.get()
		if entered_password == admin_password and admin_username == entered_username:
			messagebox.showinfo("SUCCESS", "LOGGING IN SUCCESSFUL")
			self.window.destroy()
			object2 = admin_panel()
			object2.admin()
		else:
			messagebox.showerror("ERROR", "CHECK CREDENTIALS")

	def admin_panel(self):
		self.window = tk.Tk()
		self.window.geometry("400x100")
		self.window.title("Administrator Panel")
		self.lbl_username = tk.Label(
			self.window,
			text="Enter Username: ",
			width=20,
			height=1
		)
		self.lbl_password = tk.Label(
			self.window,
			text="Enter Password: ",
			width=20,
			height=1
		)
		self.btn_login = tk.Button(
			self.window,
			text="LOGIN",
			width=40,
			height=1,
			command=self.check,
		)
		self.entry_username = tk.Entry(
			self.window,
			text="",
			width=20,
		)
		self.entry_password = tk.Entry(
			self.window,
			text="",
			width=20,
		)
		self.lbl_username.grid(row=1, column=0)
		self.lbl_password.grid(row=2, column=0)
		self.entry_username.grid(row=1, column=1)
		self.entry_password.grid(row=2, column=1)
		self.btn_login.grid(row=3, columnspan=2, column=0)
		self.window.mainloop()
