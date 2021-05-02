import subprocess
import mysql.connector
from tkinter import filedialog


def report():
    con = mysql.connector.connect(
        host='localhost',
        database='sms',
        user='root',
        password='S9843529908'
    )
    cursor = con.cursor()
    fetch_data_query = ('SELECT sms_table.Student_ID as SI, sms_table.Name, sms_table.Year_of_Admission, sms_table.Gender, sms_table.Contact_No, sms_table.Address, face.Date, face.Time, face.Status  FROM sms_table LEFT JOIN face ON face.Student_ID = sms_table.Student_ID')
    cursor.execute(fetch_data_query)
    column = cursor.fetchall()
    # print(column)
    file = open('Student_Attendance.csv', 'w')
    header = "Student_ID, Name, Year_of_Admission, Gender, Contact_No, Address, Date, Time, Status"

    with open('Student_Attendance.csv', 'a'):
        file.write(header + "\n")

    for row in column:
        # print(row)
        file.write(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + ',' + str(row[7]) + ',' + str(
            row[8]) + ',' + '\n')

    file.close()
    cursor.close()
    con.close()

    filename = filedialog.askopenfilename(initialdir="/home/santosh/PycharmProjects/FacialAttendance", title="Report",
                                          filetypes=[('csv files', '*.csv'), ('All files', '*.*')])
    subprocess.call(('xdg-open', filename))

# report()
