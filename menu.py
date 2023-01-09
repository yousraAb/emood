# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:58:17 2023

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:14:10 2022

@author: user
"""

import tkinter as tk;
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql
root=tk.Tk()
root.geometry('1000x500')
"side menu"
option_frame =tk.Frame(root,bg='#E1E1E1')

option_frame.pack(side=tk.LEFT)

"cette option  de pack propagate nous permet de resize notre frame "
option_frame.pack_propagate(False)
option_frame.configure(width=120,height=1000) 
"main page"
main_frame=tk.Frame(root,highlightbackground='black',
                    highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1000,width=1000)
'functions of button'
def hiddpage():
   for frame in main_frame.winfo_children():
        frame.destroy()
  
def cnx(): 
      
        return cur
           

           
def Historique():
    'calling function to destroy the other content'
    hiddpage()
    'dividing the main frame to wrapper'
    wrapper1=LabelFrame(main_frame,text="Emotion list")
    wrapper2=LabelFrame(main_frame,text="Search");
    wrapper2.pack(fill="both",expand="yes",padx=20,pady=7)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=16)
    'table creating usig treview'
    trv=ttk.Treeview(wrapper1 ,height="6")
    trv.pack()
    'configurate the heading'
    trv['columns'] = ('student_emotion', 'emotion description')
    trv.column("#0", width=0,  stretch=NO)
    trv.column("student_emotion",anchor=CENTER)
    trv.column("emotion description",anchor=CENTER)
    trv.heading("#0",text="",anchor=CENTER)
    trv.heading("student_emotion",text="student_emotion",anchor=CENTER)
    trv.heading("emotion description",text="emotion description",anchor=CENTER)
    'connection to database'
    connection=pymysql.connect(host="localhost",  user="root", password="",  database="emood")
    cursor= connection.cursor()
    'showing data using sql in table'
    query='select student_emotion,emotion_description from emotion'
    cursor.execute(query)
    rows=cursor.fetchall()
    'defing function inside historique to re-use it'
    def update(rows):
      trv.delete(*trv.get_children())
      for i in rows:
         trv.insert('','end',values=i)
    'call function to update rows'
    update(rows)
    'search function and clear function'
    def search ():
      query='select student_emotion,emotion_description from emotion  where student_emotion =%s'
      cursor.execute(query,(ent.get()))
      rows=cursor.fetchall()
      update(rows)
     
    def clear():
        query='select student_emotion,emotion_description from emotion'
        cursor.execute(query)
        rows=cursor.fetchall()
        update(rows)
      
      
    'search section'
    lbl=Label(wrapper2,text="search",font=('bold',15),
                     fg='#262626',bd=0)
    lbl.pack(side=tk.LEFT)
    ent=Entry(wrapper2,textvariable=search)
    ent.pack(padx=10,pady=10,side=tk.LEFT)
    'search button'
    search_btn=tk.Button(wrapper2,text='Search',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=search)
    search_btn.place(x=200,y=60)     
    'clear button'
    clear_btn=tk.Button(wrapper2,text='clear',font=('bold',15),
                   fg='#262626',bd=0,bg='#E1E1E1',command=clear)
    clear_btn.place(x=280,y=60)     
  
    
    
def Dashbord():
    hiddpage()
    f2=Frame(main_frame,width=900,height=1010,bg='white')
    f2.place(x=0,y=0)
    l2=Label(f2,text='Dashbord',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
def Emood():
    hiddpage()
    f2=Frame(main_frame,width=900,height=1010,bg='#262626')
    f2.place(x=0,y=0)
    l2=Label(f2,text='Emood',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
def logout():
    hiddpage()
    f2=Frame(main_frame,width=900,height=1010,bg='#262626')
    f2.place(x=0,y=0)
    l2=Label(f2,text='Emood',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)   
    
'creation des option button'
home_btn=tk.Button(option_frame,text='Home',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Emood)
home_btn.place(x=10,y=50)

historique_btn=tk.Button(option_frame,text='Historique',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Historique)
historique_btn.place(x=10,y=100)

dashbord_btn=tk.Button(option_frame,text='Dashboard',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Dashbord)
dashbord_btn.place(x=10,y=150)

logout_btn=tk.Button(option_frame,text='Logout',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=logout)
logout_btn.place(x=10,y=450)

root.mainloop()
