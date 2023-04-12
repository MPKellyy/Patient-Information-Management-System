from database import *

db = Database()

'''
HEADER:
this file is the test case document for this project. here i will define standard procedure as well as 
provide an example for us to follow. I will personally try to handle maintaining proper documentation as well
as actual implementation of testing functions.

USEFUL INFO:
database object is defined as 'db'

PROPER TESTING FORMAT:

    def function():
        preamble:
        here you will define what the test function is supposed to be testing, and what it's expected output is, as well
        as any other useful information regarding the function
        
        post:
        here you will define a list of testing history and results. nothing super detailed needs to be here, if output is
        wrong or an error, describe the issue briefly. if the expected output is achieved, note it.
        do not include unexpected output or errors not directly tied to the tested functions.
        
        function here
        
ITS UGLY AND I HATE IT BUT PYTHON YELLS AT ME OTHERWISE AAAAAAAAAAAAAAAAAAAAAAAA
'''




def dict_execute_test():
    '''
    preamble:
    this tests that the DB is returning a dictionary when asked to return one. it also tests to see if it goes back to
    returning tuples when doing normal operations.
    expected output is a dict, then a tuple.

    post:
    the results of the test were correct and accurate.
    '''
    test = db.dict_execute("SELECT * FROM patient_medical")
    for i in test:
        print(type(i))
    test = db.execute("SELECT * FROM patient_medical")
    for i in test:
        print(type(i))


db.connect(ADMINUSER, ADMINPASS)
dict_execute_test()
