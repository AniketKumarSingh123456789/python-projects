import zipfile,os,tkinter,patoolib
from zipfile import *
from tkinter import ttk,messagebox,filedialog
from tkinter import *
from tkinter.ttk import *
#############  Main window ##########################
cae = Tk()
cae.geometry('500x350')
cae.resizable(False,False)
cae.title('Compressor and extracter')
list_of_extensions=['zip','rar','iso','gzip','tar','7z','ace','adf','alzip','ape','ar','arc','arj','bzip2','cab','chm','compress','cpio','deb','dms','flac','lrzip','lzh','lzip','lzma','lzop','rpm','rzip','shar','shn','vhd','xz','zoo','zpaq']
#################   Functions for buttons ############################
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
def extract_all():
    if path_of_compressed_file.get()=='':
        messagebox.showwarning('','Enter the path of compressed file')
        return
    if path_to_save_file.get()=='':
        messagebox.showwarning('','Enter the path to save file after extraction')
        return
    files_compressed =  path_of_compressed_file.get().split(';')
    for i in files_compressed:
        if not os.path.exists(i):
            messagebox.showerror('','The path of compressed file doesn\'t exists')
            return
    if not os.path.exists(path_to_save_file.get()):
        messagebox.showerror('','Path to save file after extraction doesn\'t exists')
        return
    for i in files_compressed:
        extension_of_file = patoolib.get_archive_format(i)
        if extension_of_file[0] not in list_of_extensions :
            messagebox.showwarning('','Please give path of compressed  file only')
            return
    os.chdir(path_to_save_file.get())
    extraction_in_progress = Label(Extractor,text='Extraction is in progress....',width=35)
    extraction_completed = Label(Extractor,text='Extraction completed',width=35)
    extraction_in_progress.place(x=300,y=250)
    #########################   Progressbar ###################################
    progress1 = Progressbar(Extractor,length=900,mode='determinate',maximum=100,value=0)
    progress1.place(x=20,y=300)
    for i in files_compressed:
        patoolib.extract_archive(f'{i}',outdir=os.getcwd())
    # for i in files_compressed:
    #     zip1 = ZipFile(f'{i}')
    #     global list_of_compressed_files
    #     list_of_compressed_files = zip1.namelist()
    #     progress1['value'] = progress1['value'] + len(list_of_compressed_files)
    #     progress1.update()
    #     zip1.extractall(path=path_to_save_file.get())
    #     zip1.close()
    for i in files_compressed:
        if delete1.get()==1:
            os.remove(i)
    progress1.destroy()
    extraction_completed.place(x=300,y=250)
def pr():
    print(var[pos].get())
def extract_only_selected():
    selected_file_extraction = Tk()
    selected_file_extraction.geometry('1000x900')
    selected_file_extraction.title('Select file for extraction')
    #######################  Textvariable #######################
    global var,pos,ckbtn
    var = []
    with ZipFile(f'{path_of_compressed_file.get()}') as zip1:
        for i in range(len(zip1.namelist())):
            var.append(f'{i}select')
        pos = 0
        for i in var:
            i = IntVar()
            var[pos] = IntVar()
            pos = pos+1
    ##############################  Scroll bar ########################
    sbr = Scrollbar(selected_file_extraction,orient='vertical')
    sbr.place(x=980,y=0)
    ###########################  Checkbox ################################
    y_axis = 10
    pos = 0
    with ZipFile(f'{path_of_compressed_file.get()}') as zip1:
        for i in zip1.namelist():
            ckbtn = Checkbutton(selected_file_extraction,text=f'{i}',variable=var[pos])
            ckbtn.invoke()
            ckbtn.place(x=10,y=y_axis)
            ckbtn['command'] = pr
            y_axis =y_axis+30
            pos = pos+1
            sbr.configure(command=ckbtn)
    selected_file_extraction.mainloop()
def start_compression():
    if name_to_save.get()=='':
        messagebox.showerror('','Give a name to your file')
        return
    if path_of_file.get() == '':
        messagebox.showwarning('','Please select a file to compress')
        return
    number_of_comma = path_of_file.get().count(';')
    if number_of_comma==0:
        list_of_files1 = {path_of_file.get()}
        list_of_files = tuple(list_of_files1)
        if not os.path.exists(path_of_file.get()):
            messagebox.showerror('',f'{list_of_files[0]}    doesn\'t    exist')
            return
    if number_of_comma>0:
        list_of_files1 = set(path_of_file.get().split(';'))
        list_of_files = tuple(list_of_files1)
        for confirm in range(len(list_of_files)):
            if not os.path.exists(list_of_files[confirm]):
                messagebox.showerror('',f'{list_of_files[confirm]}    doesn\'t    exist')
                return
    if path_to_save_compressed_file.get() == '':
        messagebox.showwarning('','Selct a location to save your compressed file')
        return
    if not os.path.exists(path_to_save_compressed_file.get()):
        messagebox.showerror('','The location to save compressed file doesn\'t exist')
        return
    compression_in_progress = Label(Compressor,text='Compression is in progress....',width=35)
    compression_completed = Label(Compressor,text='Compression completed',width=35)
    #########################   Progressbar ###################################
    progress = Progressbar(Compressor,length=900,mode='determinate',maximum=100,value=0)
    progress.place(x=100,y=380)
    compression_in_progress.place(x=500,y=360)
    os.chdir(path_to_save_compressed_file.get())
    progress.start()
    zip1 = open(f'{name_to_save.get()}.zip','a')
    zip1.close()
    with ZipFile(f'{name_to_save.get()}.zip','w') as zip2:
        for i in list_of_files:
            the_file,the_path = path_extractor(i)
            os.chdir(the_path)
            zip2.write(f'{the_file}',compress_type=ZIP_DEFLATED)
            actual_length = len(list_of_files)
            if delete.get()==1:
                os.remove(the_file)
            progress['value'] = progress['value'] + len(list_of_files)
            progress.update()
    progress.stop()
    progress.destroy()
    compression_completed.place(x=500,y=360)
