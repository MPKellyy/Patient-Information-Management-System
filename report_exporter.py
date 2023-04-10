from account import *
import datetime
from fpdf import FPDF
from patient import *
from database import *
from tkinter import filedialog


# Function used to get patient data from database
# Returns a list of strings containing patient information based on user tier
# Inputs: an Account class
# TODO: Determine if a patients parameter is needed
def _format_data(patient, tier):
    # Header of report
    report = ["Date of access: " + str(datetime.date.today()),
              "Time of access: " + datetime.datetime.now().strftime("%H:%M:%S"), "\n"]

    if tier == 1:
        # Office staff
        name = patient.firstname + " " + patient.lastname
        report.append("Patient name: " + name)

        phone_number = patient.phone_number
        report.append("Phone number: " + str(phone_number))

        report.append("\n")
        pass
        # TODO: Add Insurance info to patient.py
        # Insurance Carrier
        # Insurance Group Number
        # Insurance Account Number

        # TODO: Add expenses to patient.py
        # insurance_amount_paid = 500.00
        # patient_amount_paid = 940.00
        # patient_amount_owed = 60.00
        # report.append("Amount paid by insurance: $" + str(insurance_amount_paid))
        # report.append("Amount paid by patient: $" + str(patient_amount_paid))
        # report.append("Amount owed by patient: $" + str(patient_amount_owed))

        # charges = {"Surgery fee": 1000.00, "Service fee": 250.00, "Misc": 250.00}
        # report.append("Charges: " + _dict_to_string(charges, " $"))
    elif tier == 2 or tier == 3:
        # Nurse and Doctor can see same information in report

        name = patient.firstname + " " + patient.lastname
        report.append("Patient name: " + str(name))

        if tier == 3:
            ssn = patient.ssn
            report.append("SSN: " + str(ssn))

        dob = patient.dob
        report.append("Date of birth: " + str(dob))

        age = patient.age
        report.append("Age: " + str(age))

        sex = patient.sex
        report.append("Sex: " + str(sex))

        race = patient.race
        report.append("Race: " + str(race))

        height = patient.height
        report.append("Height: " + str(height))

        weight = patient.weight
        report.append("Weight: " + str(weight))

        # photo = patient.photo
        # report.append("Photo: " + str(photo))

        report.append("\n")

        room_number = patient.room_number
        report.append("Room number: " + str(room_number))

        current_status = patient.current_status
        report.append("Current status: " + str(current_status))

        allowed_visitors = patient.allowed_visitors
        report.append("Allowed visitors: " + str(allowed_visitors))

        restricted_visitors = patient.restricted_visitors
        report.append("Restricted visitors: " + str(restricted_visitors))

        medical_risks = patient.medical_risks
        report.append("Medical risks: " + str(medical_risks))

        medical_history = patient.medical_history
        report.append("Medical history: " + str(medical_history))

        report.append("\n")

        admission_reason = patient.admission_reason
        report.append("Reason for admission: " + str(admission_reason))

        admission_date = patient.admission_date
        discharge_date = patient.discharge_date
        report.append("Admission date: " + str(admission_date))
        report.append("Discharge date: " + str(discharge_date))

        phone_number = patient.phone_number
        report.append("Phone number: " + str(phone_number))

        emergency_contacts = patient.emergency_contacts
        report.append("Emergency contacts: " + str(emergency_contacts))

        if tier == 3:
            family_doctor = patient.family_doctor
            report.append("Family doctor: " + family_doctor)

        care_provider = patient.care_provider
        report.append("Care provider: " + care_provider)

        report.append("\n")

        # TODO: Add prescriptions to patient.py
        # prescriptions = {"Morphine": ["1 every 6 hours", "24 tablets"], "Antibiotics": ["3 every 8 hours", "16 capsules"]}
        # _add_dict_as_bullets("Prescriptions:", prescriptions, report)
        # TODO: Add procedures to patient.py
        # procedures = {"Surgical Extraction": ["2023-02-21, 2:30 am", "Main building", "Dr. Strange"], "Skin graft": ["2023-02-23, 5:00 pm", "Cosmetic building", "House M.D"]}
        # _add_dict_as_bullets("Scheduled Procedures:", procedures, report)

        doctors_notes = patient.doctor_notes
        report.append("Doctors' notes: " + str(doctors_notes))

        nurses_notes = patient.nurse_notes
        report.append("Nurses' notes: " + str(nurses_notes))

        report.append("\n")
    else:
        name = patient.firstname + " " + patient.lastname
        report.append("Patient name: " + name)

        room_number = patient.room_number
        report.append("Room number: " + str(room_number))

        # photo = patient.photo
        # report.append("Photo: " + str(photo))

        # TODO: Allowed and Restricted visitor access?
        # allowed_visitors = patient.allowed_visitors
        # report.append("Allowed visitors: " + str(allowed_visitors))
        # restricted_visitors = patient.restricted_visitors
        # report.append("Restricted visitors: " + str(restricted_visitors))

        report.append("\n")

    # Return report as a list of strings
    return report


# Function used to save patient information as a pdf report
# Information on report depends on tier
# # NOTE: Does NOT return anything, only exports pdf
# TODO: Integrate database support, and support for report on multiple patients
def generate_report(patients, tier):
    # Test code
    filepath = ""
    try:
        filepath = filedialog.askdirectory()
        assert len(filepath) != 0
    except:
        print("Save report aborted")
        return

    report_pdf = FPDF()

    for patient in patients:
        report_pdf.add_page()
        report = _format_data(patient, tier)
        report_pdf.set_font("Arial", size=11)
        for line in report:  # (inner loop)
            print(line)
            report_pdf.cell(200, 5, txt=line, ln=1)

    report_pdf.output(filepath + "/patient_report.pdf")


# Helper function that adds contents of dictionary to report in bullet pointed format
# Inputs: header for bullet pointed section, input dictionary, list to append to
# NOTE: Does NOT return anything, it will ADD TO the input list (report_list)
def _add_dict_as_bullets(subheader, input_dict, report_list):
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
def _dict_to_string(input_dict, delimiter=" - "):
    dict_str = ""
    for key in input_dict:
        dict_str += key + delimiter + str(input_dict[key]) + ", "
    if len(dict_str) > 2:
        dict_str = dict_str[:-2]

    return dict_str


# Helper function to generate list Patients (for testing purposes)
def _generate_test_patients(num_patients):
    patient_list = []

    if not isinstance(num_patients, int) or num_patients < 1:
        return patient_list

    for i in range(0, num_patients):
        patient_list.append(Patient(i))

    return patient_list


# Testing code
#db = Database()
#db.connect(ADMINUSER, ADMINPASS)
#generate_report(db.search_patient_by_name())  # Saving sample patient data to pdf report
generate_report(_generate_test_patients(15), 3)  # Saving sample patient data to pdf report