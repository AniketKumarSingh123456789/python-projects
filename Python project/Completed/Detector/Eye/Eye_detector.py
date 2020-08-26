import tkinter,PIL,cv2,os,imutils
from tkinter import ttk,filedialog,messagebox
from PIL import Image,ImageTk
from tkinter import *
from tkinter.ttk import *
#####################   Main window ######################
detector = Tk()
detector.geometry('1000x600')
detector.resizable(0,0)
detector.title('Face detector')
###################  Textvariables #######################
global path_of_image,path_box
path_of_image = StringVar()
########################## Functions #####################
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
def browse():
    image_path = filedialog.askopenfilename()
    path_box.delete(0,END)
    path_box.insert(INSERT,image_path)
def ok():
    if path_of_image.get()=='':
        messagebox.showwarning('','Please give the path of image')
        return
    if not os.path.exists(path_of_image.get()):
        messagebox.showerror('','The given image path does\'t exists')
        return
    try:
        img_obj = PIL.Image.open(path_of_image.get())
    except:
        messagebox.showerror('','The given file is not an image')  
        return
    global canvas1
    canvas1 = Canvas(detector,width=500,height=500,bg='white')
    canvas1.place(x=10,y=90)
    frame =  cv2.cvtColor(cv2.imread(path_of_image.get()),cv2.COLOR_BGR2RGB)
    frame1 = imutils.resize(frame,width=500,height=500)
    frame2 = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame1))
    canvas1.image = frame2
    canvas1.create_image(0,0,image=frame2,anchor=NW)
def detect_face():
    img_obj2 = PIL.Image.open(path_of_image.get())
    img_obj2.save('output.png')
    img = cv2.imread('output.png')
    face_csc = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_csc.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 5)
    cv2.imwrite('output.png',img)
    canvas1.destroy()
    canvas2 = Canvas(detector,width=500,height=500,bg='white')
    canvas2.place(x=10,y=90)
    frame =  cv2.cvtColor(cv2.imread('output.png'),cv2.COLOR_BGR2RGB)
    frame1 = imutils.resize(frame,width=500,height=500)
    frame2 = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame1))
    canvas2.image = frame2
    canvas2.create_image(0,0,image=frame2,anchor=NW)
def save_image():
    dir_to_save = filedialog.asksaveasfilename(title='Save Image',filetypes=(('Image','*.jpg;*.bmp'),('Image','*.png',)))
    the_file,the_path = path_extractor(dir_to_save)
    if '.' not in the_file:
        messagebox.showwarning('','Type extension of the image')
        return
    final_img_obj = PIL.Image.open('output.png')
    current_path = os.getcwd()
    os.chdir(the_path)
    final_img_obj.save(the_file)
    os.chdir(current_path)
    messagebox.showinfo('','Image saved')
##########################  Label #######################
Label(detector,text='Enter the path of image').place(x=20,y=20)
########################## Entry box #########################
path_box = Entry(detector,width=100,textvariable=path_of_image)
path_box.place(x=170,y=20)
####################### Button ############################
Button(detector,text='OK',command=ok).place(x=800,y=20)
Button(detector,text='Browse',command=browse).place(x=900,y=20)
Button(detector,text='Detect eye',command=detect_face).place(x=870,y=300)
Button(detector,text='Save image',command=save_image).place(x=870,y=380)
detector.mainloop()