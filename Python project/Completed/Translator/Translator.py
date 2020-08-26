import googletrans,tkinter,clipboard,os
from googletrans import Translator
from tkinter import ttk,messagebox,filedialog
from tkinter import *
from tkinter.ttk import *
##############################  Main window ###########################
tranlator = Tk()
tranlator.title('Translator')
tranlator.geometry('1000x600')
tranlator.resizable(0,0)
############################### Textvariables ##########################
global input_text,translated_text
#############################  Functions ###########################
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
def paste():
  input_text.insert(INSERT,clipboard.paste())
def show_hindi_translation():
  if input_text.get(1.0,END)=='':
    messagebox.showwarning('',"Enter some text first")
    return
  translated_text.delete(1.0,END)
  try:
    transation_class = Translator(['translate.google.com'])
    translated_text1 = transation_class.translate([input_text.get(1.0,END)], dest='hi')
    for translation in translated_text1:
      translated_text.insert(INSERT,translation.text)
  except:
    messagebox.showwarning('','Please check your internet connection')
    return
def copy():
  clipboard.copy(translated_text.get(1.0,END))
def save():
  save_loc  = filedialog.asksaveasfilename(title='Save file',filetypes=(('Text file','*.txt'),('All files' ,'*.*')))
  the_file,the_path = path_extractor(save_loc)
  os.chdir(the_path)
  if '.' not in the_file:
    messagebox.showwarning('','Type the extension of file')
    return
  text_file = open(f'{the_file}.txt', 'a')
  text_file.close()
  with open(f'{the_file}.txt','w',encoding='utf-8') as text_file:
    text_file.write(translated_text.get(1.0,END))
  try:
    os.rename(f'{the_file}.txt',f'{the_file}')
  except FileExistsError:
    messagebox.showerror('','File of this name already exists')
  messagebox.showinfo('','File saved')
###############################  Label ################################
Label(tranlator,text='Enter the text').place(x=20,y=20)
Label(tranlator,text='Translated text').place(x=15,y=300)
#################################  Text widget #########################
input_text = Text(tranlator,width=90,height=17)
input_text.place(x=100,y=20)
translated_text = Text(tranlator,width=90,height=17)
translated_text.place(x=100,y=300)
##################################  Buttons #############################
Button(tranlator,text='Paste',command=paste).place(x=900,y=50)
Button(tranlator,text='Show Hindi translation',command=show_hindi_translation).place(x=860,y=150)
Button(tranlator,text='Copy',command=copy).place(x=860,y=350)
Button(tranlator,text='Save',command=save).place(x=860,y=500)
tranlator.mainloop()