def browse_file():
    global names
    names1 = filedialog.askopenfilenames()
    names = list(names1)
    file_path.delete(0,END)    
    for i in range(len(names)):
        if (len(names)-1) == i:
            file_path.insert(INSERT,f'{names[i]}')
        else:
            file_path.insert(INSERT,f'{names[i]};')
def browse_location():
    loc.delete(0,END)
    folder = filedialog.askdirectory()
    loc.insert(0,folder)
def add():
    names1 = set(filedialog.askopenfilenames())
    names = list(names1)
    if (';' not in path_of_file.get()) and  (path_of_file.get() != ''):
        file_path.insert(INSERT,';') 
    if (';' not in path_of_file.get()) and  (path_of_file.get() != ''):
        file_path.insert(INSERT,';')
    if path_of_file.get()!='' and path_of_file.get()[-1]!=';':
        file_path.insert(INSERT,';')
    for i in range(len(names)):
        if (len(names)-1) == i:
           file_path.insert(INSERT,f'{names[i]}')
        else:
           file_path.insert(INSERT,f'{names[i]};') 
def Compress():
    cae.destroy()
    global Compressor,extensions,extension
    Compressor = Tk()
    Compressor.title('Compressor')
    Compressor.geometry('1200x500')
    Compressor.resizable(False,False)
    global loc,file_path,path_of_file,path_to_save_compressed_file,progress,compression_in_progress,compression_completed,name_to_save,delete
    ###################   Textvarables ###########################
    path_of_file = StringVar()
    path_to_save_compressed_file = StringVar()
    name_to_save = StringVar()
    delete = IntVar()
    extension = StringVar()
    #########################   Labels ###########################
    Label(Compressor,text='Path of file',width=20).place(x=10,y=20)
    Label(Compressor,text='Location to save file after compression',width=35).place(x=10,y=100)
    Label(Compressor,text='Name of file',width=20).place(x=10,y=200)
    ################   Entry box  #################################
    file_path =  Entry(Compressor,width=100,textvariable=path_of_file)
    file_path.place(x=120,y=20)
    loc = Entry(Compressor,width=100,textvariable=path_to_save_compressed_file)
    loc.place(x=220,y=100)
    Entry(Compressor,width=80,textvariable=name_to_save).place(x=180,y=200)
    ################################# Combobox #######################
    extensions = Combobox(Compressor,textvariable=extension,state='readonly')
    extensions['values'] = list_of_extensions
    extensions.current(0)
    patoolib.create_archive
    extensions.place(x=780,y=200)
    ####################  Buttons #################################
    Button(Compressor,text='Browse',width=20,command=browse_file).place(x=950,y=20)
    Button(Compressor,text='Browse',width=20,command=browse_location).place(x=850,y=100)
    Button(Compressor,text='Add',width=20,command=add).place(x=800,y=20)
    Button(Compressor,text='Start Compression',width=20,command=start_compression).place(x=300,y=450)
    ########################   Check box ###############################
    Checkbutton(Compressor,text='Delete files after compression',variable=delete).place(x=100,y=300)
    Compressor.mainloop()
def Extract():
    cae.destroy()
    #####################   Main window #############################
    global Extractor
    Extractor = Tk()
    Extractor.geometry('1000x400')
    Extractor.resizable(False,False)
    Extractor.title('Extractor')
    #######################   Textvariable ##########################
    global delete1,path_of_compressed_file,path_to_save_file,password,file_path,loc,extraction_in_progress,extraction_completed,progress1
    path_of_compressed_file = StringVar()
    path_to_save_file = StringVar()
    delete1 = IntVar()
    password = StringVar()
    ########################  Labels ###################################
    Label(Extractor,text='Path of compressed file',width=25).place(x=20,y=20)
    Label(Extractor,text='Path to save after extraction',width=25).place(x=20,y=100)
    ##########################   Check box #########################################
    Checkbutton(Extractor,text='Delete compressed file after extraction',variable=delete1).place(x=100,y=180)
    ########################   Entry boxes ##################################
    file_path = Entry(Extractor,width=100,textvariable=path_of_compressed_file)
    file_path.place(x=160,y=20)
    loc = Entry(Extractor,width=100,textvariable=path_to_save_file)
    loc.place(x=200,y=100)
    ########################   Button ###############################
    Button(Extractor,text='Browse',width=20,command=browse_file).place(x=800,y=20)
    Button(Extractor,text='Browse',width=20,command=browse_location).place(x=850,y=100)
    Button(Extractor,text='Extract all',width=20,command=extract_all).place(x=300,y=350)
    Button(Extractor,text='Extract selected files',width=24,command=extract_only_selected).place(x=450,y=350)
    Extractor.mainloop()
#########################   Buttons #############################
Button(cae,text='Compress',width=20,command=Compress).place(x=150,y=100)
Button(cae,text='Extract',width=20,command=Extract).place(x=150,y=250)
cae.mainloop()