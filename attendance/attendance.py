import csv
import datetime
# from ..barcode.barcode import barcode_read as read_code
# from ..admin_database import database as db
import pandas as pd


class attendance(object):
    def __init__(self):
        # self.con = db.connect('databases//users_info.db')
        # self.curr = self.con.cursor()
        self.file = open("attendance/data.csv")

    def mark(self):
        # self.code=read_code.reader()
        print("MARKING")
        df = pd.read_csv("attendance/data.csv")
        if datetime.date in df.columns:
            pass
        else:
            x = datetime.datetime.now()
            df[x.strftime("%x")] = ""
            df.to_csv("attendance/data.csv", index=False)

    def show(self):
        print("SHOWN")


attendance().mark()
