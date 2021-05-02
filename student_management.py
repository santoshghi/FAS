import tkinter as tk
import cv2
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import re
import datetime


class student_mgmt:
    def __init__(self, parent):
        self.student_window = parent
        self.student_window.title('SMS')
        self.student_window.grab_set()
        # self.student_window.wm_attributes('-alpha', 0.5)
        # self.window.geometry('1186x645+100+200')
        self.student_window.geometry('1500x700+100+100')
        self.student_window.resizable(False, False)

        # images
        self.bg_image = Image.open('images/sms_images/sms_background.jpg')
        self.resize = self.bg_image.resize((1500, 800), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.resize)

        # Variables
        self.rollno = tk.StringVar()
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.year = tk.StringVar()
        self.contact = tk.StringVar()
        self.address = tk.StringVar()
        self.gender = tk.StringVar()
        self.dob = tk.StringVar()

        self.searchtxt = tk.StringVar()

        # labels and entries
        bg_lable = tk.Label(self.student_window, image=self.bg_image).place(x=0, y=0)

        top_title = tk.Label(self.student_window, text="Students Management System", font=("Verdana 15 underline", 25, 'bold'), relief=tk.RAISED, fg='brown').place(x=0,
                                                                                                                                                                    y=0,
                                                                                                                                                                    relwidth=1)

        student_statusBar = tk.Label(self.student_window, text='Developed by @santosh ghimire.....', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        student_statusBar.pack(side=tk.BOTTOM, fill=tk.X)

        frame = tk.Frame(self.student_window, bg='light gray')
        frame.place(x=10, y=50)
        down_title = tk.Label(frame, text='Manage Students', padx=200, pady=10, font=('Brother Deluxe 1350 Font', 20, 'bold', 'underline'), justify=tk.CENTER,
                              bg='light gray').grid(row=0, columnspan=2)

        rol_lable = tk.Label(frame, text='Student_Id', bg='light gray', font=("times new roman", 15, "bold")).grid(row=1, column=0, sticky='w', padx=50, pady=15)
        rol_entry = tk.Entry(frame, textvariable=self.rollno, bd=2, relief=tk.GROOVE, font=("", 13))
        rol_entry.grid(row=1, column=1, padx=10, sticky='w')

        name_lable = tk.Label(frame, text='Name', bg='light gray', font=("times new roman", 15, "bold")).grid(row=2, column=0, sticky='w', padx=50, pady=15)
        name_entry = tk.Entry(frame, textvariable=self.name, bd=2, relief=tk.GROOVE, font=("", 13))
        name_entry.grid(row=2, column=1, padx=10, sticky='w')

        email_lable = tk.Label(frame, text='Email', bg='light gray', font=("times new roman", 15, "bold")).grid(row=3, column=0, sticky='w', padx=50, pady=15)
        email_entry = tk.Entry(frame, textvariable=self.email, bd=2, relief=tk.GROOVE, font=("", 13))
        email_entry.grid(row=3, column=1, padx=10, sticky='w')

        year_lable = tk.Label(frame, text='Admission Year', bg='light gray', font=("times new roman", 15, "bold")).grid(row=4, column=0, sticky='w', padx=50, pady=15)
        combo_year = ttk.Combobox(frame, font=("times new roman", 13, "bold"), textvariable=self.year, cursor='hand2',
                                  values=['2073', '2074', '2075', '2076', '2077', '2078', '2079', '2080'], state='readonly').grid(row=4, column=1, padx=10, sticky='w')

        gender_lable = tk.Label(frame, text='Gender', bg='light gray', font=("times new roman", 15, "bold")).grid(row=5, column=0, sticky='w', padx=50, pady=15)
        combo_gender = ttk.Combobox(frame, font=("times new roman", 13, "bold"), textvariable=self.gender, cursor='hand2', values=['Male', 'Female', 'Others'],
                                    state='readonly').grid(row=5, column=1, padx=10, sticky='w')

        contact_lable = tk.Label(frame, text='Contact No.', bg='light gray', font=("times new roman", 15, "bold")).grid(row=6, column=0, sticky='w', padx=50, pady=15)
        contact_entry = tk.Entry(frame, textvariable=self.contact, bd=2, relief=tk.GROOVE, font=("", 13))
        contact_entry.grid(row=6, column=1, padx=10, sticky='w')

        dob_lable = tk.Label(frame, text='Date Of Birth(dd-mm-yyyy)', bg='light gray', font=("times new roman", 15, "bold")).grid(row=7, column=0, sticky='w', padx=50,
                                                                                                                                  pady=15)
        dob_entry = tk.Entry(frame, textvariable=self.dob, bd=2, relief=tk.GROOVE, font=("", 13))
        dob_entry.grid(row=7, column=1, padx=10, sticky='w')

        address_label = tk.Label(frame, text='Address', bg='light gray', font=("times new roman", 15, "bold")).grid(row=8, column=0, sticky='w', padx=50, pady=15)
        address_entry = tk.Entry(frame, textvariable=self.address, bd=2, relief=tk.GROOVE, font=("", 13))
        address_entry.grid(row=8, column=1, padx=10, sticky='w')

        # buttons
        button_frame = tk.Frame(self.student_window, bg='light gray')
        button_frame.place(x=10, y=565)

        add_button = tk.Button(button_frame, text='Add', cursor='hand2', bd=2, width=10, command=self.add_students, relief=tk.GROOVE, activebackground='light pink',
                               bg='light blue', font=("times new roman", 13, 'bold', 'underline')).grid(row=0, column=0, padx=12, pady=7, ipadx=10, ipady=10)
        update_button = tk.Button(button_frame, text='Update', cursor='hand2', bd=2, width=10, command=self.update, relief=tk.GROOVE, activebackground='light pink',
                                  bg='light blue', font=("times new roman", 13, 'bold', 'underline')).grid(row=0, column=1, padx=12, pady=7, ipadx=10, ipady=10)
        delete_button = tk.Button(button_frame, text='Delete', cursor='hand2', bd=2, width=10, command=self.delete_data, relief=tk.GROOVE, activebackground='light pink',
                                  bg='light blue', font=("times new roman", 13, 'bold', 'underline')).grid(row=0, column=2, padx=12, pady=7, ipadx=10, ipady=10)
        dataset_button = tk.Button(button_frame, text='Take Sample Face', cursor='hand2', bd=2, command=self.generate_dataset, width=10, relief=tk.GROOVE,
                                   activebackground='light pink', bg='light blue', font=("times new roman", 13, 'bold', 'underline')).grid(row=0, column=3, pady=7,
                                                                                                                                           padx=12, ipadx=16, ipady=10)

        #  details frame
        details_frame = tk.Frame(self.student_window, bg='light gray')
        details_frame.place(x=690, y=50, width=800, height=585)

        lbl_search_entry = tk.Entry(details_frame, textvariable=self.searchtxt, width=50, font=("times new roman", 13, 'bold'), cursor='pencil').grid(row=0, column=0,
                                                                                                                                                      sticky='w', padx=10,
                                                                                                                                                      pady=20, ipadx=5,
                                                                                                                                                      ipady=5)
        search_button = tk.Button(details_frame, text='Search', command=self.search_data, bg='light gray', activebackground='light pink', cursor='hand2').grid(row=0,
                                                                                                                                                               column=1,
                                                                                                                                                               ipadx=5,
                                                                                                                                                               ipady=5)
        showall_button = tk.Button(details_frame, text='Show All', command=self.fetch_data, bg='light gray', activebackground='light pink', cursor='hand2').grid(row=0,
                                                                                                                                                                 column=2,
                                                                                                                                                                 sticky='w',
                                                                                                                                                                 padx=30,
                                                                                                                                                                 pady=20,
                                                                                                                                                                 ipadx=5,
                                                                                                                                                                 ipady=5)

        # table frame
        table_frame = tk.Frame(details_frame, bg='white', relief=tk.GROOVE, bd=4)
        table_frame.place(x=10, y=70, width=780, height=505)

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=('Student Id', 'Name', 'Email', 'Year Of Admission', 'Gender', 'Contact No', 'D.O.B', 'Address'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('Student Id', text='Student Id')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Year Of Admission', text='Year Of Admission')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Contact No', text='Contact No')
        self.student_table.heading('D.O.B', text='D.O.B')
        self.student_table.heading('Address', text='Address')
        self.student_table['show'] = 'headings'
        self.student_table.pack(fill=tk.BOTH, expand=1)

        self.student_table.bind('<ButtonRelease-1>', self.get_selected_row)  # To get the value in the form
        self.fetch_data()

    # Functions
    ################### Validations Functions #####################
    def validate_studentID(self):
        student_id = self.rollno.get()
        if student_id.isdigit():
            return True
        else:
            messagebox.showwarning('Warning', 'invalid student_id Or contact_no, it most be a number!!', parent=self.student_window)
            return False

    def validate_contact(self):
        student_id = self.contact.get()
        if student_id.isdigit():
            return True
        else:
            messagebox.showwarning('Warning', 'invalid student_id Or contact_no, it most be a number!!', parent=self.student_window)
            return False

    def validate_email(self, email):
        email_format = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(email_format, email)):
            return True
        else:
            messagebox.showwarning('Warning', 'Invalid Email!!!', parent=self.student_window)
            return False

    def validate_name(self, name):
        name_format = '[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,20}$'
        if (re.search(name_format, name)):
            return True
        else:
            messagebox.showwarning('Warning', 'Invalid Name!!!', parent=self.student_window)
            return False

    def validate_address(self, address):
        name_format = '[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,20}$'
        if (re.search(name_format, address)):
            return True
        else:
            messagebox.showwarning('Warning', 'Invalid Address!!!')
            return False

    ################################################ Functions #########
    def add_students(self):
        if self.rollno.get() == "" or self.name.get() == "" or self.email.get() == "" or self.year.get() == "" or self.gender.get() == "" or self.contact.get() == "" or self.dob.get() == "" or self.address.get() == "":
            messagebox.showerror('Error', 'All field are required!!!', parent=self.student_window)
        else:
            get_studentID = (self.validate_studentID())
            get_contact = (self.validate_contact())
            if get_studentID:
                if get_contact:
                    get_name = (self.name.get())
                    name = (self.validate_name(get_name))
                    if name:
                        get_address = (self.address.get())
                        address = (self.validate_address(get_address))
                        if address:
                            con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
                            cursor = con.cursor()

                            query = 'select Student_ID from sms_table'
                            cursor.execute(query)
                            column = cursor.fetchall()
                            tup = int(self.rollno.get(), )
                            temp = False
                            for x in column:
                                if tup in x:
                                    temp = True
                                # print(x)

                            if temp:
                                messagebox.showerror('Error', 'Duplicate Student_ID !!!', parent=self.student_window)
                                con.close()

                            else:
                                get_email = (self.email.get())
                                email = (self.validate_email(get_email))
                                # print(a)
                                # print(b)
                                if email:
                                    get_date = str(self.dob.get())
                                    format = '%d-%m-%Y'
                                    try:
                                        validate = datetime.datetime.strptime(get_date, format)
                                    except ValueError:
                                        messagebox.showwarning('Warnning', 'Invalid D.O.B Format', parent=self.student_window)
                                        return False
                                    con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
                                    cursor = con.cursor()
                                    cursor.execute("insert into sms_table values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.rollno.get(),
                                                                                                             self.name.get(),
                                                                                                             self.email.get(),
                                                                                                             self.year.get(),
                                                                                                             self.gender.get(),
                                                                                                             self.contact.get(),
                                                                                                             self.dob.get(),
                                                                                                             self.address.get()))
                                    con.commit()
                                    self.fetch_data()
                                    self.clear()
                                    con.close()
                                    messagebox.showinfo('message', 'Records has been successfully Added', parent=self.student_window)

                # else:
                #     messagebox.showwarning("Warning", "Invalid Data Found, Please Enter Vaild Data!!!")
                #     return False

    def fetch_data(self):
        con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
        cursor = con.cursor()
        cursor.execute('select * from sms_table')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', tk.END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.rollno.set('')
        self.name.set('')
        self.email.set('')
        self.year.set('')
        self.gender.set('')
        self.dob.set('')
        self.contact.set('')
        self.address.set('')

    def get_selected_row(self, event):
        selected_row = self.student_table.focus()
        contents = self.student_table.item(selected_row)
        row = contents['values']
        self.rollno.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.year.set(row[3])
        self.gender.set(row[4])
        self.contact.set(row[5])
        self.dob.set(row[6])
        self.address.set(row[7])

    def update(self):
        if self.rollno.get() == "" or self.name.get() == "" or self.email.get() == "" or self.year.get() == "" or self.gender.get() == "" or self.contact.get() == "" or self.dob.get() == "" or self.address.get() == "":
            messagebox.showerror('Error', 'Please select the Data Row!!!', parent=self.student_window)
        else:
            con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
            cursor = con.cursor()
            cursor.execute("update sms_table set Name=%s, Email=%s, Year_Of_Admission=%s, Gender=%s, Contact_No=%s, DOB=%s, Address=%s where Student_ID=%s",
                           (self.name.get(),
                            self.email.get(),
                            self.year.get(),
                            self.gender.get(),
                            self.contact.get(),
                            self.dob.get(),
                            self.address.get(),
                            self.rollno.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Message", 'Record has been successfully Updated...', parent=self.student_window)

    def delete_data(self):
        if self.rollno.get() == "" or self.name.get() == "" or self.email.get() == "" or self.year.get() == "" or self.gender.get() == "" or self.contact.get() == "" or self.dob.get() == "" or self.address.get() == "":
            messagebox.showerror('Error', 'Please select the Data you want to delete!!!', parent=self.student_window)
        else:
            con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
            cursor = con.cursor()
            cursor.execute("delete from sms_table where Student_ID=%s", (self.rollno.get(),))
            con.commit()
            con.close()
            messagebox.showinfo('Message', 'Record has been successfully Deleted...', parent=self.student_window)
            self.fetch_data()
            self.clear()

    def search_data(self):
        self.clear()
        if self.searchtxt.get() == "":
            messagebox.showerror('Error', 'Please enter the valid name you want to Search!!!', parent=self.student_window)

        else:
            con = mysql.connector.connect(host='localhost', database='sms', user='root', password='S9843529908')
            cursor = con.cursor()

            cursor.execute("SELECT *" + " FROM sms_table WHERE Name LIKE (%s)", ('%' + self.searchtxt.get() + '%',))
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('', tk.END, values=row)
                    con.commit()
            con.close()

    def generate_dataset(self):
        id = self.rollno.get()
        if self.rollno.get() == "" or self.name.get() == "" or self.email.get() == "" or self.year.get() == "" or self.gender.get() == "" or self.contact.get() == "" or self.dob.get() == "" or self.address.get() == "":
            messagebox.showerror('Error', 'All Fields Are Required With Valid ID!!!', parent=self.student_window)

        else:
            if id == self.rollno.get():
                # url = "http://192.168.1.81:8080"
                # video = cv2.VideoCapture(url + '/video')
                video = cv2.VideoCapture(0)
                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def crop_face(image):
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)

                    for x, y, w, h in faces:
                        cropped_face = image[y:y + h, x:x + w]
                        return cropped_face

                a = 0
                id = id
                while True:
                    check, frame = video.read()

                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # faces = face_cascade.detectMultiScale(gray, 1.3, 3)
                    # for (x,y,w,h) in faces:
                    #     a+=1
                    #     file_path = ('/home/santosh/PycharmProjects/FacialAttendance/samplefaces/x.' +str(id) +'.'+ str(a) + '.jpg')
                    #
                    #     cv2.imwrite(file_path, gray[y:y+h, x:x+w])
                    #     cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                    # cv2.imshow('Taking Sample', frame)
                    # key = cv2.waitKey(1)
                    # if key == ord('q') or a == 100:
                    #         break
                    # video.release()
                    # cv2.destroyAllWindows()
                    # messagebox.showinfo('Message', 'Collecting sample face completed!!')

                    if crop_face(frame) is not None:
                        a += 1
                        face = cv2.resize(crop_face(frame), (400, 400))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_path = ('/home/santosh/Desktop/Project/FacialAttendance/samplefaces/face.' + str(id) + '.' + str(a) + '.jpg')
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(a), (20, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0))
                        cv2.imshow('Taking Sample face', face)

                        key = cv2.waitKey(1)
                        if key == ord('q') or a == 50:
                            break

                video.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Message', 'Collecting sample face completed!!', parent=self.student_window)

            else:
                messagebox.showerror('Error', 'Please Enter Valid Student_Id!!!', parent=self.student_window)


def show():
    student_window = tk.Toplevel()
    student_mgmt(student_window)
    student_window.mainloop()

# show()
