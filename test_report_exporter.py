from report_exporter import *
from database_tools import *

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


def _report(username, password, role, num_patients=1):
    """
        Preamble:
            Helper function that generates report for each test case wrapping it

            Inputs: username of test account, password of test account, role of account, number of patients to report on
        Post:
            PASS as of 4/23/2023
    """
    print("")

    # Handling user mis-input
    username = str(username)
    password = str(password)
    role = str(role)

    if not isinstance(num_patients, int):
        num_patients = 1

    # Ensuring no duplicate account exists
    reset(username)

    # Establishing connection to database based on role
    create_account(username, password, role)
    test_db = Database()
    test_db.connect(username, password)

    # Generating report
    generate_report(generate_test_patients(num_patients), test_db.execute("SELECT CURRENT_ROLE();"))

    delete_account(username)


def test_report_invalid_role():
    """
    Preamble:
        Test case for invalid role passed into generate_report

        Expecting console to print "Save report aborted" and a PASS
    Post:
        PASS as of 4/19/2023
    """
    print("")
    db = Database()
    db.connect(ADMINUSER, ADMINPASS)
    generate_report(generate_test_patients(5), "not_a_valid_role")


def test_volunteer_report(num_patients=1):
    """
    Preamble:
        Test case for generating a volunteer report

        Expecting one of two results:
            If cancel clicked --> console prints "Save report aborted" and a PASS
            If saved --> look for output file, verify appropriate info is shown, PASS
    Post:
        PASS as of 4/19/2023
    """
    _report("volunteer_test", "volunteer_test", "volunteer", num_patients)


def test_nurse_report(num_patients=1):
    """
    Preamble:
        Test case for generating a nurse report

        Expecting one of two results:
            If cancel clicked --> console prints "Save report aborted" and a PASS
            If saved --> look for output file, verify appropriate info is shown, PASS
    Post:
        PASS as of 4/19/2023
    """
    _report("nurse_test", "nurse_test", "nurse", num_patients)


def test_doctor_report(num_patients=1):
    """
    Preamble:
        Test case for generating a doctor report

        Expecting one of two results:
            If cancel clicked --> console prints "Save report aborted" and a PASS
            If saved --> look for output file, verify appropriate info is shown, PASS
    Post:
        PASS as of 4/19/2023
    """
    _report("doctor_test", "doctor_test", "doctor", num_patients)


def test_office_report(num_patients=1):
    """
    Preamble:
        Test case for generating a office report

        Expecting one of two results:
            If cancel clicked --> console prints "Save report aborted" and a PASS
            If saved --> look for output file, verify appropriate info is shown, PASS
    Post:
        PASS as of 4/19/2023
    """
    _report("office_test", "office_test", "office", num_patients)
