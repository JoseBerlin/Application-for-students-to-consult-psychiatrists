import datetime
from tkinter import ttk
from tkinter import *
import pymysql
from tkinter import messagebox
import tkcalendar as cal
import webbrowser

import DSM5
import Zoom

def Psychiatrist_home(self):
    self.root.title("Psychiatrist Home")
    self.name1=StringVar()
    self.email1=StringVar()
    self.age1=StringVar()
    self.gender1=StringVar()
    self.calendar1=StringVar()
    p_frame = Frame(self.root, bg='black')
    p_frame.place(x=0, y=0, height=800, width=1366)
    btn2 = Button(p_frame, text="Logout", command=self.loginform, cursor="hand2",

                  font=("times new roman", 15), fg="white", bg="orangered",

                  bd=0, width=15, height=1)

    btn2.place(x=1000, y=10)
    tabcontrol = ttk.Notebook(p_frame)

    tab1 = Frame(tabcontrol)
    tab2 = Frame(tabcontrol)

    tabcontrol.add(tab1, text='Requests                      ')
    tabcontrol.add(tab2, text='Scheduled                     ')
    tabcontrol.place(x=0, y=50, height=650, width=1300)

    f1 = Frame(tab1)
    f1.pack(fill=BOTH, expand=1)

    # btn2 = Button(f1, text="Logout", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
    # btn2.place(x=1000, y=8)
    # def dest():
    #     entry_frame.destroy()
    #     data_frame.destroy()
    #     headinglbl.destroy()
    #     btn1.destroy()
    #
    # btn1 = Button(f1, text="Home", cursor="hand2", command=dest, font=("times new roman", 15), fg="white",
    #               bg="orangered", bd=0, width=15, height=1)
    # btn1.place(x=10, y=8)

    # ***********Frame-1***************
    entry_frame = Frame(f1, bd=5, relief='ridge', bg='wheat')
    entry_frame.place(x=0, y=0, width=360, height=745)

    # api_key=StringVar()
    # api_sec=StringVar()

    # Labels of frame-1
    # reg_lbl = Label(entry_frame, text="Patient details", font=("arial", 20, "bold"), bg='wheat', fg='red')
    # reg_lbl.grid(row=0, column=0)

    roll_lbl = Label(entry_frame, text="Name", font=("", 13))
    roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

    name_lbl = Label(entry_frame, text="Age", font=("", 13))
    name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

    Fname_lbl = Label(entry_frame, text="Gender", font=("", 13))
    Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

    gen_lbl = Label(entry_frame, text="Drug and smoke", font=("", 13))
    gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

    cat_lbl = Label(entry_frame, text="E-mail", font=("", 13))
    cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)

    cal_lbl=Label(entry_frame,text="Appointment Date", font=("", 13))
    cal_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

    time_lbl= Label(entry_frame,text='Time    ', font=("", 13))
    time_lbl.grid(row=7, column=0, sticky='w', padx=10, pady=11)

    # gen_lbl = Label(entry_frame, text="API Key", font=("", 13))
    # gen_lbl.grid(row=8, column=0, sticky='w', padx=10, pady=11)
    #
    # gen_lbl = Label(entry_frame, text="API secret", font=("", 13))
    # gen_lbl.grid(row=9, column=0, sticky='w', padx=10, pady=11)
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

    contact_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.contact1)
    contact_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

    calender_entry= cal.DateEntry(entry_frame,selectmode = 'day')
    calender_entry.grid(row=6, column=1, sticky='w', padx=10, pady=11)

    self.hour_string = StringVar()
    self.min_string = StringVar()
    self.sec_string =StringVar()
    last_value_sec = ""
    last_value = ""
    f = ('Times', 20)

    min_sb = Spinbox(
        entry_frame,
        from_=00,
        to=23,
        wrap=True,
        textvariable=self.hour_string,
        width=2,
        state="readonly",
        font=f,
        justify=CENTER
    )
    sec_hour = Spinbox(
        entry_frame,
        from_=00,
        to=59,
        wrap=True,
        textvariable=self.min_string,
        font=f,
        width=2,
        justify=CENTER
    )

    sec = Spinbox(
        entry_frame,
        from_=00,
        to=59,
        wrap=True,
        textvariable=self.sec_string,
        width=2,
        font=f,
        justify=CENTER
    )

    # min_sb.grid(row=7,column=0,padx=0,pady=0)
    min_sb.place(x=120,y=290)
    sec_hour.place(x=195,y=290)
    sec.place(x=260,y=290)

    # mail_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=api_key,width=10)
    # mail_entry.grid(row=8, column=1, sticky='w', padx=10, pady=11)
    #
    # mail_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=api_sec,width=10)
    # mail_entry.grid(row=9, column=1, sticky='w', padx=10, pady=11)

    # time_entry=

    # ***************Functions*********************

    def add_data():
        if self.name1.get() == "" or self.age1.get() == "" or self.gender1.get() == "" or len(
                self.contact1.get()) != 10:
            messagebox.showerror('Error', 'Required all fields and correct field')
        else:
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute('insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                self.name1.get(), self.age1.get(), self.gender1.get(), self.email1.get(), self.contact1.get(),
                self.suggested_psychiatrist1.get()))
            con.commit()
            con.close()
            fetch_data()
            clear_data()
            messagebox.showinfo('Success', 'Record has been submitted')

    def fetch_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        xe=f"select p_mail from psy_consult where psy_mail='{self.email}' and appointment_accepted=0"
        # print(xe)
        cur.execute(xe)
        row1 = cur.fetchall()
        s=''
        # print(len(row1))
        if len(row1)!=0:
            for r in row1:
               s+="email='"+r[0]+"' or "
            # print(s)
            s="select patient_name,age,sex,smoke_and_drink,email from patient where "+s[0:-4]
            # print(s)
            cur.execute(s)
            rows=cur.fetchall()
        else:
            rows=None
            self.totalrecord.set(0)

        if rows != None:
            self.totalrecord.set(len(rows))
            table.delete(*table.get_children())

            for row in rows:
                table.insert('', END, values=row)
            con.commit()
        else:
            self.totalrecord.set(0)
        con.commit()
        con.close()

    def clear_data():
        self.name1.set("")
        self.age1.set("")
        self.gender1.set("")
        self.email1.set("")
        self.contact1.set("")
        self.calendar1.set("")
        self.hour_string.set("")
        self.min_string.set("")
        self.sec_string.set("")
        # self.suggested_psychiatrist1.set("")

    def dsm():
        if self.email1.get()!='':
            p_frame.destroy()
            DSM5.f02(self,self.contact1.get())
        else:
            messagebox.showerror('Error', 'Invalid input mail')

    def schedule():
        if len(self.hour_string.get())<2:
            self.hour_string.set(str('0'+self.hour_string.get()))
        if len(self.min_string.get())<2:
            self.min_string.set(str('0'+self.min_string.get()))
        if len(self.sec_string.get())<2:
            self.sec_string.set(str('0'+self.sec_string.get()))
        date=f"{calender_entry.get()} "
        time=f"{self.hour_string.get()}:{self.min_string.get()}:{self.sec_string.get()}"
        time_chosen=date+time
        x=datetime.datetime.now()
        time_now=x.strftime('%x')+" "+x.strftime('%X')
        if self.name1.get()!="" and self.age1.get()!="" and self.email1.get()!="" and self.gender1.get()!="":
            # if api_key.get()!="" and api_sec.get()!="":
            if time_chosen>=time_now:
                # print(time_chosen)
                da = "20" + time_chosen[6:8] + "-" + time_chosen[3:5] + "-" + time_chosen[0:2] + "T" + time_chosen[
                                                                                                       9:11] + ": " + time_chosen[
                                                                                                                      12:14] + ": " + time_chosen[
                                                                                                                                      15:17]
                # print(da)
                try:
                    con=pymysql.connect(host='localhost', user='root', password='JBjose',
                                      database='pys')
                    cur = con.cursor()
                    cur.execute("select * from api where psy_mail=%s",(self.email,))
                    r=cur.fetchone()
                    s=str(r[2])
                    # print(r[1],r[2])
                    url=Zoom.createMeeting(r[1], r[2], da)
                    # url=Zoom.createMeeting(da)
                    print(url)
                    # print(str(time_chosen))
                    cur.execute("set sql_safe_updates=0")
                    cur.execute("update psy_consult set appointment_accepted=1,appointment_time=%s,link=%s where p_name=%s and psy_mail=%s and appointment_accepted=0",(time_chosen,url,self.name1.get(),self.email,))

                    con.commit()
                    cur.close()
                    messagebox.showinfo('Added','Appointment scheduled')
                    clear_data()
                    fetch_data()
                    Psychiatrist_home(self)
                except Exception as es:
                    messagebox.showerror("Error",f"Updating error : {es}")
            else:
                messagebox.showerror("Error","Invalid date/time chosen")
            # else:
            #     messagebox.showerror("ERROR","Invalid API key/secret")
        else:
            messagebox.showerror("Error","Check the Input fields")

    def focus(e):
        cursor = table.focus()
        content = table.item(cursor)
        row = content['values']
        self.name1.set(row[0])
        self.age1.set(row[1])
        self.gender1.set(row[2])
        self.email1.set(row[3])
        self.contact1.set(row[4])
        # self.suggested_psychiatrist1.set(row[5])

    def delete_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        if self.name1.get() != None and self.name1.get() != "":
            cur.execute('update psy_consult set appointment_accepted=2 where p_name=%s and psy_mail=%s and appointment_accepted=0', (self.name1.get(),self.email))
            con.commit()
            con.close()
            Psychiatrist_home(self)
            fetch_data()
            clear_data()
            messagebox.showinfo('Success', 'Record has been deleted')
        else:
            messagebox.showerror('Error', 'Invalid input')


    # **********Frame-3 Button**************

    btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='wheat')
    btn_frame.place(x=15, y=470, width=310, height=120)

    # add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7")
    # add_btn.grid(row=0, column=1, padx=50, pady=10)

    # update_btn = Button(btn_frame, text='Update', font=("", 12), command=update_data, width="7")
    # update_btn.grid(row=0, column=2, padx=10, pady=10)

    delete_btn = Button(btn_frame, text='Reject', font=("", 12), command=delete_data, width="7")
    delete_btn.grid(row=1, column=1,padx=10,pady=10)

    clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
    clear_btn.grid(row=1, column=3,padx=10,pady=10)

    # clear_btn = Button(btn_frame, text='View DSM5 Answersheet', font=("", 12), command=dsm)
    # clear_btn.grid(row=2, column=3,padx=10,pady=10)

    delete_btn = Button(btn_frame, text='Schedule', font=("", 12), command=schedule, width="7")
    delete_btn.grid(row=2, column=1,padx=10,pady=10)

    # ***********Frame-2***************
    data_frame = Frame(f1, bd=5, relief='ridge', bg='wheat')
    data_frame.place(x=360, y=0, width=1145, height=745)
    Button(data_frame,text="Refresh",command=fetch_data).pack()

    # # ***********Frame-2 code*****************
    # search_lbl = Label(data_frame, text="Search by", font=("", 13))
    # search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)
    #
    # search_combo = ttk.Combobox(data_frame, state='readonly', textvariable=self.search_by)
    # search_combo['values'] = ('patient_name', 'contact')
    # search_combo.current(0)
    # search_combo.grid(row=0, column=1, sticky='w', padx=10, pady=14)
    #
    # search_entry = Label(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
    # search_entry.grid(row=0, column=2, sticky='w', padx=10, pady=14)
    #
    # show_btn = Button(data_frame, text='Show', font=("", 12), command=search)
    # show_btn.grid(row=0, column=3, padx=10, pady=10)
    #
    # showall_btn = Button(data_frame, text='Show All', font=("", 12), command=fetch_data)
    # showall_btn.grid(row=0, column=4, padx=10, pady=10)
    #
    # total_lbl = Label(data_frame, text="Total Records", font=("", 13))
    # total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)
    #
    # totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
    # totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

    # ************Frame-3 Treeview***************
    view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
    view_frame.place(x=20, y=40, width=800, height=520)


    x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(view_frame, orient=VERTICAL)
    table = ttk.Treeview(view_frame,
                         columns=('patient_name', 'age', 'sex', 'drug', 'email'),
                         xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.configure(command=table.xview)
    y_scroll.configure(command=table.yview)

    table.heading("patient_name", text="Name")
    table.heading("age", text="Age")
    table.heading("sex", text="Gender")
    table.heading("drug", text="Smoke and Drinking(out of 5)")
    table.heading("email", text="E-mail")
    # table.heading("contact", text="Contact")
    # table.heading("suggested_psychiatrist", text="Suggested Psychiatrist")

    table.column("patient_name", width=100)
    table.column("age", width=100)
    table.column("sex", width=100)
    table.column("drug", width=100)
    table.column("email", width=100)
    # table.column("contact", width=100)
    # table.column("suggested_psychiatrist", width=100)
    table['show'] = 'headings'
    table.bind('<ButtonRelease-1>', focus)
    fetch_data()
    table.pack(fill=BOTH, expand=1)


    #Tab2
    f2 = Frame(tab2)
    f2.pack(fill=BOTH, expand=1)
    name2=StringVar()
    age2=StringVar()
    gender2=StringVar()
    drug2=StringVar()
    email2=StringVar()

    # btn2 = Button(f2, text="Logout", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
    # btn2.place(x=1000, y=8)
    # def dest():
    #     entry_frame.destroy()
    #     data_frame.destroy()
    #     headinglbl.destroy()
    #     btn1.destroy()
    #
    # btn1 = Button(f2, text="Home", cursor="hand2", command=dest, font=("times new roman", 15), fg="white",
    #               bg="orangered", bd=0, width=15, height=1)
    # btn1.place(x=10, y=8)

    # ***********Frame-1***************
    entry_frame = Frame(f2, bd=5, relief='ridge', bg='wheat')
    entry_frame.place(x=0, y=0, width=360, height=745)

    # Labels of frame-1
    # reg_lbl = Label(entry_frame, text="Patient details", font=("arial", 20, "bold"), bg='wheat', fg='red')
    # reg_lbl.grid(row=0, column=0)

    roll_lbl = Label(entry_frame, text="Name", font=("", 13))
    roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

    name_lbl = Label(entry_frame, text="Mail", font=("", 13))
    name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

    Fname_lbl = Label(entry_frame, text="Appointment Time:", font=("", 13))
    Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

    gen_lbl = Label(entry_frame, text="Link", font=("", 13))
    gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

    # cat_lbl = Label(entry_frame, text="E-mail", font=("", 13))
    # cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)
    #
    # branch_lbl = Label(entry_frame, text="Suggested \npsychiatrist", font=("", 13))
    # branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

    # Entry box of Frame-1
    roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=name2)
    roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

    name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=age2)
    name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

    gen_combo = Label(entry_frame, textvariable=gender2)
    # gen_combo['values'] = ('Male', 'Female')
    # gen_combo.current(0)
    gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

    # branch_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.suggested_psychiatrist1)
    # branch_combo['values'] = (
    #     'Multi-specialty psychiatrist', 'Child and adolescent psychiatrist', 'Addiction psychiatrist')
    # branch_combo.current(0)
    # branch_combo.grid(row=6, column=1, sticky='w', padx=10, pady=11)

    mail_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=drug2,width=15)
    mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

    # contact_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=email2)
    # contact_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

    # ***************Functions*********************
    def fetch_data():
        try:
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute('select p_name,p_mail,appointment_time,link from psy_consult where psy_mail=%s and appointment_accepted=1',self.email)
            rows = cur.fetchall()
            if rows != 0:
                self.totalrecord.set(len(rows))
                table1.delete(*table1.get_children())

                for row in rows:
                    table1.insert('', END, values=row)
                con.commit()
                con.close()
            else:
                Label(table1,text="NO APPOINTMENTS",font=("",16)).place(x=200,y=50)
        except Exception as es:
            messagebox.showerror("ERROR",f"due to:{es}")

    def clear_data():
        name2.set("")
        age2.set("")
        gender2.set("")
        drug2.set("")
        # email2.set("")
        # self.suggested_psychiatrist1.set("")

    def focus(e):
        cursor1 = table1.focus()
        content1 = table1.item(cursor1)
        row1 = content1['values']
        name2.set(row1[0])
        age2.set(row1[1])
        gender2.set(row1[2])
        drug2.set(row1[3])
        # email2.set(row1[4])
        # self.suggested_psychiatrist1.set(row1[5])

    def delete_data():
        con = pymysql.connect(host='localhost', user='root', password='JBjose',
                              database='pys')
        cur = con.cursor()
        if age2.get() != None and age2.get() != "":
            # print(age2.get(),self.email)
            cur.execute("set sql_safe_updates=0")
            cur.execute("update psy_consult set appointment_accepted=0,appointment_time='',link='' where p_mail=%s and psy_mail=%s", (age2.get(),self.email,))
            con.commit()
            con.close()
            fetch_data()
            clear_data()
            messagebox.showinfo('Success', 'Record has been deleted')
            Psychiatrist_home(self)
        else:
            messagebox.showerror('Error', 'Invalid input')

    def join():
        new = 1
        # drug2.set("www.google.com")
        link = drug2.get()
        webbrowser.open(link, new=new)


    def dsm1():
        if age2.get()!='' or age2.get()!=None:
            DSM5.f02(self,age2.get())
            p_frame.destroy()
        else:
            messagebox.showerror('Error', 'Invalid mail')

    # **********Frame-3 Button**************

    btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='wheat')
    btn_frame.place(x=15, y=430, width=310, height=130)

    # add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7")
    # add_btn.grid(row=0, column=1, padx=50, pady=10)

    # update_btn = Button(btn_frame, text='Update', font=("", 12), command=update_data, width="7")
    # update_btn.grid(row=0, column=2, padx=10, pady=10)

    delete_btn = Button(btn_frame, text='Delete Appointment', font=("", 12), command=delete_data)
    delete_btn.grid(row=1, column=1,padx=10,pady=10)

    clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
    clear_btn.grid(row=1, column=3,padx=10,pady=10)

    #
    delete_btn = Button(btn_frame, text='Join meeting', font=("", 12), command=join)
    delete_btn.grid(row=2, column=1,padx=10,pady=10)

    delete_btn = Button(btn_frame, text='DSM5\n Answersheet', font=("", 12), command=dsm1)
    delete_btn.grid(row=2, column=2,padx=10,pady=10)

    # ***********Frame-2***************
    data_frame = Frame(f2, bd=5, relief='ridge', bg='wheat')
    data_frame.place(x=360, y=0, width=1145, height=745)
    Button(data_frame, text="Refresh", command=fetch_data).pack()

    # # ***********Frame-2 code*****************
    # search_lbl = Label(data_frame, text="Search by", font=("", 13))
    # search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)
    #
    # search_combo = ttk.Combobox(data_frame, state='readonly', textvariable=self.search_by)
    # search_combo['values'] = ('patient_name', 'contact')
    # search_combo.current(0)
    # search_combo.grid(row=0, column=1, sticky='w', padx=10, pady=14)
    #
    # search_entry = Label(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
    # search_entry.grid(row=0, column=2, sticky='w', padx=10, pady=14)
    #
    # show_btn = Button(data_frame, text='Show', font=("", 12), command=search)
    # show_btn.grid(row=0, column=3, padx=10, pady=10)
    #
    # showall_btn = Button(data_frame, text='Show All', font=("", 12), command=fetch_data)
    # showall_btn.grid(row=0, column=4, padx=10, pady=10)
    #
    # total_lbl = Label(data_frame, text="Total Records", font=("", 13))
    # total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)
    #
    # totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
    # totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

    # ************Frame-3 Treeview***************
    view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
    view_frame.place(x=20, y=40, width=800, height=520)

    x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(view_frame, orient=VERTICAL)
    table1 = ttk.Treeview(view_frame,
                         columns=('patient_name', 'age', 'sex', 'drug'),
                         xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.configure(command=table1.xview)
    y_scroll.configure(command=table1.yview)

    table1.heading("patient_name", text="Patient Name")
    table1.heading("age", text="Patient Mail")
    table1.heading("sex", text="Appointment time")
    table1.heading("drug", text="Url link")
    # table1.heading("email", text="E-mail")
    # table1.heading("contact", text="Contact")
    # table1.heading("suggested_psychiatrist", text="Suggested Psychiatrist")

    table1.column("patient_name", width=100)
    table1.column("age", width=100)
    table1.column("sex", width=100)
    table1.column("drug", width=100)
    # table1.column("email", width=100)
    # table1.column("contact", width=100)
    # table1.column("suggested_psychiatrist", width=100)
    table1['show'] = 'headings'
    table1.bind('<ButtonRelease-1>', focus)
    fetch_data()
    table1.pack(fill=BOTH, expand=1)

