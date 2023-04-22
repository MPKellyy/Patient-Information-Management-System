import tkinter as tk
from tkinter import *
from tkinter import ttk

import pymysql.err
import database
import report_exporter
import textwrap

db = database.Database()


def run_gui():
    root = Tk()
    root.title("Patient Information Management")
    root.geometry("1280x720")

    # expanded patient info page
    def open_patient_info(patient):
        global db
        role = db.execute("SELECT CURRENT_ROLE();")
        role = role[0][0].split("@")[0]
        tier = 0
        if role == "`volunteer`":
            tier = 0
        elif role == "`office`":
            tier = 1
        elif role == "`nurse`":
            tier = 2
        elif role == "`doctor`":
            tier = 3

        patient_frame = ttk.Frame(root, width=1260, height=580, padding=10, borderwidth=5, relief='solid')
        patient_frame.pack(pady=10)
        patient_frame.grid_propagate(False)

        # set up grid
        patient_frame.columnconfigure(1, weight=1)
        patient_frame.columnconfigure(2, weight=1)
        patient_frame.columnconfigure(3, weight=3)
        for i in range(1, 30):
            patient_frame.rowconfigure(i, weight=1)
        i = 1

        # tier 0 data
        if tier >= 0:
            # Patient Name
            patient_name_label = ttk.Label(patient_frame, text="Patient Name: ", font=('Arial', 12))
            patient_name_label.grid(row=i, column=1, sticky='nw')
            patient_name_data = ttk.Label(patient_frame, text=patient.get_full_name(), font=('Arial', 12))
            patient_name_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Building
            patient_building_label = ttk.Label(patient_frame, text="Building Location: ", font=('Arial', 12))
            patient_building_label.grid(row=i, column=1, sticky='nw')
            patient_building_data = ttk.Label(patient_frame, text=patient.building, font=('Arial', 12))
            patient_building_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Room Number
            patient_room_number_label = ttk.Label(patient_frame, text="Room Number: ", font=('Arial', 12))
            patient_room_number_label.grid(row=i, column=1, sticky='nw')
            patient_room_number_data = ttk.Label(patient_frame, text=patient.room_number, font=('Arial', 12))
            patient_room_number_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Bed Number
            patient_bed_number_label = ttk.Label(patient_frame, text="Bed Number: ", font=('Arial', 12))
            patient_bed_number_label.grid(row=i, column=1, sticky='nw')
            patient_bed_number_data = ttk.Label(patient_frame, text=patient.bed_number, font=('Arial', 12))
            patient_bed_number_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Restricted Visitors
            patient_restricted_visitors_label = ttk.Label(patient_frame, text="Restricted Visitors: ", font=('Arial', 12))
            patient_restricted_visitors_label.grid(row=i, column=1, sticky='nw')
            patient_restricted_visitors_data = ttk.Label(patient_frame, text=patient.restricted_visitors, font=('Arial', 12))
            patient_restricted_visitors_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Allowed Visitors
            patient_allowed_visitors_label = ttk.Label(patient_frame, text="Allowed Visitors: ", font=('Arial', 12))
            patient_allowed_visitors_label.grid(row=i, column=1, sticky='nw')
            patient_allowed_visitors_data = ttk.Label(patient_frame, text=patient.allowed_visitors, font=('Arial', 12))
            patient_allowed_visitors_data.grid(row=i, column=2, sticky='nw')
            i += 1


        # tier 1 data
        if tier >= 1:
            # Sex
            patient_sex_label = ttk.Label(patient_frame, text="Sex: ", font=('Arial', 12))
            patient_sex_label.grid(row=i, column=1, sticky='nw')
            patient_sex_data = ttk.Label(patient_frame, text=patient.sex, font=('Arial', 12))
            patient_sex_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Height
            patient_height_label = ttk.Label(patient_frame, text="Height: ", font=('Arial', 12))
            patient_height_label.grid(row=i, column=1, sticky='nw')
            patient_height_data = ttk.Label(patient_frame, text=patient.height, font=('Arial', 12))
            patient_height_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Weight
            patient_weight_label = ttk.Label(patient_frame, text="Weight: ", font=('Arial', 12))
            patient_weight_label.grid(row=i, column=1, sticky='nw')
            patient_weight_data = ttk.Label(patient_frame, text=patient.weight, font=('Arial', 12))
            patient_weight_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Date of Birth
            patient_dob_label = ttk.Label(patient_frame, text="Date of Birth: ", font=('Arial', 12))
            patient_dob_label.grid(row=i, column=1, sticky='nw')
            patient_dob_data = ttk.Label(patient_frame, text=patient.dob, font=('Arial', 12))
            patient_dob_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Age
            patient_age_label = ttk.Label(patient_frame, text="Age: ", font=('Arial', 12))
            patient_age_label.grid(row=i, column=1, sticky='nw')
            patient_age_data = ttk.Label(patient_frame, text=patient.age, font=('Arial', 12))
            patient_age_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Race
            patient_race_label = ttk.Label(patient_frame, text="Race: ", font=('Arial', 12))
            patient_race_label.grid(row=i, column=1, sticky='nw')
            patient_race_data = ttk.Label(patient_frame, text=patient.race, font=('Arial', 12))
            patient_race_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Admission Reason
            patient_admission_reason_label = ttk.Label(patient_frame, text="Admission Reason: ", font=('Arial', 12))
            patient_admission_reason_label.grid(row=i, column=1, sticky='nw')
            patient_admission_reason_data = ttk.Label(patient_frame, text=patient.admission_reason, font=('Arial', 12))
            patient_admission_reason_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Admission Date
            patient_admission_date_label = ttk.Label(patient_frame, text="Admission Date: ", font=('Arial', 12))
            patient_admission_date_label.grid(row=i, column=1, sticky='nw')
            patient_admission_date_data = ttk.Label(patient_frame, text=patient.admission_date, font=('Arial', 12))
            patient_admission_date_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Discharge Date
            patient_discharge_date_label = ttk.Label(patient_frame, text="Discharge Date: ", font=('Arial', 12))
            patient_discharge_date_label.grid(row=i, column=1, sticky='nw')
            patient_discharge_date_data = ttk.Label(patient_frame, text=patient.discharge_date, font=('Arial', 12))
            patient_discharge_date_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Mailing Address
            patient_mailing_address_label = ttk.Label(patient_frame, text="Mailing Address: ", font=('Arial', 12))
            patient_mailing_address_label.grid(row=i, column=1, sticky='nw')
            patient_mailing_address_data = ttk.Label(patient_frame, text=patient.address, font=('Arial', 12))
            patient_mailing_address_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Phone Number
            patient_phone_number_label = ttk.Label(patient_frame, text="Phone Number: ", font=('Arial', 12))
            patient_phone_number_label.grid(row=i, column=1, sticky='nw')
            patient_phone_number_data = ttk.Label(patient_frame, text=patient.phone_number, font=('Arial', 12))
            patient_phone_number_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Emergency Contacts
            patient_emergency_contacts_label = ttk.Label(patient_frame, text="Emergency Contacts: ", font=('Arial', 12))
            patient_emergency_contacts_label.grid(row=i, column=1, sticky='nw')
            patient_emergency_contacts_data = ttk.Label(patient_frame, text=patient.emergency_contacts, font=('Arial', 12))
            patient_emergency_contacts_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Family Doctor
            patient_family_doctor_label = ttk.Label(patient_frame, text="Family Doctor: ", font=('Arial', 12))
            patient_family_doctor_label.grid(row=i, column=1, sticky='nw')
            patient_family_doctor_data = ttk.Label(patient_frame, text=patient.care_provider, font=('Arial', 12))
            patient_family_doctor_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Insurance Carrier
            patient_insurance_carrier_label = ttk.Label(patient_frame, text="Insurance Carrier: ", font=('Arial', 12))
            patient_insurance_carrier_label.grid(row=i, column=1, sticky='nw')
            patient_insurance_carrier_data = ttk.Label(patient_frame, text=patient.insurance_provider, font=('Arial', 12))
            patient_insurance_carrier_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Insurance Account Number
            patient_insurance_account_number_label = ttk.Label(patient_frame, text="Insurance Account Number: ", font=('Arial', 12))
            patient_insurance_account_number_label.grid(row=i, column=1, sticky='nw')
            patient_insurance_account_number_data = ttk.Label(patient_frame, text=patient.insurance_account_num, font=('Arial', 12))
            patient_insurance_account_number_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Insurance Group Number
            patient_insurance_group_number_label = ttk.Label(patient_frame, text="Insurance Group Number: ", font=('Arial', 12))
            patient_insurance_group_number_label.grid(row=i, column=1, sticky='nw')
            patient_insurance_group_number_data = ttk.Label(patient_frame, text=patient.insurance_num, font=('Arial', 12))
            patient_insurance_group_number_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Insurance Amount Paid
            patient_insurance_amount_paid_label = ttk.Label(patient_frame, text="Insurance Amount Paid: ", font=('Arial', 12))
            patient_insurance_amount_paid_label.grid(row=i, column=1, sticky='nw')
            patient_insurance_amount_paid_data = ttk.Label(patient_frame, text=patient.insurance_amount_paid, font=('Arial', 12))
            patient_insurance_amount_paid_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Patient Amount Paid
            patient_patient_amount_paid_label = ttk.Label(patient_frame, text="Patient Amount Paid: ", font=('Arial', 12))
            patient_patient_amount_paid_label.grid(row=i, column=1, sticky='nw')
            patient_patient_amount_paid_data = ttk.Label(patient_frame, text=patient.patient_amount_paid, font=('Arial', 12))
            patient_patient_amount_paid_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # Patient Amount Owed
            patient_patient_amount_owed_label = ttk.Label(patient_frame, text="Patient Amount Owed: ", font=('Arial', 12))
            patient_patient_amount_owed_label.grid(row=i, column=1, sticky='nw')
            patient_patient_amount_owed_data = ttk.Label(patient_frame, text=patient.invoice, font=('Arial', 12))
            patient_patient_amount_owed_data.grid(row=i, column=2, sticky='nw')
            i += 1

            # History of Charges / Invoice
            patient_history_of_charges_label = ttk.Label(patient_frame, text="History of Charges: ", font=('Arial', 12))
            patient_history_of_charges_label.grid(row=i, column=1, sticky='nw')
            patient_history_of_charges_data = ttk.Label(patient_frame, text=patient.charge_history, font=('Arial', 12))
            patient_history_of_charges_data.grid(row=i, column=2, sticky='nw')
            i += 1

        # tier 2/3 data
        if tier >= 2:
            # Prescriptions
            if len(patient.prescriptions) > 70:
                patient.set_prescriptions(textwrap.fill(patient.prescriptions))
            patient_list_of_prescriptions_label = ttk.Label(patient_frame, text="List of Prescriptions: ", font=('Arial', 12))
            patient_list_of_prescriptions_label.grid(row=1, column=3, sticky='nw')
            patient_list_of_prescriptions_data = ttk.Label(patient_frame, text=patient.prescriptions, font=('Arial', 12))
            patient_list_of_prescriptions_data.grid(row=2, column=3, sticky='nw', rowspan=4)

            # Procedures
            if len(patient.procedures) > 70:
                patient.set_procedures(textwrap.fill(patient.procedures))
            patient_list_of_procedures_label = ttk.Label(patient_frame, text="List of Procedures: ", font=('Arial', 12))
            patient_list_of_procedures_label.grid(row=5, column=3, sticky='nw')
            patient_list_of_procedures_data = ttk.Label(patient_frame, text=patient.procedures, font=('Arial', 12))
            patient_list_of_procedures_data.grid(row=6, column=3, sticky='nw', rowspan=4)

            # Doctor's Notes
            if len(patient.doctor_notes) > 70:
                patient.set_doctor_notes(textwrap.fill(patient.doctor_notes))
            patient_doctors_notes_label = ttk.Label(patient_frame, text="Doctor's Notes: ", font=('Arial', 12))
            patient_doctors_notes_label.grid(row=9, column=3, sticky='nw')
            patient_doctors_notes_data = ttk.Label(patient_frame, text=patient.doctor_notes, font=('Arial', 12))
            patient_doctors_notes_data.grid(row=10, column=3, sticky='nw', rowspan=8)

            # Nurse's Notes
            if len(patient.nurse_notes) > 70:
                patient.set_nurse_notes(textwrap.fill(patient.nurse_notes))
            patient_nurses_notes_label = ttk.Label(patient_frame, text="Nurse's Notes: ", font=('Arial', 12))
            patient_nurses_notes_label.grid(row=18, column=3, sticky='nw')
            patient_nurses_notes_data = ttk.Label(patient_frame, text=patient.nurse_notes, font=('Arial', 12))
            patient_nurses_notes_data.grid(row=19, column=3, sticky='nw', rowspan=8)

        buttons_frame = ttk.Frame(root, width=1260, height=110, borderwidth=5, relief='solid')
        buttons_frame.pack()
        buttons_frame.pack_propagate(False)

        def logout():
            global db
            db.close()
            patient_frame.destroy()
            buttons_frame.destroy()
            open_login()
        logout_button = ttk.Button(buttons_frame, text="Log Out", command=logout)
        logout_button.pack(anchor='w')

        def back():
            patient_frame.destroy()
            buttons_frame.destroy()
            open_landing()
        back_button = ttk.Button(buttons_frame, text="Back", command=back)
        back_button.pack(anchor='w')

        def export():
            report_exporter.generate_report([patient], db.execute("SELECT CURRENT_ROLE();"))
        export_button = ttk.Button(buttons_frame, text="Export Report", command=export)
        export_button.pack(anchor='e')

        edit_or_save = True
        patient_name_edit = ttk.Entry(patient_frame, width=38)
        patient_building_edit = ttk.Entry(patient_frame, width=38)
        patient_room_number_edit = ttk.Entry(patient_frame, width=38)
        patient_bed_number_edit = ttk.Entry(patient_frame, width=38)
        patient_restricted_visitors_edit = ttk.Entry(patient_frame, width=38)
        patient_allowed_visitors_edit = ttk.Entry(patient_frame, width=38)
        patient_sex_edit = ttk.Entry(patient_frame, width=38)
        patient_height_edit = ttk.Entry(patient_frame, width=38)
        patient_weight_edit = ttk.Entry(patient_frame, width=38)
        patient_dob_edit = ttk.Entry(patient_frame, width=38)
        patient_age_edit = ttk.Entry(patient_frame, width=38)
        patient_race_edit = ttk.Entry(patient_frame, width=38)
        patient_admission_reason_edit = ttk.Entry(patient_frame, width=38)
        patient_admission_date_edit = ttk.Entry(patient_frame, width=38)
        patient_discharge_date_edit = ttk.Entry(patient_frame, width=38)
        patient_mailing_address_edit = ttk.Entry(patient_frame, width=38)
        patient_phone_number_edit = ttk.Entry(patient_frame, width=38)
        patient_emergency_contacts_edit = ttk.Entry(patient_frame, width=38)
        patient_family_doctor_edit = ttk.Entry(patient_frame, width=38)
        patient_insurance_carrier_edit = ttk.Entry(patient_frame, width=38)
        patient_insurance_account_number_edit = ttk.Entry(patient_frame, width=38)
        patient_insurance_group_number_edit = ttk.Entry(patient_frame, width=38)
        patient_insurance_amount_paid_edit = ttk.Entry(patient_frame, width=38)
        patient_amount_paid_edit = ttk.Entry(patient_frame, width=38)
        patient_amount_owed_edit = ttk.Entry(patient_frame, width=38)
        patient_history_of_charges_edit = ttk.Entry(patient_frame, width=38)
        patient_list_of_prescriptions_edit = tk.Text(patient_frame, width=60, height=4, wrap=WORD)
        patient_list_of_procedures_edit = tk.Text(patient_frame, width=60, height=4, wrap=WORD)
        patient_doctors_notes_edit = tk.Text(patient_frame, width=60, height=8, wrap=WORD)
        patient_nurses_notes_edit = tk.Text(patient_frame, width=60, height=8, wrap=WORD)

        fields = [(patient_name_edit, lambda p: p.get_full_name(), patient_name_data, 0),
                  (patient_building_edit, lambda p: p.building if p.building else "", patient_building_data, lambda new_value: patient.set_building(new_value)),
                  (patient_room_number_edit, lambda p: p.room_number if p.room_number else "", patient_room_number_data, lambda new_value: patient.set_room_number(new_value)),
                  (patient_bed_number_edit, lambda p: p.bed_number if p.bed_number else "", patient_bed_number_data, lambda new_value: patient.set_bed_number(new_value)),
                  (patient_restricted_visitors_edit, lambda p: p.restricted_visitors if p.restricted_visitors else "", patient_restricted_visitors_data, lambda new_value: patient.set_restricted_visitors(new_value)),
                  (patient_allowed_visitors_edit, lambda p: p.allowed_visitors if p.allowed_visitors else "", patient_allowed_visitors_data, lambda new_value: patient.set_allowed_visitors(new_value))
                  ]
        if tier >= 1:
            fields += [(patient_sex_edit, lambda p: p.sex  if p.sex else "", patient_sex_data, lambda new_value: patient.set_sex(new_value)),
                       (patient_height_edit, lambda p: p.height if p.height else "", patient_height_data, lambda new_value: patient.set_height(new_value)),
                       (patient_weight_edit, lambda p: p.weight if p.weight else "", patient_weight_data, lambda new_value: patient.set_weight(new_value)),
                       (patient_dob_edit, lambda p: p.dob if p.dob else "", patient_dob_data, lambda new_value: patient.set_dob(new_value)),
                       (patient_age_edit, lambda p: p.age if p.age else "", patient_age_data, lambda new_value: patient.set_age(new_value)),
                       (patient_race_edit, lambda p: p.race if p.race else "", patient_race_data, lambda new_value: patient.set_race(new_value)),
                       (patient_admission_reason_edit, lambda p: p.admission_reason if p.admission_reason else "", patient_admission_reason_data, lambda new_value: patient.set_admission_reason(new_value)),
                       (patient_admission_date_edit, lambda p: p.admission_date if p.admission_date else "", patient_admission_date_data, lambda new_value: patient.set_admission_date(new_value)),
                       (patient_discharge_date_edit, lambda p: p.discharge_date if p.discharge_date else "", patient_discharge_date_data, lambda new_value: patient.set_discharge_date(new_value)),
                       (patient_mailing_address_edit, lambda p: p.address if p.address else "", patient_mailing_address_data, lambda new_value: patient.set_address(new_value)),
                       (patient_phone_number_edit, lambda p: p.phone_number if p.phone_number else "", patient_phone_number_data, lambda new_value: patient.set_phone_number(new_value)),
                       (patient_emergency_contacts_edit, lambda p: p.emergency_contacts if p.emergency_contacts else "", patient_emergency_contacts_data, lambda new_value: patient.set_emergency_contacts(new_value)),
                       (patient_family_doctor_edit, lambda p: p.care_provider if p.care_provider else "", patient_family_doctor_data, lambda new_value: patient.set_care_provider(new_value)),
                       (patient_insurance_carrier_edit, lambda p: p.insurance_provider if p.insurance_provider else "", patient_insurance_carrier_data, lambda new_value: patient.set_insurance_provider(new_value)),
                       (patient_insurance_account_number_edit, lambda p: p.insurance_account_num if p.insurance_account_num else "", patient_insurance_account_number_data, lambda new_value: patient.set_insurance_account_num(new_value)),
                       (patient_insurance_group_number_edit, lambda p: p.insurance_num, patient_insurance_group_number_data, lambda new_value: patient.set_insurance_num(new_value)),
                       (patient_insurance_amount_paid_edit, lambda p: p.insurance_amount_paid if p.insurance_amount_paid else "", patient_insurance_amount_paid_data, lambda new_value: patient.set_insurance_amount_paid(new_value)),
                       (patient_amount_paid_edit, lambda p: p.patient_amount_paid if p.patient_amount_paid else "", patient_patient_amount_paid_data, lambda new_value: patient.set_patient_amount_paid(new_value)),
                       (patient_amount_owed_edit, lambda p: p.invoice, patient_patient_amount_owed_data, lambda new_value: patient.set_invoice(new_value)),
                       (patient_history_of_charges_edit, lambda p: p.charge_history if p.charge_history else "", patient_history_of_charges_data, lambda new_value: patient.set_charge_history(new_value))
                       ]
        fields2 = []
        if tier >= 2:
            fields2 += [(patient_list_of_prescriptions_edit, lambda p: p.prescriptions  if p.prescriptions else "", patient_list_of_prescriptions_data, lambda new_value: patient.set_prescriptions(new_value), 2),
                        (patient_list_of_procedures_edit, lambda p: p.procedures  if p.procedures else "", patient_list_of_procedures_data, lambda new_value: patient.set_procedures(new_value), 6)
                        ]
        if tier == 2:
            fields2 += [(patient_nurses_notes_edit, lambda p: p.nurse_notes if p.nurse_notes else "", patient_nurses_notes_data, lambda new_value: patient.set_nurse_notes(new_value), 19)]
        if tier == 3:
            fields2 += [(patient_doctors_notes_edit, lambda p: p.doctor_notes if p.doctor_notes else "", patient_doctors_notes_data, lambda new_value: patient.set_doctor_notes(new_value), 10)]
        def edit_button_function():
            nonlocal edit_or_save
            nonlocal patient_name_data
            if edit_or_save:
                row_number = 1
                for (entry, value, label, setter) in fields:
                    entry.insert(0, value(patient).replace("\n", " "))
                    entry.grid(row=row_number, column=2, sticky='nw')
                    row_number += 1
                    label.grid_forget()
                for (entry, value, label, setter, row) in fields2:
                    entry.insert(1.0, value(patient).replace("\n", " "))
                    entry.grid(row=row, column=3, sticky='nw', rowspan=4 if row < 8 else 8)
                    label.grid_forget()

                edit_button.config(text="Save Changes")
                edit_or_save = False
            else:
                # Patient Name
                patient_new_name = patient_name_edit.get().split(maxsplit=1)
                patient.set_firstname(patient_new_name[0])
                patient.set_lastname(patient_new_name[1])
                patient_name_data.config(text=patient.get_full_name())
                patient_name_edit.grid_forget()
                patient_name_edit.delete(first=0, last=tk.END)
                patient_name_data.grid(row=1, column=2, sticky='nw')

                row_number = 2
                for (entry, value, label, setter) in fields[1:]:
                    new_value = textwrap.fill(entry.get()).strip()
                    # print(value + '\t' + new_value)
                    if value(patient) != new_value:
                        setter(new_value)
                        label.config(text=new_value)
                    label.grid(row=row_number, column=2, sticky='nw')
                    entry.grid_forget()
                    entry.delete(first=0, last=tk.END)
                    row_number += 1
                for (entry, value, label, setter, row) in fields2:
                    new_value = textwrap.fill(entry.get(1.0, 'end-1c'))
                    if value(patient) != new_value:
                        setter(new_value)
                        label.config(text=new_value)
                    label.grid(row=row, column=3, sticky='nw', rowspan=4 if row < 8 else 8)
                    entry.grid_forget()
                    entry.delete(1.0, tk.END)

                db.save_patient_data(patient)
                db.commit_changes()
                edit_button.config(text="Edit Info")
                edit_or_save = True
        edit_button = ttk.Button(buttons_frame, text="Edit Info", command=edit_button_function)
        if tier >= 1:
            edit_button.pack(anchor='w')

    # landing page, has search bar, results window, various buttons at the bottom
    def open_landing():
        # left frame, for search bar and options (?)
        search_frame = ttk.Frame(root, width=400, height=580, borderwidth=5, relief='solid', padding='0i')
        search_frame.pack(side=LEFT, anchor='nw', padx=10, pady=10)
        search_frame.pack_propagate(False)
        # label for name search bar
        name_search_label = ttk.Label(search_frame, text="Name:")
        name_search_label.pack(side=LEFT, anchor='nw', pady=10)
        # name search entry field
        name_entry = ttk.Entry(search_frame, width=40)
        name_entry.pack(anchor='nw', padx=10, pady=10)
        # set of radio buttons to select whether to search by first name, last name, or full name
        name_radio_result = tk.IntVar()
        name_radio_result.set(1)
        first_name_radio = ttk.Radiobutton(search_frame, text="First Name", padding=10, value=1, variable=name_radio_result)
        first_name_radio.pack(anchor='nw')
        last_name_radio = ttk.Radiobutton(search_frame, text="Last Name", padding=10, value=2, variable=name_radio_result)
        last_name_radio.pack(anchor='nw')
        full_name_radio = ttk.Radiobutton(search_frame, text="Full Name", padding=10, value=3, variable=name_radio_result)
        full_name_radio.pack(anchor='nw')

        # search button by the name entry bar
        def search_button_function():
            # destroy existing results
            for x in results_canvas_frame.winfo_children():
                x.destroy()
            # determine whether to search first, last, or full name
            result = name_radio_result.get()
            if result == 1:
                search_for_patients(firstname=name_entry.get())
            elif result == 2:
                search_for_patients(lastname=name_entry.get())
            elif result == 3:
                search_for_patients(name=name_entry.get())
        search_button = ttk.Button(search_frame, text="Search", command=search_button_function)
        search_button.place(x=310, y=8)

        def search_for_patients(name=None, firstname=None, lastname=None):
            global db
            search_results = db.search_patient_by_name(name=name, firstname=firstname, lastname=lastname)
            result_list: list[Frame] = list()
            for i in range(len(search_results)):
                patient = search_results[i]
                # would have made search before this and now displaying results
                frame = ttk.Frame(results_canvas_frame, width=800, height=80, borderwidth=5, relief='solid')
                frame.pack()
                frame.grid_propagate(False)
                for j in range(1, 4):
                    frame.columnconfigure(j, weight=1)
                frame.rowconfigure(1, weight=1)
                patient_name_label = ttk.Label(frame, text=patient.get_full_name())
                patient_name_label.grid(column=1, row=1, sticky='w')
                patient_dob_label = ttk.Label(frame, text=patient.dob)
                patient_dob_label.grid(column=2, row=1, sticky='w')
                patient_phone_label = ttk.Label(frame, text=patient.phone_number)
                patient_phone_label.grid(column=3, row=1, sticky='w')
                patient_address_label = ttk.Label(frame, text=patient.address)
                patient_address_label.grid(column=4, row=1, sticky='w')
                frame.bind('<Double-Button-1>', lambda p=patient: patient_select(patient))
                result_list.append(frame)

        # right frame, for displaying results
        results_frame = ttk.Frame(root, width=850, height=580, borderwidth=5, relief='solid', padding=0)
        results_frame.pack(side=RIGHT, anchor='ne', padx=10, pady=10)
        results_frame.pack_propagate(False)
        # need a canvas and another frame to make it scrollable (thanks tkinter)
        results_canvas = Canvas(results_frame, width=800)
        results_canvas.pack(side=LEFT, fill='y')
        # scrollbar
        results_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=results_canvas.yview)
        results_scrollbar.pack(side=RIGHT, fill=Y)
        # make it scrollable
        results_canvas.configure(yscrollcommand=results_scrollbar.set)
        results_canvas_frame = Frame(results_canvas, padx=0, pady=0)
        results_canvas_frame.bind('<Configure>', lambda e: results_canvas.configure(scrollregion=results_canvas.bbox('all')))
        results_canvas.create_window((0, 0), window=results_canvas_frame, anchor='nw')

        # bottom frame with buttons
        buttons_frame = ttk.Frame(root, width=1260, height=110, borderwidth=5, relief='solid')
        buttons_frame.pack()
        buttons_frame.pack_propagate(False)
        buttons_frame.place(anchor='nw', x=10, y=600)

        def log_out():
            global db
            db.close()
            print('bye')
            search_frame.destroy()
            results_frame.destroy()
            buttons_frame.destroy()
            open_login()
        logout_button = ttk.Button(buttons_frame, text='Log Out', command=log_out)
        logout_button.pack(anchor='w', side=LEFT, padx=20)

        # button for exporting reports on all patients
        def export_all_patients():
            try:
                list_of_patients = db.get_all_patients()
            except:
                print("error in getting all patients")
            else:
                report_exporter.generate_report(list_of_patients, db.execute("SELECT CURRENT_ROLE();"))

        export_button = ttk.Button(buttons_frame, text="Export All Patients", command=export_all_patients)
        export_button.pack(anchor='w')

        def patient_select(e):
            print('select')
            search_frame.destroy()
            results_frame.destroy()
            buttons_frame.destroy()
            open_patient_info(e)



    def open_login():
        # login page frame
        login_frame = ttk.Frame(root, width=1280, height=720)
        login_frame.pack()
        login_frame.place(anchor='center', relx=0.5, rely=0.5)
        # username text box
        username_entry = ttk.Entry(login_frame, width=40)
        username_entry.place(x=550, y=280)
        # password text box
        password_entry = ttk.Entry(login_frame, width=40, show='*')
        password_entry.place(x=550, y=320)
        # username label text
        username_label = ttk.Label(login_frame, text="Username:")
        username_label.place(x=480, y=280)
        # password label text
        password_label = ttk.Label(login_frame, text="Password:")
        password_label.place(x=480, y=320)
        # top welcome text
        welcome_label = ttk.Label(login_frame, text="Welcome to Patient Information Management", font=("Arial", 35))
        welcome_label.place(x=200, y=100)

        # function that runs when Log In button is pressed - should eventually
        # query database and either display error message or move to landing page
        def login():
            # print(username_entry.get())
            # username_entry.delete(first=0, last=tk.END)
            # print(password_entry.get())
            # password_entry.delete(first=0, last=tk.END)
            try:
                global db
                db.connect(username_entry.get(), password_entry.get())
            except pymysql.err.OperationalError:
                error_label = ttk.Label(login_frame, text="Invalid Credentials", font=("Arial", 12))
                error_label.place(x=600, y=200)
                print("hi")
            except:
                error_label = ttk.Label(login_frame, text="Error: Please try again", font=("Arial", 12))
                error_label.place(x=600, y=200)
                print("poggers")
            else:
                # on successful login, destroy login frame and call function to open landing page
                login_frame.destroy()
                root.after(0, open_landing())
        login_button = ttk.Button(login_frame, text="Log In", command=login)
        login_button.place(x=625, y=370)
        root.mainloop()
    open_login()
