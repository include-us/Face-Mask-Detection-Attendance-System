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
		self.window.geometry("550x350")
		self.window.title("Admin Login")
		self.window.configure(background="turquoise") #background color
		#lab14 = tk.Label(self.window,text="FACE MASK DETECTION & ATTENDANCE SYSTEM",bg="turquoise", fg="dark slate gray",font = ("Simplified Arabic fixed" ,10, 'bold'))
		lab10 = tk.Label(self.window,text="",bg="turquoise",fg="dark slate gray",font=("times",30,'bold'))
		lab11 = tk.Label(self.window,text="Sign in",bg="turquoise", fg="dark slate gray",font = ("Simplified Arabic fixed" , 20, 'bold'))
		lab12 = tk.Label(self.window,text="",bg="turquoise",fg="dark slate gray",font=("Simplified arabic fixed",20,'bold'))
		lab13 = tk.Label(self.window,text="",bg="turquoise",fg="dark slate gray",font=("times",20,'bold'))
		self.lbl_username = tk.Label(
			self.window,
			text="Enter Username: ",
			font=("Simplified Arabic fixed",10,'bold'),
			width=20,
			bg="turquoise",fg="Black",
			height=2 
		)
		self.lbl_password = tk.Label(
			self.window,
			text="Enter Password: ",
			font=("Simplified Arabic fixed",10,'bold'),
			width=20,
			bg="turquoise",fg="Black",
			height=2
		)
		self.btn_login = tk.Button(
			self.window,
			text="LOGIN",
			font=("times",10,'bold'),
			width=42,
			height=3,
			bg="old lace",
			command=self.check,
		)
		self.entry_username = tk.Entry(
			self.window,
			text="",
			bg="old lace",
			width=50,
			#height=2
		)
		self.entry_password = tk.Entry(
			self.window,
			bg="old lace",
			text="",
			width=50,
			#height=2
		)
		#lab14.grid(row=1,column=0)
		lab10.grid(row=2,column=0)
		lab11.grid(row=3,columnspan=2,column=0)
		lab12.grid(row=4,column=0)
		self.lbl_username.grid(row=6, column=0)
		self.lbl_password.grid(row=7, column=0)
		self.entry_username.grid(row=6, column=1)
		self.entry_password.grid(row=7, column=1)
		lab13.grid(row=8,column=0)
		self.btn_login.grid(row=10,columnspan=2,column=1)
		self.window.mainloop()
