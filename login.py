import tkinter as tk
from tkinter import *
from tkinter import ttk


def openLogin():
    root = Tk()
    root.geometry("1280x720")
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    # username text box
    username_entry = ttk.Entry(root, width=40)
    username_entry.place(x=550, y=280)
    # password text box
    password_entry = ttk.Entry(root, width=40, show='*')
    password_entry.place(x=550, y=320)
    # username label text
    username_label = ttk.Label(root, text="Username:")
    username_label.place(x=480, y=280)
    # password label text
    password_label = ttk.Label(root, text="Password:")
    password_label.place(x=480, y=320)
    # top welcome text
    welcome_label = ttk.Label(root, text="Welcome to Patient Information Management", font=("Arial", 35))
    welcome_label.place(x=200, y=100)

    # TODO: change the prints to database query logic when database is working
    # function that runs when Log In button is pressed - should eventually
    # query database and either display error message or move to landing page
    def login():
        print(username_entry.get())
        username_entry.delete(first=0, last=tk.END)
        print(password_entry.get())
        password_entry.delete(first=0, last=tk.END)

    button = ttk.Button(root, text="Log In", command=login)
    button.place(x=625, y=370)
    root.mainloop()
