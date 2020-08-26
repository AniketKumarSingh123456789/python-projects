import tkinter,os,PIL
from PIL import Image,ImageEnhance, ImageFilter
from tkinter import ttk, filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
Artist = Tk()
Artist.geometry('1100x800')
Artist.title('Artist')
def path_extractor(full_path):
    reversed_path = full_path[::-1]
    slash_pos = reversed_path.find('/')
    reversed_file = reversed_path[:slash_pos]
    file_name = reversed_file[::-1]
    reversed_path2 = reversed_path[slash_pos+1:]
    final_path = reversed_path2[::-1]
    return file_name,final_path
def hhhh():
    global z
    z = PIL.Image.open('output.png')
###################### Preview pane ##################################
def preview():
    global preview_pane
    preview_pane = Canvas(Artist,width = 1500, height=600,bg='white')
    preview_pane.place(x = 0, y = 100)
def image_creator(image1):
    preview()
    global image2
    image2 = PhotoImage(file=image1)
    preview_pane.create_image(0,0, image=image2,anchor=NW)
def browse():
    global image,z
    image = filedialog.askopenfilename(initialdir ='/', title='Select an image', filetypes=(('Image file','*.png'),('All files', '*.*')))
    if image=='':
        messagebox.showwarning('Warning', 'Select a file')
        return 0
    try: 
        z = PIL.Image.open(image)
        the_file,the_path = path_extractor(image)
        path_box.insert(INSERT,os.getcwd()+f'\\{the_file}')
    except:
        messagebox.showerror('Error','The given path is not of an image')
        return 0
    if not image.endswith('.png'):
        path2 = image.replace('\\','/')
        path3 = path2[::-1]
        x = path3.find('/')
        reverse_file = path3[:x]
        path4 = path3[x:] 
        path5 = path4[::-1]
        os.chdir(path5)
        z.save('output.png')
        if path2:
            sure = messagebox.askyesno('','Are you sure?')
            if sure == True:
                if not os.path.exists(path2):
                    messagebox.showerror('Error','Path doen\'t exist')
                if os.path.exists(path2):
                    try:
                        PIL.Image.open(path2)
                    except OSError:
                        messagebox.showwarning('Error','The given path is not of an image')
                        return 0
                    image = 'output.png'
                    preview()
                    z= PIL.Image.open(image)
                    image_creator(image)
    else:
        preview()
        path2 = image.replace('\\','/')
        path3 = path2[::-1]
        x = path3.find('/')
        reverse_file = path3[:x]
        image = reverse_file[::-1]
        path4 = path3[x:] 
        path5 = path4[::-1]
        os.chdir(path5)
        path_box.delete(0,END)
        path_box.insert(INSERT,os.getcwd()+f'\\{the_file}')
        z= PIL.Image.open(image)
        image_creator(image)

