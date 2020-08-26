import PIL,tkinter,PyPDF2,os,fpdf
from fpdf import FPDF
from tkinter import ttk,messagebox,filedialog,font
from tkinter import *
from tkinter.ttk import *
from PIL import Image
############################ Need to add functions ##################
# 1) Convert TXT  to PDF  
# 2) Convert PDF to TXT
# 3) Combine PDFs
# 4) Create PDF by Images 
# 5) Create PDF by Text
# 6) Full fledge editor
#######################   Main window ###########################
master = Tk()
master.geometry('400x500')
master.title('PDF Master')
master.resizable(0,0)
###################### Textvariables ##########################
#####################  Functions ##############################
# --------------------------------  TXT to PDF -----------------------------------
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
def browse_txt_file():
    txt_file = filedialog.askopenfilename(title='Select a text file',filetypes=(('Text file','*.txt'),('All files','*.*')))
    if txt_file!='':
        txt_file_box.delete(0,END)
    txt_file_box.insert(INSERT,txt_file)
def browse_loc_to_save_pdf():
    loc_to_save = filedialog.askdirectory()
    if loc_to_save!='':
        save_pdf_box.delete(0,END)
    save_pdf_box.insert(INSERT,loc_to_save)
def save_pdf():
    if path_of_txt_file.get()=='':
        messagebox.showwarning('','Give the path of text file')
        return
    if path_to_save_pdf.get()=='':
        messagebox.showwarning('','Give the path to save PDF file')
        return
    if name_of_pdf.get()=='':
        messagebox.showwarning('','Give a name to file to save')
        return
    if not os.path.exists(path_of_txt_file.get()):
        messagebox.showerror('','Path of text file doesnot exists')
        return
    if not os.path.exists(path_to_save_pdf.get()):
        messagebox.showerror('','Path to save PDF file doesnot exists')
        return
    the_file,the_path = path_extractor(path_of_txt_file.get())
    os.chdir(the_path)
    try:
        with open(the_file,'r',encoding='utf-8') as f:
            f.read()
    except UnicodeDecodeError:
        messagebox.showerror('','Given file is not supported')
        return
    pdf_construct = FPDF()
    pdf_construct.add_page()
    # for i in font.families():
    #     pdf_construct.add_font(i,'',uni=1)
    align=''
    if alignment.get()=='Left':
        align='L'
    if alignment.get()=='Right':
        align='R'
    if alignment.get()=='Center':
        align='C'
    if alignment.get()=='Justify':
        align='J'
    pdf_construct.set_font(font_face.get(),size=int(font_size.get()))
    f =  open(the_file,'r',encoding='utf-8')
    for i in f.readlines():
        pdf_construct.cell(200,10,txt=i+'\n',align=align)
    f.close()
    os.chdir(path_to_save_pdf.get())
    pdf_construct.output(f'{name_of_pdf.get()}.pdf')
    messagebox.showinfo('','PDF saved')
def txt_to_pdf():
    master.destroy()
    ######################   TXT to PDF window ###################
    TXT_to_PDF = Tk()
    TXT_to_PDF.geometry('1000x600')
    TXT_to_PDF.title('TXT to PDF')
    TXT_to_PDF.resizable(0,0)
    ###################### Textvariables ##########################
    global path_of_txt_file,path_to_save_pdf,name_of_pdf,alignment,font_face,font_size,txt_file_box,save_pdf_box
    path_of_txt_file = StringVar()
    path_to_save_pdf= StringVar()
    name_of_pdf = StringVar()
    alignment = StringVar()
    font_face = StringVar()
    font_size = StringVar()
    #########################  Labels  #####################
    Label(TXT_to_PDF,text='Path of file').place(x=20,y=20)
    Label(TXT_to_PDF,text='Location to save PDF').place(x=20,y=100)
    Label(TXT_to_PDF,text='Name to save').place(x=20,y=180)
    Label(TXT_to_PDF,text='Font face').place(x=20,y=260)
    Label(TXT_to_PDF,text='Font size').place(x=20,y=340)
    Label(TXT_to_PDF,text='Alignment').place(x=20,y=420)
    ########################  Entry boxes ########################
    txt_file_box = Entry(TXT_to_PDF,width=100,textvariable=path_of_txt_file)
    txt_file_box.place(x=100,y=20)
    save_pdf_box  =  Entry(TXT_to_PDF,width=100,textvariable=path_to_save_pdf)
    save_pdf_box.place(x=170,y=100)
    Entry(TXT_to_PDF,width=100,textvariable=name_of_pdf).place(x=120,y=180)
    #######################   Comboboxes #######################
    list_of_font_size = []
    for i in range(100):
        list_of_font_size.append(i)
    font_face_box = Combobox(TXT_to_PDF,textvariable=font_face,values=font.families(),state='readonly')
    font_face_box.current(25)
    font_face_box.place(x=120,y=260)

    font_size_box = Combobox(TXT_to_PDF,textvariable=font_size,values=list_of_font_size,state='readonly')
    font_size_box.current(12)
    font_size_box.place(x=120,y=340)
    
    alignment_box = Combobox(TXT_to_PDF,textvariable=alignment,state='readonly')
    alignment_box['values'] = ['Left','Right','Center','Justify']
    alignment_box.current(0)
    alignment_box.place(x = 120,y=420)
    ##############################  Buttons ######################
    Button(TXT_to_PDF,text='Browse',command=browse_txt_file).place(x=750,y=20)
    Button(TXT_to_PDF,text='Browse',command=browse_loc_to_save_pdf).place(x=800,y=100)
    Button(TXT_to_PDF,width=20,text='Save',command=save_pdf).place(x=350,y=500)

    TXT_to_PDF.mainloop()
