# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
from consts import *


class Database:
    def __init__(self):
        connection = pymysql.connect(host=HOST, user=USER, port=PORT,
                                     passwd=PASSWORD, db=DATABASE)
        self.cursor = connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        output = self.cursor.fetchall()
        print(format(output))
        return output

    def select(self, arg1, arg2):
        self.cursor.execute("SELECT " + arg1 + " FROM " + arg2 + ";")  # execute query
        output = self.cursor.fetchall()  # puts output into a string
        print(format(output))  # prints output to console
        return output

    def select_all(self, arg1):
        self.cursor.execute("SELECT * FROM " + arg1 + ";")  # queries the doctors table
        output = self.cursor.fetchall()  # puts output into a string
        print(format(output))  # prints output to console
        return output


poggers = Database()
poggers.execute("SELECT * from doctors")
poggers.select('*', 'doctors')
poggers.select_all('doctors')