#################### Browse Button #######################
browse_image = Button(Artist,width= 7 ,text='Browse', command=browse)
browse_image.place(x = 900 , y = 10)
###################### Path input box #########################
global path_box
pathvar = StringVar()
path_box = Entry(Artist, width =100, textvariable = pathvar)
path_box.place(x = 200 , y = 10)
def path_printer():
    hhhh()
    image = pathvar.get()
    if image=='':
        
        messagebox.showwarning('Warning','Please enter the path first')
        return 0
    try:
        path2 = image.replace('\\','/')
        path3 = path2[::-1]
        x = path3.find('/')
        reverse_file = path3[:x]
        image = reverse_file[::-1]
        path4 = path3[x:] 
        path5 = path4[::-1]
        os.chdir(path5)
        z= PIL.Image.open(image)
        image_creator(image)
    except:
        messagebox.showerror('Error','The given path is not of an image')
        return 0
    if not image.endswith('.png'):
        z= PIL.Image.open(image)
        z.save('output.png')
        path2 = image.replace('\\','/')
        if path2 == '':
            messagebox.showwarning('Warning','Please enter the path first')
        else:
            if path2:
                sure = messagebox.askyesno('','Are you sure?')

                if sure == True:
                    if not os.path.exists(path2):
                        messagebox.showerror('Error','Path doen\'t exist')
                    if os.path.exists(path2):
                        try:
                            PIL.Image.open(path2)
                        except OSError:
                            messagebox.showwarning('Error','The given path is not of an image')
                            return 0
                        path3 = path2[::-1]
                        x = path3.find('/')
                        reverse_file = path3[:x]
                        file1 = 'output.png'
                        path4 = path3[x:] 
                        path5 = path4[::-1]
                        os.chdir(path5)
                        image_creator(file1)

    else:
        path2 = image.replace('\\','/')
        if path2 == '':
            messagebox.showwarning('Warning','Please enter the path first')
        else:
            if path2:
                sure = messagebox.askyesno('','Are you sure?')

                if sure == True:
                    if not os.path.exists(path2):
                        messagebox.showerror('Error','Path doen\'t exist')
                    if os.path.exists(path2):
                        try:
                            PIL.Image.open(path2)
                        except OSError:
                            messagebox.showwarning('Error','The given path is not of an image')
                            return 0
                        path3 = path2[::-1]
                        x = path3.find('/')
                        reverse_file = path3[:x]
                        file1 = reverse_file[::-1]
                        path4 = path3[x:] 
                        path5 = path4[::-1]
                        os.chdir(path5)
                        image_creator(file1)
okbtn = Button(Artist, text ='OK', width =5,command=path_printer)
okbtn.place(x= 850, y = 10)
entrylabel = Label(Artist,text=' Enter the path ')
entrylabel.place(x = 10, y =10)
################################### Variables for sliders ########################################
a = IntVar()
brightness_var = IntVar()
colour_var = IntVar()
contrast_var = IntVar()
sharpness_var  = IntVar()
################################# Functions for sliders ############################
def brightness_function(brightness_var):
    input_  = int(brightness_var)
    bright = ImageEnhance.Brightness(z)
    bright.enhance(input_).save('output.png')
    image_creator('output.png')
def colour_function(colour_var):
    colour = ImageEnhance.Color(z)
    input_ = int(colour_var)
    colour.enhance(input_).save('output.png')
    image_creator('output.png')
def contrast_function(contrast_var):
    contrast = ImageEnhance.Contrast(z)
    input_ = int(contrast_var)
    contrast.enhance(input_).save('output.png')
    image_creator('output.png')
def blur_function(a):
    b = int(a)
    z.filter(ImageFilter.GaussianBlur(radius=b)).save('output.png')
    image_creator('output.png')
def sharpness_function(sharpness_var):
    sharp = ImageEnhance.Sharpness(z)
    input_ = int(sharpness_var)
    sharp.enhance(input_).save('output.png')
    image_creator('output.png')
############################################# Sliders ############################
Brightness_slider = tkinter.Scale(Artist,orient=HORIZONTAL,from_=-10,to=10, tickinterval=1,length = 300,variable = brightness_var,command=brightness_function).place(x = 1200,y =30)
colour_slider =tkinter.Scale(Artist,orient=HORIZONTAL,from_=-10,to=10, tickinterval=1,length = 300,variable = colour_var,command=colour_function).place(x = 900, y = 30)
contrast_slider = tkinter.Scale(Artist,orient=HORIZONTAL,from_=-10,to=10, tickinterval=1,length = 300,variable =contrast_var ,command=contrast_function).place(x = 600,y = 30)
sharpness_slider = tkinter.Scale(Artist,orient=HORIZONTAL,from_=-10,to=10, tickinterval=1,length = 300,variable = sharpness_var,command= sharpness_function).place(x = 300,y =30 )
blur_slider = tkinter.Scale(Artist,orient=HORIZONTAL,from_=-10,to=10, tickinterval=1,length = 300,variable=a,command= blur_function).place(x =0 ,y = 30)
Artist.mainloop()