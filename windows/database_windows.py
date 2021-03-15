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

	def delete_command(self):
		try:
			id = int(self.entry_id.get())
			handle = db()
			handle.delete_user(id)
		except:
			messagebox.showerror("Error", "COULDNT DELETE USER")
	# --------------------------Windows----------------------------

	def add_window(self):
		self.window_add = tk.Tk()
		self.window_add.geometry("300x300")
		self.window_add.title("Add A User")

		self.window_add.mainloop()

	def delete_window(self):
		self.window_delete = tk.Tk()
		self.window_delete.geometry("400x250")
		self.window_delete.configure(background="turquoise")
		self.window_delete.title("Delete A User")
		lab01 = tk.Label(self.window_delete,text="",bg="turquoise", fg="dark slate gray",font = ("times" , 15, 'bold'))
		lab02 = tk.Label(self.window_delete,text="Delete a user",bg="turquoise", fg="dark slate gray",font = ("simplified arabic fixed" , 15, 'bold'))
		lab03 = tk.Label(self.window_delete,text="",bg="turquoise", fg="dark slate gray",font = ("times" , 15, 'bold'))
		lab04 = tk.Label(self.window_delete,text="",bg="turquoise", fg="dark slate gray",font = ("times" , 15, 'bold'))
		self.lbl_id = tk.Label(
			self.window_delete,
			text="Enter ID to be Deleted: ",
			font=("times",10,'bold'),
			bg="turquoise", fg="Black",
			height=2,
			width=20,
		)
		self.entry_id = tk.Entry(
			self.window_delete,
			width=30,
		)
		self.btn_delete = tk.Button(
			self.window_delete,
			text="DELETE",
			font=("times",10,'bold'),
			bg="old lace",
			height=2,
			width=25,
			command=self.delete_command,
		)
		lab01.grid(row=1,column=1)
		lab02.grid(row=2,columnspan=2,column=1)
		lab03.grid(row=3,column=1)
		self.lbl_id.grid(row=5, column=1)
		self.entry_id.grid(row=5, column=2)
		lab04.grid(row=6,column=1)
		self.btn_delete.grid(row=7, column=2, columnspan=2)
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
