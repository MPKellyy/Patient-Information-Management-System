from database import *


def create_account(username, password, tier=0):
    # TODO: Grant certain privileges based on tier, will do soon
    poggers.execute("CREATE USER '" + str(username) + "' IDENTIFIED BY '" + str(password) + "';");
    poggers.commitChanges()


def delete_account(username):
    poggers.execute("DROP USER " + str(username) + ";")
    poggers.commitChanges()


def display_accounts():
    accounts = poggers.select('*', 'mysql.user')
    print("Database Accounts:")
    for account in accounts:
        print(account[1])
    print("")


# Test code
print("***Before account creation***")
display_accounts()
print("***After account creation***")
create_account("test", 123)
display_accounts()
print("***After account deletion***")
delete_account("test")
display_accounts()