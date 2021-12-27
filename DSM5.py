from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

import psychiatrist_home


def f01(self):

    self.root.title("DSM5 Measure")

    # Create A Main Frame
    main_frame = Frame(self.root)
    main_frame.place(x=0,y=0, height=800, width=1200)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    #Variable for second frame
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()
    s6 = StringVar()
    s7 = StringVar()
    s8 = StringVar()
    s9 = StringVar()
    s10 = StringVar()
    s11 = StringVar()
    s12 = StringVar()
    s13 = StringVar()
    s14 = StringVar()
    s15 = StringVar()
    s16 = StringVar()
    s17 = StringVar()
    s18 = StringVar()
    s19 = StringVar()
    s20 = StringVar()
    s21 = StringVar()
    s22 = StringVar()
    s23 = StringVar()
    s24 = StringVar()
    s25 = StringVar()
    p1 = StringVar()
    p2 = StringVar()
    p3 = StringVar()
    p4 = StringVar()
    p5 = StringVar()
    p6 = StringVar()
    p7 = StringVar()
    p8 = StringVar()
    p9 = StringVar()
    p10 = StringVar()
    p11 = StringVar()
    p12 = StringVar()
    p13 = StringVar()
    p14 = StringVar()
    p15 = StringVar()
    p16 = StringVar()
    p17 = StringVar()
    p18 = StringVar()
    p19 = StringVar()
    p20 = StringVar()
    p21 = StringVar()
    p22 = StringVar()
    p23 = StringVar()
    p24 = StringVar()
    p25 = StringVar()


    Label(second_frame, text=f'DSM-5 Self-Rated Level 1 Cross-Cutting Symptom Measure\t\t\t\nChild Age 11–17',
          font=("", 20, 'bold')).grid(row=0, column=0, sticky=W)
    Label(second_frame, text=f'\t', font=("", 20, 'bold')).grid(row=0, column=1, sticky=W)
    Label(second_frame,
          text=f'0-Not at all\t1-Rare, less than a day or two\t2-Several days\t3-More than half the days\t4-Nearly every day\nDuring the past TWO (2) WEEKS, how much (or how often) have you…',
          font=("", 12, 'bold'), fg='blue').grid(row=1, column=0, sticky=W)
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='JBjose', database='pys')
        cur1 = con.cursor()
        cur1.execute(
            "select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25 from dsm_questions where id='student'")
        row = cur1.fetchall()
        j = 3
        if row!=None:
            for i in range(0, 25):
                Label(second_frame, text=f"\n{i + 1}.{row[0][i]}", font=("", 12)).grid(row=j, column=0, sticky=W)
                # Entry(second_frame).grid(row=j , column=0, sticky=E)
                # print(j)
                j += 2
        else:
            messagebox.showerror("1","Invalid Data")


        btn2 = Button(second_frame, text="Logout", command=self.loginform, cursor="hand2",

                      font=("times new roman", 15), fg="white", bg="orangered",

                      bd=0, width=15, height=1)

        btn2.place(x=1000, y=25)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s1, width=5, font=("", 12), justify=CENTER).grid(
            row=3, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s2, width=5, font=("", 12), justify=CENTER).grid(
            row=5, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s3, width=5, font=("", 12), justify=CENTER).grid(
            row=7, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s4, width=5, font=("", 12), justify=CENTER).grid(
            row=9, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s5, width=5, font=("", 12), justify=CENTER).grid(
            row=11, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s6, width=5, font=("", 12), justify=CENTER).grid(
            row=13, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s7, width=5, font=("", 12), justify=CENTER).grid(
            row=15, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s8, width=5, font=("", 12), justify=CENTER).grid(
            row=17, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s9, width=5, font=("", 12), justify=CENTER).grid(
            row=19, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s10, width=5, font=("", 12), justify=CENTER).grid(
            row=21, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s11, width=5, font=("", 12), justify=CENTER).grid(
            row=23, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s12, width=5, font=("", 12), justify=CENTER).grid(
            row=25, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s13, width=5, font=("", 12), justify=CENTER).grid(
            row=27, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s14, width=5, font=("", 12), justify=CENTER).grid(
            row=29, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s15, width=5, font=("", 12), justify=CENTER).grid(
            row=31, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s16, width=5, font=("", 12), justify=CENTER).grid(
            row=33, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s17, width=5, font=("", 12), justify=CENTER).grid(
            row=35, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s18, width=5, font=("", 12), justify=CENTER).grid(
            row=37, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s19, width=5, font=("", 12), justify=CENTER).grid(
            row=39, column=0, sticky=E)
        Spinbox(second_frame, from_=0, to=4, wrap=False, textvariable=s20, width=5, font=("", 12), justify=CENTER).grid(
            row=41, column=0, sticky=E)
        Radiobutton(second_frame, text="Yes", variable=s21, value="Yes", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=21).grid(row=43, column=0, sticky=E)
        Radiobutton(second_frame, text="Yes", variable=s22, value="Yes", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=22).grid(row=45, column=0, sticky=E)
        Radiobutton(second_frame, text="Yes", variable=s23, value="Yes", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=23).grid(row=47, column=0, sticky=E)
        Radiobutton(second_frame, text="Yes", variable=s24, value="Yes", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=24).grid(row=49, column=0, sticky=E)
        Radiobutton(second_frame, text="Yes", variable=s25, value="Yes", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=25).grid(row=51, column=0, sticky=E)
        Radiobutton(second_frame, text="No", variable=s21, value="No", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=21).grid(row=43, column=1, sticky=W)
        Radiobutton(second_frame, text="No", variable=s22, value="No", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=22).grid(row=45, column=1, sticky=W)
        Radiobutton(second_frame, text="No", variable=s23, value="No", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=23).grid(row=47, column=1, sticky=W)
        Radiobutton(second_frame, text="No", variable=s24, value="No", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=24).grid(row=49, column=1, sticky=W)
        Radiobutton(second_frame, text="No", variable=s25, value="No", width=5, font=("", 12), justify=CENTER,
                    tristatevalue=25).grid(row=51, column=1, sticky=W)
        j += 1
        Label(second_frame, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        def nxt():
            second_frame1.tkraise()
            btn2.focus()
        Button(second_frame, text="Next", font=("", 12), command=nxt ,bg='#1E94DC',fg='white').grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        Label(second_frame, text="\t", font=("", 12)).grid(row=0, column=1, sticky=N)
        con.commit()
        cur1.close()
    except Exception as es:
        messagebox.showerror("Error", f"Connection1 error: {es}")
        print(es)

    # my_label = Label(second_frame, text="It's Friday Yo!").grid(row=3, column=2)

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame1, anchor="nw")

    def to1():
        if(s21.get()!='' or s22.get()!='' or s23.get()!='' or s24.get()!='' or s25.get()!=''):
            second_frame.tkraise()
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='JBjose', database='pys')
                cur11 = con.cursor()
                str=f"insert into dsm_stu_answers(stu_mail, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25) values('{self.email}','{s1.get()}','{s2.get()}','{s3.get()}','{s4.get()}','{s5.get()}','{s6.get()}','{s7.get()}','{s8.get()}','{s9.get()}','{s10.get()}','{s11.get()}','{s12.get()}','{s13.get()}','{s14.get()}','{s15.get()}','{s16.get()}','{s17.get()}','{s18.get()}','{s19.get()}','{s20.get()}','{s21.get()}','{s22.get()}','{s23.get()}','{s24.get()}','{s25.get()}')"
                str1=f"insert into dsm_par_answers(stu_mail, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25) values('{self.email}','{p1.get()}','{p2.get()}','{p3.get()}','{p4.get()}','{p5.get()}','{p6.get()}','{p7.get()}','{p8.get()}','{p9.get()}','{p10.get()}','{p11.get()}','{p12.get()}','{p13.get()}','{p14.get()}','{p15.get()}','{p16.get()}','{p17.get()}','{p18.get()}','{p19.get()}','{p20.get()}','{p21.get()}','{p22.get()}','{p23.get()}','{p24.get()}','{p25.get()}')"
                # print(str)
                # print(str1)
                cur11.execute(str)
                cur11.execute(str1)
                messagebox.showinfo("Success","Data included successfully")
                con.commit()
                cur11.close()
                self.Form()
            except Exception as es:
                messagebox.showerror("Error",f"Updating data error: {es}")
                print(es)
        else:
            messagebox.showerror("Invalid","Missing field values")

    Label(second_frame1, text=f'DSM-5 Parent/Guardian-Rated Level 1 Cross-Cutting Symptom Measure\t\t\nChild Age 6–17',
          font=("", 20, 'bold')).grid(row=0, column=0, sticky=W)
    Label(second_frame1, text=f'\t', font=("", 20, 'bold')).grid(row=0, column=1, sticky=W)
    Label(second_frame1,
          text=f'0-Not at all\t1-Rare, less than a day or two\t2-Several days\t3-More than half the days\t4-Nearly every day\nDuring the past TWO (2) WEEKS, how much (or how often) has your child..',
          font=("", 12, 'bold'), fg='blue').grid(row=1, column=0, sticky=W)
    j = 3
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='JBjose', database='pys')
        cur2 = con.cursor()
        cur2.execute(
            "select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25 from dsm_questions where id='parent'")
        row = cur2.fetchall()
        if row!=None:
            for i in range(0, 25):
                Label(second_frame1, text=f"\n{i + 1}.{row[0][i]}", font=("", 12)).grid(row=j, column=0, sticky=W)
                # Entry(second_frame1).grid(row=j, column=0, sticky=E)
                j += 2
        else:
            messagebox.showerror("2","Invalid data")
        con.commit()
        cur2.close()
    except Exception as es:
        messagebox.showerror("Error", f"Connection2 error: {es}")
        print(es)

    btn2 = Button(second_frame1, text="Logout", command=self.loginform, cursor="hand2",

                  font=("times new roman", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)

    btn2.place(x=1000, y=25)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p1, width=5, font=("", 12), justify=CENTER).grid(
        row=3, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p2, width=5, font=("", 12), justify=CENTER).grid(
        row=5, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p3, width=5, font=("", 12), justify=CENTER).grid(
        row=7, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p4, width=5, font=("", 12), justify=CENTER).grid(
        row=9, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p5, width=5, font=("", 12), justify=CENTER).grid(
        row=11, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p6, width=5, font=("", 12), justify=CENTER).grid(
        row=13, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p7, width=5, font=("", 12), justify=CENTER).grid(
        row=15, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p8, width=5, font=("", 12), justify=CENTER).grid(
        row=17, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p9, width=5, font=("", 12), justify=CENTER).grid(
        row=19, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p10, width=5, font=("", 12),
            justify=CENTER).grid(row=21, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p11, width=5, font=("", 12),
            justify=CENTER).grid(row=23, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p12, width=5, font=("", 12),
            justify=CENTER).grid(row=25, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p13, width=5, font=("", 12),
            justify=CENTER).grid(row=27, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p14, width=5, font=("", 12),
            justify=CENTER).grid(row=29, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p15, width=5, font=("", 12),
            justify=CENTER).grid(row=31, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p16, width=5, font=("", 12),
            justify=CENTER).grid(row=33, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p17, width=5, font=("", 12),
            justify=CENTER).grid(row=35, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p18, width=5, font=("", 12),
            justify=CENTER).grid(row=37, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p19, width=5, font=("", 12),
            justify=CENTER).grid(row=39, column=0, sticky=E)
    Spinbox(second_frame1, from_=0, to=4, wrap=False, textvariable=p20, width=5, font=("", 12),
            justify=CENTER).grid(row=41, column=0, sticky=E)
    Radiobutton(second_frame1, text="Yes", variable=p21, value="Yes", width=5, font=("", 12), justify=CENTER,
                tristatevalue=71).grid(row=43, column=0, sticky=E)
    Radiobutton(second_frame1, text="Yes", variable=p22, value="Yes", width=5, font=("", 12), justify=CENTER,
                tristatevalue=72).grid(row=45, column=0, sticky=E)
    Radiobutton(second_frame1, text="Yes", variable=p23, value="Yes", width=5, font=("", 12), justify=CENTER,
                tristatevalue=73).grid(row=47, column=0, sticky=E)
    Radiobutton(second_frame1, text="Yes", variable=p24, value="Yes", width=5, font=("", 12), justify=CENTER,
                tristatevalue=74).grid(row=49, column=0, sticky=E)
    Radiobutton(second_frame1, text="Yes", variable=p25, value="Yes", width=5, font=("", 12), justify=CENTER,
                tristatevalue=75).grid(row=51, column=0, sticky=E)
    Radiobutton(second_frame1, text="No", variable=p21, value="No", width=5, font=("", 12), justify=CENTER,
                tristatevalue=71).grid(row=43, column=1, sticky=W)
    Radiobutton(second_frame1, text="No", variable=p22, value="No", width=5, font=("", 12), justify=CENTER,
                tristatevalue=72).grid(row=45, column=1, sticky=W)
    Radiobutton(second_frame1, text="No", variable=p23, value="No", width=5, font=("", 12), justify=CENTER,
                tristatevalue=73).grid(row=47, column=1, sticky=W)
    Radiobutton(second_frame1, text="No", variable=p24, value="No", width=5, font=("", 12), justify=CENTER,
                tristatevalue=74).grid(row=49, column=1, sticky=W)
    Radiobutton(second_frame1, text="No", variable=p25, value="No", width=5, font=("", 12), justify=CENTER,
                tristatevalue=75).grid(row=51, column=1, sticky=W)

    j += 1
    Button(second_frame1, text="Back", font=("", 12), command=lambda: second_frame.tkraise(),bg='Orangered',fg='white').grid(row=j, column=0,
                                                                                                   sticky=N)
    j += 1
    Button(second_frame1, text="Submit", font=("", 12), command=to1,bg='#1E94DC',fg='white').grid(row=j, column=0)
    j += 1
    Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
    Label(second_frame1, text="", font=("", 12)).grid(row=j + 1, column=0, sticky=N)
    Label(second_frame1, text="", font=("", 12)).grid(row=j + 1, column=1, sticky=N)
    j += 1
    Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
    j += 1
    Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
    j += 1
    Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
    j += 1
    # Button(second_frame1, text="Next", font=("", 12), command=to).grid(row=j, column=0, sticky=N)
    # j += 1
    Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
    j += 1
    Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
    j += 1
    Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
    j += 1
    Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
    Label(second_frame1, text="\t", font=("", 12)).grid(row=0, column=1, sticky=N)
    # my_label = Label(second_frame1, text="It's Friday Yo!").grid(row=3, column=2)
    def psyc1():
        main_frame.destroy()
        psychiatrist_home.Psychiatrist_home(self)

    btn2 = Button(second_frame, text="Home", command=psyc1, cursor="hand2",

                  font=("times new roman", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)

    btn2.place(x=1000, y=25)

    second_frame.tkraise()


def f02(self,p_email):

    self.root.title("DSM5")

    # Create A Main Frame
    main_frame = Frame(self.root)
    main_frame.place(x=0,y=0, height=800, width=1200)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    #Variable for second frame
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()
    s6 = StringVar()
    s7 = StringVar()
    s8 = StringVar()
    s9 = StringVar()
    s10 = StringVar()
    s11 = StringVar()
    s12 = StringVar()
    s13 = StringVar()
    s14 = StringVar()
    s15 = StringVar()
    s16 = StringVar()
    s17 = StringVar()
    s18 = StringVar()
    s19 = StringVar()
    s20 = StringVar()
    s21 = StringVar()
    s22 = StringVar()
    s23 = StringVar()
    s24 = StringVar()
    s25 = StringVar()
    p1 = StringVar()
    p2 = StringVar()
    p3 = StringVar()
    p4 = StringVar()
    p5 = StringVar()
    p6 = StringVar()
    p7 = StringVar()
    p8 = StringVar()
    p9 = StringVar()
    p10 = StringVar()
    p11 = StringVar()
    p12 = StringVar()
    p13 = StringVar()
    p14 = StringVar()
    p15 = StringVar()
    p16 = StringVar()
    p17 = StringVar()
    p18 = StringVar()
    p19 = StringVar()
    p20 = StringVar()
    p21 = StringVar()
    p22 = StringVar()
    p23 = StringVar()
    p24 = StringVar()
    p25 = StringVar()

    Label(second_frame, text=f'DSM-5 Self-Rated Level 1 Cross-Cutting Symptom Measure—Child Age 11–17\t',
          font=("", 20, 'bold')).grid(row=0, column=0, sticky=W)
    Label(second_frame, text=f'\t', font=("", 20, 'bold')).grid(row=0, column=1, sticky=W)
    Label(second_frame,
          text=f'0-Not at all\t1-Rare, less than a day or two\t2-Several days\t3-More than half the days\t4-Nearly every day\nDuring the past TWO (2) WEEKS, how much (or how often) the patient…',
          font=("", 12, 'bold'), fg='blue').grid(row=1, column=0, sticky=W)
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='JBjose', database='pys')
        cur13 = con.cursor()
        cur13.execute(
            "select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25 from dsm_questions where id='student'")
        row = cur13.fetchall()
        cur13.execute(
            "select a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25 from dsm_stu_answers where stu_mail=%s",
            (p_email,))
        # con.commit()
        # print(p_email)
        row1 = cur13.fetchone()
        # print(row[0],"\n",row1[0])
        j = 3
        if row!=None:
            if row1!=None:
                for i in range(0, 25):
                    Label(second_frame, text=f"\n{i + 1}.{row[0][i]}", font=("", 12)).grid(row=j, column=0, sticky=W)
                    # Entry(second_frame).grid(row=j , column=0, sticky=E)
                    # print(j)
                    Label(second_frame,text=f'{row1[i]}', width=5, font=("", 12), justify=CENTER).grid(row=j, column=0, sticky=SE)
                    j += 2
            else:
                messagebox.showerror("Ans","Student answer error")
        else:
            messagebox.showerror("Q","student Question error")

        j += 1
        Label(second_frame, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        def nxt1():
            second_frame1.tkraise()
            btn2.focus()
        Button(second_frame, text="Next", font=("", 12), command=nxt1,bg='#1E94DC',fg='white').grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        Label(second_frame, text="\t", font=("", 12)).grid(row=0, column=1, sticky=N)
        con.commit()
        cur13.close()
    except Exception as es:
        messagebox.showerror("Error", f"Connection3 error: {es}")
        print(es)

    # my_label = Label(second_frame, text="It's Friday Yo!").grid(row=3, column=2)

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame1 = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame1, anchor="nw")

    def to2():
        if p21.get()!='' or p22.get()!='' or p23.get()!='' or p24.get()!='' or p25.get()!='':
            # second_frame.tkraise()
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='JBjose', database='pys')
                cur14 = con.cursor()
                str=f"insert into dsm_stu_answers(stu_mail, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25) values('{self.email}','{s1.get()}','{s2.get()}','{s3.get()}','{s4.get()}','{s5.get()}','{s6.get()}','{s7.get()}','{s8.get()}','{s9.get()}','{s10.get()}','{s11.get()}','{s12.get()}','{s13.get()}','{s14.get()}','{s15.get()}','{s16.get()}','{s17.get()}','{s18.get()}','{s19.get()}','{s20.get()}','{s21.get()}','{s22.get()}','{s23.get()}','{s24.get()}','{s25.get()}')"
                str1=f"insert into dsm_par_answers(stu_mail, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25) values('{self.email}','{p1.get()}','{p2.get()}','{p3.get()}','{p4.get()}','{p5.get()}','{p6.get()}','{p7.get()}','{p8.get()}','{p9.get()}','{p10.get()}','{p11.get()}','{p12.get()}','{p13.get()}','{p14.get()}','{p15.get()}','{p16.get()}','{p17.get()}','{p18.get()}','{p19.get()}','{p20.get()}','{p21.get()}','{p22.get()}','{p23.get()}','{p24.get()}','{p25.get()}')"
                # print(str)
                # print(str1)
                cur14.execute(str)
                cur14.execute(str1)
                messagebox.showinfo("Success","Data included successfully")
                con.commit()
                cur14.close()
                self.Form()
            except Exception as es:
                messagebox.showerror("Error",f"Updating data error: {es}")
                print(es)

    Label(second_frame1, text=f'DSM-5 Parent/Guardian-Rated Level 1 Cross-Cutting Symptom Measure—Child\t \nAge 6–17',
          font=("", 20, 'bold')).grid(row=0, column=0, sticky=W)
    Label(second_frame1, text=f'\t', font=("", 20, 'bold')).grid(row=0, column=1, sticky=W)
    Label(second_frame1,
          text=f'0-Not at all\t1-Rare, less than a day or two\t2-Several days\t3-More than half the days\t4-Nearly every day\n(Parent/Guardian answer)During the past TWO (2) WEEKS, how much (or how often) has your child..',
          font=("", 12, 'bold'), fg='blue').grid(row=1, column=0, sticky=W)
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='JBjose', database='pys')
        cur15 = con.cursor()
        cur15.execute(
            "select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25 from dsm_questions where id='parent'")
        row = cur15.fetchall()
        cur15.execute("select a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25 from dsm_par_answers where stu_mail=%s",(p_email,))
        # con.commit()
        row1=cur15.fetchone()
        j = 3
        if row!=None:
            if row1!=None:
                for i in range(0, 25):
                    Label(second_frame1, text=f"\n{i + 1}.{row[0][i]}", font=("", 12)).grid(row=j, column=0, sticky=W)
                    # Entry(second_frame1).grid(row=j, column=0, sticky=E)
                    Label(second_frame1,text=f'{row1[i]}', width=5, font=("", 12), justify=CENTER).grid(row=j, column=0, sticky=SE)
                    j += 2
            else:
                messagebox.showerror("Ans","Parent answers error")
        else:
            messagebox.showerror("Q","Parent Questions error")

        j += 1
        Button(second_frame1, text="Back", font=("", 12), command=lambda: second_frame.tkraise(),bg='Orangered',fg='White').grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0)
        j += 1
        Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        Label(second_frame1, text="", font=("", 12)).grid(row=j + 1, column=0, sticky=N)
        Label(second_frame1, text="", font=("", 12)).grid(row=j + 1, column=1, sticky=N)
        j += 1
        Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame1, text="", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        # Button(second_frame1, text="Next", font=("", 12), command=to).grid(row=j, column=0, sticky=N)
        # j += 1
        Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        j += 1
        Label(second_frame1, text="\t", font=("", 12)).grid(row=j, column=0, sticky=N)
        Label(second_frame1, text="\t", font=("", 12)).grid(row=0, column=1, sticky=N)
        def psyc():
            main_frame.destroy()
            psychiatrist_home.Psychiatrist_home(self)
        btn2 = Button(second_frame1, text="Home", command=psyc, cursor="hand2",

                      font=("times new roman", 15), fg="white", bg="orangered",

                      bd=0, width=15, height=1)

        btn2.place(x=1000, y=25)
        con.commit()
        cur15.close()
    except Exception as es:
        messagebox.showerror("Error", f"Connection4 error: {es}")
        print(es)

    # my_label = Label(second_frame1, text="It's Friday Yo!").grid(row=3, column=2)

    second_frame.tkraise()

