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
import historique as hs
from login import LoginPage

root=tk.Tk()
root.geometry('10000x500')
root.title("EMood")
root.iconbitmap("logoEmood.ico")
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
main_frame.configure(height=1000,width=100000)

def default_Emood():
    wrapper1=LabelFrame(main_frame,text="Company IT-Solution")
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=7)
    l2=Label(wrapper1,text='Welcome to the system  of Emotion Detection ',fg='#50537A')
    l2.config(font=('Comic Sans MS',45))
    l2.place(x=10,y=150-45)
    l3=Label(wrapper1,text='This system is delivred to the University  in order to Detect Emotion ',fg='#50537A')
    l3.config(font=('Comic Sans MS',20))
    l3.place(x=20,y=250-45)
'functions of button'
def hiddpage():
   for frame in main_frame.winfo_children():
        frame.destroy()

                      
def Historique():
 'calling function to destroy the other content'
 hiddpage()
 'calling function historique'
 hs.Historique(main_frame)
   
       
def Dashbord():
    hiddpage()
    wrapper1=LabelFrame(main_frame,text="Emotion detection")
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=7)
    bouton_lancer = Button(wrapper1,bg='#DCDCDC',  text='Lancer')
    bouton_lancer.place(x = 400 , y = 300 , width = 300,height=100)
    wrapper1.bind('<Return>', dashbord.detection)
    bouton_lancer.bind ("<Button-1>", dashbord.detection)
def logout():
    root.destroy()
    w=tk.Tk()
    obj= LoginPage(w)
   
    
   


  
    
'creation des option button'

historique_btn=tk.Button(option_frame,text='Historique',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Historique)
historique_btn.place(x=10,y=100)
dashbord_btn=tk.Button(option_frame,text='Dashboard',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=Dashbord)
dashbord_btn.place(x=10,y=150)


home_btn=tk.Button(option_frame,text='Logout',font=('bold',15),
                     fg='#262626',bd=0,bg='#E1E1E1',command=logout)
home_btn.place(x=10,y=750)

default_Emood()


root.mainloop()

