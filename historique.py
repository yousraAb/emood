# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:14:10 2022

@author: user
"""

import tkinter as tk;
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
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
    

def Historique():
    hiddpage()
    f2=Frame(main_frame,width=1000,height=1000,bg='white')
    f2.place(x=250,y=145); 
    my_game = ttk.Treeview(f2)
    my_game['columns'] = ('student_emotion', 'emotion description')
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("student_emotion",anchor=CENTER)
    my_game.column("emotion description",anchor=CENTER)
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("student_emotion",text="student_emotion",anchor=CENTER)
    my_game.heading("emotion description",text="emotion description",anchor=CENTER)
    my_game.insert(parent='',index='end',iid=0,text='',
      values=('1','Ninja'))
    my_game.insert(parent='',index='end',iid=1,text='',
      values=('2','Ranger'))
    my_game.insert(parent='',index='end',iid=2,text='',
      values=('3','Deamon'))
    my_game.insert(parent='',index='end',iid=3,text='',
      values=('4','Dragon'))
    my_game.insert(parent='',index='end',iid=4,text='',
      values=('5','CrissCross'))
    my_game.insert(parent='',index='end',iid=5,text='',
      values=('6','ZaqueriBlack'))
    my_game.pack()
  
    
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
   
    
'creation des oprion button'
home_btn=tk.Button(option_frame,text='Home',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Emood)
home_btn.place(x=10,y=50)

historique_btn=tk.Button(option_frame,text='Historique',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Historique)
historique_btn.place(x=10,y=100)
dashbord_btn=tk.Button(option_frame,text='Dashboard',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Dashbord)
dashbord_btn.place(x=10,y=150)

root.mainloop()
