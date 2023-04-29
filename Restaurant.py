# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:24:10 2022

@author: riyam
"""

from tkinter import *
import datetime as d
import sqlite3 as s 
a1=d.datetime.now()

import random
n=random.randint(1000,3000)
n=str(n)
print("Reference value is : ",n)

root=Tk()
root.geometry("1700x1600")
root.title("restaurant")
root.config(bg="lime")

def dest():
    root.destroy()

def reset():
    p3.set("")
    p4.set("")
    p5.set("")
    p6.set("")
    p7.set("")
    p8.set("")
    n12.set("")
    p10.set("")
    p11.set("")
    p12.set("")
    p13.set("")

#define variable----------------------------
e3=IntVar()
e4=IntVar()
e5=IntVar()
e6=IntVar()
e7=IntVar()
e8=IntVar()
e9=IntVar()
e10=IntVar()
e11=IntVar()
e12=IntVar()
e13=IntVar()


def cmbne():
    n12.set(n)
    g=n
    a=p3.get()
    b=p4.get()
    c=p5.get()
    d=p6.get()
    e=p7.get()
    f=p8.get()
    h=p10.get()
    i=p11.get()
    j=p12.get()
    k=p13.get()
    

    
    if(a==""):
        cost1=0
    else:
        cost1=int(a)*10
        print("Tea cost is : ",cost1)
    
    if(b==""):
        cost2=0
    else:
        cost2=int(b)*30
        print("Drinks cost is : ",cost2)
        
    if(c==""):
        cost3=0
    else:
        cost3=int(c)*20
        print("Ice-Cream cost is : ",cost3)
             
    if(d==""):
        cost4=0
    else:
        cost4=int(d)*70
        print("Idly cost is : ",cost4)
     
    if(e==""):
        cost5=0
    else:
        cost5=int(e)*50
        print("Dosa cost is : ",cost5)
    
    if(f==""):
        cost6=0
    else:
        cost6=int(f)*60
        print("Rice-Plate cost is : ",cost6)
    
    
    t = cost1+cost2+cost3+cost4+cost5+cost6
    t1=str(t)
    p10.set(t1)
    print("Cost-Of-Meal is : ",t1)
    
    
    sgst=(t*15)/100
    sgst1=str(sgst)
    p11.set(sgst1)
    print("SGST is : ",sgst1)
    
    
    cgst=(t*12)/100
    cgst1=str(cgst)
    p12.set(cgst1)
    print("CGST is : ",cgst1)
    
    Total=t+sgst+cgst
    total1 = str(Total)
    p13.set(total1)
    print("Total Cost is : ",total1)
    
    lst=[a,b,c,d,e,f,g,t1,sgst1,cgst1,total1]
    
######################################################################################################################################
    
    conn=s.connect('Restaurant.db')
    with conn:
       cursor=conn.cursor()
    o=s.connect('Restaurant.db')
    if o:
       print("Database is created and connected")
    cur=o.cursor()
    cur.execute("create table if not exists RestaurantEntry(Tea text,Drinks text,Ice_Cream text,Idly text,Dosa text,Rice_Plate text,\
            Reference text,Cost_Of_Meal text,SGST text,CGST text,Total_Cost text) ")
    cur.execute("insert into RestaurantEntry values(?,?,?,?,?,?,?,?,?,?,?)",lst)
    o.commit()
    o.close()
    
########################################################################################################################################
  
############################################################################################################################3

l1=Label(root,text="SAI RESTAURANT",font=('Verdana',30,'bold'),width=60,height=3,bg="black",fg="cyan")
l1.place(x=0,y=0)

l2=Label(root,text=a1,font=('Verdana',12,'bold'),width=30,height=2,bg="black",fg="cyan")
l2.place(x=650,y=100)

l3=Label(root,text="Tea",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l3.place(x=10,y=200)

p3 = StringVar()
e3=Entry(root,text=p3,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e3.place(x=250,y=200)

l4=Label(root,text="Drinks",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l4.place(x=10,y=260)

p4=StringVar()
e4=Entry(root,text=p4,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e4.place(x=250,y=260)

l5=Label(root,text="Ice-Cream",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l5.place(x=10,y=320)

p5=StringVar()
e5=Entry(root,text=p5,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e5.place(x=250,y=320)

l6=Label(root,text="Idly",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l6.place(x=10,y=380)

p6=StringVar()
e6=Entry(root,text=p6,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e6.place(x=250,y=380)

l7=Label(root,text="Dosa",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l7.place(x=10,y=440)

p7=StringVar()
e7=Entry(root,text=p7,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e7.place(x=250,y=440)

l8=Label(root,text="Rice-Plate",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l8.place(x=10,y=500)

p8=StringVar()
e8=Entry(root,text=p8,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e8.place(x=250,y=500)

l9=Label(root,text="References",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l9.place(x=620,y=200)

n12=StringVar()
e9=Entry(root,text=n12,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e9.place(x=850,y=200)

l10=Label(root,text="Cost Of Meal",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l10.place(x=620,y=260)

p10=StringVar()
e10=Entry(root,text=p10,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e10.place(x=850,y=260)

l11=Label(root,text="SGST",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l11.place(x=620,y=320)

p11=StringVar()
e11=Entry(root,text=p11,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e11.place(x=850,y=320)

l12=Label(root,text="CGST",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l12.place(x=620,y=380)

p12=StringVar()
e12=Entry(root,text=p12,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e12.place(x=850,y=380)

l13=Label(root,text="Total Cost",font=('times new roman',12,'bold'),bg="black",fg="white",width=18,height=2)
l13.place(x=620,y=440)

p13=StringVar()
e13=Entry(root,text=p13,font=('Verdana',10,'bold'),justify='right',width=30,bd=15)
e13.place(x=850,y=440)



b10=Button(root,text="Total",font=('times new roman',12,'bold'),bd=10,width=15,height=1,bg="cyan",activebackground="green2",
          command=cmbne)
b10.place(x=100,y=650)

b11=Button(root,text="Reset",font=('times new roman',12,'bold'),bd=10,width=15,height=1,bg="cyan",activebackground="green2",
          command=reset)
b11.place(x=300,y=650)

b12=Button(root,text="Exit",font=('times new roman',12,'bold'),bd=10,width=15,height=1,bg="cyan",activebackground="green2",
          command=dest)
b12.place(x=500,y=650)


###############################################################################################################################


def enterInfo():
    q10=str(p10.get())
    q11=str(p11.get())
    q12=str(p12.get())
    q13=str(p13.get())
    
    txtpaySlip.delete("1.0",END)
    txtpaySlip.insert(END,"\t\tPay Slip\n\n\n\n")
    txtpaySlip.insert(END,"References :"+n+"\n\n")
    txtpaySlip.insert(END,"Cost Of Meal : "+q10+" \n\n")
    txtpaySlip.insert(END,"SGST : "+q11+" \n\n")
    txtpaySlip.insert(END,"CGST : "+q12+" \n\n")
    txtpaySlip.insert(END,"Total Cost : "+q13+" \n\n\n")
    txtpaySlip.insert(END,"Thanks for visiting and giving us a chance to offer our services!!!\n\n")
    txtpaySlip.insert(END,"\tHave a nice day!!\n\n")
    rslt=txtpaySlip.get("1.0","end")
    print(rslt)



# DateOfOrder=StringVar()
f1=Frame(root,width=350,height=500,bd=10,bg="cyan")
f1.pack(side=RIGHT)

paySlip=Label(f1,text=a1,font=('arial',12,'bold'),fg="green",width=20,height=2)
paySlip.grid(row=0,column=0)
txtpaySlip=Text(f1,height=22,width=34,bd=16,font=('arial',13,'bold'))
txtpaySlip.grid(row=1,column=0)

b13=Button(root,text="View Slip",font=('arial',12,'bold'),bd=10,width=15,height=1,bg="cyan",activebackground="green2",
           command=enterInfo)
b13.place(x=700,y=650)

mainloop()
