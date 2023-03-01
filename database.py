# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql

host = "please consult the discord for this link"   # DO NOT COMMIT THIS LINK TO THE REPO OR ANYONE WHO GRABS IT
                                                    # CAN MESS WITH DATA IN THE DB
                                                    # will look into a more permanent solution
port = 3306
user = 'admin'
password = 'AdminPass'
database = "patient_information"

connection = pymysql.connect(host=host, user=user, port=port, passwd=password, db=database)
with connection:
    cur = connection.cursor()
    cur.execute("SELECT * FROM doctors;")  # queries the doctors table
    output = cur.fetchone()                # puts output into a string
    print(format(output))                  # prints output to console

    # this code just created and inserted some data into the database, do not rerun this code
    #
    # cur.execute("CREATE TABLE doctors (name VARCHAR(255), position VARCHAR(255), "
    #            "username VARCHAR(255), password VARCHAR(255));")
    # cur.execute("INSERT INTO doctors (name, position, username, password) "
    #            "VALUES ('McNicholas' ,'surgeon', 'McN007', 'adim')")
    # connection.commit()
