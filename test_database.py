from database import *
db = Database()
db.connect(ADMINUSER, ADMINPASS)

'''
HEADER:
This file is a test case document for database. Whenever a test case is added to this document, you MUST provide
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
    '''
        Preamble:
            test connecting to the DB

        Post:
            PASS as of 4/23/2023
        '''
    testdb = Database()
    testdb.connect(ADMINUSER,ADMINPASS)

def test_get_all_patients():
    '''
    Preamble:
        tests getting all patients

    Post:
        PASS as of 4/23/2023
    '''
    db.get_all_patients()

def test_get_columns():
    '''
        Preamble:
            gets all the columns in a table

        Post:
            PASS as of 4/23/2023
    '''
    db.get_columns('patient_medical')

def test_get_user_role():
    '''
        Preamble:
            tests catching the user role, outputs the role

        Post:
            PASS as of 4/23/2023
        '''
    db.get_user_role()
    print(db.role)

def test_execute():
    '''
        Preamble:
            executes a simple query

        Post:
            PASS as of 4/23/2023
        '''
    db.execute("SELECT * FROM patient_medical WHERE patientID = 3")

def test_search_patient_by_name():
    '''
        Preamble:
            tests a partial search of everyone named john

        Post:
            PASS as of 4/23/2023
        '''
    db.search_patient_by_name(None, 'john')

def test_select():
    '''
        Preamble:
            selects something from a table

        Post:
            PASS as of 4/23/2023
        '''
    db.select('*','patient_medical')

def test_select_all():
    '''
        Preamble:
            selects everything from a table

        Post:
            PASS as of 4/23/2023
        '''
    db.select_all('patient_medical')

def test_set_user_role():
    '''
        Preamble:
            tests changing the user role by setting the role

        Post:
            PASS as of 4/23/2023
        '''
    db.set_user_role('administrator')

#def test_close():
'''
    Preamble:
        closes the connection to the DB.
        COMMENTED OUT BECAUSE OF DESTRUCTIVE CONSEQUENSES TO REST OF FILE
    Post:
        PASS as of 4/23/2023
    '''
#    db.close()

def test_connect():
    '''
        Preamble:
            connects to the database

        Post:
            PASS as of 4/23/2023
        '''
    testdb = Database()
    testdb.connect(ADMINUSER,ADMINPASS)

def test_get_username_role_str():
    '''
        Preamble:
            gets the username role as a string

        Post:
            PASS as of 4/23/2023
        '''
    db.get_username_role_str()







