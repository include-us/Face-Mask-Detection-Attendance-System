import csv
import datetime
from os import name
from barcode.barcode import barcode_read as read_code
from admin_database import database
import pandas as pd
import sqlite3 as db


class attendance(object):

    def __init__(self):
        self.file = open("attendance/data.csv")
        self.con = db.connect('databases//users_info.db')
        self.curr = self.con.cursor()

    def mark(self):
        found = 0
        self.code = read_code().reader()
        print("MARKING")
        df = pd.read_csv("attendance/data.csv")
        if datetime.datetime.now().strftime("%x") in df.columns:
            pass
        else:
            x = datetime.datetime.now()
            df[x.strftime("%x")] = "absent"
            df.to_csv("attendance/data.csv", index=False)
        for codefind in df.barcode:
            if str(codefind) == self.code:
                df.loc[int(self.code)-1,
                       datetime.datetime.now().strftime("%x")] = "present"
                df.to_csv("attendance/data.csv", index=False)
                found = 1
                break
        if not found:
            print("NOT FOUND")

            self.curr.execute(
                "SELECT * FROM USERS where id=" + (str(self.code)))
            rows = self.curr.fetchall()
            print(rows[0][0])
            if int(rows[0][0]) == int(self.code):
                # print(len(df))
                df.loc[len(df), "barcode"] = self.code
                df.loc[len(df)-1, "name"] = rows[0][1]
                df["barcode"] = df["barcode"].astype(int)
                df.to_csv("attendance/data.csv", index=False)

    def show(self):
        print("SHOWN")
