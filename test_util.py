from util import *

'''
HEADER:
This file is a test case document for utils. Whenever a test case is added to this document, you MUST provide
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


def test_create_id():
    '''
    Preamble:
        This tests that the id creation function produces the expected string. Expected to PASS, no output

    Post:
        PASS as of 4/14/2023
    '''
    assert create_patient_id(1111) == "00001111"


def test_literal():
    '''
    Preamble:
        This tests that the literal converter function produces the expected string. Expected to PASS, no output

    Post:
        PASS as of 4/14/2023
    '''
    assert literal("test") == "\'" + "test" + "\'"

