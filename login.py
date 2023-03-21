import tkinter as tk
from tkinter import *
from tkinter import ttk


def run_gui():
    root = Tk()
    root.title("Patient Information Management")
    root.geometry("1280x720")
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
        # todo: fix the placing of this button idfk

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
            print('bye')
            search_frame.destroy()
            results_frame.destroy()
            buttons_frame.destroy()
            open_login()
            # todo: also delete account info
        logout_button = ttk.Button(buttons_frame, text='Log Out', command=log_out)
        logout_button.pack(anchor='w', side=LEFT, padx=20)

        def patient_select(e):
            # todo: make this go to patient page
            print('click')

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
            print(username_entry.get())
            username_entry.delete(first=0, last=tk.END)
            print(password_entry.get())
            password_entry.delete(first=0, last=tk.END)
            if 1:
                # on successful login, destroy login frame and call function to open landing page
                login_frame.destroy()
                root.after(0, open_landing())

        button = ttk.Button(login_frame, text="Log In", command=login)
        button.place(x=625, y=370)
        root.mainloop()
    open_login()
