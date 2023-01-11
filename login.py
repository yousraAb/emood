from tkinter import *
from PIL import ImageTk, Image
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk, messagebox
import pymysql
import os


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\pink.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#fee6ed', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Bienvenue"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', '35', "bold"), bg="#fee6ed",
                             fg='#bdb9b1',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=100)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\emood.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#fee6ed')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=120)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#fee6ed')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=580, y=80)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#fee6ed", fg="#6b6a69",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#fee6ed", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#fee6ed", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#fee6ed')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#fee6ed')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#bdb9b1', cursor='hand2',  fg='white',command=self.login_func)
        self.login.place(x=20, y=10)
  
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#fee6ed", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#fee6ed", fg="#fee6ed",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#fee6ed')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    def login_func(self):
         if self.username_entry.get()=="" or self.password_entry.get()=="":
             messagebox.showerror("Error!","All fields are required",parent=self.window)
         else:
             try:
                 connection=pymysql.connect(host="localhost",  user="root", password="",  database="emood")
                 cur = connection.cursor()
                 cur.execute("select * from user where login=%s and pass=%s",(self.username_entry.get(),self.password_entry.get()))
                 row=cur.fetchone()
                 if row == None:
                     messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=self.window)
                     
                 else:
                    
                     self.redirect_window()

             except Exception as e:
                  messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

         
    def redirect_window(self):
                 self.window.destroy()
                 # Importing the signup window.
                 # The page must be in the same directory
                 import menu
                 
                
         
    def reset_fields(self):
                 self.username_entry.delete(0,END)
                 self.password_entry.delete(0,END)


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()