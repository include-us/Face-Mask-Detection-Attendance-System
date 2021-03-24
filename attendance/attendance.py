import csv
import datetime
from os import name
from barcode.barcode import barcode_read as read_code
from admin_database import database as db
import pandas as pd


class attendance(object):
    def __init__(self):
        # self.con = db.connect('databases//users_info.db')
        # self.curr = self.con.cursor()
        self.file = open("attendance/data.csv")

    def mark(self):
        self.code=read_code().reader()
        print("MARKING")
        df = pd.read_csv("attendance/data.csv")
        if datetime.datetime.now().strftime("%x") in df.columns:
            pass
        else:
            x = datetime.datetime.now()
            df[x.strftime("%x")] = "absent"
            df.to_csv("attendance/data.csv", index=False)
        for codefind in df.barcode:
            if str(codefind)==self.code:
                df.loc[int(self.code)-1,datetime.datetime.now().strftime("%x")]="present"
                df.to_csv("attendance/data.csv", index=False)
                break

    def show(self):
        print("SHOWN")


