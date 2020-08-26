import tkinter
from tkinter import ttk,messagebox
from tkinter import *
from tkinter.ttk import *
################### Main window ############################
Loger = Tk()
Loger.geometry('300x400')
Loger.title('Loger')
Loger.resizable(False,False)
############################ Functions ########################################
def sign():
    Sign_up_window = Tk()
    Sign_up_window.geometry('800x600')
    Sign_up_window.title('Sign up form')
    Sign_up_window.resizable(False,False)
    def com():
        global gender_box
        gender_box = Combobox(Sign_up_window,textvariable=gender,state='readonly')
        gender_box.place(x=150,y=150)
    def com1():
        com()
        gender_box['values'] = ['Male','Female','Others']
        gender_box.current(0)
    #################  Textvariables ########################
    Name= StringVar()
    age = StringVar()
    gender = StringVar()
    occupation = StringVar()
    salary = StringVar()
    residence = StringVar()
    Email = StringVar()
    password = StringVar()
    sub = IntVar()
    ############################  Labels #############################################
    Label(Sign_up_window,text='Name').place(x=100,y=50)
    Label(Sign_up_window,text='Age').place(x=100,y=100)
    Label(Sign_up_window,text='Gender').place(x=100,y=150)
    Label(Sign_up_window,text='Occupation').place(x=100,y=200)
    Label(Sign_up_window,text='Salary(Monthly)').place(x=100,y=250)
    Label(Sign_up_window,text='Residence').place(x=100,y=300)
    Label(Sign_up_window,text='Email').place(x=100,y=350)
    Label(Sign_up_window,text='Password').place(x=100,y=400)
    ##################  Entry box ####################################
    Entry(Sign_up_window,width=50,textvariable=Name).place(x=150,y=50)
    Entry(Sign_up_window,width=50,textvariable=age).place(x=150,y=100)
    Entry(Sign_up_window,width=50,textvariable=Email).place(x=170,y=350)
    Entry(Sign_up_window,width=50,textvariable=password).place(x=170,y=400)
    #####################  Radiobutton ##################################
    Radiobutton(Sign_up_window,width=20,text='Bussinessman',value='Bussinessman',variable=occupation).place(x=200,y=200)
    Radiobutton(Sign_up_window,width=20,text='Farmer',value='Farmer',variable=occupation).place(x=350,y=200)
    Radiobutton(Sign_up_window,width=20,text='Indian',value='Indian',variable=residence).place(x=250,y=300)
    Radiobutton(Sign_up_window,width=20,text='Non Indian',value='Non Indian',variable=residence).place(x=350,y=300)
    ##################  Combobox ################################
    com1()
    salary_box  = Combobox(Sign_up_window,textvariable=salary,state='readonly')
    salary_box.place(x=200,y=250)
    salary_box['values'] = ['More than 20000','Less than 20000','More than 50000']
    salary_box.current(0)
    ###############  Checkbox ###########################
    Checkbutton(Sign_up_window,text='Subscribe to our newsletter',variable=sub).place(x=170,y=450)
    ###############  Create account function ######################################
    def Create_account():
        if Name.get()=='':
            messagebox.showwarning('','Please enter the name')
            return
        if age.get() == '':
            messagebox.showwarning('','Please fill the age')
            return
        try:
            int(age.get())
        except:
            messagebox.showerror('','Age must be numbers')
            return
        if int(age.get()) <0:
            messagebox.showerror('','Age can\'t be negative')
            return
        if int(age.get()) < 15:
            messagebox.showwarning('','Sorry your age is too low to fill the form')
            return
        if residence.get()=='':
            messagebox.showwarning('','Choose your residence')
            return
        if password.get()=='':
            messagebox.showwarning('','Please fill the password')
            return
        if occupation.get()=='':
            messagebox.showwarning('','Choose your occupation')
            return
        if Email.get()=='':
            messagebox.showwarning('','Fill the email')
            return
        if '@' not in Email.get() or '.com' not in Email.get():
            messagebox.showwarning('','Invalid email')
            return
        email = Email.get()
        dot_com = email.find('.com')
        at_the_rate = email.find('@')
        if email[at_the_rate+1:dot_com]=='':
            messagebox.showwarning('','Invalid email')
            return
        if email[:at_the_rate] == '':
            messagebox.showwarning('','Invalid email')
            return
        with open('Server.txt','a') as sv:
            with open('Server.txt','r') as sv1:
                if Email.get() in sv1.read():
                    messagebox.showwarning('','User already registered')
                    return
                else:
                    sv.write(f'{Name.get()},{Email.get()},{password.get()},{salary.get()},{residence.get()},{age.get()},{gender.get()},{sub.get()}\n')
                    messagebox.showinfo('','User registered')
        Entry(Sign_up_window,width=50,textvariable=Name).delete(0,END)
        Entry(Sign_up_window,width=50,textvariable=age).delete(0,END)
        Entry(Sign_up_window,width=50,textvariable=Email).delete(0,END)
        Entry(Sign_up_window,width=50,textvariable=password).delete(0,END)
        gender_box.current(0)
        salary_box.current(0)
    ##################################  Button ######################################
    Button(Sign_up_window,text='Create account',command=Create_account).place(x=200,y=500)
    ##########################  End of sign up form  ############################
    Sign_up_window.mainloop()
