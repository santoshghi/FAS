import tkinter as tk
from tkinter import *

# import pyttsx3
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

global flag


class Login_system():
    def __init__(self, window):
        self.window = window
        self.window.title("Login System")
        self.window.geometry("1600x900+0+0")
        self.window.resizable(False, False)

        # images
        self.bg_icon = ImageTk.PhotoImage(Image.open("images/loginbackground.jpg"))
        self.user_icon = tk.PhotoImage(file="images/user.png")
        self.pass_icon = ImageTk.PhotoImage(Image.open("images/passwd.jpeg"))
        self.logo_icon = ImageTk.PhotoImage(Image.open("images/logo.png"))
        self.login_icon = ImageTk.PhotoImage(Image.open("images/loginbutton.jpeg"))

        # variable
        self.uname = tk.StringVar()
        self.passd = tk.StringVar()

        bg_label = tk.Label(self.window, image=self.bg_icon).place(x=0, y=0, relwidth=1, relheight=1)

        title = tk.Label(self.window, text="Login To Facial Attendance System(FAS)!!", justify=tk.CENTER, font=("times new roman", 40, "bold"), fg="green",
                         bg="light gray", bd=5, relief=tk.GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = tk.Frame(self.window, bg="white")
        Login_Frame.place(x=550, y=150)

        logolbl = tk.Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=15)

        lbluser = tk.Label(Login_Frame, text="Username", image=self.user_icon, compound=tk.LEFT, font=("times new roman", 20, "bold"), bg="white").grid(row=1, column=0,
                                                                                                                                                        padx=20, pady=5)
        txtuser = tk.Entry(Login_Frame, textvariable=self.uname, bd=2, relief=tk.GROOVE, font=("", 15)).grid(row=1, column=1, padx=20)

        lblpass = tk.Label(Login_Frame, text="Password", image=self.pass_icon, compound=tk.LEFT, font=("times new roman", 20, "bold"), bg="white").grid(row=2, column=0,
                                                                                                                                                        padx=20, pady=5)
        txtpass = tk.Entry(Login_Frame, textvariable=self.passd, show='*', bd=2, relief=tk.GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log = tk.Button(Login_Frame, image=self.login_icon, bg="gray", bd=0, cursor='hand2', command=self.login, activebackground="gold").grid(row=3, columnspan=2,
                                                                                                                                                   pady=5)
        login_statusBar = tk.Label(window, text='Developed by @santosh ghimire.....', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        login_statusBar.pack(side=tk.BOTTOM, fill=tk.X)

        window.bind('<Return>', self.login)

    def login(self, event=''):

        if self.uname.get() == "" or self.passd.get() == "":
            messagebox.showerror("Error", "All fields are required!!")

        else:
            con = mysql.connector.connect(
                host='localhost',
                database='login_FAS',
                user='root',
                password='S9843529908'
            )
            # print(con)
            cursor = con.cursor()
            cursor.execute("select * from login where password=%s AND name=%s", (self.passd.get(), self.uname.get()))
            result = cursor.fetchone()
            # print(result)
            if result:
                global flag
                flag = True

                message = messagebox.askquestion("Login Successful!!", "Do you want to continue?")
                if message == 'yes':
                    self.window.destroy()

            else:
                self.clear()
                messagebox.showerror("Error", "Invalid Username or Password ??")
            con.commit()
            con.close()

    def clear(self):
        self.uname.set('')
        self.passd.set('')


window = tk.Tk()
obj = Login_system(window)
window.mainloop()

