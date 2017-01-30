from tkinter import *
import csv

friend_Contacts=[
    ['Dominica, kim','343-1234'],
    ['Dominica, lee','689-1234'],
    ['Ruri, kim','345-1234'],
    ['Lisa, jung','343-1562'],
]

def friend_Pos():
    return int(select.curselection()[0])

def addfriend():
    friend_Contacts.append([nameVar.get(),phoneVar.get()])
    setSelect()

def updatefriend():
    friend_Contacts[friend_Pos()]=[nameVar.get(),phoneVar.get()]
    setSelect()

def deletefriend():
    del friend_Contacts[friend_Pos()]
    setSelect()
def savefriend():
    csv_file=open("myFriend.csv","w")
    cw=csv.writer(csv_file, delimiter=',')
    cw.writerow(["name",'phone'])
    for name,phone in friend_Contacts:
        cw.writerow([name,phone])

def makeFrame():
    global  nameVar,phoneVar,select
    my_f=Tk()

    frame1=Frame(my_f)
    frame1.pack()

    Label(frame1,text="Name").grid(row=0,column=0,sticky=W)
    nameVar=StringVar()
    name=Entry(frame1,textvariable=nameVar)
    name.grid(row=0,column=1,sticky=W)

    Label(frame1, text="Phone").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    name = Entry(frame1, textvariable=phoneVar)
    name.grid(row=1, column=1, sticky=W)

    frame2=Frame(my_f)
    frame2.pack()
    b1 = Button(frame2, text="추가", command=addfriend)
    b2 = Button(frame2, text="수정", command=updatefriend)
    b3 = Button(frame2, text="삭제", command=deletefriend)
    b4 = Button(frame2, text="CSV", command=savefriend)
    b1.pack(side=LEFT);b2.pack(side=LEFT)
    b3.pack(side=LEFT);b4.pack(side=LEFT)

    frame3 = Frame(my_f)
    frame3.pack()
    select = Listbox(frame3)
    select.pack(side=LEFT,fill=BOTH,expand=1)
    select.bind("<<ListBoxSelect>>",onSelect)
    return my_f

def onSelect(val):
    name,phone=friend_Contacts[friend_Pos()]
    nameVar.set(name)
    phoneVar.set(phone)

def setSelect():
    friend_Contacts.sort()
    select.delete(0, END)
    for name,phone in friend_Contacts:
        select.insert(END,name)

mframe=makeFrame()
setSelect()
mframe.mainloop()
