# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import cryptography
from consts import *
from patient import Patient
from util import create_patient_id, literal


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.role = None
        self.patient_table = None

    # PUBLIC METHODS
    def add_patient(self, patient=None):
        # if left blank, random patient will be generated
        if not patient:
            patient = self.create_random_patient()
        fields = ''
        values = ''
        for key in list(patient.data.keys())[1:]:
            if patient.data[key]:
                fields += key + ', '
                values += literal(str(patient.data[key])) + ','

        # strip trailing commas
        fields = fields[:-2]
        values = values[:-1]
        query = "INSERT INTO " + self.patient_table + "(" + fields + ') VALUES (' + values + ');'
        self.cursor.execute(query)

    def commit_changes(self, override=False):
        if override:
            self.connection.commit()
        else:
            verification = input("Are you sure you would like to commit changes to database? (y/n) ")
            if verification.lower() == 'y':
                print("Changes committed. ")
                self.connection.commit()
            else:
                print("Changes discarded. ")

    def connect(self, USER, PASSWORD):
        self.connection = pymysql.connect(host=HOST, user=USER, port=PORT,
                                          passwd=PASSWORD, db=DATABASE)
        self.cursor = self.connection.cursor()
        self.get_user_role()



    def create_random_patient(self):
        # any Patient object with no input parameters will be filled with random data
        while True:
            patient = Patient(self.get_next_id())
            print(patient)
            user_input = input("Try again? (y/n) ")
            if user_input.lower() == 'n':
                return patient

    def get_next_id(self):
        # TODO: query database for largest patientID
        output = self.select('patientID', self.patient_table)
        patientIDs = [int(item[0]) for item in output]
        return create_patient_id(max(patientIDs) + 1)

    def get_all_patients(self):
        # return list of patient objects
        raw_output = self.select_all(self.patient_table)
        patients = self._patients_query_to_objects(raw_output)
        for p in patients:
            print(p)
            print()
        return patients

    def get_columns(self, table):
        return self.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='" + table + "'")

    def get_user_role(self):
        role = self.execute("SELECT CURRENT_ROLE();")
        role = role[0][0]
        role = role.split("@")
        role = role[0].replace("`", "")
        self.role = role
        self.patient_table = "patient_"+self.role

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def save_patient_data(self, patient):
        # TODO: keep track of values that have been changed and only update those
        for key in patient.changes:
            query = "UPDATE " + self.patient_table + " SET " + key + " = " + literal(patient.data[key]) \
                         + " WHERE patientID = " + patient.patientID + ";"
            print(query)
            self.execute(query)

    def search_patient_by_name(self, name=None, firstname=None, lastname=None):
        """example use:
            input: name="John Doe" or firstname="John", lastname="Doe" -> returns all patients named John Doe
            input: name="John" -> returns all patients with firstname or lastname "John"
            input: firstname="John" -> returns all patients with firstname John
            input: lastname="Doe" -> returns all patients with lastname Doe
            input: firstname="John",
            input: None -> returns all patients
        """
        if name:
            name_split = name.split(" ")
            if len(name_split) == 2:
                firstname, lastname = literal(name.split(" ")[0]), literal(name.split(" ")[1])
            else:
                firstname, lastname = literal(name.split(" ")[0]), literal(name.split(" ")[0])
            query = self.patient_table + " WHERE firstname = " + firstname + \
                    " OR lastname = " + lastname + ";"
        elif firstname and lastname:
            query = self.patient_table + " WHERE firstname = " + firstname + \
                    " AND lastname = " + lastname + ";"
        elif firstname and not lastname:
            firstname = literal(firstname)
            query = self.patient_table + " WHERE firstname = " + firstname + ";"
        elif lastname and not firstname:
            lastname = literal(lastname)
            query = self.patient_table + " WHERE lastname = " + lastname + ";"
        else:
            return self.get_all_patients()

        return self._patients_query_to_objects(self.select_all(query))

    def select(self, arg1, arg2):
        return self.execute("SELECT " + arg1 + " FROM " + arg2 + ";")  # execute query

    def select_all(self, arg1):
        try:
            output = self.execute("SELECT * FROM " + arg1 + ";")  # queries the table
        except pymysql.err.ProgrammingError:  # in case table doesnt exist
            output = "Table Does not exist"
        except pymysql.err.OperationalError:
            output = "Access denied"
        print(format(output))  # prints output to console
        return output

    def close(self):
        self.cursor.close()
        self.connection.close()

    # PRIVATE METHODS
    def _patients_query_to_objects(self, raw_output):
        patients_list = [[item for item in raw_output[i]] for i in range(0, len(raw_output))]
        raw_fields = self.get_columns(self.patient_table)
        fields = [item[0] for item in raw_fields]

        output = []
        for p in patients_list:
            data = {}
            for i in range(0, len(p)):
                key = fields[i].replace('(', '').replace(')', '').replace(',', '')
                data[key] = p[i]
            new_patient = Patient(patientID=p[0], data=data)
            output.append(new_patient)
        return output


# user = input("enter username:")
# passw = input("enter password:")
# db = Database()
# db.connect(user, passw)
# db.search_patient_by_name("john doe")
# db.select('*', 'Accounts')
# db.select_all('Accounts')


# """EXAMPLE CODE FOR DATABASE CHANGES"""
# user = 'root'
# passw = 'AdminPass'
# poggers = Database()
# poggers.connect(user, passw)
#
# # CREATE RANDOM PATIENT example
# # when no input is given, random patients are automatically generated until one is approved
# poggers.add_patient()
#
# # CREATE and EDIT RANDOM PATIENT example
# # random patients are auto generated until one is approved
# random_patient = poggers.create_random_patient()
# random_patient.set_age('70')
# random_patient.set_weight('150 lbs')
# poggers.add_patient(random_patient)  # patient will be added to database with changes
#
# # SEARCH and EDIT EXISTING PATIENT example
# patients_list = poggers.search_patient_by_name(lastname="Nagel")  # get all patients with lastname Nagel
# patient = patients_list[0]  # get first patient in list (in this case there is only one)
# patient.set_doctor_notes("Example Doctor Notes")
# print(patient.changes)
# print(patient)
# poggers.save_patient_data(patient)  # save changes to database
# poggers.commit_changes()
#
# # get patient data
# print(patient.patientID)
# print(patient.emergency_contacts)
#
# # see list of all patients
# poggers.get_all_patients()
#
# # more search by name examples
# poggers.search_patient_by_name(firstname="John")
# poggers.search_patient_by_name(firstname="John", lastname="Doe")
# poggers.search_patient_by_name(name="John Doe")
# poggers.search_patient_by_name()  # same as get_all_patients()
