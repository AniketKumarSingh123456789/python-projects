import tkinter,os,wikipedia,fpdf
from tkinter import ttk,filedialog,messagebox
from tkinter import *
from tkinter.ttk import *
###########################  Main window #######################
info = Tk()
info.title('Information master')
info.geometry('1000x600')
info.resizable(0,0)
##########################  Textvariable #######################
global topic,answer
topic = StringVar()
######################### Label ###############################
Label(info,text='Enter any topic').place(x=20,y=20)
Label(info,text='Answer').place(x=20,y=150)
#############################  Functions ######################
def path_extractor(full_path):
    if '\\' in full_path:
        reversed_path = full_path[::-1]
        slash_pos = reversed_path.find('\\')
        reversed_file = reversed_path[:slash_pos]
        file_name = reversed_file[::-1]
        reversed_path2 = reversed_path[slash_pos+1:]
        final_path = reversed_path2[::-1]
        return file_name,final_path    
    reversed_path = full_path[::-1]
    slash_pos = reversed_path.find('/')
    reversed_file = reversed_path[:slash_pos]
    file_name = reversed_file[::-1]
    reversed_path2 = reversed_path[slash_pos+1:]
    final_path = reversed_path2[::-1]
    return file_name,final_path
def show_info():
    if topic.get()=="":
        messagebox.showwarning('','PLease enter any topic')
        return
    answer.delete(1.0,END)
    try:
        answer.insert(INSERT,wikipedia.summary(topic.get()))
    except wikipedia.exceptions.PageError:
        messagebox.showinfo('',f'Sorry! there is no any information related to {topic.get()}')
        return
    except wikipedia.exceptions.DisambiguationError:
        messagebox.showinfo('',f'There are many topic related to {topic.get()}\nPlease specify')
        return
    except:
        messagebox.showerror('','Please check your internet connection')
        return
def save():
    if answer.get(1.0,END)=='':
        messagebox.showinfo('','PLease search any topic before save')
        return
    save_loc = filedialog.asksaveasfilename(title='Save as',filetypes=(('Txt file','*.txt'),('All types','*.*')))
    the_file,the_path = path_extractor(save_loc)
    if '.' not in the_file:
        messagebox.showwarning('','Please type the extension of file')
        return
    dot_pos = the_file.find('.')
    os.chdir(the_path)
    if the_file[dot_pos+1:]=='pdf':
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font('Arial',size=20)
        pdf.cell(10,10,txt=f"{answer.get(1.0,END)}",ln=1,align="L")
        pdf.output(f"{the_file}")
        messagebox.showinfo('','File saved')
        return
    with open(f'{the_file}.txt','a',encoding='utf-8') as file_name:
        file_name.write(answer.get(1.0,END))
    os.rename(f'{the_file}.txt',f'{the_file}')
    messagebox.showinfo('','File saved')
##########################  Entry box #########################
Entry(info,width=100,textvariable=topic).place(x=150,y=20)
answer = Text(info,width=100,height=20)
answer.place(x=70,y=150)
######################### Button ##############################
Button(info,text='Show Information',command=show_info).place(x=880,y=300)
Button(info,text='Save',command=save).place(x=880,y=390)
info.mainloop()