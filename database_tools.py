from database import *

# Connecting to database
db = Database()
db.connect(ADMINUSER, ADMINPASS)

"""
Used to create account
Inputs:
username - account username, string
password - account password, string
tier - account tier, int
test - optional: True if using test tables (must be labeled patient_medical_test and patient_accounting_test), bool
"""
def create_account(username, password, role):
    # Ensuring user input for tier is valid
    roles = ["volunteer", "nurse", "doctor"]

    if role not in roles:
        # Defaults to volunteer status
        role = "volunteer"

    # Creating account
    db.execute("CREATE USER '" + str(username) + "' IDENTIFIED BY '" + str(password) + "';")
    db.commit_changes(override=True)
    grant_query = "GRANT '" + role + "' TO '" + username + "'@'%';"
    role_query = "SET DEFAULT ROLE '" + role + "' TO '" + username + "'@'%';"
    db.execute(grant_query)
    db.commit_changes(override=True)
    db.execute(role_query)
    db.commit_changes(override=True)


"""
Deletes account in database
Inputs:
username - account username, string
"""
def delete_account(username):
    db.execute("DROP USER " + str(username) + ";")
    db.commit_changes(override=True)


"""
Lists all accounts in database
Inputs:
show_permissions - optional, if set to True, shows all permissions for that account, bool
"""
def display_accounts(show_permissions=False):
    # Getting all accounts
    accounts = db.select("user", "mysql.user")

    # We don't want to display these
    virtual_databases = ["mysql.infoschema", "mysql.session", "mysql.sys"]

    # Listing the accounts
    for account in accounts:
        # If it is not a user account, skip
        if account[0] in virtual_databases:
            continue

        # Display username
        print(account[0])

        # If permissions flag set, show permissions
        if show_permissions and account[0] not in virtual_databases:
            try:
                show_account_permissions(account[0])
            except:
                pass

            print("")

    # Here to keep spacing consistent
    if not show_permissions:
        print("")


"""
Sets an accounts table permissions (used in account creation function)
Inputs:
username - account username, string
table_name - name of table to set permissions for, string
col_names - string-list of column names to set permissions for (assuming they exist!)
permissions - string-list of permissions you want to set for user (must be valid permission settings!)
"""
def set_account_permission(username, table_name, col_names, permissions):
    # Constructing query
    query = "GRANT "

    # Appending desired permissions
    for permission in permissions:
        query += permission + ", "

    query = query[:-2]
    query += " ("

    # Appending desired columns
    for col_name in col_names:
        query += col_name + ", "

    # Finalizing and executing query
    query = query[:-2]
    query += ") ON " + str(table_name) + " TO " + str(username) + ";"

    db.execute(query)
    db.commit_changes(override=True)


"""
Shows an accounts table permissions
Input:
username - account username, string
"""
def show_account_permissions(username):
    # Acquiring permissions
    permissions = db.execute("SHOW GRANTS FOR " + username + ";")

    # Printing returned permissions
    for permission in permissions:
        print(permission[0])


"""
Creates table in database
Inputs:
table_name - name of table to create, string
col_dict - a dictionary where each key is the string of a column name and value is a SQL value as a string
"""
def create_table(table_name, col_dict={"col1": "INT"}):
    # Must have at least one table entry, return if len 0 provided
    if len(col_dict) == 0:
        print("Aborting table creation, must have at least one dictionary entry")
        return

    # Constructing query
    query = "CREATE TABLE " + str(table_name) + " ( "

    for col_name in col_dict.keys():
        query += col_name + " " + col_dict[col_name] + ", "

    query = query[:-2]
    query += ");"

    # Executing query
    db.execute(query)
    db.commit_changes(override=True)


"""
Used to delete table from database
Inputs:
table_name - name of table to delete, string
"""
def delete_table(table_name):
    db.execute("DROP TABLE " + str(table_name) + ";")
    db.commit_changes(override=True)


"""
Displays all tables in database
"""
def display_tables():
    tables = db.execute("SHOW TABLES")

    for i in range(0, len(tables)):
        name = tables[i][0]
        print(name)

    print("")


"""
Test case for table creation
"""
def table_creation_test():
    print("***Before table creation***")
    display_tables()

    print("***After table creation***")
    create_table("test_table", {"col1": "INT", "col2": "INT"})
    display_tables()

    print("***After table deletion***")
    delete_table("test_table")
    display_tables()


"""
Test case for displaying all accounts in database
"""
def display_accounts_test():
    print("***Displaying accounts without permissions flag***")
    display_accounts()

    print("***Displaying accounts with permissions flag set***")
    display_accounts(show_permissions=True)


"""
Test case for creating every account tier on our current tables
"""
def account_creation_test_on_actual_tables():
    # TODO: If this test fails, DO NOT DROP THESE TABLES. You need to delete the test accounts before rerunning.

    print("***Before account creation***")
    display_accounts()

    print("\n***After account creation***")
    create_account("volunteer_test", 123, 0)
    create_account("office_test", 123, 1)
    create_account("nurse_test", 123, 2)
    create_account("doctor_test", 123, 3)
    display_accounts(show_permissions=True)

    print("\n***After account deletion***")
    delete_account("volunteer_test")
    delete_account("office_test")
    delete_account("nurse_test")
    delete_account("doctor_test")
    display_accounts()


"""
Helper functions used for resetting tests if something fails
Deletes user
TODO: DO NOT use this for any test labeled (actual_tables)
"""
def reset(username):
    try:
        delete_account(username)
    except:
        pass


# display_accounts_test()
# table_creation_test()
# account_creation_test_on_actual_tables()