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
import dashbord as dashbord



'functions of button'
       
def Historique(main_frame):
    'dividing the main frame to wrapper'
    wrapper1=LabelFrame(main_frame,text="Emotion list")
    wrapper2=LabelFrame(main_frame,text="Search");
    wrapper2.pack(fill="both",expand="yes",padx=20,pady=7)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=16)
    'table creating usig treview'
    trv=ttk.Treeview(wrapper1 ,height=10)
    trv.pack(pady=30)
    
    
    
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
                     fg='#262626',bd=0,bg='#E1E1E1',height=1,command=search)
    search_btn.place(x=200,y=100)     
    'clear button'
    clear_btn=tk.Button(wrapper2,text='clear',font=('bold',15),
                   fg='#262626',bd=0,bg='#E1E1E1',height=1,command=clear)
    clear_btn.place(x=280,y=100)     
  
    

 
