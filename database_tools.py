from database import *


"""
Used to create account
Inputs:
username - account username, string
password - account password, string
tier - account tier, int
test - optional: True if using test tables (must be labeled patient_medical_test and patient_accounting_test), bool
"""
def create_account(username, password, tier=0, test=False):
    # Name of tables accounts can have access to
    tables = ["patient_accounting", "patient_medical"]

    # If testing, append "_test" with the assumptions made above
    if test:
        for i in range(0, len(tables)):
            tables[i] += "_test"

    # Ensuring user input for tier is valid
    tiers = [0, 1, 2, 3]

    if tier not in tiers:
        # Defaults to volunteer status
        tier = 0

    # Creating account
    poggers.execute("CREATE USER '" + str(username) + "' IDENTIFIED BY '" + str(password) + "';")
    poggers.commitChanges()

    # Setting account permissions
    # TODO: Limit some columns to INSERT/SELECT/UPDATE only
    if tier == 0:
        # TODO: Need to add columns for room_number, restricted visitors, and allowed visitors
        set_account_permission(username, tables[0], ['firstname', 'lastname'], ["SELECT"])
    elif tier == 1:
        set_account_permission(username, tables[0], ['firstname', 'lastname', 'address', 'marital_status',
                                                     'employment_status', 'employer', 'insurance_provider',
                                                     'insurance_contact', 'invoice', 'patient_amount_paid',
                                                     'insurance_amount_paid', 'pay_plan', 'pay_history',
                                                     'phone_number', 'insurance_account_num', 'charge_history'],
                                                    ["SELECT", "UPDATE"])
    else:
        set_account_permission(username, tables[1], ['firstname', 'lastname', 'room_number', 'sex', 'age', 'height',
                                                     'weight', 'race', 'dob', 'care_provider', 'current_status',
                                                     'medical_risks', 'allowed_visitors', 'restricted_visitors',
                                                     'admission_date', 'admission_reason', 'discharge_date',
                                                     'emergency_contacts', 'family_doctor', 'medical_history', 'photo',
                                                     'phone_number', 'ssn'], ["SELECT", "UPDATE", "INSERT"])


"""
Deletes account in database
Inputs:
username - account username, string
"""
def delete_account(username):
    poggers.execute("DROP USER " + str(username) + ";")
    poggers.commitChanges()


"""
Lists all accounts in database
Inputs:
show_permissions - optional, if set to True, shows all permissions for that account, bool
"""
def display_accounts(show_permissions=False):
    # Getting all accounts
    accounts = poggers.select("user", "mysql.user")

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

    poggers.execute(query)
    poggers.commitChanges()


"""
Shows an accounts table permissions
Input:
username - account username, string
"""
def show_account_permissions(username):
    # Acquiring permissions
    permissions = poggers.execute("SHOW GRANTS FOR " + username + ";")

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
    poggers.execute(query)
    poggers.commitChanges()


"""
Used to delete table from database
Inputs:
table_name - name of table to delete, string
"""
def delete_table(table_name):
    poggers.execute("DROP TABLE " + str(table_name) + ";")
    poggers.commitChanges()


"""
Displays all tables in database
"""
def display_tables():
    print(poggers.execute("SHOW TABLES"))
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
Test case of account creation on dummy tables
"""
def account_creation_test_on_dummy_tables():
    # These are the accounts created with their respective tier tables
    account_table = {
        "volunteer_test": "patient_accounting_test",
        "office_test": "patient_accounting_test",
        "medical_test": "patient_medical_test"
    }

    # If left over dummy tables/accounts are present, delete them
    for account in account_table.keys():
        try:
            reset(account, account_table[account])
        except:
            pass

    # Creating dummy tables
    create_table("patient_accounting_test", {
        "firstname": "VARCHAR(255)",
        "lastname": "VARCHAR(255)",
        "address": "VARCHAR(255)",
        "marital_status": "VARCHAR(255)",
        "employment_status": "VARCHAR(50)",
        "employer": "VARCHAR(50)",
        "insurance_provider": "VARCHAR(50)",
        "insurance_contact": "VARCHAR(500)",
        "invoice": "INT",
        "patient_amount_paid": "INT",
        "insurance_amount_paid": "INT",
        "pay_plan": "VARCHAR(255)",
        "pay_history": "VARCHAR(500)",
        "phone_number": "VARCHAR(20)",
        "insurance_account_num": "VARCHAR(50)",
        "charge_history": "VARCHAR(500)"
    })

    create_table("patient_medical_test", {
        "firstname": "VARCHAR(255)",
        "lastname": "VARCHAR(255)",
        "room_number": "INT",
        "sex": "VARCHAR(255)",
        "age": "INT",
        "height": "VARCHAR(255)",
        "weight": "VARCHAR(50)",
        "race": "VARCHAR(50)",
        "dob": "DATE",
        "care_provider": "VARCHAR(50)",
        "current_status": "VARCHAR(50)",
        "medical_risks": "VARCHAR(500)",
        "allowed_visitors": "VARCHAR(500)",
        "restricted_visitors": "VARCHAR(500)",
        "admission_date": "DATE",
        "admission_reason": "VARCHAR(255)",
        "discharge_date": "DATE",
        "emergency_contacts": "VARCHAR(500)",
        "family_doctor": "VARCHAR(255)",
        "medical_history": "VARCHAR(2000)",
        "photo": "BLOB",
        "phone_number": "VARCHAR(20)",
        "ssn": "VARCHAR(20)"
    })

    # Account creation
    print("***Before account creation***")
    display_accounts()

    print("\n***After account creation***")
    create_account("volunteer_test", 123, 0, test=True)
    create_account("office_test", 123, 1, test=True)
    create_account("medical_test", 123, 2, test=True)
    display_accounts(show_permissions=True)

    # Account and table deletion (NOTE: only deleting dummy tables here. NEVER delete our actual tables.)
    print("\n***After account deletion***")
    delete_account("volunteer_test")
    delete_account("office_test")
    delete_account("medical_test")
    display_accounts()
    delete_table("patient_accounting_test")
    delete_table("patient_medical_test")


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
    create_account("medical_test", 123, 2)
    display_accounts(show_permissions=True)

    print("\n***After account deletion***")
    delete_account("volunteer_test")
    delete_account("office_test")
    delete_account("medical_test")
    display_accounts()


"""
Helper functions used for resetting tests if something fails
Deletes user
TODO: DO NOT use this for any test labeled (actual_tables)
"""
def reset(username, table_name):
    try:
        delete_account(username)
    except:
        pass

    try:
        delete_table(table_name)
    except:
        pass


# account_creation_test_on_dummy_tables()
# account_creation_test_on_actual_tables()
# table_creation_test()
# display_accounts_test()
