from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='Mani@01)*@))#', database='stdb')
def insert(roll, name, branch):
    res = con.cursor()
    op = "insert into studinfo (roll,name,branch) values (%s,%s,%s)"
    data = (roll, name, branch)
    res.execute(op,data)
    con.commit()
    print("Data inserted succesfully")
def delete(roll):
    res = con.cursor()
    op = "delete from studinfo where roll=%s"
    data = (roll,)
    res.execute(op, data)
    con.commit()
    print("Deleted")
def update(roll, name, branch, id):
    res = con.cursor()
    op = "update studinfo set roll=%s,name=%s,branch=%s where roll=%s"
    data = (roll, name, branch, id)
    res.execute(op, data)
    con.commit()
    print("Updated")
def select():
    res = con.cursor()
    op = "select * from studinfo order by roll ASC"
    res.execute(op)
    result = res.fetchall()
    print(tabulate(result, headers=["ROLL NO.", "NAME", "BRANCH"]))
    print()
while True:
    print("1.Insert Data")
    print("2.Delete Data")
    print("3.Display")
    print("4.Update data")
    print("5.exit")
    choice = int(input("Enter your choice : "))
    print()
    if choice == 1:
        name = input("Enter your Name: ")
        roll = input("Enter your Roll no.: ")
        branch = input("Enter your Branch: ")
        insert(roll, name, branch)
    elif choice == 2:
        roll = input("Enter Roll to delete : ")
        
        delete(roll)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter Previous roll: ")
        name = input("Enter your name: ")
        roll = input("Enter your Roll no.: ")
        branch = input("Enter your Branch: ")
        update(roll, name, branch, id)
    elif choice == 5:
        quit()
    else:
        print(("Enter valid choice"))

