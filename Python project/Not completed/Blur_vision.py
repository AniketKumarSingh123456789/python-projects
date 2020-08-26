import os,tkinter,pytesseract,speech_recognition,PIL
from tkinter import messagebox,ttk,filedialog
from tkinter import *
from tkinter.ttk import *
#####################   Main window #################
vision = Tk()
vision.title('Blur Vision')
vision.geometry('900x250')
vision.resizable(0,0)
#######################  Textvariables ###################
global path_of_image,path_of_image_box,language,language_box
path_of_image = StringVar()
language = StringVar()
######################  Functions ########################
def browse_img():
    img = filedialog.askopenfilename(initialdir='/',title='Select an Image')
    if img!='':
        path_of_image_box.delete(0,END)
        path_of_image_box.insert(INSERT,img)    
def speak_text():
    pass
def save_as_txt():
    pass
def save_as_speech():
    pass
####################  Labels ############################
Label(vision,text="Choose image").place(x=20,y=20)
Label(vision,text="Choose Language").place(x=20,y=100)
#######################  Entry box #######################
path_of_image_box = Entry(vision,textvariable=path_of_image,width=100)
path_of_image_box.place(x=120,y=20)
#########################  Comboboxes ################### 
language_box =  Combobox(vision,textvariable=language,state='readonly',width=30)
language_box.place(x=150,y=100)
#######################  Buttons #########################
Button(vision,text="Browse",command=browse_img).place(x=750,y=20)
Button(vision,text="Speak Text",command=speak_text).place(x=100,y=200)
Button(vision,text="Save As Text File",command=save_as_txt).place(x=200,y=200)
Button(vision,text="Save As Speech",command=save_as_speech).place(x=350,y=200)
vision.mainloop()