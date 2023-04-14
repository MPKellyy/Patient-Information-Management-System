import tkinter as tk
from tkinter import *
from tkinter import ttk

import pymysql.err
import database
import report_exporter

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
        for i in range(1, 22):
            patient_frame.rowconfigure(i, weight=1)
        i = 1

        # tier 0 data
        if tier >= 0:
            patient_patient_name_label = ttk.Label(patient_frame, text="Patient Name: " + patient.get_full_name(), font=('Arial', 15))
            patient_patient_name_label.grid(row=i, column=1, sticky='nw')

            patient_building_label = ttk.Label(patient_frame, text="Building Location: " + "Placeholder", font=('Arial', 15))
            patient_building_label.grid(row=i+1, column=1, sticky='nw')

            patient_room_number_label = ttk.Label(patient_frame, text="Room Number: " + patient.room_number, font=('Arial', 15))
            patient_room_number_label.grid(row=i+2, column=1, sticky='nw')

            patient_bed_number_label = ttk.Label(patient_frame, text="Bed Number: " + "Placeholder", font=('Arial', 15))
            patient_bed_number_label.grid(row=i+3, column=1, sticky='nw')

            patient_restricted_visitors_label = ttk.Label(patient_frame, text="Restricted Visitors: " + patient.restricted_visitors, font=('Arial', 15))
            patient_restricted_visitors_label.grid(row=i+4, column=1, sticky='nw')

            patient_allowed_visitors_label = ttk.Label(patient_frame, text="Allowed Visitors: " + patient.allowed_visitors, font=('Arial', 15))
            patient_allowed_visitors_label.grid(row=i+5, column=1, sticky='nw')

            i += 6

        # tier 1 data TODO: only show if account tier >=1
        if tier >= 1:
            patient_admission_reason_label = ttk.Label(patient_frame, text="Admission Reason: " + patient.admission_reason, font=('Arial', 15))
            patient_admission_reason_label.grid(row=i, column=1, sticky='nw')

            patient_admission_date_label = ttk.Label(patient_frame, text="Admission Date: " + patient.admission_date, font=('Arial', 15))
            patient_admission_date_label.grid(row=i+1, column=1, sticky='nw')

            patient_discharge_date_label = ttk.Label(patient_frame, text="Discharge Date: " + patient.discharge_date, font=('Arial', 15))
            patient_discharge_date_label.grid(row=i+2, column=1, sticky='nw')

            patient_mailing_address_label = ttk.Label(patient_frame, text="Mailing Address: " + "Placeholder", font=('Arial', 15))
            patient_mailing_address_label.grid(row=i+3, column=1, sticky='nw')

            patient_phone_number_label = ttk.Label(patient_frame, text="Phone Number: " + patient.phone_number, font=('Arial', 15))
            patient_phone_number_label.grid(row=i+4, column=1, sticky='nw')

            patient_emergency_contacts_label = ttk.Label(patient_frame, text="Emergency Contacts: " + patient.emergency_contacts, font=('Arial', 15))
            patient_emergency_contacts_label.grid(row=i+5, column=1, sticky='nw')

            patient_family_doctor_label = ttk.Label(patient_frame, text="Family Doctor: " + patient.care_provider, font=('Arial', 15))
            patient_family_doctor_label.grid(row=i+6, column=1, sticky='nw')

            patient_insurance_carrier_label = ttk.Label(patient_frame, text="Insurance Carrier: " + "Placeholder", font=('Arial', 15))
            patient_insurance_carrier_label.grid(row=i+7, column=1, sticky='nw')

            patient_insurance_account_number_label = ttk.Label(patient_frame, text="Insurance Account Number: " + "Placeholder", font=('Arial', 15))
            patient_insurance_account_number_label.grid(row=i+8, column=1, sticky='nw')

            patient_insurance_group_number_label = ttk.Label(patient_frame, text="Insurance Group Number: " + "Placeholder", font=('Arial', 15))
            patient_insurance_group_number_label.grid(row=i+9, column=1, sticky='nw')

            patient_insurance_amount_paid_label = ttk.Label(patient_frame, text="Insurance Amount Paid: " + "Placeholder", font=('Arial', 15))
            patient_insurance_amount_paid_label.grid(row=i+10, column=1, sticky='nw')

            patient_patient_amount_paid_label = ttk.Label(patient_frame, text="Patient Amount Paid: " + "Placeholder", font=('Arial', 15))
            patient_patient_amount_paid_label.grid(row=i+11, column=1, sticky='nw')

            patient_patient_amount_owed_label = ttk.Label(patient_frame, text="Patient Amount Owed: " + "Placeholder", font=('Arial', 15))
            patient_patient_amount_owed_label.grid(row=i+12, column=1, sticky='nw')

            patient_history_of_charges_label = ttk.Label(patient_frame, text="History of Charges: " + "Placeholder", font=('Arial', 15))
            patient_history_of_charges_label.grid(row=i+13, column=1, sticky='nw')

            i += 14

        # tier 2/3 data TODO: only show if account tier >=2 (and make only doctors able to edit doctor notes, same for nurses)
        if tier >= 2:
            patient_list_of_prescriptions_label = ttk.Label(patient_frame, text="List of Prescriptions: " + "Placeholder", font=('Arial', 15))
            patient_list_of_prescriptions_label.grid(row=1, column=2, sticky='nw')

            patient_list_of_procedures_label = ttk.Label(patient_frame, text="List of Procedures: " + "Placeholder", font=('Arial', 15))
            patient_list_of_procedures_label.grid(row=5, column=2, sticky='nw')

            patient_doctors_notes_label = ttk.Label(patient_frame, text="Doctor's Notes: " + "Placeholder", font=('Arial', 15))
            patient_doctors_notes_label.grid(row=9, column=2, sticky='nw')

            patient_nurses_notes_label = ttk.Label(patient_frame, text="Nurse's Notes: " + "Placeholder", font=('Arial', 15))
            patient_nurses_notes_label.grid(row=15, column=2, sticky='nw')

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
            print(db.execute("SELECT CURRENT_ROLE();"))
            report_exporter.generate_report([patient], db.execute("SELECT CURRENT_ROLE();"))
        export_button = ttk.Button(buttons_frame, text="Export Report", command=export)
        export_button.pack(anchor='e')

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
                patient_address_label = ttk.Label(frame, text="Placeholder")
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
            # todo: also delete account info
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

        # TODO: change the prints to database query logic when database is working
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
                error_label = ttk.Label(login_frame, text="Invalid Credentials", font=("Arial", 15))
                error_label.place(x=600, y=200)
                print("hi")
            except:
                error_label = ttk.Label(login_frame, text="Error: Please try again", font=("Arial", 15))
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
