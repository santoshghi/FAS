import tkinter as tk
from PIL import ImageTk, Image
# from tkinter import messagebox
import student_management
import train_classifier
import faceRecognition
import open_dataset
import student_report
from login import flag
from tkinter import ttk
import time


if flag:
    class dashboardWindow(object):
        def __init__(self,dash_window):

            self.dash_window = dash_window
            self.dash_window.config(bg='gold')
            self.dash_window.title("Welcome To Facial Attendance System(FAS) Dashboard")
            self.dash_window.geometry("1300x866+200+100")
            self.dash_window.resizable(False,False)

            # images
            self.background_icon = ImageTk.PhotoImage(Image.open('images/dash_board_images/dashboard_background.jpg'))

            self.sms_icon = Image.open('images/dash_board_images/sms.png')
            self.resize = self.sms_icon.resize((366, 360), Image.ANTIALIAS)
            self.sms_icon = ImageTk.PhotoImage(self.resize)

            self.training_icon = Image.open('images/dash_board_images/training1.jpeg')
            self.resize = self.training_icon.resize((366, 360), Image.ANTIALIAS)
            self.training_icon = ImageTk.PhotoImage(self.resize)

            self.recognition_icon = Image.open('images/dash_board_images/face_recognition.jpeg')
            self.resize = self.recognition_icon.resize((366, 360), Image.ANTIALIAS)
            self.recognition_icon = ImageTk.PhotoImage(self.resize)

            self.dataset_icon = Image.open('images/dash_board_images/dataset.jpg')
            self.resize = self.dataset_icon.resize((366, 360), Image.ANTIALIAS)
            self.dataset_icon = ImageTk.PhotoImage(self.resize)

            self.report_icon =Image.open('images/dash_board_images/report2.png')
            self.resize = self.report_icon.resize((366, 360), Image.ANTIALIAS)
            self.report_icon = ImageTk.PhotoImage(self.resize)

            self.exit_icon = Image.open('images/dash_board_images/exit.png')
            self.resize = self.exit_icon.resize((366, 360), Image.ANTIALIAS)
            self.exit_icon = ImageTk.PhotoImage(self.resize)


            dash_label = tk.Label(self.dash_window, image=self.background_icon).place(x=0,y=0, relwidth=1, relheight=1)

            dash_frame = tk.Frame(self.dash_window)
            dash_frame.place(x=100, y=20)


            button_sms = tk.Button(dash_frame, image=self.sms_icon, command=self.sms_open, cursor='hand2', relief=tk.GROOVE, bd=3, activebackground='dark red').grid(row=0, column=0)

            button_train = tk.Button(dash_frame, image=self.training_icon, command=self.train, cursor='hand2', relief=tk.GROOVE, bd=3, activebackground='dark red').grid(row=0, column=1)

            button_recognize = tk.Button(dash_frame, image=self.recognition_icon, command=self.face_recognize, cursor='hand2', relief=tk.GROOVE, bd=3, activebackground='dark red').grid(row=0, column=2)

            dash_frame1 = tk.Frame(self.dash_window)
            dash_frame1.place(x=100, y=396)

            button_dataset = tk.Button(dash_frame1, image=self.dataset_icon, command=self.dataset, cursor='hand2', relief=tk.GROOVE, bd=3, activebackground='dark red').grid(row=1, column=0)

            button_report = tk.Button(dash_frame1, image=self.report_icon, command=self.report, cursor='hand2', relief=tk.GROOVE, bd=3, activebackground='dark red').grid(row=1, column=1)

            button_exit = tk.Button(dash_frame1, image=self.exit_icon, cursor='hand2', relief=tk.GROOVE, bd=3, command=self.exit, activebackground='dark red').grid(row=1, column=2)

        # Functions
        def click(self):
            # my_progress['value'] += 20
            # my_progress.start(10)
            my_progress = ttk.Progressbar(parent=dash_window, orient=tk.HORIZONTAL, length=300, mode='determinate')
            my_progress.pack(side=tk.TOP)
            for x in range(10):
                my_progress['value'] += 10
                dash_window.update_idletasks()
                time.sleep(1)

        def exit(self):
            self.dash_window.destroy()


        def sms_open(self):
            student_management.show()

        def train(self):
            train_classifier.training_classifier('samplefaces')

        def face_recognize(self):
            faceRecognition.faceRecog()

        def dataset(self):
            x = open_dataset.opendataset()

        def report(self):
            student_report.report()


    dash_window = tk.Tk()
    dash_board = dashboardWindow(dash_window)
    dash_window.mainloop()

# else:
#     messagebox.showerror('Error', 'Login Error')