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


def create_table(table_name, col_dict={"co1": "INT"}):
    if len(col_dict) == 0:
        print("Aborting table creation, must have at least one dictionary entry")
        return

    query = "CREATE TABLE " + str(table_name) + " ( "

    for col_name in col_dict.keys():
        query += col_name + " " + col_dict[col_name] + ", "

    query = query[:-2]
    query += ");"

    # print(query)

    poggers.execute(query)
    poggers.commitChanges()


def delete_table(table_name):
    poggers.execute("DROP TABLE " + str(table_name) + ";")
    poggers.commitChanges()


def display_tables():
    print(poggers.execute("SHOW TABLES"))


def table_creation_test():
    print("***Before table creation***")
    display_tables()
    print("***After table creation***")
    create_table("test_table", {"col1": "INT", "col2": "INT"})
    display_tables()
    print("***After table deletion***")
    delete_table("test_table")
    display_tables()


def display_accounts_test():
    print("Displaying accounts without permissions flag:")
    display_accounts()

    print("Displaying accounts with permissions flag set:")
    display_accounts(permissions=True)


# table_creation_test()
