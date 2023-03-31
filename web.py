
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk
import mysql.connector

con = mysql.connector.Connect(host="localhost", user="root", password="Mani@01)*@))#", database="detaildb")
mw = Tk()

#Enter button
def enter(event):
    display()

#display data
def display():
    cur = con.cursor()
    roll=e1.get()
    info = "select * from stdinfo where roll='{}'".format(roll)
    cur.execute(info)
    result = cur.fetchall()
    if result==[]:
        messagebox.showinfo("error","No student found")
    else:
        print(result)
        for i, (roll, name, branch,atten,cgpa) in enumerate(result, 1):
            listBox.insert("", "end", values=(roll, name, branch,atten,cgpa))
    e1.delete(0,END)

#inserting data
def insert():
    def data():
        cur=con.cursor()
        name=e1.get()
        id=e2.get()
        branch=e3.get()
        cgpa=e4.get()
        attendence=e5.get()
        if name:
            op = "insert into stdinfo (roll,name,branch,atten,cgpa) values('{}','{}','{}',{},{})".format(id,name,branch,attendence,cgpa)
            cur.execute(op)
            con.commit()
            messagebox.showinfo("Msg","Inserted Succesfully!")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
        else:
            messagebox.showinfo("Error","No data inserted")
    entry = Tk()
    entry.title("New user")
    entry.config(bg='ghost white')
    entry.geometry("600x300")
    Label(entry,text="NEW USER:",font="Times 14",bg='ghost white').place(x=10,y=10)
    l = Label(entry, text="Enter Name : ", font="Times 14",bg='ghost white')
    l.place(x=10, y=40)
    Label(entry, text="Enter roll:", font="Times 14",bg='ghost white').place(x=10, y=70)
    Label(entry, text="Enter Branch:", font="Times 14",bg='ghost white').place(x=10, y=100)
    Label(entry, text="Enter cgpa:", font="Times 14",bg='ghost white').place(x=10, y=130)
    Label(entry, text="Enter attendence:", font="Times 14",bg='ghost white').place(x=10, y=160)
    e1 = Entry(entry, width=35)
    e1.place(x=140, y=40)
    e2 = Entry(entry,width=35)
    e2.place(x=140,y=70)
    e3=Entry(entry,width=20)
    e3.place(x=140,y=100)
    e4=Entry(entry,width=20)
    e4.place(x=140,y=130)
    e5=Entry(entry,width=20)
    e5.place(x=140,y=160)
    b3=Button(entry,text="SUBMIT",font="Times 14",bg='SkyBlue1',command=data)
    b3.place(x=140,y=220)
    b4=Button(entry,text="CLOSE",font="Times 14",bg='orange',command=entry.destroy)
    b4.place(x=140,y=260)

global e1
global e2
global e3
global e4
global e5
#mw.geometry("600x500")
roll = StringVar()
mw.title("NNRG")
logo = Image.open('nnrg.png')
logo = logo.resize((1100,150))
pic = ImageTk.PhotoImage(logo)
l = Label(mw, image=pic)
l.grid()
h = Label(mw, text="Enter HallTicket NO.", font="Times 14", width=15, height=2)
h.grid()
e1 = Entry(mw, textvariable=roll, width=35)
e1.bind("<Return>",enter)
e1.grid()
b1 = Button(mw, text="SUBMIT", font="Times 14",bg='SkyBlue1',state='disabled', command=display)
b1.grid()
b2 = Button(mw, text="New user?", font="Times 14", fg="white", bg="light sky blue", command=insert)
b2.grid()
def check(*args):
    if(len(roll.get())==10):
        b1.config(state='normal')
    else:
        b1.config(state='disabled')
cols = ('Roll', 'Name', 'Branch', 'Attendence', 'CGPA')
listBox = ttk.Treeview(mw, columns=cols, show="headings")
theme=ttk.Style(mw)
theme.theme_use("clam")
for col in cols:
    listBox.column(col,anchor=CENTER)
    listBox.heading(col, text=col,anchor=CENTER)
    listBox.grid()
    listBox.place()
b5=Button(mw,text='CLOSE',font='Times 14',bg='red2',fg='black',command=mw.destroy)
b5.grid()
roll.trace('w',check)
mw.mainloop()
