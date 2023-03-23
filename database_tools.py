from database import *


def create_account(user_name, password, tier=0):
    tiers = [0, 1, 2, 3]

    if tier not in tiers:
        tier = 0

    poggers.execute("CREATE USER '" + str(user_name) + "' IDENTIFIED BY '" + str(password) + "';");
    poggers.commitChanges()

    # TODO: Limit some columns to INSERT/SELECT/UPDATE only
    if tier == 0:
        set_account_permission(user_name, "Patients_Test", ['patient_name', 'building_location', 'room_number', 'bed_number', 'restricted_visitors', 'allowed_visitors'], ["SELECT"])
    elif tier == 1:
        set_account_permission(user_name, "Patients_Test", ['patient_name', 'building_location', 'room_number', 'bed_number', 'restricted_visitors', 'allowed_visitors', 'admission_reason', 'admission_date', 'discharge_date', 'mailing_address', 'phone_numbers', 'emergency_contacts', 'family_doctor', 'insurance_carrier', 'insurance_account_number', 'insurance_group_number', 'insurance_amount_paid', 'patient_amount_paid', 'patient_amount_owed', 'history_of_charges'], ["SELECT", "UPDATE"])
    else:
        set_account_permission(user_name, "Patients_Test", ['patient_name', 'building_location', 'room_number', 'bed_number', 'restricted_visitors', 'allowed_visitors', 'admission_reason', 'admission_date', 'discharge_date', 'mailing_address', 'phone_numbers', 'emergency_contacts', 'family_doctor', 'insurance_carrier', 'insurance_account_number', 'insurance_group_number', 'insurance_amount_paid', 'patient_amount_paid', 'patient_amount_owed', 'history_of_charges', 'prescriptions', 'procedures', 'doctors_notes', 'nurses_notes'], ["SELECT", "UPDATE", "INSERT"])


def delete_account(user_name):
    poggers.execute("DROP USER " + str(user_name) + ";")
    poggers.commitChanges()


def display_accounts(permissions=False):
    accounts = poggers.select("user", "mysql.user")
    virtual_databases = ["mysql.infoschema", "mysql.session", "mysql.sys", "rdsadmin"]

    for account in accounts:
        if account[0] in virtual_databases:
            continue

        print(account[0])

        if permissions and account[0] not in virtual_databases:
            show_account_permissions(account[0])
            print("")

    print("")


def set_account_permission(user_name, table_name, col_names, permissions):
    query = "GRANT "

    for permission in permissions:
        query += permission + ", "

    query = query[:-2]
    query += " ("

    for col_name in col_names:
        query += col_name + ", "

    query = query[:-2]
    query += ") ON " + str(table_name) + " TO " + str(user_name) + ";"

    poggers.execute(query)
    poggers.commitChanges()


def show_account_permissions(user_name):
    permissions = poggers.execute("SHOW GRANTS FOR " + user_name + ";")

    for permission in permissions:
        print(permission[0])


def create_table(table_name, col_dict={"col1": "INT"}):
    if len(col_dict) == 0:
        print("Aborting table creation, must have at least one dictionary entry")
        return

    query = "CREATE TABLE " + str(table_name) + " ( "

    for col_name in col_dict.keys():
        query += col_name + " " + col_dict[col_name] + ", "

    query = query[:-2]
    query += ");"

    poggers.execute(query)
    poggers.commitChanges()


def delete_table(table_name):
    poggers.execute("DROP TABLE " + str(table_name) + ";")
    poggers.commitChanges()


def display_tables():
    print(poggers.execute("SHOW TABLES"))
    print("")


# TODO: Put test cases in separate file
def account_creation_test():
    try:
        reset("test", "Patients_Test")
    except:
        pass

    create_table("Patients_Test", {
        "patient_name": "INT",
        "building_location": "INT",
        "room_number": "INT",
        "bed_number": "INT",
        "restricted_visitors": "INT",
        "allowed_visitors": "INT",
        "admission_reason": "INT",
        "admission_date": "INT",
        "discharge_date": "INT",
        "mailing_address": "INT",
        "phone_numbers": "INT",
        "emergency_contacts": "INT",
        "family_doctor": "INT",
        "insurance_carrier": "INT",
        "insurance_account_number": "INT",
        "insurance_group_number": "INT",
        "insurance_amount_paid": "INT",
        "patient_amount_paid": "INT",
        "patient_amount_owed": "INT",
        "history_of_charges": "INT",
        "prescriptions": "INT",
        "procedures": "INT",
        "doctors_notes": "INT",
        "nurses_notes": "INT"
    })

    print("***Before account creation***")
    display_accounts()

    print("***After account creation***")
    create_account("test", 123, 2)
    display_accounts(permissions=True)

    print("***After account deletion***")
    delete_account("test")
    display_accounts()
    delete_table("Patients_Test")


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
    print("***Displaying accounts without permissions flag***")
    display_accounts()

    print("***Displaying accounts with permissions flag set***")
    display_accounts(permissions=True)


def reset(user, table):
    try:
        delete_account(user)
    except:
        pass

    try:
        delete_table(table)
    except:
        pass


#account_creation_test()
#table_creation_test()
#display_accounts_test()
