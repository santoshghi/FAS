import subprocess
import sys
from tkinter import filedialog

def opendataset():

    filename = filedialog.askopenfilename(initialdir="/home/santosh/PycharmProjects/FacialAttendance/samplefaces",
                                          title="Dataset", filetypes=[('jpg files', '*.jpg'), ('All files', '*.*')])

    imageViewer = {'linux': 'xdg-open',
                   'win64': 'eog',
                   'darwin': 'open'}[sys.platform]
    subprocess.run([imageViewer, filename])

# opendataset()
