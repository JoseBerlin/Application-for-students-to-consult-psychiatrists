import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql
from tkinter import messagebox
import webbrowser


def Patient_home(self):
    self.root.title("Home")
    p_frame = Frame(self.root, bg='black')
    p_frame.place(x=0, y=0, height=800, width=1366)
    btn2 = Button(p_frame, text="Logout", command=self.loginform, cursor="hand2",

                  font=("times new roman", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)

    btn2.place(x=1000, y=10)
    # btn2 = Button(p_frame, text="Profile", command=self.loginform, cursor="hand2",
    #
    #               font=("times new roman", 15), fg="white", bg="orangered",
    #
    #               bd=0, width=15, height=1)
    #
    # btn2.place(x=800, y=10)
    tabcontrol = ttk.Notebook(p_frame)

    tab1 = Frame(tabcontrol)
    tab2 = Frame(tabcontrol)
    tab3 = Frame(tabcontrol)
    tab4 = Frame(tabcontrol)
    tab5 = Frame(tabcontrol)

    tabcontrol.add(tab1, text='Suggested Psychiatrists       ')
    tabcontrol.add(tab2, text='All psychiatrists             ')
    tabcontrol.add(tab3, text='Requested                     ')
    tabcontrol.add(tab4, text='Accepted                      ')
    tabcontrol.add(tab5, text='Rejected                      ')
    tabcontrol.place(x=0, y=50, height=650, width=1200)

    f1 = Frame(tab1,bg='#9BABB6')
    f1.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(f1,bg='#9BABB6')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas,bg='#9BABB6')
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    # con = pymysql.connect(host='localhost', user='root', password='JBjose',
    #                       database='pys')
    # cur = con.cursor()

    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside1 = StringVar(second_frame)

    # Set the default value of the variable
    value_inside1.set("Select")

    def req_appointment():
        if value_inside1.get() == "Select" or self.name == "":
            messagebox.showerror("Error", "111The field must be selected")
        else:
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute("select patient_name,email from patient where patient_name=%s and email=%s",
                        (self.name, self.email,))
            p_data = cur.fetchall()
            cur.execute("select name,email from psychiatrist where name=%s", (value_inside1.get(),))
            psy_data = cur.fetchall()
            cur.execute("select p_mail from psy_consult where p_mail=%s", (self.email,))
            p_count = cur.fetchall()
            # print(p_data[0][0], p_data[0][1], psy_data[0][0], psy_data[0][1])
            if len(p_count) == 0:
                cur.execute(
                    "insert into psy_consult values(%s,%s,%s,%s,'0','','','')",(p_data[0][0],p_data[0][1],psy_data[0][0],psy_data[0][1],))
                messagebox.showinfo("Success","Appointment requested")
            else:
                cur.execute(
                    f"insert into psy_consult values('{p_data[0][0]}','{p_data[0][1]}','{psy_data[0][0]}','{psy_data[0][1]}','0','','','')")
                messagebox.showinfo("Success", "Appointment requested")
            con.commit()
            cur.close()

    con = pymysql.connect(host='localhost', user='root', password='JBjose',
                          database='pys')
    cur = con.cursor()
    cur.execute("select patient_name,email,suggested_psychiatrist from patient where patient_name=%s and email=%s",
                (self.name, self.email,))
    p_data=cur.fetchall()

    cur.execute("select name,age,sex,email,contact,psychiatrist_type from psychiatrist where got_approved=1 and psychiatrist_type=%s",(p_data[0][2],))
    rows = cur.fetchall()
    Label(second_frame, text=f"Total Psychiatrists: {len(rows)}", font=('Times new roman', 14, 'bold')).grid(row=0,
                                                                                                             column=3,
                                                                                                             padx=0,
                                                                                                             pady=0)
    con.commit()
    cur.close()
    Label(second_frame, text="Select Psychiatrist name:").grid(row=1, column=4, padx=10, pady=10)
    lb1 = []
    for i in range(len(rows)):
        lb1.insert(i, rows[i][0])
    question_menu = OptionMenu(second_frame, value_inside1, *lb1)
    question_menu.grid(row=1, column=5, pady=10, padx=0)
    submit_button = Button(second_frame, text='Get Appointment', command=req_appointment)
    submit_button.grid(row=1, column=6, padx=0, pady=10)
    # opt = OptionMenu(second_frame, valu, *lb1)
    # opt.grid(row=1, column=5, pady=10, padx=0)
    # Button(second_frame, text="Consult", command=req_appointment).grid(row=1, column=6)
    n = 3
    Label(second_frame, text=f'NAME', font=('Times new roman', 16, 'bold')).grid(row=2, column=3, pady=10, padx=30)
    Label(second_frame, text=f'AGE', font=('Times new roman', 14, 'bold')).grid(row=2, column=4, pady=10, padx=10)
    Label(second_frame, text=f'GENDER', font=('Times new roman', 14, 'bold')).grid(row=2, column=5, pady=10, padx=10)
    Label(second_frame, text=f'E-MAIL', font=('Times new roman', 14, 'bold')).grid(row=2, column=6, pady=10, padx=10)
    Label(second_frame, text=f'CONTACT', font=('Times new roman', 14, 'bold')).grid(row=2, column=7, pady=10, padx=10)
    Label(second_frame, text=f'TYPE', font=('Times new roman', 14, 'bold')).grid(row=2, column=8, pady=10, padx=10)
    for i in rows:
        Label(second_frame, text=f'dr.{i[0]}'.upper(), font=('Times new roman', 20, 'bold')).grid(row=n, column=3,
                                                                                                  pady=10, padx=10)
        Label(second_frame, text=f'{i[1]}').grid(row=n + 1, column=4, pady=10, padx=10)
        Label(second_frame, text=f'{i[2]}').grid(row=n + 1, column=5, pady=10, padx=10)
        Label(second_frame, text=f'{i[3]}').grid(row=n + 1, column=6, pady=10, padx=10)
        Label(second_frame, text=f'{i[4]}').grid(row=n + 1, column=7, pady=10, padx=10)
        Label(second_frame, text=f'{i[5]}').grid(row=n + 1, column=8, pady=10, padx=10)
        n += 5


    #***Helloooooooooooooo This thing works, never touch this
    f1 = Frame(tab2,bg='#9BABB6')
    f1.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(f1,bg='#9BABB6')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas,bg='#9BABB6')
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    con = pymysql.connect(host='localhost', user='root', password='JBjose',
                          database='pys')
    cur = con.cursor()

    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside = StringVar(second_frame)

    # Set the default value of the variable
    value_inside.set("Select")

    def req_appointment():
        if value_inside.get() == "Select" or self.name == "":
            messagebox.showerror("Error", "The field must be selected", parent=self.root)
        else:
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute("select patient_name,email from patient where patient_name=%s and email=%s", (self.name, self.email,))
            p_data = cur.fetchall()
            cur.execute("select name,email from psychiatrist where name=%s", (value_inside.get(),))
            psy_data = cur.fetchall()
            cur.execute("select * from psy_consult where p_mail=%s", (self.email,))
            p_count1 = cur.fetchall()
            # print(p_data[0][0],p_data[0][1],psy_data[0][0],psy_data[0][1])
            # print(len(p_count1))
            cur.execute("select * from psy_consult where p_mail=%s and psy_mail=%s and appointment_accepted=0",(p_data[0][1],psy_data[0][1]))
            row=cur.fetchall()
            if row==None or len(row)==0:
                cur.execute(
                    "insert into psy_consult values(%s,%s,%s,%s,'0','','','')",(p_data[0][0],p_data[0][1],psy_data[0][0],psy_data[0][1],))
                messagebox.showinfo("Success", "Appointment requested")
            else:
                messagebox.showerror("Appointment Found","Found an exiting pending appointment")
            con.commit()
            cur.close()

    cur.execute("select name,age,sex,email,contact,psychiatrist_type from psychiatrist where got_approved=1")
    rows = cur.fetchall()
    Label(second_frame, text=f"Total Psychiatrists: {len(rows)}", font=('Times new roman', 14, 'bold')).grid(row=0,
                                                                                                             column=3,
                                                                                                             padx=0,
                                                                                                             pady=0)
    con.commit()
    cur.close()
    Label(second_frame, text="Select Psychiatrist name:").grid(row=1, column=4, padx=10, pady=10)
    lb1 = []
    for i in range(len(rows)):
        lb1.insert(i, rows[i][0])
    question_menu = OptionMenu(second_frame, value_inside, *lb1)
    question_menu.grid(row=1, column=5, pady=10, padx=0)
    submit_button = Button(second_frame, text='Get Appointment', command=req_appointment)
    submit_button.grid(row=1, column=6, padx=0, pady=10)
    # opt = OptionMenu(second_frame, valu, *lb1)
    # opt.grid(row=1, column=5, pady=10, padx=0)
    # Button(second_frame, text="Consult", command=req_appointment).grid(row=1, column=6)
    n = 3
    Label(second_frame, text=f'NAME', font=('Times new roman', 16, 'bold')).grid(row=2, column=3, pady=10, padx=30)
    Label(second_frame, text=f'AGE', font=('Times new roman', 14, 'bold')).grid(row=2, column=4, pady=10, padx=10)
    Label(second_frame, text=f'GENDER', font=('Times new roman', 14, 'bold')).grid(row=2, column=5, pady=10, padx=10)
    Label(second_frame, text=f'E-MAIL', font=('Times new roman', 14, 'bold')).grid(row=2, column=6, pady=10, padx=10)
    Label(second_frame, text=f'CONTACT', font=('Times new roman', 14, 'bold')).grid(row=2, column=7, pady=10, padx=10)
    Label(second_frame, text=f'TYPE', font=('Times new roman', 14, 'bold')).grid(row=2, column=8, pady=10, padx=10)
    for i in rows:
        Label(second_frame, text=f'dr.{i[0]}'.upper(), font=('Times new roman', 20, 'bold')).grid(row=n, column=3,
                                                                                                  pady=10, padx=10)
        Label(second_frame, text=f'{i[1]}').grid(row=n + 1, column=4, pady=10, padx=10)
        Label(second_frame, text=f'{i[2]}').grid(row=n + 1, column=5, pady=10, padx=10)
        Label(second_frame, text=f'{i[3]}').grid(row=n + 1, column=6, pady=10, padx=10)
        Label(second_frame, text=f'{i[4]}').grid(row=n + 1, column=7, pady=10, padx=10)
        Label(second_frame, text=f'{i[5]}').grid(row=n + 1, column=8, pady=10, padx=10)
        n += 5

    #Tab3
    f1 = Frame(tab3,bg='#9BABB6')
    f1.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(f1,bg='#9BABB6')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas,bg='#9BABB6')
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # ***********Frame-1***************
    entry_frame = Frame(f1, bd=5, relief='ridge', bg='wheat')
    entry_frame.place(x=20, y=0, width=360, height=745)

    # Labels of frame-1
    # reg_lbl = Label(entry_frame, text="Request details", font=("arial", 20, "bold"), bg='wheat', fg='red')
    # reg_lbl.grid(row=0, columnspan=2)

    roll_lbl = Label(entry_frame, text="Patient Name", font=("", 13))
    roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

    name_lbl = Label(entry_frame, text="Patient mail", font=("", 13))
    name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

    Fname_lbl = Label(entry_frame, text="Psychiatrist", font=("", 13))
    Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

    gen_lbl = Label(entry_frame, text="Psychiatrist mail", font=("", 13))
    gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

    # cat_lbl = Label(entry_frame, text="Contact no", font=("", 13))
    # cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)
    #
    # branch_lbl = Label(entry_frame, text="Suggested \npsychiatrist", font=("", 13))
    # branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

    # Entry box of Frame-1
    roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.name1)
    roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

    name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.age1)
    name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

    gen_combo = Label(entry_frame, textvariable=self.gender1)
    # gen_combo['values'] = ('Male', 'Female')
    # gen_combo.current(0)
    gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

    # branch_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.suggested_psychiatrist1)
    # branch_combo['values'] = (
    #     'Multi-specialty psychiatrist', 'Child and adolescent psychiatrist', 'Addiction psychiatrist')
    # branch_combo.current(0)
    # branch_combo.grid(row=6, column=1, sticky='w', padx=10, pady=11)

    mail_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.email1)
    mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

    # contact_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.contact1)
    # contact_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

    # ***************Functions*********************
    def fetch_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        cur.execute('select p_name,p_mail,psy_name,psy_mail from psy_consult where p_mail=%s and appointment_accepted=0', self.email)
        rows = cur.fetchall()

        if rows != 0:
            self.totalrecord.set(len(rows))
            table.delete(*table.get_children())

            for row in rows:
                table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_data():
        self.name1.set("")
        self.age1.set("")
        self.gender1.set("")
        self.email1.set("")
        # self.contact1.set("")
        # self.suggested_psychiatrist1.set("")

    def focus(e):
        cursor = table.focus()
        content = table.item(cursor)
        row = content['values']
        self.name1.set(row[0])
        self.age1.set(row[1])
        self.gender1.set(row[2])
        self.email1.set(row[3])
        # self.contact1.set(row[4])
        # self.suggested_psychiatrist1.set(row[5])

    def delete_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        if self.name1.get() != None and self.name1.get() != "":
            # print(self.age1.get(),self.email1.get())
            cur.execute('delete from psy_consult where p_mail=%s and psy_mail=%s and appointment_accepted=0', (self.age1.get(),self.email1.get()))
            con.commit()
            con.close()
            fetch_data()
            clear_data()
            messagebox.showinfo('Success', 'Record has been deleted')
        else:
            messagebox.showerror('Error', 'Invalid input')
        fetch_data()

    def search():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        cur.execute("select patient_name,age,sex,email,contact,suggested_psychiatrist from patient where " + str(
            self.search_by.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()

        if len(rows) != 0:
            table.delete(*table.get_children())

            for row in rows:
                table.insert('', END, values=row)

            con.commit()
        else:
            messagebox.showinfo('Not found', 'Record not found')

        con.close()

    # **********Frame-3 Button**************

    btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='wheat')
    btn_frame.place(x=15, y=430, width=310, height=70)

    # add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7")
    # add_btn.grid(row=0, column=1, padx=50, pady=10)

    # update_btn = Button(btn_frame, text='Update', font=("", 12), command=update_data, width="7")
    # update_btn.grid(row=0, column=2, padx=10, pady=10)

    delete_btn = Button(btn_frame, text='Delete Req', font=("", 12), command=delete_data, width="9")
    delete_btn.grid(row=1, column=1, padx=50, pady=10)

    clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
    clear_btn.grid(row=1, column=2, padx=10, pady=10)

    # ***********Frame-2***************
    data_frame = Frame(f1, bd=5, relief='ridge', bg='wheat')
    data_frame.place(x=380, y=0, width=1145, height=745)

    Button(data_frame,text="Refresh",command=fetch_data).pack()

    # ************Frame-3 Treeview***************
    view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
    view_frame.place(x=20, y=40, width=800, height=520)

    x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(view_frame, orient=VERTICAL)
    table = ttk.Treeview(view_frame,
                         columns=('patient_name', 'age', 'sex', 'email'),
                         xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.configure(command=table.xview)
    y_scroll.configure(command=table.yview)

    table.heading("patient_name", text="Patient Name")
    table.heading("age", text="Patient email")
    table.heading("sex", text="Psychiatrist Name")
    table.heading("email", text="Psyychiatrist E-mail")

    table.column("patient_name", width=100)
    table.column("age", width=100)
    table.column("sex", width=100)
    table.column("email", width=100)
    table['show'] = 'headings'
    table.bind('<ButtonRelease-1>', focus)
    fetch_data()
    table.pack(fill=BOTH, expand=1)



    #tab4
    name2=StringVar()
    p_mail2=StringVar()
    psy_name2=StringVar()
    psy_mail2=StringVar()
    appointment_t=StringVar()
    link=StringVar()
    f2 = Frame(tab4,bg='#9BABB6')
    f2.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(f2,bg='#9BABB6')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(f2, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas,bg='#9BABB6')
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # ***********Frame-1***************
    entry_frame = Frame(f2, bd=5, relief='ridge', bg='wheat')
    entry_frame.place(x=20, y=0, width=360, height=745)

    # Labels of frame-1
    # reg_lbl = Label(entry_frame, text="Appointment Details", font=("arial", 20, "bold"), bg='wheat', fg='red')
    # reg_lbl.grid(row=0, columnspan=2)

    roll_lbl = Label(entry_frame, text="Patient Name", font=("", 13))
    roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

    name_lbl = Label(entry_frame, text="Patient mail", font=("", 13))
    name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

    Fname_lbl = Label(entry_frame, text="Psychiatrist", font=("", 13))
    Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

    gen_lbl = Label(entry_frame, text="Psychiatrist mail", font=("", 13))
    gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

    cat_lbl = Label(entry_frame, text="Appointment_time", font=("", 13))
    cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)
    #
    branch_lbl = Label(entry_frame, text="Link", font=("", 13))
    branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

    # Entry box of Frame-1
    roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=name2)
    roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

    name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=p_mail2)
    name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

    gen_combo = Label(entry_frame, textvariable=psy_name2)
    # gen_combo['values'] = ('Male', 'Female')
    # gen_combo.current(0)
    gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

    mail_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=psy_mail2)
    mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

    appointment_t_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=appointment_t)
    appointment_t_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

    link_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=link,width=15)
    link_entry.grid(row=6, column=1, sticky='w', padx=10, pady=11)

    # ***************Functions*********************
    def fetch_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        cur.execute('select p_name,p_mail,psy_name,psy_mail,appointment_time,link from psy_consult where p_mail=%s and appointment_accepted=1', self.email)
        rows1 = cur.fetchall()

        if rows1 != 0:
            self.totalrecord.set(len(rows1))
            table1.delete(*table1.get_children())

            for row in rows1:
                table1.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_data():
        name2.set("")
        p_mail2.set("")
        psy_name2.set("")
        psy_mail2.set("")
        appointment_t.set('')
        link.set('')
        # self.contact1.set("")
        # self.suggested_psychiatrist1.set("")

    def focus(e):
        cursor1 = table1.focus()
        content1 = table1.item(cursor1)
        row1 = content1['values']
        name2.set(row1[0])
        p_mail2.set(row1[1])
        psy_name2.set(row1[2])
        psy_mail2.set(row1[3])
        appointment_t.set(row1[4])
        link.set(row1[5])
        # self.contact1.set(row[4])
        # self.suggested_psychiatrist1.set(row[5])

    def delete_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        if name2.get() != None and name2.get() != "":
            # print(p_mail2.get(),psy_mail2.get())
            cur.execute('delete from psy_consult where p_mail=%s and psy_mail=%s and appointment_accepted=1', (p_mail2.get(),psy_mail2.get()))
            con.commit()
            con.close()
            fetch_data()
            clear_data()
            messagebox.showinfo('Success', 'Record has been deleted')
        else:
            messagebox.showerror('Error', 'Invalid input')
    #
    # def search():
    #     con = pymysql.connect(host='localhost', user='root', password='JBjose',
    #                           database='pys')
    #     cur = con.cursor()
    #     cur.execute("select patient_name,age,sex,email,contact,suggested_psychiatrist from patient where " + str(
    #         self.search_by.get()) + " LIKE '%" + str(
    #         self.search_txt.get()) + "%'")
    #     rows = cur.fetchall()
    #
    #     if len(rows) != 0:
    #         table1.delete(*table1.get_children())
    #
    #         for row in rows:
    #             table1.insert('', END, values=row)
    #
    #         con.commit()
    #     else:
    #         messagebox.showinfo('Not found', 'Record not found')
    #
    #     con.close()

    def join():
        new=1
        url=link.get()
        webbrowser.open(url, new=new)

    # **********Frame-3 Button**************

    btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='wheat')
    btn_frame.place(x=15, y=430, width=310, height=70)

    # add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7")
    # add_btn.grid(row=0, column=1, padx=50, pady=10)

    # update_btn = Button(btn_frame, text='Update', font=("", 12), command=update_data, width="7")
    # update_btn.grid(row=0, column=2, padx=10, pady=10)

    delete_btn = Button(btn_frame, text='Cancel Appointment', font=("", 12), command=delete_data)
    delete_btn.grid(row=1, column=1, padx=10, pady=10)

    clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
    clear_btn.grid(row=1, column=2, padx=10, pady=10)

    clear_btn = Button(btn_frame, text='join now', font=("", 12), command=join, width="7")
    clear_btn.grid(row=1, column=2, padx=10, pady=10)

    # ***********Frame-2***************
    data_frame = Frame(f2, bd=5, relief='ridge', bg='wheat')
    data_frame.place(x=380, y=0, width=1145, height=745)

    Button(data_frame,text="Refresh",command=fetch_data).pack()

    # ************Frame-3 Treeview***************
    view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
    view_frame.place(x=20, y=40, width=800, height=520)

    x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(view_frame, orient=VERTICAL)
    table1 = ttk.Treeview(view_frame,
                         columns=('p_name','p_mail','psy_name','psy_mail','appointment_time','link'),
                         xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.configure(command=table1.xview)
    y_scroll.configure(command=table1.yview)

    table1.heading('p_name', text="Patient Name")
    table1.heading('p_mail', text="Patient email")
    table1.heading('psy_name', text="Psychiatrist Name")
    table1.heading('psy_mail', text="Psychiatrist E-mail")
    table1.heading('appointment_time', text="Appointment Time")
    table1.heading('link', text="Join link")

    table1.column('p_name', width=100)
    table1.column('p_mail', width=100)
    table1.column('psy_name', width=100)
    table1.column('psy_mail', width=100)
    table1.column('appointment_time', width=100)
    table1.column('link', width=100)
    table1['show'] = 'headings'
    table1.bind('<ButtonRelease-1>', focus)
    fetch_data()
    table1.pack(fill=BOTH, expand=1)



    #tab5
    name3=StringVar()
    p_mail3=StringVar()
    psy_name3=StringVar()
    psy_mail3=StringVar()
    f3 = Frame(tab5,bg='#9BABB6')
    f3.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(f3,bg='#9BABB6')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(f3, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas,bg='#9BABB6')
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # ***********Frame-1***************
    entry_frame = Frame(f3, bd=5, relief='ridge', bg='wheat')
    entry_frame.place(x=20, y=0, width=360, height=745)

    # Labels of frame-1
    # reg_lbl = Label(entry_frame, text="Appointment details", font=("arial", 20, "bold"), bg='wheat', fg='red')
    # reg_lbl.grid(row=0, columnspan=2)

    roll_lbl = Label(entry_frame, text="Patient Name", font=("", 13))
    roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

    name_lbl = Label(entry_frame, text="Patient mail", font=("", 13))
    name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

    Fname_lbl = Label(entry_frame, text="Psychiatrist", font=("", 13))
    Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

    gen_lbl = Label(entry_frame, text="Psychiatrist mail", font=("", 13))
    gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

    # cat_lbl = Label(entry_frame, text="Contact no", font=("", 13))
    # cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)
    #
    # branch_lbl = Label(entry_frame, text="Suggested \npsychiatrist", font=("", 13))
    # branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

    # Entry box of Frame-1
    roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=name3)
    roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

    name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=p_mail3)
    name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

    gen_combo = Label(entry_frame, textvariable=psy_name3)
    # gen_combo['values'] = ('Male', 'Female')
    # gen_combo.current(0)
    gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

    mail_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=psy_mail3)
    mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

    # ***************Functions*********************
    def fetch_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        cur.execute('select p_name,p_mail,psy_name,psy_mail from psy_consult where p_mail=%s and appointment_accepted=2', self.email)
        rows2 = cur.fetchall()

        if rows2 != 0:
            self.totalrecord.set(len(rows2))
            table2.delete(*table2.get_children())

            for row in rows2:
                table2.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_data():
        name3.set("")
        p_mail3.set("")
        psy_name3.set("")
        psy_mail3.set("")
        # self.contact1.set("")
        # self.suggested_psychiatrist1.set("")

    def focus(e):
        cursor2 = table2.focus()
        content2 = table2.item(cursor2)
        row1 = content2['values']
        name3.set(row1[0])
        p_mail3.set(row1[1])
        psy_name3.set(row1[2])
        psy_mail3.set(row1[3])
        # self.contact1.set(row[4])
        # self.suggested_psychiatrist1.set(row[5])

    def delete_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        if name3.get() != None and name3.get() != "":
            # print(p_mail3.get(),psy_mail3.get())
            cur.execute('delete from psy_consult where p_mail=%s and psy_mail=%s and appointment_accepted=2', (p_mail3.get(),psy_mail3.get()))
            con.commit()
            con.close()
            fetch_data()
            clear_data()
            messagebox.showinfo('Success', 'Record has been deleted')
        else:
            messagebox.showerror('Error', 'Invalid input')


    # **********Frame-3 Button**************

    btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='wheat')
    btn_frame.place(x=15, y=430, width=310, height=70)

    # add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7")
    # add_btn.grid(row=0, column=1, padx=50, pady=10)

    # update_btn = Button(btn_frame, text='Update', font=("", 12), command=update_data, width="7")
    # update_btn.grid(row=0, column=2, padx=10, pady=10)

    delete_btn = Button(btn_frame, text='Delete record', font=("", 12), command=delete_data)
    delete_btn.grid(row=1, column=1, padx=50, pady=10)

    clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
    clear_btn.grid(row=1, column=2, padx=10, pady=10)

    # ***********Frame-2***************
    data_frame = Frame(f3, bd=5, relief='ridge', bg='wheat')
    data_frame.place(x=380, y=0, width=1145, height=745)

    Button(data_frame,text="Refresh",command=fetch_data).pack()

    # ************Frame-3 Treeview***************
    view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
    view_frame.place(x=20, y=40, width=800, height=520)

    x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(view_frame, orient=VERTICAL)
    table2 = ttk.Treeview(view_frame,
                         columns=('patient_name', 'age', 'sex', 'email'),
                         xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.configure(command=table2.xview)
    y_scroll.configure(command=table2.yview)

    table2.heading("patient_name", text="Patient Name")
    table2.heading("age", text="Patient email")
    table2.heading("sex", text="Psychiatrist Name")
    table2.heading("email", text="Psyychiatrist E-mail")

    table2.column("patient_name", width=100)
    table2.column("age", width=100)
    table2.column("sex", width=100)
    table2.column("email", width=100)
    table2['show'] = 'headings'
    table2.bind('<ButtonRelease-1>', focus)
    fetch_data()
    table2.pack(fill=BOTH, expand=1)