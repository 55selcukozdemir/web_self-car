import sqlite3 as sql

from torch import row_stack

class Sql:
    def __init__(self) -> None:
        with sql.connect("parameters.db") as database:
            cursor =  database.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS valuu(id INTEGER PRIMARY KEY, lower_h INTEGER, lower_s INTEGER, lower_v INTEGER, upper_h INTEGER, upper_s INTEGER, upper_v INTEGER)")


    def hsv_valuses(self,
                    lower_h,
                    lower_s,
                    lower_v,
                    upper_h,
                    upper_s,
                    upper_v):
        with sql.connect("parameters.db") as database:    
            cursor =  database.cursor()
            cursor.execute("INSERT INTO valuu(lower_h, lower_s, lower_v, upper_h, upper_s, upper_v) VALUES (?,?,?,?,?,?)", (lower_h,lower_s,lower_v,upper_h,upper_s,upper_v))
            database.commit()

    def getHsvValues(self):
        with sql.connect("parameters.db") as database:
            database.row_factory = sql.Row
            cursor = database.cursor()
            cursor.execute("SELECT * FROM valuu")
            rows = cursor.fetchall()
            return rows

    def updateHsv(self,
                    lower_h,
                    lower_s,
                    lower_v,
                    upper_h,
                    upper_s,
                    upper_v):
        with sql.connect("parameters.db") as database:    
            cursor =  database.cursor()
            cursor.execute("UPDATE valuu SET lower_h = ?, lower_s  = ? , lower_v  = ?, upper_h  = ?, upper_s  = ?, upper_v  = ? WHERE id = 1", (lower_h,lower_s,lower_v,upper_h,upper_s,upper_v))
            database.commit()
            cursor.close()