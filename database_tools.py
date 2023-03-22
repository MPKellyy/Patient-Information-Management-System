from database import *


def create_account(username, password, tier=0):
    # TODO: Grant certain privileges based on tier, will do soon
    poggers.execute("CREATE USER '" + str(username) + "' IDENTIFIED BY '" + str(password) + "';");
    poggers.commitChanges()


def delete_account(username):
    poggers.execute("DROP USER " + str(username) + ";")
    poggers.commitChanges()


def display_accounts(permissions=False):
    accounts = poggers.select('*', 'mysql.user')
    privileges = poggers.execute("SELECT * FROM information_schema.user_privileges")

    for account in accounts:
        print(account[1])

        if permissions:
            key = "'" + account[1] + "'@'" + account[0] + "'"
            for privilege in privileges:
                if key == privilege[0]:
                    print("\t" + privilege[-2] + ": " + privilege[-1])

    print("")


# TODO: Put test cases in separate file
def account_creation_test():
    print("***Before account creation***")
    display_accounts()
    print("***After account creation***")
    create_account("test", 123)
    display_accounts()
    print("***After account deletion***")
    delete_account("test")
    display_accounts()


def create_table(table_name, data_dict={}):
    poggers.execute("CREATE TABLE " + str(table_name) + " (test_id INT);")
    poggers.commitChanges()


def delete_table(table_name):
    poggers.execute("DROP TABLE " + str(table_name) + ";")
    poggers.commitChanges()


def display_tables():
    poggers.execute("SHOW TABLES")


# TODO: Add this test to a separate test file, currently NOT working
def table_creation_test():
    print("***Before table creation***")
    display_tables()
    print("***After table creation***")
    create_table("test_table")
    display_tables()
    print("***After table deletion***")
    delete_table("test_table")
    display_tables()


display_accounts(permissions=True)
#display_accounts()
