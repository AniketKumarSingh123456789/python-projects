import tkinter,cv2,device as d,threading,time
from tkinter import ttk,messagebox
from tkinter import *
from tkinter.ttk import *
#############################   Main window  ##########################
snapshot = Tk()
snapshot.title('Take snapshot')
snapshot.geometry('1000x600')
snapshot.resizable(False,False)
#############################   Device confirmation and variables  ###################
global start_streaming_button,stop_streaming_button,capture_button,screen,selected_camera,stream
stream = 0
selected_camera  = StringVar()
try:
    list_of_cameras = d.getDeviceList()
except:
    messagebox.showerror('','Device not found')
    exit()
no_of_cameras = len(list_of_cameras)
############################  Functions for buttons ######################
def start_streaming_button1():
    pos_of_selected_camera = list_of_cameras.index(selected_camera.get())
    cap = cv2.VideoCapture(pos_of_selected_camera)
    screen = Canvas(snapshot,width = cap.get(3), height=cap.get(4),bg='white')
    screen.place(x = 0, y = 100)
    while True:
        ret,frame = cap.read()
        cv2.imwrite('Snapshot.png',frame)
        screen.create_image(0,0, image=PhotoImage(file='Snapshot.png'),anchor=NW)
        time.sleep(2)
        # if stream == 0:
        #     cap.release()
        #     break
def start_streaming():
    stream = 1
    thr = threading.Thread(target=start_streaming_button1)
    thr.daemon = 1
    thr.start()
def stop_streaming():
    pass
def capture():
    pass
#############################  Label ################################
Label(snapshot,text='Select Camera').place(x=50,y=50)
#############################  Combobox  ############################
list_of_cameras_box = Combobox(snapshot,height=20,width=30,state='readonly',values=list_of_cameras,textvariable=selected_camera)
list_of_cameras_box.current(0)
list_of_cameras_box.place(x=200,y=50)
############################  Canvas ################################

############################# Buttons ###############################
start_streaming_button = Button(snapshot,text='Start streaming',command=start_streaming)
start_streaming_button.place(x=500,y=50)
stop_streaming_button = Button(snapshot,text='Stop streaming',command=stop_streaming,state='disable')
stop_streaming_button.place(x=650,y=50)
capture_button = Button(snapshot,text='Capture',command=capture,state='disable')
capture_button.place(x=800,y=50)
snapshot.mainloop()