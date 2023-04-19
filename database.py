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
        try:
            self.cursor.execute(query)
            output = self.cursor.fetchall()
        except pymysql.err.ProgrammingError:
            output = "Programming bug found"
        except pymysql.err.OperationalError:
            output = "Operational error thrown"
        print(format(output))
        return output

    def commitChanges(self):
        self.connection.commit()

    def select(self, arg1, arg2):
        try:
            self.cursor.execute("SELECT " + arg1 + " FROM " + arg2 + ";")  # execute query
            output = self.cursor.fetchall()  # puts output into a string
        except pymysql.err.ProgrammingError:
            output = "Programming bug found"
        except pymysql.err.OperationalError:
            output = "Operational error thrown"

        print(format(output))  # prints output to console
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

user = input("enter username:")
passw = input("enter password:")
poggers = Database(user, passw)
#poggers.execute("ALTER TABLE Accounts ALTER COLUMN Password SET INVISIBLE;")
#poggers.select('*', 'Accounts')
poggers.select_all('Accounts')