# ----------------------------------  PDF to TXT -----------------------------------
def pdf_to_txt():
    pass
def combine_pdfs():
    pass
#----------------------------------  Image to PDF ---------------------------------
def browse_images():
    list_of_images = filedialog.askopenfilenames()
    list_of_images = list(list_of_images)
    if list_of_images != []:
        list_of_images_box.delete(0,END)
        for i in list_of_images:
            if list_of_images[-1] == i:
                list_of_images_box.insert(INSERT,i)
                break
            list_of_images_box.insert(INSERT,i+';')

def browse_save_dir():
    path = filedialog.askdirectory()
    if path!='':
        path_to_save_box.delete(0,END)
        path_to_save_box.insert(INSERT,path)

def generate_pdf():
    if list_of_images.get()=='':
        messagebox.showwarning('','Select images')
        return
    if path_to_save_img_pdf.get()=='':
        messagebox.showwarning('','Select path to save PDF')
        return
    if name_to_save_img_pdf.get()=='':
        messagebox.showwarning('','Give a name to save the PDF')
        return
    if os.path.exists(f'{path_to_save_img_pdf.get()}/{name_to_save_img_pdf.get()}.pdf'):
        ask = messagebox.askyesno('','The given file name already exists\nDo you want ot replace it?')
        if ask == False:
            return
    list_of_img = list_of_images.get().split(';')
    list_without_first_image = []
    objects_of_imgs = []
    for i in list_of_img:
        try:
            PIL.Image.open(i)
        except Exception as e:
            print(e)
            messagebox.showerror('','Please select images only')
            return
    for i in list_of_img:
        if list_of_img[0] == i:
            continue
        list_without_first_image.append(i)
    for i in list_without_first_image:
        objects_of_imgs.append(PIL.Image.open(i).convert('RGB'))

    os.chdir(path_to_save_img_pdf.get())
    final = PIL.Image.open(list_of_img[0]).convert('RGB')
    try:
        final.save(f'{name_to_save_img_pdf.get()}.pdf','PDF',resolution=100.0,save_all=True,append_images=objects_of_imgs)
    except OSError:
        messagebox.showerror('','Choose different name')
        return
    messagebox.showinfo('','PDF saved')

def pdf_by_image():
    master.destroy()
    #########################  Image to PDF window ##############################
    img_to_pdf = Tk()
    img_to_pdf.geometry('900x400')
    img_to_pdf.title('Image to PDF')
    img_to_pdf.resizable(0,0)
    #########################  Textvariables ################################
    global path_to_save_img_pdf,list_of_images,list_of_images_box,path_to_save_box,name_to_save_box,name_to_save_img_pdf
    path_to_save_img_pdf = StringVar()
    list_of_images = StringVar()
    name_to_save_img_pdf = StringVar()
    ######################## Labels ###############################
    Label(img_to_pdf,text='Select all images').place(x=50,y=50)
    Label(img_to_pdf,text='Choose location to save').place(x=50,y=150)
    Label(img_to_pdf,text='Name to save').place(x=50,y=250)
    ####################### Textboxes ####################
    list_of_images_box = Entry(img_to_pdf,textvariable=list_of_images,width=85)
    list_of_images_box.place(x=170,y=50)
    path_to_save_box = Entry(img_to_pdf,textvariable=path_to_save_img_pdf,width=80)
    path_to_save_box.place(x=200,y=150)
    name_to_save_box = Entry(img_to_pdf,textvariable=name_to_save_img_pdf,width=80)
    name_to_save_box.place(x=200,y=250)
    ####################### Buttons ######################
    Button(img_to_pdf,text='Browse',command=browse_images).place(x=700,y=50)
    Button(img_to_pdf,text='Browse',command=browse_save_dir).place(x=700,y=150)
    Button(img_to_pdf,text='Generate PDF',width=20,command=generate_pdf).place(x=350,y=350)
    img_to_pdf.mainloop()

def pdf_by_txt():
    pass
def full_editor():
    pass

#########################  Buttons #############################
Button(master,width=30,text='Convert Text file  to PDF',command=txt_to_pdf).place(x=80,y=20)
Button(master,width=30,text='Convert  PDF  to Text file',command=pdf_to_txt).place(x=80,y=100)
Button(master,width=30,text='Combine PDFs',command=combine_pdfs).place(x=80,y=180)
Button(master,width=30,text='Create PDF by Images',command=pdf_by_image).place(x=80,y=260)
Button(master,width=30,text='Create PDF by Text',command=pdf_by_txt).place(x=80,y=340)
Button(master,width=30,text=' Full fledge editor ',command=full_editor).place(x=80,y=420)
master.mainloop()