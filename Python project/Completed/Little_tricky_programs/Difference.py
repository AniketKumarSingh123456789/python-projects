import tkinter,os,cv2,PIL,imutils
from tkinter import ttk,filedialog,messagebox
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageChops,ImageTk
#####################   Main window ###################
difference = Tk()
difference.geometry("1000x700")
difference.title('Difference finder')
difference.resizable(False,False)
#################  Textvariables ######################
global path_of_img1,path_of_img2,first_img,second_img
path_of_img1  = StringVar()
path_of_img2 = StringVar()
######################   Labels ####################
Label(difference,text='Path of first image').place(x=10,y=10)
Label(difference,text='Path of second image').place(x=10,y=60)
#####################  Functions & Canvas  #################
def browse_img1():
    global img1
    first_img.delete(0,END)
    img1 = filedialog.askopenfilename()
    first_img.insert(INSERT,img1)
def first_pane():
    global canvas1
    canvas1 = Canvas(difference,width=300,height=500,bg='white')
    canvas1.place(x=10,y=100)
def second_pane():
    global canvas2
    canvas2 = Canvas(difference,width=300,height=500,bg='white')
    canvas2.place(x=350,y=100)
def browse_img2():
    global img2
    second_img.delete(0,END)
    img2 = filedialog.askopenfilename()
    second_img.insert(INSERT,img2)
def import_img1():
    if path_of_img1.get() == "":
        messagebox.showwarning('','Please input the file\'s path')
        return
    if not os.path.exists(path_of_img1.get()):
        messagebox.showerror('','The given path doesn\'t exists')
        return
    try:
        Image.open(path_of_img1.get())
    except:
        messagebox.showerror('','The given file path is not of an image')
        return
    first_pane()
    frame =  cv2.cvtColor(cv2.imread(path_of_img1.get()),cv2.COLOR_BGR2RGB)
    frame1 = imutils.resize(frame,width=300,height=500)
    frame2 = ImageTk.PhotoImage(image=Image.fromarray(frame1))
    canvas1.image = frame2
    canvas1.create_image(0,0,image=frame2,anchor=NW)
def import_img2():
    if path_of_img2.get() == "":
        messagebox.showwarning('','Please input the file\'s path')
        return
    if not os.path.exists(path_of_img2.get()):
        messagebox.showerror('','The given path doesn\'t exists')
        return
    try:
        Image.open(path_of_img2.get())
    except:
        messagebox.showerror('','The given file path is not of an image')
        return
    second_pane()
    frame =  cv2.cvtColor(cv2.imread(path_of_img2.get()),cv2.COLOR_BGR2RGB)
    frame1 = imutils.resize(frame,width=300,height=500)
    frame2 = ImageTk.PhotoImage(image=Image.fromarray(frame1))
    canvas2.image = frame2
    canvas2.create_image(0,0,image=frame2,anchor=NW)
def show_differences():
    try:
        diff = ImageChops.difference(Image.open(path_of_img1.get()),Image.open(path_of_img2.get()))
    except:
        messagebox.showerror('','Both image are totally different')
        return
    if diff.getbbox():
        messagebox.showinfo('','Highlighted area are  the difference')
        diff.show()
####################  Entry boxes ######################
first_img = Entry(difference,width=100,textvariable=path_of_img1)
first_img.place(x=150,y=10)
second_img = Entry(difference,width=100,textvariable=path_of_img2)
second_img.place(x=150,y=60)
######################  Buttons ######################
Button(difference,text='Browse',width=10,command=browse_img1).place(x=850,y=10)
Button(difference,text='Browse',width=10,command=browse_img2).place(x=850,y=60)
Button(difference,text='OK',width=10,command=import_img1).place(x=780,y=10)
Button(difference,text='OK',width=10,command=import_img2).place(x=780,y=60)
Button(difference,text='Show differences',width=25,command=show_differences).place(x=200,y=650)
difference.mainloop()