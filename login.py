import tkinter as tk
from tkinter import *
from tkinter import ttk


def openLogin():
    root = Tk()
    root.geometry("1280x720")
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    usernameEntry = ttk.Entry(root, width=40)
    usernameEntry.place(x=550, y=280)
    passwordEntry = ttk.Entry(root, width=40, show='*')
    passwordEntry.place(x=550, y=320)
    usernameLabel = ttk.Label(root, text="Username:")
    usernameLabel.place(x=480, y=280)
    passwordLabel = ttk.Label(root, text="Password:")
    passwordLabel.place(x=480, y=320)
    welcomeLabel = ttk.Label(root, text="Welcome to Patient Information Management", font=("Arial", 35))
    welcomeLabel.place(x=200, y=100)

    def login():
        print(usernameEntry.get())
        usernameEntry.delete(first=0, last=tk.END)
        print(passwordEntry.get())
        passwordEntry.delete(first=0, last=tk.END)

    button = ttk.Button(root, text="Log In", command=login)
    button.place(x=625, y=370)
    root.mainloop()


