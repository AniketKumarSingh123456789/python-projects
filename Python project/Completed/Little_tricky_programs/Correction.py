import tkinter,os,textblob,clipboard
from tkinter import ttk,filedialog,messagebox
from textblob import TextBlob
from tkinter import *
from tkinter.ttk import *
##########################  Main window #######################
correction = Tk()
correction.title('Error finder')
correction.geometry('300x300')
correction.resizable(False,False)

############################ Functions ##########################
def path_extractor(full_path):
    reversed_path = full_path[::-1]
    slash_pos = reversed_path.find('/')
    reversed_file = reversed_path[:slash_pos]
    file_name = reversed_file[::-1]
    reversed_path2 = reversed_path[slash_pos+1:]
    final_path = reversed_path2[::-1]
    return file_name,final_path
def copy():
    clipboard.copy(raw_text.get(1.0,END))
def paste():
    global paste_txt
    paste_txt = clipboard.paste()
    raw_text.insert(INSERT,paste_txt)
def correct():
    global corrected_text
    actual_words = raw_text.get(1.0,END)
    corrected_words = TextBlob(actual_words)
    corrected_text.delete(1.0,END)
    corrected_text.insert(INSERT,corrected_words.correct())
def copy_correct():
    clipboard.copy(corrected_text.get(1.0,END))
def save_correct():
    file_path = filedialog.asksaveasfilename(title='Save text',filetypes=(('Text file','*.txt'),('All files','*.*')))
    the_file,the_path = path_extractor(file_path)
    if '.' not in the_file:
        messagebox.showwarning('','Please type the extensions of file')
        return
    os.chdir(the_path)
    dot_pos = the_file.find('.')
    with open(f'{the_file[:dot_pos]}.txt','w') as final_file:
        final_file.write(corrected_text.get(1.0,END))
    os.rename(f'{the_file[:dot_pos]}.txt',the_file)
def enter_text():
    correction.destroy()
    ##########################  Main window ##################
    enter = Tk()
    enter.geometry('1000x700')
    enter.title('Enter the text')
    enter.resizable(False,False)
    ###################### Labels ########################
    global Correction_label,raw_text,corrected_text
    Label(enter,text='Enter the text').place(x=20,y=20)
    Label(enter,text='Correction').place(x=20,y=350)
    ##################### Text ###########################
    raw_text = Text(enter,width=100,height=15)
    raw_text.place(x=100,y=20)
    corrected_text = Text(enter,width=100,height=18)
    corrected_text.place(x=100,y=350)
    ##################### Buttons ########################
    Button(enter,text='Copy',command=copy).place(x=910,y=35)
    Button(enter,text='Paste',command=paste).place(x=910,y=125)
    Button(enter,text='Show correction',command=correct).place(x=905,y=225)
    Button(enter,text='Copy',command=copy_correct).place(x=905,y=465)
    Button(enter,text='Save correction',command=save_correct).place(x=905,y=565)
    enter.mainloop()
# -------------------------------------- END OF ENTER THE TEXT ----------------------------------- 
def save_correction():
    file_path = filedialog.asksaveasfilename(title='Save text',filetypes=(('Text file','*.txt'),('All files','*.*')))
    the_file,the_path = path_extractor(file_path)
    if '.' not in the_file:
        messagebox.showwarning('','Please type the extensions of file')
        return
    os.chdir(the_path)
    dot_pos = the_file.find('.')
    with open(f'{the_file[:dot_pos]}.txt','w') as final_file:
        final_file.write(corrected_text1.get(1.0,END))
    os.rename(f'{the_file[:dot_pos]}.txt',the_file)
def copy_corrected():
    clipboard.copy(corrected_text1.get(1.0,END))
def show_correction():
    global corrected_text
    actual_words = raw_text1.get(1.0,END)
    corrected_words = TextBlob(actual_words)
    corrected_text1.delete(1.0,END)
    corrected_text1.insert(INSERT,corrected_words.correct())
def copy_raw():
    clipboard.copy(raw_text1.get(1.0,END))
def paste_raw():
    raw_text1.insert(INSERT,clipboard.paste())
def browse_text_file():
    global file_name
    file_name = filedialog.askopenfilename()
    path_of_text_file.delete(0,END)
    path_of_text_file.insert(INSERT,file_name)
def import_text_file():
    global num
    if path_of_text_file.get()=='':
        messagebox.showwarning('','First enter the file path')
        return
    if not os.path.exists(file_name):
        messagebox.showwarning('','The given file path doesn\'t exists')
        return
    if not path_of_text_file.get().endswith('.txt'):
        messagebox.showerror('The give file path is not text file')
        return
    num  = 3
    messagebox.showinfo('','Text file imported')
def show_text():
    try:
        print(num)
    except:
        messagebox.showwarning('','You need to first import the text file.\nClick import button')
        return
    raw_text1.delete(1.0,END)
    with open(file_name,'r') as text_file:
        raw_text1.insert(INSERT,text_file.read())
def input_text_file():
    correction.destroy()
    global input_text_file_win
    input_text_file_win = Tk()
    input_text_file_win.geometry('1000x900')
    input_text_file_win.title('Input text file')
    input_text_file_win.resizable(0,0)
    ############################### Textvariables ###############
    global text_of_file,raw_text1,corrected_text1,path_of_text_file
    text_of_file = StringVar()
    #########################  Label #########################
    Label(input_text_file_win,text='Enter path of text file').place(x=20,y=20)
    Label(input_text_file_win,text='Text of input file').place(x=10,y=100)
    Label(input_text_file_win,text='Corrected text').place(x=10,y=430)
    ##########################  Entry ############################
    path_of_text_file = Entry(input_text_file_win,width=100,textvariable=text_of_file)
    path_of_text_file.place(x=170,y=20)
    ##########################  Text widget ######################
    raw_text1 = Text(input_text_file_win,width=100,height=15)
    raw_text1.place(x=100,y=100)
    corrected_text1 = Text(input_text_file_win,width=100,height=18)
    corrected_text1.place(x=100,y=430)
    ##########################  Buttons ####################
    Button(input_text_file_win,text='Browse',command=browse_text_file).place(x=900,y=20)
    Button(input_text_file_win,text='Import',command=import_text_file).place(x=800,y=20)
    Button(input_text_file_win,text='Show text of file',command=show_text).place(x=907,y=120)
    Button(input_text_file_win,text='Copy',command=copy_raw).place(x=907,y=170)
    Button(input_text_file_win,text='Paste',command=paste_raw).place(x=907,y=230)
    Button(input_text_file_win,text='Show correction',command=show_correction).place(x=907,y=300)
    Button(input_text_file_win,text='Copy',command=copy_corrected).place(x=910,y=550)
    Button(input_text_file_win,text='Save correction',command=save_correction).place(x=910,y=600)
    input_text_file_win.mainloop()
######################### Buttons #############################
Button(correction,text='Enter the text',width=20,command=enter_text).place(x=100,y=70)
Button(correction,text='Input text file',width=20,command=input_text_file).place(x=100,y=200)
correction.mainloop()