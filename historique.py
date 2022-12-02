from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

w=Tk()
w.geometry('1166x718')
w.configure(bg='#262626')#E1E1E1')
w.resizable(0,0)
w.title('Toggle Menu')


def default_Emood():
    f2=Frame(w,width=1166,height=718,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Emood',fg='#50537A',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
 
                      
def Emood():
    f1.destroy()
    f2=Frame(w,width=1166,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Emood',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    toggle_win()
 

def Dashbord():
    f1.destroy()
    f2=Frame(w,width=1166,height=455,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Dashbord',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    toggle_win()
   
    

def Historique():
    f1.destroy()
    f2=Frame(w,width=1166,height=718,bg='white')
    f2.place(x=210,y=230-45); 
    
    listdata=[('id','emotion','description'),
             (1,'happy','course computer science'),
                (2,'sad','course in math'),
                (3,'upset','TP'),
                (4,'ANGRY','FIRST DAY School')];
    totalrow=len(listdata);
    totalcolum=len(listdata[0]); 
    toggle_win()
   
    for i in range(totalrow):
      for j in range(totalcolum):  
         e=Entry(f2, width=28,fg='blue',font=('Arial',15,'bold'))
         e.grid(row=i,column=j)
         e.insert(END,listdata[i][j])
  


def toggle_win():
    global f1
    f1=Frame(w,width=300,height=718,bg='#E1E1E1')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'E M O O D','#50537A','#E1E1E1',Emood)
    bttn(0,117,'D A S H B O R D','#50537A','#E1E1E1',Dashbord)
    bttn(0,154,'H I S T O R I Q U E','#50537A','#E1E1E1',Historique)

    #
    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=toggle_win,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#E1E1E1',
           activebackground='#E1E1E1').place(x=5,y=10)
    

default_Emood()

img1 = ImageTk.PhotoImage(Image.open("open.png"))

global b2
b2=Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)
 

w.mainloop()
