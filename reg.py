import sqlite3
from tkinter import *
from tkinter import messagebox
from sqlite3 import *
con=sqlite3.connect("detail.db")
def enter(event):
    insert()
def insert():
    cur=con.cursor()
    name=e1.get()
    mail=e2.get()
    mobile=e3.get()
    se=v.get()
    add=ad.get("1.0","end-1c")
    if se==1:
        sex='FEMALE'
    else:
        sex='MALE'
    if name and mail and mobile and v:
        inf="insert into data(name,mail,mobile,sex,address)values('{}','{}',{},'{}','{}')".format(name,mail,mobile,sex,add)
        cur.execute(inf)
        con.commit()
        messagebox.showinfo("MSG","Registered succesfully")
        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        ad.delete("1.0","end-1c")
    else:
        messagebox.showinfo("ERROR","Enter data!")
mw=Tk()
mw.title("Student registration")
mw.geometry('720x480')
global e1
global e2
global e3
l=Label(mw,text="Registration",font="Times 20",width=9,height=1)
l.place(x=300,y=10)

n=Label(mw,text="Enter Name : ",font="Times 14")
n.place(x=10,y=70)

e1=Entry(mw,width=35)
e1.place(x=150,y=74)

m=Label(mw,text="Enter Mail : ",font="Times 14")
m.place(x=10,y=100)

e2=Entry(mw,width=35)
e2.place(x=150,y=104)

p=Label(mw,text="Enter Mobile no. : ",font="Times 14")
p.place(x=10,y=130)

e3=Entry(mw,width=35)
e3.place(x=150,y=134)

g=Label(mw,text="Gender : ",font="Times 14")
g.place(x=10,y=164)

v=IntVar()
fe=Radiobutton(mw,text="FEMALE",font="Times 12",variable=v,value=1)
fe.place(x=150,y=164)

ma=Radiobutton(mw,text="MALE",font="Times 12",variable=v,value=2)
ma.place(x=260,y=164)

s=Label(mw,text="Subject : ",font="Times 16")
s.place(x=10,y=194)

#check boxes
c1=Checkbutton(mw,text="Python",font="Times 15")
c1.place(x=150,y=195)

c2=Checkbutton(mw,text="CPP",font="Times 14")
c2.place(x=250,y=195)

c3=Checkbutton(mw,text="Java",font="Times 14")
c3.place(x=150,y=225)

c1=Checkbutton(mw,text="C",font="Times 15")
c1.place(x=250,y=225)

a=Label(mw,text="Address : ",font="Times 14")
a.place(x=10,y=265)

ad=Text(mw,width=40,height=5)
ad.place(x=150,y=265)

b1=Button(mw,text="CANCEL",font="Times 14",bg="white",command=mw.destroy)
b1.place(x=150,y=380)

b2=Button(mw,text="SUBMIT",font="Times 14",bg="orange",command=insert)
b2.bind("<Return>",enter)
b2.place(x=350,y=380)
mw.mainloop()