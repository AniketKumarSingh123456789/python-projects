import tkinter,os,smtplib,email,webbrowser
from tkinter import ttk,messagebox,filedialog
from tkinter import *
from tkinter.ttk import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
####################   Main window ################################
Send_email = Tk()     
Send_email.title('Postman')
Send_email.geometry('800x600')
Send_email.resizable(False,False)
################################   Textvariables #####################################
global path
sender_email = StringVar()     
sender_password = StringVar()
receiver_email = StringVar()
subject = StringVar()
message= StringVar()
path_of_file = StringVar()
#####################################   Functions  ##################################
def path_extractor(full_path):
    reversed_path = full_path[::-1]
    slash_pos = reversed_path.find('/')
    reversed_file = reversed_path[:slash_pos]
    file_name = reversed_file[::-1]
    reversed_path2 = reversed_path[slash_pos+1:]
    final_path = reversed_path2[::-1]
    return file_name,final_path
def browse1():
    global list_of_files
    list_of_files = filedialog.askopenfilenames()
    if (';' not in path_of_file.get()) and  (path_of_file.get() != ''):
        path.insert(INSERT,';')
    if path_of_file.get()!='' and path_of_file.get()[-1]!=';':
        path.insert(INSERT,';')
    for i in range(len(list_of_files)):
        if (len(list_of_files)-1) == i:
            path.insert(INSERT,f'{list_of_files[i]}')
        else:
            path.insert(INSERT,f'{list_of_files[i]};')
def browse():
    list_of_files = filedialog.askopenfilenames()
    path.delete(0,END)
    for i in range(len(list_of_files)):
        if (len(list_of_files)-1) == i:
            path.insert(INSERT,f'{list_of_files[i]}')
        else:
            path.insert(INSERT,f'{list_of_files[i]};')
def send_mail():
    list_of_service_providers = ['gmail','yahoo','hotmail','outlook']
    if sender_email.get() == '':
        messagebox.showwarning('','Fill the sender\'s email')
        return
    if receiver_email.get() == '':
        messagebox.showwarning('','Fill the receiver\'s email')
        return
    if ('@' not in sender_email.get()) or ('.com' not in sender_email.get()):
        messagebox.showerror('','Sender\'s email id is invalid')
        return
    if ('@' not in receiver_email.get()) or ('.com' not in receiver_email.get()):
        messagebox.showerror('','Receiver\'s email is invalid')
        return
    if sender_email.get().count('@') > 1:
        messagebox.showerror('','Sender\'s email is invalid')
        return
    if receiver_email.get().count('@') > 1:
        messagebox.showerror('','Receiver\'s email is invalid')
        return        
    if sender_password.get()=='':
        messagebox.showwarning('','Fill the password')
        return
    at_the_rate1=sender_email.get().find('@')
    at_the_rate2 = receiver_email.get().find('@')
    dot_com1 = sender_email.get().find('.com')
    dot_com2 = receiver_email.get().find('.com')
    service_provider1 = sender_email.get()[at_the_rate1+1:dot_com1]
    service_provider2 = receiver_email.get()[at_the_rate2+1:dot_com2]
    if service_provider1 == '':
        messagebox.showerror('','Sender\'s email is invalid')
        return
    if service_provider2 == '':
        messagebox.showerror('','Receiver\'s email is invalid')
        return
    if sender_email.get()[:at_the_rate1] == '':
        messagebox.showerror('','Sender\'s email is invalid')
        return
    if receiver_email.get()[:at_the_rate2] == '':
        messagebox.showerror('','Receiver\'s email is invalid')
        return
    if service_provider1 not in list_of_service_providers:
        messagebox.showinfo('',f'Sorry we don\'t provide any service for {service_provider1}\nWe provide service only for gmail , yahoo, hotmail and outlook ')
        return
    if path_of_file.get().count(';') > 0:
        list_of_the_files = path_of_file.get().split(';')
    if  (path_of_file.get().count(';') == 0) and (path_of_file.get() != ''):
        list_of_the_files = []
        list_of_the_files.append(path_of_file.get())
    if  (path_of_file.get().count(';') == 0) and (path_of_file.get() == ''):
        list_of_the_files = None
    if list_of_the_files != None:
        for i in list_of_the_files:
            if (not os.path.exists(i)) and (i!=''):
                messagebox.showerror('',f'{i} \ndoes\'t exist')
                return
    if service_provider1=='gmail':
        account = smtplib.SMTP('smtp.gmail.com',587)
    if service_provider1=='outlook' or service_provider1=='hotmail':
        account = smtplib.SMTP('smtp-mail.outlook.com',587)
    if service_provider1=='yahoo':
        account = smtplib.SMTP('smtp.mail.yahoo.com',587)
    account.ehlo()
    account.starttls()
    try:
        account.login(sender_email.get(),sender_password.get())
    except:
        if service_provider1=='gmail':
            correct = tkinter.messagebox.askyesno('','Please check your email-id and password\nAre both correct?')
            if correct==True:
                webbrowser.open('https://myaccount.google.com/lesssecureapps')
                return
            if correct==False:
                tkinter.messagebox.showwarning('','Then correct them')
                return
        else:
            tkinter.messagebox.showerror('','Your email-id or password is incorrect')
            return
    if list_of_the_files == None:    
        account.sendmail(sender_email.get(),receiver_email.get(),f'Subject:{subject.get()} \n\n{message.get(1.0,END)}')
        account.quit()
        messagebox.showinfo('Email Sent','Email sent succesfully')
        return
    if list_of_the_files != None:
        msg = MIMEMultipart()
        msg['From'] = sender_email.get()
        msg['To'] = receiver_email.get()
        msg['Subject'] = subject.get()
        body = message.get(1.0,END)
        msg.attach(MIMEText(body,'plain'))
    for i in list_of_the_files:
        the_file,the_path = path_extractor(i)
        os.chdir(the_path)
        attachment  = open(the_file,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+the_file)
        msg.attach(part)
    text = msg.as_string()
    account.sendmail(sender_email.get(),receiver_email.get(),text)
    account.quit()
    messagebox.showinfo('Email Sent','Email sent succesfully')
##########################################  Labels #####################################
Label(Send_email,text='Sender\'s email',width=25).place(x=20,y=30)
Label(Send_email,text='Sender\'s password',width=25).place(x=20,y=90)
Label(Send_email,text='Receiver\'s email',width=25).place(x=20,y=150)
Label(Send_email,text='Subject',width=25).place(x=20,y=210)
Label(Send_email,text='Path of file',width=25).place(x=20,y=270)
Label(Send_email,text='Text',width=25).place(x=20,y=330)
####################################### Entry boxes #################################
Entry(Send_email,width=100,textvariable=sender_email).place(x=120,y=30)
Entry(Send_email,width=100,show="*",textvariable=sender_password).place(x=140,y=90)
Entry(Send_email,width=100,textvariable=receiver_email).place(x=120,y=150)
Entry(Send_email,width=100,textvariable=subject).place(x=100,y=210)
path = Entry(Send_email,width=80,textvariable=path_of_file)
path.place(x=100,y=270)
message = Text(Send_email,height=14,width=70,padx=4,pady=2,wrap='word',font='arial')
message.place(x=60,y=330)
###################################  Buttons ##########################################
Button(Send_email,text='Browse',width=10,command=browse).place(x=680,y=270)
Button(Send_email,text='Send',width=10,command=send_mail).place(x=710,y=500)
Button(Send_email,text='Add',width=10,command=browse1).place(x=600,y=270)
Send_email.mainloop()