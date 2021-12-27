from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class admin_Patients:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1300x700")

        self.name1 = StringVar()
        self.age1 = StringVar()
        self.gender1 = StringVar()
        self.email1 = StringVar()
        self.contact1 = StringVar()
        self.suggested_psychiatrist1 = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.totalrecord = StringVar()

    def now(self):
        self.root.title("Managing patient")
        headinglbl = Label(self.root, text="Patient management", font=("arial", 24, "bold"), bg='wheat', fg='red')
        headinglbl.place(x=500, y=8)

        # btn2 = Button(self.root, text="Logout", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        # btn2.place(x=1000, y=8)
        def dest():
            entry_frame.destroy()
            data_frame.destroy()
            headinglbl.destroy()
            btn1.destroy()

        btn1 = Button(self.root, text="Home", cursor="hand2", command=dest, font=("times new roman", 15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn1.place(x=10, y=8)

        # ***********Frame-1***************
        entry_frame = Frame(self.root, bd=5, relief='ridge', bg='wheat')
        entry_frame.place(x=20, y=50, width=360, height=745)

        # Labels of frame-1
        reg_lbl = Label(entry_frame, text="Patient details", font=("arial", 20, "bold"), bg='wheat', fg='red')
        reg_lbl.grid(row=0, columnspan=2)

        roll_lbl = Label(entry_frame, text="Name", font=("", 13))
        roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        name_lbl = Label(entry_frame, text="Age", font=("", 13))
        name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        Fname_lbl = Label(entry_frame, text="Gender", font=("", 13))
        Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        gen_lbl = Label(entry_frame, text="E-mail", font=("", 13))
        gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        cat_lbl = Label(entry_frame, text="Contact no", font=("", 13))
        cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        branch_lbl = Label(entry_frame, text="Suggested \npsychiatrist", font=("", 13))
        branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        # Entry box of Frame-1
        roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.name1)
        roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

        name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.age1)
        name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

        gen_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.gender1)
        gen_combo['values'] = ('Male', 'Female')
        gen_combo.current(0)
        gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        branch_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.suggested_psychiatrist1)
        branch_combo['values'] = (
        'Multi-specialty psychiatrist', 'Child and adolescent psychiatrist', 'Addiction psychiatrist')
        branch_combo.current(0)
        branch_combo.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        mail_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.email1)
        mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        contact_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.contact1)
        contact_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

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
            cur.execute('select patient_name,age,sex,email,contact,suggested_psychiatrist from patient')
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
            self.contact1.set("")
            self.suggested_psychiatrist1.set("")

        def focus(e):
            cursor = table.focus()
            content = table.item(cursor)
            row = content['values']
            self.name1.set(row[0])
            self.age1.set(row[1])
            self.gender1.set(row[2])
            self.email1.set(row[3])
            self.contact1.set(row[4])
            self.suggested_psychiatrist1.set(row[5])

        def update_data():
            if self.name1.get() == "" or self.age1.get() == "" or self.gender1.get() == "" or self.suggested_psychiatrist1.get() == "" or self.email1.get() == "" or len(
                    self.contact1.get()) != 10:
                messagebox.showerror('Error', 'Required all fields and correct fields')
            else:
                con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                      database='pys')
                cur = con.cursor()
                cur.execute(
                    'update patient set patient_name=%s , age=%s , sex=%s , email=%s , contact=%s , suggested_psychiatrist=%s',
                    (self.name1.get(), self.age1.get(), self.gender1.get(), self.email1.get(), self.contact1.get(),
                     self.suggested_psychiatrist1.get(),
                     ))
                con.commit()
                con.close()
                fetch_data()
                clear_data()
                messagebox.showinfo('Success', 'Record has been updated')

        def delete_data():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            if self.name1.get()!=None and self.name1.get()!="":
                cur.execute('delete from patient where patient_name=%s ', self.name1.get())
                con.commit()
                con.close()
                fetch_data()
                clear_data()
                messagebox.showinfo('Success', 'Record has been deleted')
            else:
                messagebox.showerror('Error', 'Invalid input')

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

        delete_btn = Button(btn_frame, text='Delete', font=("", 12), command=delete_data, width="7")
        delete_btn.grid(row=1, column=1, padx=50, pady=10)

        clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
        clear_btn.grid(row=1, column=2, padx=10, pady=10)

        # ***********Frame-2***************
        data_frame = Frame(self.root, bd=5, relief='ridge', bg='wheat')
        data_frame.place(x=380, y=50, width=1145, height=745)

        # ***********Frame-2 code*****************
        search_lbl = Label(data_frame, text="Search by", font=("", 13))
        search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)

        search_combo = ttk.Combobox(data_frame, state='readonly', textvariable=self.search_by)
        search_combo['values'] = ('patient_name', 'contact')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, sticky='w', padx=10, pady=14)

        search_entry = Entry(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
        search_entry.grid(row=0, column=2, sticky='w', padx=10, pady=14)

        show_btn = Button(data_frame, text='Show', font=("", 12), command=search)
        show_btn.grid(row=0, column=3, padx=10, pady=10)

        showall_btn = Button(data_frame, text='Show All', font=("", 12), command=fetch_data)
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        total_lbl = Label(data_frame, text="Total Records", font=("", 13))
        total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)

        totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
        totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

        # ************Frame-3 Treeview***************
        view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
        view_frame.place(x=20, y=100, width=800, height=520)

        x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
        y_scroll = Scrollbar(view_frame, orient=VERTICAL)
        table = ttk.Treeview(view_frame,
                             columns=('patient_name', 'age', 'sex', 'email', 'contact', 'suggested_psychiatrist'),
                             xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.configure(command=table.xview)
        y_scroll.configure(command=table.yview)

        table.heading("patient_name", text="Name")
        table.heading("age", text="Age")
        table.heading("sex", text="Gender")
        table.heading("email", text="E-mail")
        table.heading("contact", text="Contact")
        table.heading("suggested_psychiatrist", text="Suggested Psychiatrist")

        table.column("patient_name", width=100)
        table.column("age", width=100)
        table.column("sex", width=100)
        table.column("email", width=100)
        table.column("contact", width=100)
        table.column("suggested_psychiatrist", width=100)
        table['show'] = 'headings'
        table.bind('<ButtonRelease-1>', focus)
        fetch_data()
        table.pack(fill=BOTH, expand=1)

    def now1(self):
        self.root.title("Manage Psychiatrist")
        headinglbl = Label(self.root, text="Psychiatrists", font=("arial", 24, "bold"), bg='wheat',
                           fg='red')
        headinglbl.place(x=500, y=8)

        # btn2 = Button(self.root, text="Logout", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        # btn2.place(x=1000, y=8)
        def dest():
            entry_frame.destroy()
            data_frame.destroy()
            headinglbl.destroy()
            btn1.destroy()

        btn1 = Button(self.root, text="Back", cursor="hand2", command=dest, font=("times new roman", 15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn1.place(x=10, y=8)

        # ***********Frame-1***************
        entry_frame = Frame(self.root, bd=5, relief='ridge', bg='wheat')
        entry_frame.place(x=20, y=50, width=360, height=745)

        # Labels of frame-1
        reg_lbl = Label(entry_frame, text="Psychiatrist details", font=("arial", 20, "bold"), bg='wheat', fg='red')
        reg_lbl.grid(row=0, columnspan=2)

        roll_lbl = Label(entry_frame, text="Name", font=("", 13))
        roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        name_lbl = Label(entry_frame, text="Age", font=("", 13))
        name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        Fname_lbl = Label(entry_frame, text="Gender", font=("", 13))
        Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        gen_lbl = Label(entry_frame, text="E-mail", font=("", 13))
        gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        cat_lbl = Label(entry_frame, text="Contact no", font=("", 13))
        cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        branch_lbl = Label(entry_frame, text="Psychiatrist type", font=("", 13))
        branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        # Entry box of Frame-1
        roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.name1)
        roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

        name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.age1)
        name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

        gen_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.gender1)
        gen_combo['values'] = ('Male', 'Female')
        gen_combo.current(0)
        gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        branch_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.suggested_psychiatrist1)
        branch_combo['values'] = (
            'Multi-specialty psychiatrist', 'Child and adolescent psychiatrist', 'Addiction psychiatrist')
        branch_combo.current(0)
        branch_combo.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        mail_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.email1)
        mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        contact_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.contact1)
        contact_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

        # ***************Functions*********************

        def add_data():
            if self.name1.get() == "" or self.age1.get() == "" or self.gender1.get() == "" or len(
                    self.contact1.get()) != 10:
                messagebox.showerror('Error', 'Required all fields and correct field')
            else:
                con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                      database='pys')
                cur = con.cursor()
                cur.execute('insert into psychiatrist values(%s,%s,%s,%s,%s,%s)', (
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
            cur.execute('select name,age,sex,email,contact,psychiatrist_type from psychiatrist where got_approved=1')
            rows = cur.fetchall()

            if rows != 0:
                self.totalrecord.set(len(rows))
                table.delete(*table.get_children())
                for row in rows:
                    table.insert('', END, values=row)
                con.commit()
            else:
                l1 = Label(entry_frame, text="NO Requests")
                l1.place(x=50, y=50)
            con.close()

        def clear_data():
            self.name1.set("")
            self.age1.set("")
            self.gender1.set("")
            self.email1.set("")
            self.contact1.set("")
            self.suggested_psychiatrist1.set("")

        def focus(e):
            cursor = table.focus()
            content = table.item(cursor)
            row = content['values']
            self.name1.set(row[0])
            self.age1.set(row[1])
            self.gender1.set(row[2])
            self.email1.set(row[3])
            self.contact1.set(row[4])
            self.suggested_psychiatrist1.set(row[5])

        def update_data():
            if self.name1.get() == "" or self.age1.get() == "" or self.gender1.get() == "" or self.suggested_psychiatrist1.get() == "" or self.email1.get() == "" or len(
                    self.contact1.get()) != 10:
                messagebox.showerror('Error', 'Required all fields and correct fields')
            else:
                con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                      database='pys')
                cur = con.cursor()
                cur.execute(
                    'update psychiatrist set patient_name=%s , age=%s , sex=%s , email=%s , contact=%s , suggested_psychiatrist=%s',
                    (self.name1.get(), self.age1.get(), self.gender1.get(), self.email1.get(), self.contact1.get(),
                     self.suggested_psychiatrist1.get(),
                     ))
                con.commit()
                con.close()
                fetch_data()
                clear_data()
                messagebox.showinfo('Success', 'Record has been updated')

        def delete_data():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            if self.name1.get()!=None and self.name1.get()!="":
                cur.execute('delete from psychiatrist where name=%s and got_approved=1 ', self.name1.get())
                cur.execute('update register set form=1 where username=%s ', self.name1.get())
                con.commit()
                con.close()
                fetch_data()
                clear_data()
                messagebox.showinfo('Success', 'Record has been deleted')
            else:
                messagebox.showerror('Error', 'Invalid input')

        def approve():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute('set sql_safe_updates=0')
            cur.execute('update psychiatrist set got_approved=1 where name=%s ', self.name1.get())
            cur.execute('update register set form=2 where username=%s and email=%s ',
                        (self.name1.get(), self.email1.get(),))
            con.commit()
            con.close()
            messagebox.showinfo('Success', f'{self.name1.get()}, Psychiatrist has been approved')
            fetch_data()
            clear_data()

        def search():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute("select name,age,sex,email,contact,psychiatrist_type from psychiatrist where " + str(
                self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%' and got_approved=1")
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

        # update_btn = Button(btn_frame, text='Approve', font=("", 12), command=approve, width="7")
        # update_btn.grid(row=1, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text='Delete', font=("", 12), command=delete_data, width="7")
        delete_btn.grid(row=0, column=1, padx=50, pady=10)

        clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
        clear_btn.grid(row=0, column=2, padx=10, pady=10)

        # ***********Frame-2***************
        data_frame = Frame(self.root, bd=5, relief='ridge', bg='wheat')
        data_frame.place(x=380, y=50, width=1145, height=745)

        # ***********Frame-2 code*****************
        search_lbl = Label(data_frame, text="Search by", font=("", 13))
        search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)

        search_combo = ttk.Combobox(data_frame, state='readonly', textvariable=self.search_by)
        search_combo['values'] = ('name', 'psychiatrist_type')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, sticky='w', padx=10, pady=14)

        search_entry = Entry(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
        search_entry.grid(row=0, column=2, sticky='w', padx=10, pady=14)

        show_btn = Button(data_frame, text='Show', font=("", 12), command=search)
        show_btn.grid(row=0, column=3, padx=10, pady=10)

        showall_btn = Button(data_frame, text='Show All', font=("", 12), command=fetch_data)
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        total_lbl = Label(data_frame, text="Total Records", font=("", 13))
        total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)

        totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
        totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

        # ************Frame-3 Treeview***************
        view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
        view_frame.place(x=20, y=100, width=800, height=520)

        x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
        y_scroll = Scrollbar(view_frame, orient=VERTICAL)
        table = ttk.Treeview(view_frame, columns=('name', 'age', 'sex', 'email', 'contact', 'psychiatrist_type'),
                             xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.configure(command=table.xview)
        y_scroll.configure(command=table.yview)

        table.heading("name", text="Name")
        table.heading("age", text="Age")
        table.heading("sex", text="Gender")
        table.heading("email", text="E-mail")
        table.heading("contact", text="Contact")
        table.heading("psychiatrist_type", text="Suggested Psychiatrist")

        table.column("name", width=100)
        table.column("age", width=100)
        table.column("sex", width=100)
        table.column("email", width=100)
        table.column("contact", width=100)
        table.column("psychiatrist_type", width=100)
        table['show'] = 'headings'
        table.bind('<ButtonRelease-1>', focus)
        fetch_data()
        table.pack(fill=BOTH, expand=1)


    def now2(self):
        self.root.title("Psychiatrist account Request")
        headinglbl = Label(self.root, text="Request from Psychiatrists", font=("arial", 24, "bold"), bg='wheat',
                           fg='red')
        headinglbl.place(x=450, y=8)

        # btn2 = Button(self.root, text="Logout", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        # btn2.place(x=1000, y=8)
        def dest():
            entry_frame.destroy()
            data_frame.destroy()
            headinglbl.destroy()
            btn1.destroy()

        btn1 = Button(self.root, text="Back", cursor="hand2", command=dest, font=("times new roman", 15), fg="white",
                      bg="orangered", bd=0, width=15, height=1)
        btn1.place(x=10, y=8)

        # ***********Frame-1***************
        entry_frame = Frame(self.root, bd=5, relief='ridge', bg='wheat')
        entry_frame.place(x=20, y=50, width=360, height=745)

        # Labels of frame-1
        reg_lbl = Label(entry_frame, text="Requests pending", font=("arial", 20, "bold"), bg='wheat', fg='red')
        reg_lbl.grid(row=0, columnspan=2)

        roll_lbl = Label(entry_frame, text="Name", font=("", 13))
        roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        name_lbl = Label(entry_frame, text="Age", font=("", 13))
        name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        Fname_lbl = Label(entry_frame, text="Gender", font=("", 13))
        Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        gen_lbl = Label(entry_frame, text="E-mail", font=("", 13))
        gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        cat_lbl = Label(entry_frame, text="Contact no", font=("", 13))
        cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        branch_lbl = Label(entry_frame, text="Psychiatrist type", font=("", 13))
        branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        # Entry box of Frame-1
        roll_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.name1)
        roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

        name_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.age1)
        name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

        gen_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.gender1)
        gen_combo['values'] = ('Male', 'Female')
        gen_combo.current(0)
        gen_combo.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        branch_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.suggested_psychiatrist1)
        branch_combo['values'] = (
        'Multi-specialty psychiatrist', 'Child and adolescent psychiatrist', 'Addiction psychiatrist')
        branch_combo.current(0)
        branch_combo.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        mail_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.email1)
        mail_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        contact_entry = Label(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.contact1)
        contact_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

        # ***************Functions*********************

        def add_data():
            if self.name1.get() == "" or self.age1.get() == "" or self.gender1.get() == "" or len(
                    self.contact1.get()) != 10:
                messagebox.showerror('Error', 'Required all fields and correct field')
            else:
                con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                      database='pys')
                cur = con.cursor()
                cur.execute('insert into psychiatrist values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
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
            cur.execute('select name,age,sex,email,contact,psychiatrist_type from psychiatrist where got_approved=0')
            rows = cur.fetchall()

            if rows != 0:
                self.totalrecord.set(len(rows))
                table.delete(*table.get_children())

                for row in rows:
                    table.insert('', END, values=row)
                con.commit()
            else:
                l1 = Label(entry_frame, text="NO Requests")
                l1.place(x=50, y=50)
            con.close()

        def clear_data():
            self.name1.set("")
            self.age1.set("")
            self.gender1.set("")
            self.email1.set("")
            self.contact1.set("")
            self.suggested_psychiatrist1.set("")

        def focus(e):
            cursor = table.focus()
            content = table.item(cursor)
            row = content['values']
            self.name1.set(row[0])
            self.age1.set(row[1])
            self.gender1.set(row[2])
            self.email1.set(row[3])
            self.contact1.set(row[4])
            self.suggested_psychiatrist1.set(row[5])

        def update_data():
            if self.name1.get() == "" or self.age1.get() == "" or self.gender1.get() == "" or self.suggested_psychiatrist1.get() == "" or self.email1.get() == "" or len(
                    self.contact1.get()) != 10:
                messagebox.showerror('Error', 'Required all fields and correct fields')
            else:
                con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                      database='pys')
                cur = con.cursor()
                cur.execute(
                    'update psychiatrist set patient_name=%s , age=%s , sex=%s , email=%s , contact=%s , suggested_psychiatrist=%s',
                    (self.name1.get(), self.age1.get(), self.gender1.get(), self.email1.get(), self.contact1.get(),
                     self.suggested_psychiatrist1.get(),
                     ))
                con.commit()
                con.close()
                fetch_data()
                clear_data()
                messagebox.showinfo('Success', 'Record has been updated')

        def delete_data():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            if self.name1.get()!=None and self.name1.get()!="":
                cur.execute('delete from psychiatrist where name=%s and got_approved=0 ', self.name1.get())
                cur.execute('update register set form=3 where username=%s ', self.name1.get())
                con.commit()
                con.close()
                fetch_data()
                clear_data()
                messagebox.showinfo('Success', 'Record has been deleted')
            else:
                messagebox.showerror('Error', 'Invalid input')

        def approve():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            if self.name1.get()!=None and self.name1.get()!="":
                cur.execute('set sql_safe_updates=0')
                cur.execute('update psychiatrist set got_approved=1 where name=%s ', self.name1.get())
                cur.execute('update register set form=2 where username=%s and email=%s ',
                            (self.name1.get(), self.email1.get(),))
                con.commit()
                con.close()
                messagebox.showinfo('Success', f'{self.name1.get()}, Psychiatrist has been approved')
            else:
                messagebox.showerror('Error', 'Invalid input')
            fetch_data()
            clear_data()

        def search():
            con = pymysql.connect(host='localhost', user='root', password='JBjose',
                                  database='pys')
            cur = con.cursor()
            cur.execute("select name,age,sex,email,contact,psychiatrist_type from psychiatrist where " + str(
                self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%' and got_approved=0")
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
        btn_frame.place(x=15, y=430, width=310, height=120)

        # add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7")
        # add_btn.grid(row=0, column=1, padx=50, pady=10)

        update_btn = Button(btn_frame, text='Approve', font=("", 12), command=approve, width="7")
        update_btn.grid(row=1, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text='Reject', font=("", 12), command=delete_data, width="7")
        delete_btn.grid(row=0, column=1, padx=50, pady=10)

        clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7")
        clear_btn.grid(row=0, column=2, padx=10, pady=10)

        # ***********Frame-2***************
        data_frame = Frame(self.root, bd=5, relief='ridge', bg='wheat')
        data_frame.place(x=380, y=50, width=1145, height=745)

        # ***********Frame-2 code*****************
        search_lbl = Label(data_frame, text="Search by", font=("", 13))
        search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)

        search_combo = ttk.Combobox(data_frame, state='readonly', textvariable=self.search_by)
        search_combo['values'] = ('name', 'psychiatrist_type')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, sticky='w', padx=10, pady=14)

        search_entry = Entry(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
        search_entry.grid(row=0, column=2, sticky='w', padx=10, pady=14)

        show_btn = Button(data_frame, text='Show', font=("", 12), command=search)
        show_btn.grid(row=0, column=3, padx=10, pady=10)

        showall_btn = Button(data_frame, text='Show All', font=("", 12), command=fetch_data)
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        total_lbl = Label(data_frame, text="Total Records", font=("", 13))
        total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)

        totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
        totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

        # ************Frame-3 Treeview***************
        view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
        view_frame.place(x=20, y=100, width=800, height=520)

        x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
        y_scroll = Scrollbar(view_frame, orient=VERTICAL)
        table = ttk.Treeview(view_frame, columns=('name', 'age', 'sex', 'email', 'contact', 'psychiatrist_type'),
                             xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.configure(command=table.xview)
        y_scroll.configure(command=table.yview)

        table.heading("name", text="Name")
        table.heading("age", text="Age")
        table.heading("sex", text="Gender")
        table.heading("email", text="E-mail")
        table.heading("contact", text="Contact")
        table.heading("psychiatrist_type", text="Suggested Psychiatrist")

        table.column("name", width=100)
        table.column("age", width=100)
        table.column("sex", width=100)
        table.column("email", width=100)
        table.column("contact", width=100)
        table.column("psychiatrist_type", width=100)
        table['show'] = 'headings'
        table.bind('<ButtonRelease-1>', focus)
        fetch_data()
        table.pack(fill=BOTH, expand=1)
