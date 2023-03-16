from account import *
import datetime
from fpdf import FPDF


# Function used to get patient data from database
# Returns a list of strings containing patient information based on user tier
# Inputs: an Account class
# TODO: Determine if a patients parameter is needed
def scrape_data(account, patients=None):
    # Header of report
    report = ["Accessed by: " + str(account.get_user()), "Tier of User: " + str(account.get_tier()),
              "Date of Access: " + str(datetime.date.today()),
              "Time of Access: " + datetime.datetime.now().strftime("%H:%M:%S"), "\n"]

    # If tier is at least 0, add this info to report
    if account.get_tier() >= 0:
        name = "John Doe"
        report.append("Patient name: " + name)

        building = "Main"
        report.append("Building: " + building)

        floor_number = 1
        report.append("Floor number: " + str(floor_number))

        room_number = 117
        report.append("Room number: " + str(room_number))

        bed_number = 5
        report.append("Bed number: " + str(bed_number))

        restricted_visitors = ["Ronald McDonald", "Michael Jackson"]
        report.append("Restricted visitors: " + ", ".join(restricted_visitors))

        approved_visitors = ["Jane Doe", "John Snow"]
        report.append("Restricted visitors: " + ", ".join(approved_visitors))
        report.append("\n")

    # If tier is at least 1, add this info to report
    if account.get_tier() >= 1:
        admission_reason = "Arrow to the knee"
        report.append("Reason for admission: " + admission_reason)

        admission_date = "2023-02-21"
        discharge_date = None
        report.append("Admission date: " + str(admission_date))
        report.append("Discharge date: " + str(discharge_date))

        street = "123 Sesame Street"
        city = "Huntsville"
        state = "Alabama"
        zip = 45678
        mailing_address = [street, city, state, str(zip)]
        report.append("Mailing address: " + ", ".join(mailing_address))

        phone_numbers = {"Home": None, "Mobile": 11111111, "Work": 2222222}
        report.append("Phone numbers: " + dict_to_string(phone_numbers))

        emergency_contacts = {"Jane Doe": 1800, "John Snow": 8100}
        report.append("Emergency Contacts: " + dict_to_string(emergency_contacts))

        family_doctor = "House M.D"
        report.append("Family doctor: " + family_doctor)

        insurance_carrier = "Progressive"
        report.append("Insurance Carrier: " + insurance_carrier)

        account_number = 3333333
        group_number = 4444444
        report.append("Account number: " + str(account_number))
        report.append("Group number: " + str(group_number))

        insurance_amount_paid = 500.00
        patient_amount_paid = 940.00
        patient_amount_owed = 60.00
        report.append("Amount paid by insurance: $" + str(insurance_amount_paid))
        report.append("Amount paid by patient: $" + str(patient_amount_paid))
        report.append("Amount owed by patient: $" + str(patient_amount_owed))

        charges = {"Surgery fee": 1000.00, "Service fee": 250.00, "Misc": 250.00}
        report.append("Charges: " + dict_to_string(charges, " $"))

        report.append("\n")

    # If tier is at least 2, add this info to report
    if account.get_tier() >= 2:
        prescriptions = {"Morphine": ["1 every 6 hours", "24 tablets"], "Antibiotics": ["3 every 8 hours", "16 capsules"]}
        add_dict_as_bullets("Prescriptions:", prescriptions, report)

        procedures = {"Surgical Extraction": ["2023-02-21, 2:30 am", "Main building", "Dr. Strange"], "Skin graft": ["2023-02-23, 5:00 pm", "Cosmetic building", "House M.D"]}
        add_dict_as_bullets("Scheduled Procedures:", procedures, report)

        doctors_notes = {"House M.D": ["Knee has an arrow", "Refer to surgeon"], "Dr. Strange": ["Arrow removed"]}
        add_dict_as_bullets("Doctors' Notes:", doctors_notes, report)

        nurses_notes = {"Nurse Joy": ["Recovery has been going well post-operation"]}
        add_dict_as_bullets("Nurses' Notes:", nurses_notes, report)

    # Return report as a list of strings
    return report


# Function used to save patient information as a pdf report
# Information on report depends on tier
# # NOTE: Does NOT return anything, only exports pdf
# TODO: Integrate database support, and support for report on multiple patients
def save_reports(account, patients=None):
    report_pdf = FPDF()

    # for patient in patients (outer loop)
    report_pdf.add_page()
    report = scrape_data(account)
    report_pdf.set_font("Arial", size=11)
    for line in report:  # (inner loop)
        print(line)
        report_pdf.cell(200, 5, txt=line, ln=1)

    # (Outside outer loop)
    report_pdf.output("report.pdf")


# Helper function that adds contents of dictionary to report in bullet pointed format
# Inputs: header for bullet pointed section, input dictionary, list to append to
# NOTE: Does NOT return anything, it will ADD TO the input list (report_list)
def add_dict_as_bullets(subheader, input_dict, report_list):
    report_list.append(subheader)
    for key in input_dict:
        report_list.append("        " + key + ":")
        for note in input_dict[key]:
            report_list.append("                * " + note)


# Helper function that converts dictionary to a string
# All key/value pairs are separated by commas
# Programmer can set the delimiter/symbol that separates each key and value (comma by default)
# Inputs: a dictionary to convert, an optional string of desired delimiter
# Returns: string of dictionary
def dict_to_string(input_dict, delimiter=" - "):
    dict_str = ""
    for key in input_dict:
        dict_str += key + delimiter + str(input_dict[key]) + ", "
    if len(dict_str) > 2:
        dict_str = dict_str[:-2]

    return dict_str


# Testing code
testing = Account("Michael", 2)  # Creating account of tier 2
save_reports(testing)  # Saving sample patient data to pdf report
