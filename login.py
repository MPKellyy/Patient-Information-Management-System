import tkinter as tk
from tkinter import *
from tkinter import ttk

import pymysql.err

import database

db = ""
def run_gui():
    root = Tk()
    root.title("Patient Information Management")
    root.geometry("1280x720")

    # expanded patient info page
    def open_patient_info():
        patient_frame = ttk.Frame(root, width=1260, height=700, padding=10, borderwidth=5, relief='solid')
        patient_frame.pack(pady=10)
        patient_frame.grid_propagate(False)

        # set up grid
        patient_frame.columnconfigure(1, weight=1)
        patient_frame.columnconfigure(2, weight=2)
        patient_frame.columnconfigure(3, weight=1)
        patient_frame.columnconfigure(4, weight=2)
        for i in range(1, 20):
            patient_frame.rowconfigure(i, weight=1)

        # tier 0 data
        patient_patient_name_label = ttk.Label(patient_frame, text="Patient Name:", font=('Arial', 16))
        patient_patient_name_label.grid(row=1, column=1, sticky='nw')

        patient_building_label = ttk.Label(patient_frame, text="Building Location:", font=('Arial', 16))
        patient_building_label.grid(row=2, column=1, sticky='nw')

        patient_room_number_label = ttk.Label(patient_frame, text="Room Number:", font=('Arial', 16))
        patient_room_number_label.grid(row=3, column=1, sticky='nw')

        patient_bed_number_label = ttk.Label(patient_frame, text="Bed Number:", font=('Arial', 16))
        patient_bed_number_label.grid(row=4, column=1, sticky='nw')

        patient_restricted_visitors_label = ttk.Label(patient_frame, text="Restricted Visitors:", font=('Arial', 16))
        patient_restricted_visitors_label.grid(row=5, column=1, sticky='nw')

        patient_allowed_visitors_label = ttk.Label(patient_frame, text="Allowed Visitors:", font=('Arial', 16))
        patient_allowed_visitors_label.grid(row=6, column=1, sticky='nw')

        # tier 1 data TODO: only show if account tier >=1
        patient_admission_reason_label = ttk.Label(patient_frame, text="Admission Reason:", font=('Arial', 16))
        patient_admission_reason_label.grid(row=7, column=1, sticky='nw')

        patient_admission_date_label = ttk.Label(patient_frame, text="Admission Date:", font=('Arial', 16))
        patient_admission_date_label.grid(row=8, column=1, sticky='nw')

        patient_discharge_date_label = ttk.Label(patient_frame, text="Discharge Date:", font=('Arial', 16))
        patient_discharge_date_label.grid(row=9, column=1, sticky='nw')

        patient_mailing_address_label = ttk.Label(patient_frame, text="Mailing Address:", font=('Arial', 16))
        patient_mailing_address_label.grid(row=10, column=1, sticky='nw')

        patient_phone_number_label = ttk.Label(patient_frame, text="Phone Number:", font=('Arial', 16))
        patient_phone_number_label.grid(row=11, column=1, sticky='nw')

        patient_emergency_contacts_label = ttk.Label(patient_frame, text="Emergency Contacts:", font=('Arial', 16))
        patient_emergency_contacts_label.grid(row=12, column=1, sticky='nw')

        patient_family_doctor_label = ttk.Label(patient_frame, text="Family Doctor:", font=('Arial', 16))
        patient_family_doctor_label.grid(row=13, column=1, sticky='nw')

        patient_insurance_carrier_label = ttk.Label(patient_frame, text="Insurance Carrier:", font=('Arial', 16))
        patient_insurance_carrier_label.grid(row=14, column=1, sticky='nw')

        patient_insurance_account_number_label = ttk.Label(patient_frame, text="Insurance Account Number:", font=('Arial', 16))
        patient_insurance_account_number_label.grid(row=15, column=1, sticky='nw')

        patient_insurance_group_number_label = ttk.Label(patient_frame, text="Insurance Group Number:", font=('Arial', 16))
        patient_insurance_group_number_label.grid(row=16, column=1, sticky='nw')

        patient_insurance_amount_paid_label = ttk.Label(patient_frame, text="Insurance Amount Paid:", font=('Arial', 16))
        patient_insurance_amount_paid_label.grid(row=17, column=1, sticky='nw')

        patient_patient_amount_paid_label = ttk.Label(patient_frame, text="Patient Amount Paid:", font=('Arial', 16))
        patient_patient_amount_paid_label.grid(row=18, column=1, sticky='nw')

        patient_patient_amount_owed_label = ttk.Label(patient_frame, text="Patient Amount Owed:", font=('Arial', 16))
        patient_patient_amount_owed_label.grid(row=19, column=1, sticky='nw')

        patient_history_of_charges_label = ttk.Label(patient_frame, text="History of Charges:", font=('Arial', 16))
        patient_history_of_charges_label.grid(row=20, column=1, sticky='nw')

        # tier 2/3 data TODO: only show if account tier >=2 (and make only doctors able to edit doctor notes, same for nurses)
        patient_list_of_prescriptions_label = ttk.Label(patient_frame, text="List of Prescriptions:", font=('Arial', 16))
        patient_list_of_prescriptions_label.grid(row=1, column=3, sticky='nw')

        patient_list_of_procedures_label = ttk.Label(patient_frame, text="List of Procedures:", font=('Arial', 16))
        patient_list_of_procedures_label.grid(row=2, column=3, sticky='nw')

        patient_doctors_notes_label = ttk.Label(patient_frame, text="Doctor's Notes:", font=('Arial', 16))
        patient_doctors_notes_label.grid(row=3, column=3, sticky='nw')

        patient_nurses_notes_label = ttk.Label(patient_frame, text="Nurse's Notes:", font=('Arial', 16))
        patient_nurses_notes_label.grid(row=12, column=3, sticky='nw')

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
        # search button by the name entry bar

        def search_button_function():
            # todo: make this query db for what's in name_entry
            print('hi')
            for x in results_canvas_frame.winfo_children():
                x.destroy()
            search_for_patients()
        search_button = ttk.Button(search_frame, text="Search", command=search_button_function)
        search_button.place(x=310, y=8)

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
            db = ""
            print('bye')
            search_frame.destroy()
            results_frame.destroy()
            buttons_frame.destroy()
            open_login()
            # todo: also delete account info
        logout_button = ttk.Button(buttons_frame, text='Log Out', command=log_out)
        logout_button.pack(anchor='w', side=LEFT, padx=20)

        def patient_select(e):
            print('click')
            search_frame.destroy()
            results_frame.destroy()
            buttons_frame.destroy()
            open_patient_info()

        def search_for_patients():
            result_list: list[Frame] = list()
            for i in range(200):
                # would have made search before this and now displaying results
                frame = ttk.Frame(results_canvas_frame, width=800, height=80, borderwidth=5, relief='solid')
                frame.pack()
                frame.pack_propagate(False)
                a = ttk.Label(frame, text=str(i))
                a.pack()
                frame.bind('<Double-Button-1>', patient_select)
                result_list.append(frame)

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
                db = database.Database(username_entry.get(), password_entry.get())
            except pymysql.err.OperationalError:
                error_label = ttk.Label(login_frame, text="Invalid Credentials", font=("Arial", 15))
                error_label.place(x=600, y=200)
                print("hi")
            except:
                print("poggers")
            else:
                # on successful login, destroy login frame and call function to open landing page
                login_frame.destroy()
                root.after(0, open_landing())

        button = ttk.Button(login_frame, text="Log In", command=login)
        button.place(x=625, y=370)
        root.mainloop()
    open_login()
