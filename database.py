# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import cryptography
from consts import *
from patient import Patient


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
            self.cursor.execute("SELECT * FROM " + arg1 + ";")  # queries the table
            output = self.cursor.fetchall()  # puts output into a string
        except pymysql.err.ProgrammingError: #in case table doesnt exist
            output = "Table Does not exist"
        except pymysql.err.OperationalError:
            output = "Access denied"
        print(format(output))  # prints output to console
        return output

    def create_random_patient(self, patientID):
        # any Patient object with no input parameters will be filled with random data
        return Patient(self.get_next_id())

    def insert_patient(self, patient):
        fields = ''
        values = ''
        for key in patient.data.keys():
            if patient.data[key]:
                fields += key + ', '
                values += '\'' + str(patient.data[key]) + '\','

        # strip trailing commas
        fields = fields[:-2]
        values = values[:-1]
        query = "INSERT INTO patient_medical (" + fields + ') VALUES (' + values + ');'
        print(query)
        self.cursor.execute(query)

    def get_next_id(self):
        # TODO: query database for largest patientID
        return '00000001'

    def see_columns(self, table):
        self.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='" + table + "'")

user = 'root'
passw = 'AdminPass'
poggers = Database(user, passw)
#poggers.execute("ALTER TABLE Accounts ALTER COLUMN Password SET INVISIBLE;")
#poggers.select('*', 'Accounts')
poggers.select_all('patient_medical')


