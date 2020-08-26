import tkinter,imageio,numpy,scipy,os,PIL,imutils,cv2
from cv2 import *
from scipy import ndimage
from tkinter import filedialog,messagebox,ttk
from PIL import Image,ImageTk
from tkinter import *
from tkinter.ttk import *
########################   Main window ########################
sketch = Tk()
sketch.geometry('1000x700')
sketch.title('Sketch')
sketch.resizable(False,False)
#############################  Textvariables ######################
global sketch_preview_pane,path_of_image,path_entry,path_of_image1
path_of_image = StringVar()
#########################  Functions #################################
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
def image_pane():
    global image_preview_pane
    image_preview_pane = Canvas(sketch,width=450,height=550,bg='white')
    image_preview_pane.place(x=10,y=60)
def sketch_pane():
    global sketch_preview_pane
    sketch_preview_pane = Canvas(sketch,width=450,height=550,bg='white')
    sketch_preview_pane.place(x=500,y=60)
def browse():
    global image_name,frame,x
    image_name = filedialog.askopenfilename(title='Select an image')
    try:
        img_obj = PIL.Image.open(image_name)
    except:
        if image_name=="":
            return
        if not os.path.exists(image_name):
            messagebox.showerror('','The given file path doesn\'t exists')
            return
        messagebox.showerror('','The given file is not an image')
        return
    path_entry.delete(0,END)
    path_entry.insert(INSERT,image_name)
def ok():
    global x
    if path_entry.get()=='':
        messagebox.showwarning('','Please enter the path of image ')
        return
    if not os.path.exists(path_entry.get()):
        messagebox.showerror('','The given path  doesn\'t exists')
        return
    the_file,the_path = path_extractor(path_entry.get())
    try:
        img_obj = PIL.Image.open(path_entry.get())
        os.chdir(the_path)
    except:
        messagebox.showerror('','The given file is not of image')
        return
    frame = cv2.cvtColor(cv2.imread(the_file), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=450, height=550)
    frame = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    image_pane()
    x = 1
    image_preview_pane.image = frame
    image_preview_pane.create_image(0,0,image = frame,anchor=NW)
def convert_to_sketch():
    global final_sketch,x
    try:
        print(x)
    except:
        messagebox.showwarning('','First you import an image')
        return
    the_file,the_path = path_extractor(path_entry.get())
    os.chdir(the_path)
    ####################### Converting in grayscale #####################
    read = imageio.imread(path_entry.get())
    grayscale = numpy.dot(read[...,:3],[0.299,0.587,0.114])
    subtract  = 255-grayscale
    filter = scipy.ndimage.filters.gaussian_filter(subtract,sigma=10)
    ###################### Converting in sketch ####################### 
    sketch_ = filter*255/(255-grayscale)
    sketch_[sketch_>255]=255
    sketch_[grayscale==255]=255
    final_sketch = sketch_.astype('uint8')
    cv2.imwrite('output.png',final_sketch) 
    ####################### Drawing sketch ###################
    sketch_pane()
    frame = cv2.cvtColor(cv2.imread('output.png'), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=450, height=550)
    frame = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    x = 1
    sketch_preview_pane.image = frame
    sketch_preview_pane.create_image(0,0,image = frame,anchor=NW)
def save_sketch():
    try:
        print(x)
    except:
        messagebox.showwarning('','First you create sketch of  an image')
        return
    path_to_save = filedialog.asksaveasfilename(filetypes=(('Image file','*.png'),('Image file','*.jpg')))
    the_file,the_path = path_extractor(path_to_save)
    os.chdir(the_path)
    if '.' not in the_file:
        messagebox.showwarning('','Please type the extension')
        return
    dot_pos = the_file.find('.')
    if the_file[dot_pos+1:]!='jpg' and  the_file[dot_pos+1:]!='png':
        messagebox.showwarning('','Invalid image extension')
        return
    cv2.imwrite(the_file,final_sketch) 
    messagebox.showinfo('','Sketch saved')
###########################   Labels ############################
Label(sketch,text='Path of image').place(x=20,y=20)
############################   Textboxes #######################
path_entry = Entry(sketch,width=100,textvariable=path_of_image)
path_entry.place(x=130,y=20)
###########################  Buttons ###########################
Button(sketch,text='Browse',command=browse).place(x=870,y=20)
Button(sketch,text='OK',command=ok).place(x=780,y=20)
Button(sketch,text='Convert to sketch',command=convert_to_sketch).place(x=400,y=650)
Button(sketch,text='Save sketch',command=save_sketch).place(x=600,y=650)
sketch.mainloop()