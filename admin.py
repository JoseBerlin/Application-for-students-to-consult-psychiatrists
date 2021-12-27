
from tkinter import *

import pymysql
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import admin_home


def Admin(self):
    self.root.title("Admin")

    frame_admin=Frame(self.root,bg="White")
    frame_admin.place(x=0,y=0,width=1366,height=700)

    btn2 = Button(frame_admin, text="Logout", command=self.loginform, cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)

    btn2.place(x=1000, y=10)

    Button(frame_admin, text="Manage patient", font=("Times new roman",34),bg="#1E94DC",fg='white', command=admin_home.admin_Patients(self.root).now).place(x=200, y=100, height=100, width=400)
    Button(frame_admin, text="Manage Psychiatrist",bg="#1E94DC",fg='white', command=admin_home.admin_Patients(self.root).now1, font=("Times new roman", 34)).place(x=700, y=100, height=100, width=400)
    Button(frame_admin, text="Request from Psychiatrists",bg="#1E94DC",fg='white', command=admin_home.admin_Patients(self.root).now2, font=("Times new roman", 34)).place(x=325, y=300, height=100, width=600)
