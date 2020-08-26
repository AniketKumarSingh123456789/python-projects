import tkinter,os,pytube,requests,threading,subprocess
from tkinter import ttk,filedialog,messagebox
from tkinter import *
from pytube import YouTube
from tkinter.ttk import *
##########################    Main window    #############################
vid_down = Tk()
vid_down.title('Youtube Video Downloader')
vid_down.geometry('1000x500')
vid_down.resizable(0,0)
#########################  Textvariables   ###############################
global url_of_video,path_to_save_video,name_of_file,url_of_video_box,name_of_file_box,fetch_detail_btn,browse_path_btn,start_downloading_btn,url_label,location_of_video_label,name_of_file_label
url_of_video = StringVar()
location_to_save_video = StringVar()
name_of_file =StringVar()
#########################  Functions    ###############################
fetch_value = 0
def set_items():
    if type_of_download.get()=='Only Audio':
        extensions['values'] = ['mp3','wav','flac','aac','wma','ogg','mid','aif','4mp']
        extensions.current(0)
        resolutions['values'] = audio_formats
        resolutions.current(0)
    if type_of_download.get()=='Video without Audio':
        extensions['values'] = ['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b']
        extensions.current(1)
        resolutions['values'] = video_formats
        resolutions.current(0)
    if type_of_download.get()=='Video with Audio':
        Label(vid_down,text='Select audio quality').place(x=200,y=250)
        extensions['values'] = ['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b']
        extensions.current(1)
        resolutions['values'] = video_formats
        resolutions.current(0)
def formats():
    global type_of_download,extension,resolution,type1,type2,type3,extensions,resolutions,formats_label
    type_of_download = StringVar()
    extension = StringVar()
    resolution = StringVar()
    # --------------------------      LABEL     -----------------------------
    formats_label =  Label(vid_down,text='Formats')
    formats_label.place(x=30,y=270)
    # ----------------------------   COMBOBOXES   ------------------------------
    extensions = Combobox(vid_down,textvariable=extension,width=10,state='readonly',values=['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b'])
    extensions.place(x=350,y=270)
    extensions.current(0)

    resolutions = Combobox(vid_down,textvariable=resolution,width=10,state='readonly',values=video_formats)
    resolutions.place(x=450,y=270)
    resolutions.current(0)

    # ------------------------------   RADIOBUTTONS ----------------------------
    type1 = Radiobutton(vid_down,text='Video with Audio',width=28,value='Video with Audio',variable=type_of_download,command=set_items)
    type1.place(x=150,y=270)
    type1.invoke()
    type2 = Radiobutton(vid_down,text='Only Audio',width=30,value='Only Audio',variable=type_of_download,command=set_items)
    type2.place(x=150,y=310)
    type3 = Radiobutton(vid_down,text='Video without Audio',width=30,value='Video without Audio',variable=type_of_download,command=set_items)
    type3.place(x=150,y=350)

def fetch():
    global fetch_value,videos,audio_formats,video_formats
    if url_of_video.get()=='':
        messagebox.showwarning('','Give the URL')
        return
    try:
        requests.get('https://www.google.com',stream=1)
    except:
        messagebox.showerror('','Please check your internet connection')
        return
    try:
        requests.get(url_of_video.get(),stream=1)
    except:
        messagebox.showerror('','URL not found')
        return
    try:
        yt = YouTube(url_of_video.get())
    except pytube.exceptions.LiveStreamError:
        messagebox.showerror('','The Video is live so it can\'t be downloaded')
        return
    except pytube.exceptions.VideoUnavailable:
        messagebox.showerror('','Video is unavailabel')
        return
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror('','Invalid URL')
        return
    except pytube.exceptions.PytubeError:
        messagebox.showerror('','Please restart the software')
        return
    except Exception as e:
        print(e)
        exit()
    videos = yt.streams.all()
    video_formats = []
    audio_formats = []
    for i in videos:
        if 'video' in i.mime_type:
            video_formats.append(i.resolution)
        if 'audio' in i.mime_type:
            audio_formats.append(i.abr)
    fetch_value = 1
    video_formats = list(set(video_formats))
    audio_formats = list(set(audio_formats))
    video_formats.sort()
    video_formats.reverse()
    audio_formats.sort()
    audio_formats.reverse()
    for i in videos:
        print(i)
    formats()
def send_to_fetch():
    send = threading.Thread(target=fetch)
    send.daemon =1
    send.start()
def browse():
    path = filedialog.askdirectory()
    if path!='':
        path_to_save_video.delete(0,END)
        path_to_save_video.insert(INSERT,path)
