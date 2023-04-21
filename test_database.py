from database import *
db = Database()
db.connect(ADMINUSER, ADMINPASS)

'''
HEADER:
This file is a test case document for report_exporter. Whenever a test case is added to this document, you MUST provide
 a sufficient description of the case you are trying to assess.

USEFUL INFO:
For Pycharm to recognize your function as a test case, it MUST start with the prefix "test_", as shown below.
Simply run the file and let Pycharm handle the rest! Make sure to check the console once testing is complete!

PROPER TESTING FORMAT:

    def function():
        preamble:
        here you will define what the test function is supposed to be testing, and what it's expected output is, as well
        as any other useful information regarding the function

        post:
        here you will define a list of testing history and results. nothing super detailed needs to be here, if output is
        wrong or an error, describe the issue briefly. if the expected output is achieved, note it.
        do not include unexpected output or errors not directly tied to the tested functions.
'''


def test_dict_execute():
    '''
    Preamble:
        This tests that the DB is returning a dictionary when asked to return one. it also tests to see if it goes back
        to returning tuples when doing normal operations. expected output is a dict, then a tuple.

    Post:
        PASS as of 4/13/2023
    '''
    print("")
    test = db.dict_execute("SELECT * FROM patient_medical")
    for i in test:
        print(type(i))
    test = db.execute("SELECT * FROM patient_medical")
    for i in test:
        print(type(i))


def test_connect():
    testdb = Database()
    testdb.connect(ADMINUSER,ADMINPASS)

def test_get_all_patients():
    db.get_all_patients()

def test_get_columns():
    db.get_columns('patient_medical')

def test_get_user_role():
    db.get_user_role()

def test_execute():
    db.execute("SELECT * FROM patient_medical WHERE patientID = 3")





