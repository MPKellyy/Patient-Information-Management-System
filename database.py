# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
class Database:

    def __int__(self, host):
        self.host = host                                    # DO NOT COMMIT THIS LINK TO THE REPO OR ANYONE WHO GRABS IT
                                                            # CAN MESS WITH DATA IN THE DB
                                                            # will look into a more permanent solution.
        port = 3306
        user = 'admin'
        password = 'AdminPass'
        database = "patient_information"

        self.connection = pymysql.connect(host=host, user=user, port=port, passwd=password, db=database)

    def select(self):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM doctors;")  # queries the doctors table
            output = cur.fetchone()                # puts output into a string
            print(format(output))                  # prints output to console


def main():
    poggers = Database("patient-info.c7dbj8qezzsr.us-east-2.rds.amazonaws.com")
    poggers.select()
