# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import cryptography
from consts import *


class Database:
    def __init__(self, USER, PASSWORD):
        self.connection = pymysql.connect(host=HOST, user=USER, port=PORT,
                                     passwd=PASSWORD, db=DATABASE)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        output = self.cursor.fetchall()
        # print(format(output))
        return output

    def commitChanges(self):
        self.connection.commit()

    def select(self, arg1, arg2):
        self.cursor.execute("SELECT " + arg1 + " FROM " + arg2 + ";")  # execute query
        output = self.cursor.fetchall()  # puts output into a string
        # print(format(output))  # prints output to console
        return output

    def select_all(self, arg1):
        try:
            self.cursor.execute("SELECT * FROM " + arg1 + ";")  # queries the doctors table
            output = self.cursor.fetchall()  # puts output into a string
        except pymysql.err.ProgrammingError: #in case table doesnt exist
            output = "Table Does not exist"
        except pymysql.err.OperationalError:
            output = "Access denied"
        print(format(output))  # prints output to console
        return output

    def close(self):
        self.cursor.close()
        self.connection.close()

# user = input("enter username:")
# passw = input("enter password:")
# db = Database(user, passw)
# db.execute("ALTER TABLE Accounts ALTER COLUMN Password SET INVISIBLE;")
# db.select('*', 'Accounts')
# db.select_all('Accounts')