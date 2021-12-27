from tkinter import messagebox

import mysql.connector
from tkinter import *

import psychiatrist_home


def psy_pending(self):
    self.root.title("Application pending")
    frame_psyhome= Canvas(self.root,bg='White')
    fram(frame_psyhome,frame_psyhome)
    frame_psyhome.place(x=0,y=0,width=1366, height=700)
    # btn2 = Button(frame_psyhome, text="Logout", command=self.loginform, cursor="hand2", font=("times new roman", 15),
    #               fg="white", bg="orangered", bd=0, width=15, height=1)
    Label(frame_psyhome, text="Sorry\n Seems Your application haven't got approved yet",
          font=("Times new roman", 32, "bold"), fg="red",bg='White').place(x=220, y=300)
def psy_rejected(self):
    self.root.title("Application rejected")
    frame_psyhome= Frame(self.root)
    frame_psyhome.place(x=0,y=0,width=1366, height=700)
    fram(frame_psyhome,frame_psyhome)
    def reapply():
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='JBjose',database='pys')
            cur=con.cursor()
            cur.execute('delete from psychiatrist where email=%s',(self.email,))
            cur.execute('update register set form=0 where username=%s and email=%s',(self.name,self.email,))
            con.commit()
            con.close()
            messagebox.showinfo('Note','Login to re apply', parent=self.root)
            frame_psyhome.destroy()
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'

                                 , parent=self.root)
            print(str(es))
    def del_acc():
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='JBjose',database='pys')
            cur=con.cursor()
            cur.execute('delete from psychiatrist where email=%s',(self.email,))
            cur.execute('delete from register where username=%s and email=%s',(self.name,self.email,))
            con.commit()
            con.close()
            messagebox.showerror('Note','Account deleted successfully', parent=self.root)
            frame_psyhome.destroy()
        except Exception as es:
            messagebox.showerror('Error', f'Error Due to : {str(es)}'

                                 , parent=self.root)
            print(str(es))

    Label(frame_psyhome, text="Sorry\n Seems Your application got rejected",
          font=("Times new roman", 32, "bold"), fg="red",bg='White').place(x=220, y=300)
    btn2 = Button(frame_psyhome, text="Re-apply", command=reapply, cursor="hand2", font=("times new roman", 12),bg='#1E94DC',fg='white')
    btn3 = Button(frame_psyhome, text="Delete account", command=del_acc, cursor="hand2", font=("times new roman", 12),bg='#1E94DC',fg='white')
    btn2.place(x=520,y=465)
    btn3.place(x=500,y=520)
def fram(f1,f2):
    def dest():
        f2.destroy()
        btn1.destroy()
    btn1 = Button(f1, text="Back", cursor="hand2", command=dest, font=("times new roman", 15), fg="white",
                  bg="orangered", bd=0, width=15, height=1)
    btn1.place(x=10, y=8)
