import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image
import cv2
import os
from tkinter import messagebox

def training_classifier(data_dir):
    def click():
        import time
        for i in range(1, 100, 1):
            progress['value'] = i
            win.update_idletasks()
            label.config(text=str(i) + '%')
            time.sleep(.03)
        progress['value'] = 100
        win.destroy()

    win = tk.Toplevel()
    win.geometry('1000x80+350+300')
    win.resizable(False, False)

    label = tk.Label(win, font='arial 15 bold')
    label.pack(padx=10)
    progress = ttk.Progressbar(win, length=1000, mode='determinate', value=0)
    progress.pack(padx=10)
    win.title('Training Data..')

    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    # print(path)
    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split('.')[1])
        # print(id)
        # print(imageNp)
        faces.append(imageNp)
        ids.append(id)
    ids = np.array(ids)

    classifier1 = cv2.face.LBPHFaceRecognizer_create()
    # print(classifier)

    # labels = np.random.randint(1, size=len(faces))
    # print(labels)

    # classifier1.train(faces,np.array(labels))
    classifier1.train(faces, ids)
    classifier1.write('classifier.yml')

    click()
    messagebox.showinfo('Message', 'Train Successfully!!!')
    win.mainloop()
# training_classifier('samplefaces')