def Sign_in():
    Loger.destroy()
    #################  Sign in window  #########################
    Sign_in_window = Tk()
    Sign_in_window.geometry('600x400')
    Sign_in_window.title('Log in form')
    Sign_in_window.resizable(False,False)
    ###############  Text variables ######################
    Email = StringVar()
    password = StringVar()
    #######################   Labels ###########################
    Label(Sign_in_window,text='Email id').place(x=100,y=50)
    Label(Sign_in_window,text='Password').place(x=100,y=150)
    ##################################  Entry box ###################################
    Entry(Sign_in_window,width=50,textvariable=Email).place(x=170,y=50)
    Entry(Sign_in_window,width=50,textvariable=password).place(x=170,y=150)
    ###################  Function ###############################
    def log_in():
        if Email.get()=='':
            messagebox.showwarning('','Fill the email')
            return
        if '@' not in Email.get() or '.com' not in Email.get():
            messagebox.showwarning('','Invalid email')
            return
        email = Email.get()
        password1 = password.get()
        dot_com = email.find('.com')
        at_the_rate = email.find('@')
        if email[at_the_rate+1:dot_com]=='':
            messagebox.showwarning('','Invalid email')
            return
        if email[:at_the_rate] == '':
            messagebox.showwarning('','Invalid email')
            return
        if password.get()=='':
            messagebox.showwarning('','Fill the password')
            return
        if email[at_the_rate+1:dot_com]=='':
            messagebox.showwarning('','Invalid email')
            return
        with open('Server.txt','r') as sv:
            for lines in sv.readlines():
                first_com = lines.find(',')
                second_com = lines.find(',',first_com+1)
                third_com = lines.find(',',second_com+1)
                username = lines[:first_com]
                if (email == lines[first_com+1:second_com]) and (password1==  lines[second_com+1:third_com]):
                    messagebox.showinfo('',f'Welcome {username}')
                    return
                if (email == lines[first_com+1:second_com]) and (password1 !=  lines[second_com+1:third_com]):
                    messagebox.showerror('','Wrong password')
                    return
                continue
        messagebox.showwarning('','User not found')
    ####################  Button ##################################
    Button(Sign_in_window,text='Log in',command=log_in).place(x=200,y=300)
    #####################  End of sign in window #######################
    Sign_in_window.mainloop()
def Sign_up():
    Loger.destroy()
    sign()
###################  sign in and sign up buttons
Button(Loger,width=20,text='Sign up',command=Sign_up).place(x=100,y=150)
Button(Loger,width=20,text='Log in',command=Sign_in).place(x=100,y=300)
##########################  End of the application #########################
Loger.mainloop()
