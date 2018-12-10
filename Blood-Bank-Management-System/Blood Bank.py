from tkinter import *
import cx_Oracle
import os

connectString = os.getenv('con_connect')
con = cx_Oracle.connect('system/deepak123@127.0.0.1/InsuranceManagement')
cursor = con.cursor()
root = Tk()
image1 = PhotoImage(file="C://users/admin/Desktop/blood.png")
panel = Label(root, image=image1, bg="black").place(x=0, y=0, relwidth=1, relheight=1)
root.title("BLOOD BANK")
root.geometry("1200x672")
root.configure(background='white')
l3 = Label(root, text="BLOOD BANK SYSTEM", bg='pink', font="Helvetica 15 bold",fg='Black').place(x=450, y=40, w=300, h=40)
l1 = Label(root, text="Click to enter the details of the donor", bg='orange', font="Helvetica 12").place(x=80, y=100,
                                                                                                        w=300, h=40)
b1 = Button(root, text="Donor Details", command=lambda: donordetails()).place(x=80, y=150)
l2 = Label(root, text="Click to enter the details of the blood",bg='magenta', font="Helvetica 12").place(x=80, y=200,
                                                                                                        w=300, h=40)
b2 = Button(root, text="Blood Details", command=lambda: blooddetails()).place(x=80, y=250)
l3 = Label(root, text="Click to make a request for blood", bg='cyan', font="Helvetica 12").place(x=80, y=300, w=300,
                                                                                                  h=40)
b3 = Button(root, text="Blood Request", command=lambda: requestblood()).place(x=80, y=350)
b2 = Button(root, text="EXIT", command=lambda: stop(root)).place(x=220, y=400)
v = StringVar()


def insertDonor(name, age, gender, address, contactno,id):
    insert = "INSERT INTO donor(name,age,gender,address,contactno,id) VALUES(:1,:2,:3,:4,:5,:6)"
    cursor.execute(insert,(name,int(age),gender,address,int(contactno),int(id)))
    con.commit()



def insertBlood(bloodgroup, platelet, rbc,id):
    insert = "INSERT INTO blood(bloodgroup,platelet,rbc,regdate,id) VALUES(:1,:2,:3,SYSDATE,:4)"


    cursor.execute(insert,(bloodgroup,platelet,rbc,id))
    con.commit()


def retrieve(bg):
    request = "select * from donor d,blood b where d.id=b.id and b.bloodgroup='" + bg + "'"
    cursor.execute(request)
    rows = cursor.fetchall()
    con.commit()
    print(len(rows))
    return rows


def sel():
    selection = "You selected the option " + str(v.get())
    print(selection)


def donordetails():
    # global v
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("480x480")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12",background='#FF8F8F').place(x=80, y=40)
    l2 = Label(root, text="Age:", bg='white', font="Helvetica 12",background='#FF8F8F').place(x=80, y=80)
    l3 = Label(root, text="Gender:", bg='white', font="Helvetica 12",background='#FF8F8F').place(x=80, y=120)
    l4 = Label(root, text="Address:", bg='white', font="Helvetica 12",background='#FF8F8F').place(x=80, y=220)
    l5 = Label(root, text="Contact:", bg='white', font="Helvetica 12",background='#FF8F8F').place(x=80, y=260)
    l6 = Label(root, text="ID:", bg='white', font="Helvetica 12",background='#FF8F8F').place(x=80, y=300)
    e1 = Entry(root)
    e1.place(x=160, y=40)
    e2 = Entry(root)
    e2.place(x=160, y=80)
    r1 = Radiobutton(root, text="Male", variable=v, value="Male", command=sel,background='#FF8F8F').place(x=160, y=120)
    v.set(3)
    r2 = Radiobutton(root, text="Female", variable=v, value="Female", command=sel,background='#FF8F8F').place(x=160, y=150)
    r3 = Radiobutton(root, text="Other", variable=v, value="Other", command=sel,background='#FF8F8F').place(x=160, y=180)
    # e3=Entry(root)
    # e3.place(x=100,y=120)
    e4 = Entry(root)
    e4.place(x=160, y=220)
    e5 = Entry(root)
    e5.place(x=160, y=260)
    e6=Entry(root)
    e6.place(x=160,y=300)
    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=160,y=340)

    b1=Button(root,text="Submit",command=lambda : insertDonor(e1.get(),e2.get(),str(v.get()),e4.get(),e5.get(),e6.get())).place(x=80,y=340)

    root.mainloop()


def blooddetails():
    root = Tk()
    root.title("BLOOD BANK")
    root.geometry("500x360")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="ID:", font="Helvetica 12",background='#FF8F8F').place(x=40, y=40, w=250, h=20)
    l1 = Label(root, text="Blood Group:", font="Helvetica 12",background='#FF8F8F').place(x=40, y=80, w=250, h=20)
    l2 = Label(root, text="PLatetelet count (in 100 thousands):", font="Helvetica 12",background='#FF8F8F').place(x=40, y=120, w=250, h=20)
    l3 = Label(root, text="RBC count (in millions):", font="Helvetica 12",background='#FF8F8F').place(x=40, y=160, w=250, h=20)
    # l4=Label(root,text="Date Of Entry count:").place(x=40,y=160)
    e4=Entry(root)
    e4.place(x=350,y=40)
    e1 = Entry(root)
    e1.place(x=350, y=80)
    e2 = Entry(root)
    e2.place(x=350, y=120)
    e3 = Entry(root)
    e3.place(x=350, y=160)
    b2 = Button(root, text="Back", command=lambda: stop(root)).place(x=200, y=200)
    b1 = Button(root, text="Submit", command=lambda: insertBlood(e1.get(), e2.get(), e3.get(),e4.get())).place(x=40, y=200)

    # img = PhotoImage(file="/home/aishwarya/Downloads/b1.gif")
    # panel = Label(root, image = img,bg="#F6B88D").place(x=200,y=200,w=400,h=400)

    root.mainloop()


def grid1(bg):
    root = Tk()
    root.title("LIST OF MATCHING DONORS")
    root.geometry("1280x480")
    root.configure(background='#0C43F0')
    rows = retrieve(bg)
    Label(root, text='NAME', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=0, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='AGE', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=1, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='GENDER', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=2, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='ADDRESS', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=3, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='CONTACT NO', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=4, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='ID', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=5, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='BLOOD GROUP', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=6, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='PLATELET', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=7, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
    Label(root, text='RBC', bg="#0C43F0", font="Verdana 15 bold").grid(row=0, column=8, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)

    x = 1
    for row in rows:
        Label(root, text=row[0], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[1], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[2], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[3], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[4], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=4, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[5], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=5, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[6], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=6, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[7], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=7, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        Label(root, text=row[8], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=8, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)

        x = x + 1
    root.mainloop()


def requestblood():
    root = Tk()
    root.title("BLOOD BANK")
    root.geometry("720x360")
    root.configure(background='#FF8F8F')
    l = Label(root, text="Enter the blood group").place(x=50, y=50, w=400, h=40)
    e = Entry(root)
    e.place(x=500, y=50)
    b2 = Button(root, text="Back", command=lambda: stop(root)).place(x=600, y=100)
    b = Button(root, text="ENTER", command=lambda: grid1(e.get())).place(x=500, y=100)
    root.mainloop()


def stop(root):
    root.destroy()


root.mainloop()