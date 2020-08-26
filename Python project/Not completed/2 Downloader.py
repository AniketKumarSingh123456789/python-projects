import requests,tkinter,os,threading
from tkinter import *
from tkinter import ttk,filedialog,messagebox
from tkinter.ttk import *
######################   Main window #######################
downloader = Tk()
downloader.geometry('1000x400')
downloader.title('File downloader')
downloader.resizable(False,False)
####################   Text variables ##############################
global browse_btn,name_of_file_box,url_box,name_to_save_label,location_to_save_label,url_of_file_label,path,URLs,location,status,label_of_download,name,start_download_btn,stop_download_btn,pause_download_btn
URLs = StringVar()
location = StringVar()
name = StringVar()
pause_list = ['Resume','Pause']
progressing_download = StringVar()
###################   Function for button #################################
class value:
    value_to_pause = 0
    value_to_stop = 0
    loop_break = 0
def browse():
    path.delete(0,END)
    path_to_save_file = filedialog.askdirectory()
    path.insert(INSERT,path_to_save_file)
def start_downloading():
    if URLs.get()=='':
        messagebox.showwarning('','Please fill the URL of file to start download')
        return
    if location.get()=='':
        messagebox.showwarning('','Give a location to save the file')
        return
    if not os.path.exists(location.get()):
        messagebox.showerror('','The given path to save the file doesn\'t exists')
        return
    if name.get()=='':
        messagebox.showwarning('','Give a name tto your file')
        return
    os.chdir(location.get())
    if os.path.exists(name.get()):
        messagebox.showwarning('','The given file name already exists\nPlease choose another name')
        return
    #######################   Progress bar ###############################
    global status
    status = Progressbar(downloader,length=800,orient='horizontal',maximum=100,mode='determinate',variable=progressing_download)
    try:
        requests.get('https://www.google.com')
    except requests.exceptions.ConnectionError:
        messagebox.showerror('','Please check your internet connection')
        return
    try:
        file_request = requests.get(URLs.get(),stream=1)
    except:
        messagebox.showerror('','Invalid URL')
        return
    url_of_file_label['state'] = 'disable'
    location_to_save_label['state'] = 'disable'
    name_to_save_label['state'] = 'disable'
    url_box['state'] = 'disable'
    name_of_file_box['state'] = 'disable'
    path['state'] = 'disable'
    start_download_btn['state'] = 'disable'
    pause_download_btn['state'] = 'enable'
    stop_download_btn['state'] = 'enable'
    browse_btn['state'] = 'disable'
    status.place(x=30,y=250)
    is_chunked = file_request.headers.get('transfer-encoding','') == 'chunked'
    content_length = file_request.headers.get('content-length')
    total_size = 0
    if not is_chunked and content_length.isdigit():
        total_size = int(content_length)
    else:
        content_length = None
        messagebox.showerror('','The given URL cannot be downloaded')
    chunk_size = 1024
    try:
        with open(name.get(),'wb') as f:
            for chunk in file_request.iter_content(chunk_size=chunk_size):
                if value.value_to_pause==0 and value.value_to_stop==0:
                    current_file_size = os.stat(f'{name.get()}').st_size
                    percent = (current_file_size/total_size)*100
                    status['value']=percent
                    f.write(chunk)
                if value.value_to_stop==1:
                    status.destroy()
                    url_of_file_label['state'] = 'enable'
                    location_to_save_label['state'] = 'enable'
                    name_to_save_label['state'] = 'enable'
                    url_box['state'] = 'enable'
                    name_of_file_box['state'] = 'enable'
                    path['state'] = 'enable'
                    start_download_btn['state'] = 'enable'
                    pause_download_btn['text'] = 'Pause'
                    pause_download_btn['state'] = 'disable'
                    stop_download_btn['state'] = 'disable'
                    browse_btn['state'] = 'enable'
                    messagebox.showinfo('','Download cancelled by you')
                    value.loop_break = 0
                    value.value_to_stop = 0
                    value.value_to_pause = 0
                    os.remove(name.get())
                    return
                elif value.value_to_pause==1:
                    while True:
                        if value.value_to_pause==0:
                            current_file_size = os.stat(f'{name.get()}').st_size
                            percent = (current_file_size/total_size)*100
                            status['value']=percent
                            f.write(chunk)
                            break
                        if value.loop_break==1:
                            break
                        continue
    except ConnectionAbortedError:
        value.value_to_pause = 0
        value.value_to_stop = 0
        value.loop_break = 0
        messagebox.showwarning('','Please check your internet connection')
        return
    except PermissionError:
        os.remove(name.get())
    else:
        value.value_to_pause = 0
        value.value_to_stop = 0
        value.loop_break = 0
        messagebox.showinfo('','Download Completed')
    finally:
        status.destroy()
        url_of_file_label['state'] = 'enable'
        location_to_save_label['state'] = 'enable'
        name_to_save_label['state'] = 'enable'
        url_box['state'] = 'enable'
        name_of_file_box['state'] = 'enable'
        path['state'] = 'enable'
        start_download_btn['state'] = 'enable'
        pause_download_btn['state'] = 'disable'
        stop_download_btn['state'] = 'disable'
        browse_btn['state'] = 'enable'
def start_downloading_thread():
    global thread
    thread = threading.Thread(target=start_downloading)
    thread.daemon = 1
    thread.start()
def pause_downloading_thread():
    if pause_download_btn['text'] == 'Pause':
        value.value_to_pause = 1
    if pause_download_btn['text'] == 'Resume':
        value.value_to_pause = 0
    popped_item = pause_list.pop(0)
    pause_list.append(popped_item)
    pause_download_btn['text'] = pause_list[1]
def stop_downloading():
    choice = messagebox.askyesno('','Are you sure to stop the download?')
    if choice==True:
        value.value_to_stop = 1
        value.loop_break = 1
####################  Labels ###############################
url_of_file_label = Label(downloader,text='Enter the URL of file',width=20)
url_of_file_label.place(x=20,y=20)
location_to_save_label = Label(downloader,text='Enter the location to save file',width=30)
location_to_save_label.place(x=20,y=100)
name_to_save_label = Label(downloader,text='Name of file with extension  to save file',width=40)
name_to_save_label.place(x=20,y=180)
#####################  Entry box ##################################
url_box = Entry(downloader,width=120,textvariable=URLs)
url_box.place(x=150,y=20)
path = Entry(downloader,width=100,textvariable=location)
path.place(x=200,y=100)
name_of_file_box = Entry(downloader,width=80,textvariable=name)
name_of_file_box.place(x=250,y=180)
#############################   Buttons  ##################################
browse_btn = Button(downloader,text='Browse',width=20,command=browse)
browse_btn.place(x=850,y=100)
start_download_btn = Button(downloader,text='Start downloding',width=20,command=start_downloading_thread)
start_download_btn.place(x=200,y=350)
pause_download_btn =  Button(downloader,text='Pause',width=15,command=pause_downloading_thread,state='disable')
pause_download_btn.place(x=450,y=350)
stop_download_btn = Button(downloader,text='Cancel',width=15,command=stop_downloading,state='disable')
stop_download_btn.place(x=650,y=350)
downloader.mainloop()