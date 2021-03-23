import csv
from ..admin_database import database as db
from ..barcode.barcode import barcode_read as read_code

class attendance(object):
    def __init__(self):
        self.con = db.connect('databases//users_info.db')
        self.curr = self.con.cursor()
    def mark(self):
        print("MARKED")
    def show(self):
        print("SHOWN")