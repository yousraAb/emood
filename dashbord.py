import tkinter

master=tkinter.Tk()
master.title("place() method")
master.geometry("1166x718")
master.configure(bg='gray')#E1E1E1')
master.resizable(0,0)
master.title('Dashboard')

button3=tkinter.Button(master, text="Lancer",width=40,bg='#262626',fg='white')
button3.place(x=400, y=260)

master.mainloop()