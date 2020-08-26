import tkinter,wikipedia,os
from tkinter import messagebox,filedialog,ttk
from tkinter import *
from tkinter.ttk import *
# -----------------------------------  MAIN WINDOW --------------------------------
random_wiki = Tk()
random_wiki.resizable(0,0)
random_wiki.title('Random  wikipedia  page  generator')
random_wiki.geometry('650x600')
# ---------------------------------   TEXTVARIABLES --------------------------------
global summary
# ---------------------------------  FUNCTIONS ------------------------------------
def generate():
    random_topic = wikipedia.random()
    choice = messagebox.askyesno('',f'The article is about "{random_topic}"\nDo you want to read?')
    if choice==True:
        summary.delete(1.0,END)
        summary.insert(INSERT,wikipedia.summary(random_topic))
def save():
    location = filedialog.asksaveasfilename(initialdir='/',title='Selext locatiion to save file',filetypes=(('*.txt','Text File'),('*.*','All Files')))
    print(location)
# ---------------------------------  LABELS ----------------------------------------
Label(random_wiki,text='Summary').place(x=10,y=30)
# --------------------------------  TEXT WIDGET ------------------------------------
summary = Text(random_wiki,width=50,height=35)
summary.place(x=80,y=30)
# -----------------------------------  BUTTONS ---------------------------------------
Button(random_wiki,text='Generate random article',command=generate).place(x=500,y=100)
Button(random_wiki,text='Save',command=save).place(x=550,y=250)
random_wiki.mainloop()