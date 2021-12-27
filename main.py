import tkinter as Tk
import mysql.connector
from tkinter import *
from datetime import *

import admin
import predict
import patient_home
import psychiatrist_home
import psychiatrist_pending
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import DSM5


class Login:

    def __init__(self, root):

        self.root = root

        self.root.title("Psychiatrist for students")

        self.root.geometry("1200x700")

        # self.root.resizable(False, False)

        self.loginform()
        self.name = ""
        self.email = ""

        self.profession = StringVar()
        self.name1 = StringVar()
        self.age1 = StringVar()
        self.gender1 = StringVar()
        self.email1 = StringVar()
        self.contact1 = StringVar()
        self.suggested_psychiatrist1 = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.totalrecord = StringVar()

    def loginform(self):

        self.root.title("Login")

        Frame_login = Frame(self.root, bg="white")

        Frame_login.place(x=0, y=0, height=800, width=1366)

        canvas = tk.Canvas(Frame_login, width=1366, height=800)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("Images/Form.png").resize((1366, 800), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.Frame_input = Frame(self.root, bg='white')

        self.Frame_input.place(x=320, y=130, height=450, width=350)

        label1 = Label(self.Frame_input, text="Login Here", font=('impact', 32, 'bold'),

                       fg="black", bg='white')

        label1.place(x=75, y=20)

        label2 = Label(self.Frame_input, text="E-mail", font=("Goudy old style", 20, "bold"),

                       fg='orangered', bg='white')

        label2.place(x=30, y=95)

        self.email_txt = Entry(self.Frame_input, font=("times new roman", 15, "bold"),

                               bg='lightgray')

        self.email_txt.place(x=30, y=145, width=270, height=35)

        label3 = Label(self.Frame_input, text="Password", font=("Goudy old style", 20, "bold"),

                       fg='orangered', bg='white')

        label3.place(x=30, y=195)

        self.password = Entry(self.Frame_input, font=("times new roman", 15, "bold"),

                              bg='lightgray', show='*')

        self.password.place(x=30, y=245, width=270, height=35)

        # btn1 = Button(self.Frame_input, text="forgot password?", cursor='hand2',
        #
        #               font=('calibri', 10), bg='white', fg='black', bd=0)
        #
        # btn1.place(x=125, y=305)

        btn2 = Button(self.Frame_input, text="Login", command=self.login, cursor="hand2",

                      font=("times new roman", 15), fg="white", bg="orangered",

                      bd=0, width=15, height=1)

        btn2.place(x=90, y=340)

        btn3 = Button(self.Frame_input, command=self.Register, text="Not Registered?register"

                      , cursor="hand2", font=("calibri", 10), bg='white', fg="black", bd=0)

        btn3.place(x=110, y=390)

    def login(self):

        if self.email_txt.get() == "" or self.password.get() == "":

            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:

                con = pymysql.connect(host='localhost', user='root', password='JBjose', database='pys')

                cur = con.cursor()
                cur.execute("set sql_safe_updates=0")
                cur.execute('select * from register where email=%s and password=%s'
                            , (self.email_txt.get(), self.password.get(),))

                row = cur.fetchone()
                con.commit()
                cur.execute("select * from dsm_stu_answers where stu_mail=%s", (self.email_txt.get(),))
                row1 = cur.fetchone()

                if row == None:

                    messagebox.showerror('Error', 'Invalid email And Password'

                                         , parent=self.root)

                    # self.loginclear()

                    self.email_txt.focus()

                else:
                    if row[0] == "student" and row[4] == 0:
                        self.name = row[1]
                        self.email = row[3]
                        if row1 == None:
                            DSM5.f01(self)
                            self.loginclear()
                        else:
                            self.Form()
                            self.loginclear()
                    elif row[0] == "student" and row[4] == 1:
                        self.name = row[1]
                        self.email = row[3]
                        # patient_home.Home(self)
                        patient_home.Patient_home(self)
                        self.loginclear()
                    elif row[0] == "psychiatrist" and row[4] == 0:
                        self.name = row[1]
                        self.email = row[3]
                        self.Form1()
                        self.loginclear()
                    elif row[0] == "psychiatrist" and row[4] == 1:
                        self.name = row[1]
                        self.email = row[3]
                        psychiatrist_pending.psy_pending(self)
                        self.loginclear()
                    elif row[0] == "psychiatrist" and row[4] == 2:
                        self.name = row[1]
                        self.email = row[3]
                        psychiatrist_home.Psychiatrist_home(self)
                        self.loginclear()
                    elif row[0] == "psychiatrist" and row[4] == 3:
                        self.name = row[1]
                        self.email = row[3]
                        psychiatrist_pending.psy_rejected(self)
                        self.loginclear()
                    elif row[0] == "admin":
                        self.name = row[1]
                        self.email = row[3]
                        admin.Admin(self)
                        self.loginclear()
                        # patients.admin_Patients(self.root)
                    cur.close()
                    con.close()

            except Exception as es:

                messagebox.showerror('Error m', f'Error Due to : {str(es)}'

                                     , parent=self.root)
                print(str(es))
            # finally:
            # self.email_txt.delete(0, END)
            # self.password.delete(0, END)

    def Register(self):

        self.root.title("Register")

        Frame_login1 = Frame(self.root, bg="white")

        Frame_login1.place(x=0, y=0, height=800, width=1366)

        canvas = tk.Canvas(Frame_login1, width=1366, height=800)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("Images/Form.png").resize((1366, 800), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # self.img = ImageTk.PhotoImage(file="background-2.jpg")

        # img = Label(Frame_login1, image=self.img).place(x=0, y=0, width=1366, height=700)

        frame_input2 = Frame(self.root, bg='white')

        frame_input2.place(x=320, y=130, height=500, width=630)

        label1 = Label(frame_input2, text="Register Here", font=('impact', 32, 'bold'),

                       fg="black", bg='white')

        label1.place(x=45, y=20)

        label2 = Label(frame_input2, text="Name", font=("Goudy old style", 20, "bold"),

                       fg='orangered', bg='white')

        label2.place(x=30, y=95)

        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"),

                           bg='lightgray')

        self.entry.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input2, text="Password", font=("Goudy old style", 20, "bold"),

                       fg='orangered', bg='white')

        label3.place(x=30, y=195)

        self.entry2 = Entry(frame_input2, font=("times new roman", 15, "bold"),

                            bg='lightgray',show='*')

        self.entry2.place(x=30, y=245, width=270, height=35)

        label4 = Label(frame_input2, text="Email-id", font=("Goudy old style", 20, "bold"),

                       fg='orangered', bg='white')

        label4.place(x=330, y=95)

        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"),

                            bg='lightgray')

        self.entry3.place(x=330, y=145, width=270, height=35)

        label5 = Label(frame_input2, text="Confirm Password",

                       font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')

        label5.place(x=330, y=195)

        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"),

                            bg='lightgray',show='*')

        self.entry4.place(x=330, y=245, width=270, height=35)

        label6 = Label(frame_input2, text="What profession?",

                       font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')

        label6.place(x=230, y=290)

        r1 = Radiobutton(frame_input2, text="Student", font=("Goudy old style", 20, "bold"),

                         variable=self.profession, value="student", tristatevalue=0,bg="White")

        r1.place(x=275, y=330)

        # r2 = Radiobutton(frame_input2, text="Parent", font=("Goudy old style", 10),
        #
        #                  variable=self.profession, value="parent", tristatevalue=0)
        #
        # r2.place(x=275, y=350)

        r3 = Radiobutton(frame_input2, text="Psychiatrist", font=("Goudy old style", 20, "bold"),

                         variable=self.profession, value="psychiatrist", tristatevalue=0,bg="white")

        r3.place(x=275, y=375)

        btn2 = Button(frame_input2, command=self.register, text="Register"

                      , cursor="hand2", font=("times new roman", 15), fg="white",

                      bg="orangered", bd=0, width=15, height=1)

        btn2.place(x=250, y=425)

        btn3 = Button(frame_input2, command=self.loginform,

                      text="Already Registered?Login", cursor="hand2",

                      font=("calibri", 10), bg='white', fg="black", bd=0)

        btn3.place(x=250, y=470)

    def register(self):

        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "" or self.profession.get() == "":

            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            # `print`(self.profession.get())

        elif '.' not in self.entry3.get() or '@' not in self.entry3.get():

            messagebox.showerror("Error", "Invalid E-mail format"

                                 , parent=self.root)

        elif self.entry2.get() != self.entry4.get():

            messagebox.showerror("Error", "Password and Confirm Password Should Be Same"

                                 , parent=self.root)

        else:

            try:
                con = mysql.connector.connect(host="localhost", user="root", password="JBjose",

                                              database="pys")

                cur = con.cursor()
                cur.execute("select * from register where email=%s"

                            , (self.entry3.get(),))

                row = cur.fetchone()

                if row != None:

                    messagebox.showerror("Error"

                                         , "User already Exist,Please try with another Email"

                                         , parent=self.root)

                    self.regclear()

                    self.entry.focus()

                else:
                    cur.execute("insert into register values(%s,%s,%s,%s,%s)"

                                , (self.profession.get(),

                                   self.entry.get(),

                                   self.entry2.get(),

                                   self.entry3.get(),

                                   int(0)))

                    con.commit()

                    con.close()

                    messagebox.showinfo("Registration Success", "Please login to fill the form"

                                        , parent=self.root)
                    self.loginform()

                    self.regclear()

            except Exception as es:

                messagebox.showerror("Error", f"Error due to:{str(es)}"

                                     , parent=self.root)
                print(str(es))

    def regclear(self):

        self.entry.delete(0, END)

        self.entry2.delete(0, END)

        self.entry3.delete(0, END)

        self.entry4.delete(0, END)

        self.profession.set("")

    def loginclear(self):

        self.email_txt.delete(0, END)

        self.password.delete(0, END)

    def Form(self):
        self.root.title("Personal details")

        Frame_login = Frame(self.root, bg="#333333")

        Frame_login.place(x=0, y=0, height=700, width=1366)

        # self.img = ImageTk.PhotoImage(file="Images/img.png")
        #
        # img = Label(Frame_login, image=self.img).place(x=0, y=0, height=700, width=1366)

        btn2 = Button(Frame_login, text="Logout", command=self.loginform, cursor="hand2",

                      font=("times new roman", 15), fg="white", bg="orangered",

                      bd=0, width=15, height=1)

        btn2.place(x=1000, y=10)

        label1 = Label(Frame_login, text="Personal details"

                       , font=('times new roman', 32, 'bold'),

                       fg="white", bg='#333333')

        label1.place(x=375, y=0)

        label2 = Label(Frame_login, text="Application form"

                       , font=('times new roman', 16, 'bold'),

                       fg="white", bg='#333333')

        label2.place(x=0, y=75)

        ## Frame question pg1
        frame_p1 = Frame(Frame_login, bg='#333333')
        frame_p1.place(x=0, y=120, height=500, width=1000)

        Label(frame_p1, text="Name:", font=('times new roman', 12), fg='white', bg='#333333').place(x=10, y=0)
        self.Name = Entry(frame_p1)
        self.Name.insert(END, self.name)
        self.Name.place(x=60, y=0)
        Label(frame_p1, text=self.name, font=('times new roman', 12), fg='black').place(x=60, y=0, width=150)
        Label(frame_p1, text="Age:", font=('times new roman', 12), fg='white', bg='#333333').place(x=210, y=0)
        self.Age = Entry(frame_p1)
        self.Age.place(x=260, y=0)
        Label(frame_p1, text="Gender:", font=('times new roman', 12), fg='white', bg='#333333').place(x=400, y=0)
        self.Gender = StringVar()
        Radiobutton(frame_p1, text="Male", variable=self.Gender, value="Male", tristatevalue="Age", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=460, y=0)
        Radiobutton(frame_p1, text="Female", variable=self.Gender, value="Female", tristatevalue="Age", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=540, y=0)
        # Radiobutton(frame_p1, text="Other", variable=self.Gender, value="Other", tristatevalue="Age", fg='#FAB647',
        #             bg='#333333', font=('times new roman', 13)).place(x=630, y=0)
        Label(frame_p1, text="Contact:", font=('times new roman', 12), fg='white', bg='#333333').place(x=730, y=0)
        self.contact = Entry(frame_p1)
        self.contact.place(x=800, y=0)

        label4 = Label(frame_p1, text="1]Physical health", font=('times new roman', 14), fg='white', bg='#333333')
        label4.place(x=10, y=30)

        self.present_health = StringVar()

        Radiobutton(frame_p1, text="Excellent", variable=self.present_health, value="0", tristatevalue="rb1",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=70)
        Radiobutton(frame_p1, text="Very Good", variable=self.present_health, value="4", tristatevalue="rb1",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=100, y=70)
        Radiobutton(frame_p1, text="Good", variable=self.present_health, value="2", tristatevalue="rb1", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=200, y=70)
        Radiobutton(frame_p1, text="Fair", variable=self.present_health, value="1", tristatevalue="rb1", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=300, y=70)
        Radiobutton(frame_p1, text="poor", variable=self.present_health, value="3", tristatevalue="rb1", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=400, y=70)
        label4 = Label(frame_p1, text="2] Mental Health", font=('times new roman', 14), fg='white', bg='#333333')
        label4.place(x=10, y=120)

        self.mental_health = StringVar()

        Radiobutton(frame_p1, text="Excellent", variable=self.mental_health, value="0", tristatevalue="rb2",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=160)
        Radiobutton(frame_p1, text="Very Good", variable=self.mental_health, value="4", tristatevalue="rb2",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=100, y=160)
        Radiobutton(frame_p1, text="Good", variable=self.mental_health, value="2", tristatevalue="rb2", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=200, y=160)
        Radiobutton(frame_p1, text="Fair", variable=self.mental_health, value="1", tristatevalue="rb2", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=300, y=160)
        Radiobutton(frame_p1, text="poor", variable=self.mental_health, value="3", tristatevalue="rb2", fg='#FAB647',
                    bg='#333333', font=('times new roman', 13)).place(x=400, y=160)
        label4 = Label(frame_p1, text="3] Smoking/Drugs usage (In a week)", font=('times new roman', 14), fg='white',
                       bg='#333333')
        label4.place(x=10, y=210)

        self.smoke_drug = StringVar()

        Radiobutton(frame_p1, text="Not at all", variable=self.smoke_drug, value="0", tristatevalue="rb3",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=250)
        Radiobutton(frame_p1, text="rare/1 or 2 days", variable=self.smoke_drug, value="1", tristatevalue="rb3",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=300)
        Radiobutton(frame_p1, text="several days", variable=self.smoke_drug, value="2", tristatevalue="rb3",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=350)
        Radiobutton(frame_p1, text="more than half days", variable=self.smoke_drug, value="3", tristatevalue="rb3",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=400)
        Radiobutton(frame_p1, text="Nearly every day", variable=self.smoke_drug, value="4", tristatevalue="rb3",
                    fg='#FAB647', bg='#333333', font=('times new roman', 13)).place(x=10, y=450)

        Button(Frame_login, text="Submit", state='normal', command=self.form,bg='#1E94DC',fg='white').place(x=500, y=645)

    def form(self):
        if self.Name.get() == "" or self.Age.get() == "" or self.Gender.get() == "" or self.present_health.get() == "" or self.mental_health.get() == "" or self.smoke_drug.get() == "" or self.contact.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="JBjose",

                                              database="pys")

                cur = con.cursor()
                cur.execute("select * from patient where patient_name=%s and contact=%s"

                            , (self.Name.get(), self.contact.get()))

                row = cur.fetchone()
                self.ML = StringVar()
                self.ML = predict.ml(int(self.present_health.get()), int(self.mental_health.get()),
                                     int(self.smoke_drug.get()))
                # print(self.ML,"\n",self.email)

                if row != None:

                    messagebox.showerror("Error", "Patient already Exist", parent=self.root)

                    self.form_clr()

                    self.contact.focus()

                else:
                    cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (str(self.Name.get()), str(self.Age.get()), str(self.Gender.get()), str(self.email),
                                 str(self.present_health.get()), str(self.mental_health.get()),
                                 str(self.smoke_drug.get()),
                                 str(self.contact.get()), str(self.ML),))
                    cur.execute("update register set form=1 where email=%s", (str(self.email),))

                    con.commit()

                    con.close()

                    messagebox.showinfo("Success", "Register Succesfull"

                                        , parent=self.root)

                    self.form_clr()
                    self.loginform()

            except Exception as es:

                messagebox.showerror("Error", f"Error due to:{str(es)}"

                                     , parent=self.root)
                print(str(es))

    def form_clr(self):
        self.Age.delete(0, END)
        self.Gender.set(0)
        self.contact.delete(0, END)
        self.present_health.set("")
        self.mental_health.set("")
        self.smoke_drug.set("")

    def Form1(self):
        self.root.title("Personal Details")
        psyc_frame = Canvas(self.root)
            # .place(x=0, y=0)
        img = ImageTk.PhotoImage(Image.open("Images/img_1.png").resize((1200, 700), Image.ANTIALIAS))
        psyc_frame.background=img
        bg = psyc_frame.create_image(0, 0, anchor=tk.NW, image=img)
        psyc_frame.place(x=0,y=0, height=700, width=1200)
        btn2 = Button(psyc_frame, text="Logout", command=self.loginform, cursor="hand2",

                      font=("times new roman", 15), fg="white", bg="orangered",

                      bd=0, width=15, height=1)
        btn2.grid(row=0,column=7,sticky=NE)
        # btn2.place(x=1000, y=10)
        Label(psyc_frame, text="Fill the form", font=("Times new roman", 32, "bold"),bg='#48465C',fg='white').grid(row=0,column=1, sticky=N)
            # .place(x=300, y=50 + 0)
        Label(psyc_frame,
              text="Note: The answer you choose will be the final,\n If it is found to be wrong your account request may be rejected!!",
              font=("Times new roman", 12, "bold"), fg="red",bg='#48465C').grid(row=1,column=1,sticky=W)
            # .place(x=400, y=50 + 50, height=40)
        Label(psyc_frame, text="\n\nName:", font=("Times new roman", 16, "bold"),bg='#48465C',fg='white').grid(row=2,column=0,sticky=W)
            # .place(x=0, y=50 + 100)
        self.e1 = Entry(psyc_frame,width=len(self.name))
        self.e1.insert(END, self.name)
        self.e1.grid(row=2,column=1,sticky=SW)
            # .place(x=50, y=50 + 100, width=50)
        Label(psyc_frame, text=self.name, font=("Times new roman", 16),bg='#48465C',fg='#FBC469').grid(row=2,column=1,sticky=SW)
            # .place(x=50, y=50 + 100, width=50)
        Label(psyc_frame, text="\n\nAge:", font=("Times new roman", 16, "bold"),bg='#48465C',fg='white').grid(row=3,column=0,sticky=W)
            # .place(x=100, y=50 + 100)
        self.Age = Entry(psyc_frame,bg='grey',fg='Black',width=15, font=("Times new roman", 16))
        self.Age.grid(row=3,column=1,sticky=SW)
            # .place(x=150, y=50 + 100)
        Label(psyc_frame, text="\n\nContact:", font=("Times new roman", 16, 'bold'),bg='#48465C',fg='white').grid(row=4,column=0,sticky=W)
            # .place(x=300, y=50 + 100)
        self.contact = Entry(psyc_frame,bg='grey',fg='Black',width=15, font=("Times new roman", 16))
        self.contact.grid(row=4,column=1,sticky=SW)
            # .place(x=400, y=50 + 100)
        Label(psyc_frame, text="\nSex:\n", font=("Times new roman", 16, 'bold'),bg='#48465C',fg='white').grid(row=5,column=0,sticky=W)
            # .place(x=0, y=50 + 130)
        self.Gender = StringVar()
        Radiobutton(psyc_frame, text="Male", font=("Times new roman", 16), variable=self.Gender, value="Male",
                    tristatevalue="rb1",bg='#48465C',fg='#FBC469').grid(row=5,column=1,sticky=NW)
            # .place(x=60, y=50 + 130)
        Radiobutton(psyc_frame, text="Female", font=("Times new roman", 16), variable=self.Gender, value="Female",
                    tristatevalue="rb1",bg='#48465C',fg='#FBC469').grid(row=5,column=1,sticky=SW)
            # .place(x=60, y=50 + 160)
        # Label(psyc_frame,text="API key:", font=("Times new roman", 16, 'bold'),bg='#48465C',fg='white').grid(row=6,column=0,sticky=W)
        # a=Text(psyc_frame, font=("Times new roman", 12, 'bold'),width=20,height=2,bg='grey',fg='black')
        # a.insert(END,"YzmM88nvSlCUXsgfwp08sw")
        # a.grid(row=6,column=1,sticky=W)
        # Label(psyc_frame, text="(Change with\n your api key)", font=("Times new roman", 10),bg='#48465C',fg='#FBC469').grid(row=6,column=1,sticky=S)
        # Label(psyc_frame,text="API Secret key:", font=("Times new roman", 16, 'bold'),bg='#48465C',fg='white').grid(row=7,column=0,sticky=W)
        # b=Text(psyc_frame, font=("Times new roman", 12, 'bold'),width=20,height=2,bg='grey',fg='black')
        # b.insert(END,"E0G3kdbb3D2u9R7ww44NbVsNYSLueyZNGyDr")
        # b.grid(row=7,column=1,sticky=W)
        # Label(psyc_frame, text="(Change with your\n api secret key)", font=("Times new roman", 10),bg='#48465C',fg='#FBC469').grid(row=7,column=1,sticky=S)
        # Radiobutton(psyc_frame, text="Other", font=("Times new roman", 12), variable=self.Gender, value="Other",
        #             tristatevalue="rb1").place(x=60, y=50 + 190)
        self.psyc = StringVar()
        Label(psyc_frame, text="\n\nWhat type of Psychiatrist are you?\t", font=("Times new roman", 16, 'bold'),bg='#48465C',fg='white').grid(row=8,column=0,sticky=W)
            # .place(x=0, y=70 + 210)
        Radiobutton(psyc_frame, text='Child and adolescent psychiatrist', variable=self.psyc,
                    value='Child and adolescent psychiatrist', font=("Times new roman", 16), tristatevalue='1',bg='#48465C',fg='#FBC469').grid(row=8,column=1,sticky=SW)
            # .place(x=60, y=80 + 240)
        Radiobutton(psyc_frame, text='Addiction psychiatrist', variable=self.psyc, value='Addiction psychiatrist',
                    font=("Times new roman", 16), tristatevalue='1',bg='#48465C',fg='#FBC469').grid(row=9,column=1,sticky=W)
            # .place(x=60, y=80 + 270)
        Radiobutton(psyc_frame, text='Multi-specialty psychiatrist', variable=self.psyc,
                    value='Multi-specialty psychiatrist', font=("Times new roman", 16), tristatevalue='1',bg='#48465C',fg='#FBC469').grid(row=10,column=1,sticky=W)
            # .place(x=60, y=80 + 300)
        self.api_k=StringVar()
        self.api_s=StringVar()
        def rt():
            # self.api_k.set(a.get("1.0", "end-1c"))
            # self.api_s.set(b.get("1.0", "end-1c"))
            self.api_k.set("YzmM88nvSlCUXsgfwp08sw")
            self.api_s.set("E0G3kdbb3D2u9R7ww44NbVsNYSLueyZNGyDr")
            # print(self.api_k.get(),self.api_s.get())
            self.form1()
        Button(psyc_frame, text="submit>>", font=("Times new roman", 16), command=rt,bg='#1E94DC',fg='white').grid(row=4,column=2,sticky=E)
            # .place(x=500, y=450)

    def form1(self):
        if self.e1.get() == "" or self.Age.get() == "" or self.Gender.get() == "" or self.contact.get() == "" or self.psyc.get() == "" or self.api_k.get()=="" or self.api_s.get()=="":
            messagebox.showerror('Invalid Input', 'please make sure you have entered valid input', parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="JBjose",

                                              database="pys")

                cur = con.cursor()
                cur.execute("select * from psychiatrist where name=%s and contact=%s"

                            , (self.e1.get(), self.contact.get()))

                row = cur.fetchone()
                if row != None:

                    messagebox.showerror("Error", "Psychiatrist already Exist", parent=self.root)

                    self.form1_clr()

                    self.contact.focus()

                else:
                    cur.execute("insert into psychiatrist values(%s,%s,%s,%s,%s,%s,'0')",
                                (str(self.e1.get()), str(self.Age.get()), str(self.Gender.get()),
                                 str(self.contact.get()), str(self.email),
                                 str(self.psyc.get()),))
                    cur.execute("update register set form=1 where email=%s", (str(self.email),))
                    cur.execute("insert into api values(%s,%s,%s)",(self.email,self.api_k.get(),self.api_s.get(),))

                    con.commit()

                    con.close()

                    messagebox.showinfo("Success", "Application Sent successfully"

                                        , parent=self.root)
                    self.loginform()

                    self.form1_clr()

            except Exception as es:

                messagebox.showerror("Error", f"Error due to:{str(es)}"

                                     , parent=self.root)
                print(str(es))

    def form1_clr(self):
        self.Age.delete(0, END)
        self.contact.delete(0, END)
        self.psyc = ""
        self.Gender.set("")


root = Tk()

ob = Login(root)

root.mainloop()
