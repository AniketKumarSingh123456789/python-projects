import PIL,pytesseract,tkinter,os,tqdm,time
from PIL import Image
from tkinter import ttk,filedialog,messagebox
from tkinter import *
from tkinter.ttk import *
###############   Main window ##################
reader = Tk()
reader.resizable(False,False)
reader.geometry('900x600')
reader.title('Reader')
#######################   textvariables #########################
path = StringVar()
global text,text1
###################   Functions ################################
list_of_excluded_extensions = ['zip','rar','exe','msi','dmg','jpg','png','gif','jpeg']
def path_extractor(full_path):
    reversed_path = full_path[::-1]
    slash_pos = reversed_path.find('/')
    reversed_file = reversed_path[:slash_pos]
    file_name = reversed_file[::-1]
    reversed_path2 = reversed_path[slash_pos+1:]
    final_path = reversed_path2[::-1]
    return file_name,final_path
def import_img():
    global image,image_path
    if path.get()=='':
        messagebox.showwarning('','Please  first input the path of image')
        return
    if "'" in path.get():
        image_path = path.get().replace("'",'')
    if '"' in path.get():
        image_path = path.get().replace('"','')
    if '"' not in path.get() and  "'" not in path.get():
        image_path = path.get() 
    if not os.path.exists(image_path):
        messagebox.showerror('','The path doesn\'t exists')
        return
    try:
        image =  PIL.Image.open(image_path)
    except:
        messagebox.showerror('','The given path is not of an image')
        return
    messagebox.showinfo('','Image imported')
def browse():
    image_path = filedialog.askopenfilename(title='Select an image')
    path_box.delete(0,END)
    path_box.insert(INSERT,image_path)
def Extract_text():
    pytesseract.pytesseract.tesseract_cmd = r"E:\softwares\Installed\Tesseract\tesseract.exe"
    try:
        text1 = pytesseract.image_to_string(image)
    except NameError:
        messagebox.showinfo('','You need to first import the image before extract text\nClick Import button')
        return
    except:
        messagebox.showinfo('','Sorry it is difficult to extract text')
        return
    text.delete(1.0,END)
    text.insert(INSERT,text1)
    messagebox.showinfo('','Text extracted successfully')
def save_text():
    if text.get(1.0,END)=='':
        messagebox.showerror('','Please first extract any text')
        return
    choice = messagebox.askyesno('','Do you want to save it')
    if choice==True:
        final_file_path = filedialog.asksaveasfilename(initialdir='/',title='Save text',filetypes=(('Text file','*.txt'),('All file types','*.*')))
        the_file,the_path =  path_extractor(final_file_path)
        if '.' not in the_file:
            messagebox.showwarning('','Please type the extensions of file')
            return
        os.chdir(the_path)
        dot_pos = the_file.find('.')
        extension  = the_file[dot_pos:]
        if extension in list_of_excluded_extensions:
            messagebox.showerror('','Sorry this file type is not supported')
            return
        with open(f'{the_file}.txt','w') as f:
            f.write(f'{text.get(1.0,END)}')
        if extension=='txt':
            return
        os.rename(f'{the_file}.txt',f'{the_file}')
        messagebox.showinfo('','File saved')
###############   Text widget ################
text = Text(reader,width=90,height=30)
text.place(x=0,y=50)
##################  Labels ###################### 
Label(reader,text='Path of image').place(x=20,y=20)
#################  Entry box ########################
path_box = Entry(reader,width=80,textvariable=path)
path_box.place(x=150,y=20)
################   Buttons ###########################
Button(reader,text='Import',command=import_img).place(x=700,y=20)
Button(reader,text='Browse',command=browse).place(x=800,y=20)
Button(reader,text='Extract text',command=Extract_text).place(x=750,y=200)
Button(reader,text='Save',command=save_text).place(x=750,y=280)
reader.mainloop()