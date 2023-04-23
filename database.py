# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import pymysql.cursors
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
        else:
            patient.patientID = self.get_next_id()
        fields = ''
        values = ''

        # insert into patient_medical
        medical_data = patient.get_patient_medical_data()
        for key in list(medical_data.keys())[1:]:
            if medical_data[key]:
                fields += key + ', '
                values += literal(str(medical_data[key])) + ','

        # strip trailing commas
        fields = fields[:-2]
        values = values[:-1]

        query = "INSERT INTO patient_medical" + "(" + fields + ') VALUES (' + values + ');'
        print(query)
        self.execute(query)

        # insert into patient_accounting
        accounting_data = patient.get_patient_accounting_data()

        for key in list(accounting_data.keys())[1:]:
            query = "UPDATE patient_accounting" + " SET " + key + " = " + literal(accounting_data[key]) \
                    + " WHERE accountingID = " + patient.patientID + ";"
            self.execute(query)

    def commit_changes(self, override=True):
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

    def get_all_patients(self, output_results=False):
        # return list of patient objects
        patients_list = self.select_all(self.patient_table)
        patients = self._patients_query_to_objects(patients_list)
        if output_results:
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

        if self.role == 'administrator':
            self.patient_table = 'patient_medical'
        else:
            self.patient_table = "patient_" + self.role

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def dict_execute(self, query):
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(query)
        output = self.cursor.fetchall()
        self.cursor = self.connection.cursor(pymysql.cursors.Cursor)
        return output

    def save_patient_data(self, patient):
        print(patient.changes)
        medical_data = patient.get_patient_medical_data()
        for key in patient.changes:
            table_to_update = 'patient_medical' if key in medical_data else 'patient_accounting'
            query = "UPDATE " + table_to_update + " SET " + str(key) + " = " + literal(patient.data[key]) \
                    + " WHERE patientID = " + str(patient.patientID) + ";"
            print(query)
            try:
                self.execute(query)
                print("Change to field \'" + key + "\' successful. ")
            except Exception as e:
                print(e)
                #print("You are logged in as a " + self.role + ". You do not have access to field: " + key)

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
                firstname, lastname = literal(name.split(" ")[0] + '%'), literal(name.split(" ")[1] + '%')
            else:
                firstname, lastname = literal(name.split(" ")[0] + '%'), literal(name.split(" ")[0] + '%')
            query = self.patient_table + " WHERE firstname LIKE " + firstname + \
                    " OR lastname LIKE " + lastname
        elif firstname and lastname:
            firstname, lastname = literal(firstname + '%'), literal(lastname + '%')
            query = self.patient_table + " WHERE firstname LIKE " + firstname + \
                    " AND lastname LIKE " + lastname
        elif firstname and not lastname:
            firstname = literal(firstname + '%')
            query = self.patient_table + " WHERE firstname LIKE " + firstname
        elif lastname and not firstname:
            lastname = literal(lastname + '%')
            query = self.patient_table + " WHERE lastname LIKE " + lastname
        else:
            return self.get_all_patients()

        return self._patients_query_to_objects(self.select_all(query))

    def select(self, arg1, arg2):
        return self.execute("SELECT " + arg1 + " FROM " + arg2 + ";")  # execute query

    def select_all(self, arg1):
        query = "SELECT * FROM " + arg1 + ";"
        print(query)
        try:
            output = self.dict_execute(query)  # queries the table
            return output
        except pymysql.err.ProgrammingError:  # in case table doesnt exist
            print("Table Does not exist")
        except pymysql.err.OperationalError:
            print("Access denied")

    def set_user_role(self, role):
        self.role = role
        self.patient_table = 'patient_' + self.role

    def close(self):
        self.cursor.close()
        self.connection.close()

    def get_username_role_str(self):
        role = self.execute("SELECT CURRENT_ROLE();")
        role = role[0][0].split("@")[0]
        username = self.execute('SELECT CURRENT_USER();')
        username_role_str = username[0][0].split("@")[0] + '\n'
        if role == "`volunteer`":
            username_role_str += "Volunteer"
        elif role == "`office`":
            username_role_str += "Office Staff"
        elif role == "`nurse`":
            username_role_str += "Nurse"
        elif role == "`doctor`":
            username_role_str += "Doctor"
        else:
            username_role_str += "Error Retrieving Role"
        return username_role_str

    # PRIVATE METHODS
    def _patients_query_to_objects(self, patients_list):
        output = []
        for data in patients_list:
            new_patient = Patient(patientID=data['patientID'], data=data)
            output.append(new_patient)
        return output


# user = input("enter username:")
# passw = input("enter password:")
# db = Database()
# db.connect(user, passw)
# test = db.dict_execute("SELECT * FROM patient_medical")
# for i in test:
#     print(i['firstname'])
# db.select('*', 'Accounts')
# db.select_all('Accounts')


"""EXAMPLE CODE FOR DATABASE CHANGES"""
db = Database()
db.connect(ADMINUSER, ADMINPASS)
db.set_user_role('administrator')

patient = Patient(firstname='Julia', lastname='Duff', sex='F')
patient.randomize_all_missing_data()
db.add_patient(patient)
db.commit_changes(override=False)

# returns all patients with firstname beginning with Jo
db.search_patient_by_name(firstname='Jo')

# returns all patients with lastname beginning with Doe
db.search_patient_by_name(firstname='Doe')

# returns all patients with initials J. D.
db.search_patient_by_name(firstname='J', lastname='D')

# returns all patient with first initial J. OR last initial D.
db.search_patient_by_name(name='J D')





