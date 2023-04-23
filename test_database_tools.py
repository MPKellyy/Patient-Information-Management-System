from database_tools import *

'''
HEADER:
This file is a test case document for database_tools. Whenever a test case is added to this document, you MUST provide
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

def test_create_account():
    """
    Preamble:
        Test case for creating every account tier, expecting visually correct output in console and PASS rating
        from Pycharm

        Note: Will always pass barring any critical errors thrown, so make sure to review console contents as well
    Post:
        PASS as of 4/19/2023
    """

    reset("volunteer_test")
    reset("office_test")
    reset("nurse_test")
    reset("doctor_test")

    print("\n***Before account creation***")
    display_accounts()

    print("\n***After account creation***")
    create_account("volunteer_test", 123, "volunteer")
    create_account("office_test", 123, "office")
    create_account("nurse_test", 123, "nurse")
    create_account("doctor_test", 123, "doctor")
    display_accounts(show_permissions=True)

    print("\n***After account deletion***")
    delete_account("volunteer_test")
    delete_account("office_test")
    delete_account("nurse_test")
    delete_account("doctor_test")
    display_accounts()


def test_display_accounts():
    """
    Preamble:
        Test case for displaying all accounts in database, expecting visually correct output in console and PASS rating
        from Pycharm

        Note: Will always pass barring any critical errors thrown, so make sure to review console contents as well
    Post:
        PASS as of 4/19/2023
    """
    print("\n***Displaying accounts without permissions flag***")
    display_accounts()

    print("***Displaying accounts with permissions flag set***")
    display_accounts(show_permissions=True)


def test_show_account_permission():
    """
    Preamble:
        displays the permissions currently given to an account
    Post:
        PASS as of 4/23/2023
    """
    show_account_permissions('volunteer')


def test_create_table_delete_table():
    """
    Preamble:
        Test case for table creation, expecting visually correct output in console and PASS rating from Pycharm

        Note: Will always pass barring any critical errors thrown, so make sure to review console contents as well
    Post:
        PASS as of 4/19/2023
    """

    print("\n***Before table creation***")
    display_tables()

    print("***After table creation***")
    create_table("test_table", {"col1": "INT", "col2": "INT"})
    display_tables()

    print("***After table deletion***")
    delete_table("test_table")
    display_tables()

def test_display_table():
    """
        Preamble:
            displays all tables in a list to the console
        Post:
            PASS as of 4/23/2023
        """
    display_tables()