def download():
    actual_resolution = resolution.get()
    actual_format = extension.get()
    if type_of_download.get()=='Only Audio':
        for i in videos:
            if i.abr==actual_resolution:
                i.download(location_to_save_video.get())
                actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                subprocess.check_output(f'ffmpeg -i "{actual_name}.webm" {name_of_file.get()}.{actual_format}', shell=True)
                os.remove(f'{actual_name}.webm')
                messagebox.showinfo('','Audio downloaded')
                break
    elif type_of_download.get()=='Video without Audio':
        for i in videos:
            if i.resolution == actual_resolution:
                if i.mime_type=='video/webm' and actual_format=='webm':
                    i.download(location_to_save_video.get())
                    actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                    os.rename(f'{actual_name}.webm',f'{name_of_file.get()}.webm')
                    messagebox.showinfo('','Video downloaded')
                    break
                elif i.mime_type=='video/mp4' and actual_format=='mp4':
                    i.download(location_to_save_video.get())
                    actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                    os.rename(f'{actual_name}.mp4',f'{name_of_file.get()}.mp4')
                    messagebox.showinfo('','Video downloaded')
                    break   
                elif  (i.mime_type=='video/webm') and  (actual_format!='webm' and actual_format!='mp4'):
                    i.download(location_to_save_video.get())
                    actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                    subprocess.check_output(f'ffmpeg -i "{actual_name}.webm" -an -vcodec copy "{name_of_file.get()}.{actual_format}"',shell=True)
                    os.remove(f'{actual_name}.webm')
                    messagebox.showinfo('','Video downloaded')
                    break
    elif type_of_download.get()=='Video with Audio':
        for i in videos:
            if i.resolution == actual_resolution:
                if i.mime_type=='video/webm' and actual_format=='webm':
                    i.download(location_to_save_video.get())
                    actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                    os.rename(f'{actual_name}.webm',f'{name_of_file.get()}.webm')
                    messagebox.showinfo('','Video downloaded')
                    break
                elif i.mime_type=='video/mp4' and actual_format=='mp4':
                    i.download(location_to_save_video.get())
                    actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                    os.rename(f'{actual_name}.mp4',f'{name_of_file.get()}.mp4')
                    messagebox.showinfo('','Video downloaded')
                    break 
                elif  (i.mime_type=='video/webm') and  (actual_format!='webm' and actual_format!='mp4'):
                    i.download(location_to_save_video.get())
                    actual_name = i.title.replace('#','').replace(';','').replace(':','').replace('.','')
                    try:
                        subprocess.check_output(f'ffmpeg -i "{actual_name}.webm" "{name_of_file.get()}.{actual_format}"',shell=True)
                    except subprocess.CalledProcessError:
                        if os.path.exists(f'{name_of_file.get()}.{actual_format}'):
                            os.remove(f'{name_of_file.get()}.{actual_format}')
                        subprocess.check_output(f'ffmpeg -i "{actual_name}.webm" -c:v libx264 "{name_of_file.get()}.{actual_format}"',shell=True)
                    os.remove(f'{actual_name}.webm')
                    messagebox.showinfo('','Video downloaded')
                    break
    url_of_video_box['state'] = 'enable'
    path_to_save_video['state'] = 'enable'
    name_of_file_box['state'] = 'enable'
    fetch_detail_btn['state'] = 'enable'
    browse_path_btn['state'] = 'enable'
    start_downloading_btn['state'] = 'enable'
    type1['state'] = 'enable'
    type2['state'] = 'enable'
    type3['state'] = 'enable'
    extensions['state'] = 'enable'
    extensions['state'] = 'readonly'
    resolutions['state'] = 'enable'
    resolutions['state'] = 'readonly'
    name_of_file_label['state'] = 'enable'
    location_of_video_label['state'] = 'enable'
    name_of_file_label['state'] = 'enable'
    url_label['state'] = 'enable'
    formats_label['state'] = 'enable'
def download_prerequests():
    global fetch_value
    if fetch_value==0:
        messagebox.showwarning('','Please fetch details before downloading')
        return
    if location_to_save_video.get()=='':
        messagebox.showwarning('','Give a location to download video')
        return
    if not os.path.exists(location_to_save_video.get()):
        messagebox.showerror('','Invalid location to save video')
        return
    if name_of_file.get()=='':
        messagebox.showwarning('','Give a name to the file')
        return
    os.chdir(location_to_save_video.get())
    if os.path.exists(name_of_file.get()+extension.get()):
        messagebox.showerror('','File already exists at given location ')
        return
    url_of_video_box['state'] = 'disable'
    path_to_save_video['state'] = 'disable'
    name_of_file_box['state'] = 'disable'
    fetch_detail_btn['state'] = 'disable'
    browse_path_btn['state'] = 'disable'
    start_downloading_btn['state'] = 'disable'
    type1['state'] = 'disable'
    type2['state'] = 'disable'
    type3['state'] = 'disable'
    extensions['state'] = 'disable'
    resolutions['state'] = 'disable'
    name_of_file_label['state'] = 'disable'
    location_of_video_label['state'] = 'disable'
    name_of_file_label['state'] = 'disable'
    url_label['state'] = 'disable'
    formats_label['state'] = 'disable'
    download_thread = threading.Thread(target=download)
    download_thread.daemon=1
    download_thread.start()
#########################   Labels   ###############################
url_label = Label(vid_down,text='URL of video')
url_label.place(x=30,y=30)
location_of_video_label = Label(vid_down,text='Location to save video')
location_of_video_label.place(x=30,y=110)
name_of_file_label = Label(vid_down,text='Name of file')
name_of_file_label.place(x=30,y=190)
#########################   Entry boxes   ###############################
url_of_video_box = Entry(vid_down,width=100,textvariable=url_of_video)
url_of_video_box.place(x=130,y=30)
path_to_save_video = Entry(vid_down,width=100,textvariable=location_to_save_video)
path_to_save_video.place(x=180,y=110)
name_of_file_box = Entry(vid_down,width=100,textvariable=name_of_file)
name_of_file_box.place(x=130,y=190)
#########################   Button    ###############################
fetch_detail_btn = Button(vid_down,width=15,text='Fetch details',command=send_to_fetch)
fetch_detail_btn.place(x=780,y=30)
browse_path_btn = Button(vid_down,width=15,text='Browse',command=browse)
browse_path_btn.place(x=800,y=110)
start_downloading_btn = Button(vid_down,width=20,text='Start Downloading',command=download_prerequests)
start_downloading_btn.place(x=350,y=450)
vid_down.mainloop()