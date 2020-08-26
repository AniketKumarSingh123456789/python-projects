import sys,tkinter,scipy,threading,cv2,matplotlib,sounddevice,os,time,subprocess,pyaudio,device,shutil,noisereduce,device
from tkinter import ttk,filedialog,messagebox
from tkinter import *
from PyQt5 import QtWidgets
from tkinter.ttk import *
from scipy.io import wavfile
from sounddevice import *
import matplotlib.pyplot as plt
##################  Main window ########################
media = Tk()
media.resizable(False,False)
media.geometry('400x500')
media.title('Media handler')
######################  Functions ########################
def browse_video():
    video_file_path = filedialog.askopenfilename(initialdir='/',title='Select a video',filetypes=(('Video file','*.mp4;*.webm;*.mpeg'),('Video file','*.m4a;*.m4v;*.m4b;*.f4b;.mov;*.wmv')))
    location_of_video.delete(0,END)
    location_of_video.insert(INSERT,video_file_path)
def browse_audio():
    audio_file_path = filedialog.askopenfilename(initialdir='/',title='Select an audio',filetypes=(('Audio file','*.mp3;*.wav;*.flac'),('Audio file','*.aac;*.wma;*.aif;*.ogg;.mid;*.4mp')))
    location_of_audio.delete(0,END)
    location_of_audio.insert(INSERT,audio_file_path)
def browse_final_video():
    directory_of_final_video = filedialog.askdirectory()
    location_of_final_video.delete(0,END)
    location_of_final_video.insert(INSERT,directory_of_final_video)
def start_combining():
    if path_of_video.get()=='':
        messagebox.showwarning('','Please fill the path of video file')
        return
    if path_of_audio.get()=='':
        messagebox.showwarning('','Please fill the path of audio file')
        return
    if path_of_final_video.get()=='':
        messagebox.showwarning('','Please fill the path of final video output')
        return
    if not os.path.exists(path_of_video.get()):
        messagebox.showwarning('','The video not exists at it\'s given path ')
        return    
    if not os.path.exists(path_of_audio.get()):
        messagebox.showwarning('','The audio  not exists at it\'s given path ')
        return
    if not os.path.exists(path_of_final_video.get()):
        messagebox.showwarning('','The directory to save final output not exists')
        return
    if not (location_of_video.get().endswith('.m4a') or path_of_video.get().endswith('.mpg') or path_of_video.get().endswith('.mp4') or path_of_video.get().endswith('.webm') or path_of_video.get().endswith('.m4v') or path_of_video.get().endswith('.m4b') or path_of_video.get().endswith('.wmv') or path_of_video.get().endswith('.mov') or path_of_video.get().endswith('.f4b')):
        messagebox.showerror('','The given video file is not video')
        return
    if not (path_of_audio.get().endswith('.flac') or path_of_audio.get().endswith('.mp3') or path_of_audio.get().endswith('.wav') or path_of_audio.get().endswith('.aac') or path_of_audio.get().endswith('.wma') or path_of_audio.get().endswith('.aif') or path_of_audio.get().endswith('.ogg') or path_of_audio.get().endswith('.mid') or path_of_audio.get().endswith('.4mp') ):
        messagebox.showerror('','The given audio file is not audio')
        return
    if final_video_name.get()=='':
        messagebox.showwarning('','Please fill the name of final video')
        return
    os.chdir(path_of_final_video.get())
    subprocess.check_output(f'ffmpeg -i "{path_of_audio.get()}" -i "{path_of_video.get()}" -vcodec copy "{final_video_name.get()}"."{format_of_video.get()}"',shell=True)
    messagebox.showinfo('','Audio and video combined successfully')
    if play.get()==1:
        os.startfile(final_video_name.get()+"."+format_of_video.get())
def combiner():
    media.destroy()
    ################### Combine window ########################
    global combine
    combine = Tk()
    combine.resizable(False,False)
    combine.geometry('1000x550')
    combine.title('Combine')
    ###################### Textvariables ##################
    global path_of_audio,path_of_video,path_of_final_video,location_of_audio,location_of_video,location_of_final_video,complete_label,final_video_name,format_of_video,play
    path_of_video = StringVar()
    path_of_audio = StringVar()
    path_of_final_video = StringVar()
    play = IntVar()
    final_video_name = StringVar()
    format_of_video = StringVar()
    ################### Labels ##########################
    Label(combine,text='Path of video').place(x=20,y=20)
    Label(combine,text='Path of audio').place(x=20,y=80)
    Label(combine,text='Location to save final video',width=35).place(x=20,y=140)
    Label(combine,text='Name of final video',width=35).place(x=20,y=200)
    complete_label =  Label(combine,text='Combining complete',width=35)
    ###################### Entry box ######################
    location_of_video =  Entry(combine,width=100,textvariable=path_of_video)
    location_of_video.place(x=100,y=20)
    location_of_audio = Entry(combine,width=100,textvariable=path_of_audio)
    location_of_audio.place(x=100,y=80)
    location_of_final_video = Entry(combine,width=100,textvariable=path_of_final_video)
    location_of_final_video.place(x=170,y=140)
    final_name_of_video =  Entry(combine,width=100,textvariable=final_video_name)
    final_name_of_video.place(x=150,y=200)
    #############################  Checkbox ##############
    Checkbutton(combine,text='Play video after combining',variable=play).place(x=240,y=270)
    ###########################  Combobox ################
    formats = Combobox(combine,textvariable=format_of_video,state='readonly')
    formats['values'] = ['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b']
    formats.current(1)
    formats.place(x=800,y=200)
    #################### Buttons #########################
    Button(combine,text='Browse',command=browse_video).place(x=750,y=20)
    Button(combine,text='Browse',command=browse_audio).place(x=750,y=80)
    Button(combine,text='Browse',command=browse_final_video).place(x=800,y=140)
    Button(combine,text='Start combining',command=start_combining).place(x=400,y=450)
    combine.mainloop()
# ------------------------------------------- END OF COMBINING PROGRAM --------------------------
def browse_video_file():
    video_file_path = filedialog.askopenfilename(initialdir='/',title='Select a video',filetypes=(('Video file','*.mp4;*.webm;*.mpg'),('Video file','*.m4a;*.m4v;*.m4b;*.f4b;.mov;*.wmv')))
    file_dir.delete(0,END)
    file_dir.insert(INSERT,video_file_path)
def browse_save_location(): 
    location_to_save_both_file = filedialog.askdirectory()
    save_dir.delete(0,END)
    save_dir.insert(INSERT,location_to_save_both_file)
def start_seperation():
    if location_of_video.get() == '':
        messagebox.showwarning('','Please give the path of video file')
        return
    if location_to_save.get()=='':
        messagebox.showwarning('','Please give a location to save files after seperation')
        return
    if name_of_video.get()=='':
        messagebox.showwarning('','Give a name to save your video file')
        return
    if name_of_audio.get()=='':
        messagebox.showwarning('','Give a name to save your audio file')
        return
    if not os.path.exists(location_of_video.get()):
        messagebox.showerror('','df')
        return
    if not os.path.exists(location_to_save.get()):
        messagebox.showerror('','Directory to save audio and video files doesn\'t exists')
        return
    if not (location_of_video.get().endswith('.m4a') or location_of_video.get().endswith('.mpg') or  location_of_video.get().endswith('.mp4') or  location_of_video.get().endswith('.webm') or  location_of_video.get().endswith('.m4v') or  location_of_video.get().endswith('.m4b') or  location_of_video.get().endswith('.wmv') or  location_of_video.get().endswith('.mov') or  location_of_video.get().endswith('.f4b' )):
        messagebox.showerror('','The given video file is not video')
        return
    os.chdir(location_to_save.get())    
    subprocess.check_output(f'ffmpeg -i "{location_of_video.get()}" -an -vcodec copy "{name_of_video.get()}.{video_format.get()}" ',shell=True)
    subprocess.check_output(f'ffmpeg -i "{location_of_video.get()}" -vn "{name_of_audio.get()}.{audio_format.get()}" ',shell=True)
    messagebox.showinfo('','Audio and video seperated successfully')
    if play_video.get()==1:
        os.startfile(name_of_video.get()+"."+video_format.get())
    if play_audio.get()==1:
        os.startfile(name_of_audio.get()+"."+audio_format.get())
def seperator():
    media.destroy()
    #####################  Seperate window ########################
    global seperate
    seperate = Tk()
    seperate.geometry('1000x550')
    seperate.title('Seperate')
    seperate.resizable(0,0)
    #################  Textvariables ####################
    global location_of_video,location_to_save,name_of_video,name_of_audio,save_dir,file_dir,format_of_video,format_of_audio,video_format,audio_format,play_audio,play_video
    location_of_video = StringVar()
    location_to_save = StringVar()
    name_of_video = StringVar()
    name_of_audio = StringVar()
    video_format = StringVar()
    audio_format = StringVar()
    play_audio = IntVar()
    play_video = IntVar()
    ####################### Labels #################################
    Label(seperate,text='Location of file').place(x=20,y=20)
    Label(seperate,text='Location to save audio and video after seperation').place(x=20,y=80)
    Label(seperate,text='Name of video').place(x=20,y=140)
    Label(seperate,text='Name of audio').place(x=20,y=200)
    ###################### Entry boxes ###########################
    file_dir = Entry(seperate,width=100,textvariable=location_of_video)
    file_dir.place(x=120,y=20)
    save_dir = Entry(seperate,width=100,textvariable=location_to_save)
    save_dir.place(x=290,y=80)
    Entry(seperate,width=100,textvariable=name_of_video).place(x=120,y=140)
    Entry(seperate,width=100,textvariable=name_of_audio).place(x=120,y=200)
    ######################### Combobox #################################
    format_of_video =  Combobox(seperate,textvariable =video_format,state='readonly')
    format_of_video['value'] =  ['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b']
    format_of_video.current(1)
    format_of_video.place(x=750,y=140)
    format_of_audio = Combobox(seperate,textvariable =audio_format,state='readonly')
    format_of_audio['values'] = ['mp3','wav','flac','aac','wma','ogg','mid','aif','4mp']
    format_of_audio.current(0)
    format_of_audio.place(x=750,y=200)
    #############################  Checkbox ##############
    Checkbutton(seperate,text='Play audio after seperation',variable=play_audio).place(x=100,y=270)
    Checkbutton(seperate,text='Play video after seperation',variable=play_video).place(x=100,y=350)
    ##########################  Buttons ##############################
    Button(seperate,text='Browse',command=browse_video_file).place(x=750,y=20)
    Button(seperate,text='Browse',command=browse_save_location).place(x=920,y=80)
    Button(seperate,text='Start seperation',command=start_seperation).place(x=400,y=450)
    seperate.mainloop()
# -------------------------------- END OF SEPERATOR  PROGRAM----------------------------------------
# ---------------------------------   FUNCTIONS OF WEBCAM RECORDING ------------------------
def browse_loc_to_save_recorded_video():
    directory = filedialog.askdirectory()
    loc_to_save_video.delete(0,END)
    loc_to_save_video.insert(INSERT,directory)
def start_video_rec():
    print(var_for_mic.get(),var_for_webcam.get())
# -----------------------------------  FUNCTIONS OF  RECORD PC SCREEN ------------------------------
def browse_path():
    actual_location = filedialog.askdirectory()
    if actual_location!='':
        location_of_video.delete(0,END)
    location_of_video.insert(INSERT,actual_location)
def hightlight_mouse_():
    pass 
def rec_system_sound():
    pass
def start_screen_rec():
    pass
def pause_screen_rec():
    pass
def stop_screen_rec():
    pass
def full_screen():
    if  width_box['state'] != 'readonly' and height_box['state'] != 'readonly':
        width_box['state'] = 'readonly'
        height_box['state'] = 'readonly'
def custom_size():
    width_box['state'] = 'write'
    height_box['state'] = 'write'
def select_screen():
    if  width_box['state'] != 'readonly' and height_box['state'] != 'readonly':
        width_box['state'] = 'readonly'
        height_box['state'] = 'readonly'
# -------------------------------------  FUNCTIONS OF RECORD PC SCREEN AND WEBCAM -------------------
# -------------------------------------  FUNCTIONS OF RECORD PC SCREEN AND WEBCAM ENDS  -------------------
def choose_next():
    if choose_option_for_video_rec.get()=='':
        messagebox.showwarning('','Please choose a option')
        return
    video_rec.destroy()
    if choose_option_for_video_rec.get()=='Record from webcam':
        ########################  Record from webcam window ###################
        global rec_from_webcam
        rec_from_webcam = Tk()
        rec_from_webcam.geometry('1000x600')
        rec_from_webcam.title('Record from webcam')
        rec_from_webcam.resizable(0,0)
        ###########################  Textvariables #############################
        global var_for_webcam,var_for_mic,loc_to_save_recorded_video,video_format,play_after_rec,loc_to_save_video,name_of_recorded_video,audio_devices,webcams,audio_device,webcam
        loc_to_save_recorded_video = StringVar()
        name_of_recorded_video =StringVar()
        video_format = StringVar()
        audio_device = StringVar()
        webcam = StringVar()
        play_after_rec = IntVar()
        var_for_webcam = StringVar()
        var_for_mic = StringVar()
        ###########################  Labels ##################################
        Label(rec_from_webcam,text='Path to save video after recording').place(x=20,y=20)
        Label(rec_from_webcam,text='Name of file').place(x=20,y=100)
        Label(rec_from_webcam,text='Choose Webcam').place(x=20,y=200)
        Label(rec_from_webcam,text='Choose Microphone').place(x=20,y=300)
        ############################## Entry boxes ###########################
        loc_to_save_video = Entry(rec_from_webcam,width=100,textvariable=loc_to_save_recorded_video)
        loc_to_save_video.place(x=250,y=20)
        Entry(rec_from_webcam,width=100,textvariable=name_of_recorded_video).place(x=100,y=100)
        ############################### Combobox #############################
        format_of_video =  Combobox(rec_from_webcam,textvariable =video_format,state='readonly')
        format_of_video['value'] =  ['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b']
        format_of_video.current(1)
        format_of_video.place(x=750,y=100)
        list_of_mic = []
        list_of_webcams = device.getDeviceList()
        number_of_devices = pyaudio.PyAudio().get_host_api_info_by_index(0).get('deviceCount')
        for i in range(0,number_of_devices):
            if 'Input' in pyaudio.PyAudio().get_device_info_by_host_api_device_index(0,i).get("name"):
                continue
            if pyaudio.PyAudio().get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
                list_of_mic.append(pyaudio.PyAudio().get_device_info_by_host_api_device_index(0,i).get("name"))
        webcams = Combobox(rec_from_webcam,width=50,textvariable=var_for_webcam,state='readonly')
        webcams['value'] = list_of_webcams
        webcams.current(0)
        webcams.place(x=150,y=200)
        audio_devices = Combobox(rec_from_webcam,width=50,textvariable=var_for_mic,state='readonly')
        audio_devices['value'] = list_of_mic
        audio_devices.current(0)
        audio_devices.place(x=150,y=300)
        ##############################  Checkbutons #########################
        Checkbutton(rec_from_webcam,text='Play video after recording',variable=play_after_rec).place(x=300,y=200)
        ################################# Button ###########################
        Button(rec_from_webcam,text='Browse',command=browse_loc_to_save_recorded_video).place(x=880,y=20)
        Button(rec_from_webcam,width=23,text='Start recording',command=start_video_rec).place(x=300,y=500)
        rec_from_webcam.mainloop()
# ----------------------------------  RECORD WEBCAM ENDS -----------------------------
    if choose_option_for_video_rec.get()=='Record PC screen':
        ##########################   Record PC screen  Window #######################
        global rec_screen
        rec_screen = Tk()
        rec_screen.geometry('1000x600')
        rec_screen.title('Record Computer Screen')
        rec_screen.resizable(0,0)
        ##############################   Textvariables ##############################
        global location_of_video,screen_area,width,width_box,height_box,height,location_to_save_video,name_of_video_to_save,video_format1,format_of_video1,record_system_sound,hightlight_mouse_pointer,play_video1
        location_to_save_video = StringVar()
        name_of_video_to_save = StringVar()
        video_format1 = StringVar()
        screen_area = StringVar()
        width = StringVar()
        height = StringVar()
        record_system_sound = IntVar()
        hightlight_mouse_pointer = IntVar()
        play_video1 = IntVar()
        ################################# Labels ##################################
        Label(rec_screen,text='Location to save video').place(x=20,y=20)
        Label(rec_screen,text='Name of  video').place(x=20,y=100)
        Label(rec_screen,text='X').place(x=280,y=400)
        ###################################  Entry box ###########################
        location_of_video = Entry(rec_screen,width=100,textvariable=location_to_save_video)
        location_of_video.place(x=150,y=20)
        Entry(rec_screen,width=100,textvariable=name_of_video_to_save).place(x=150,y=100)
        width_box = Entry(rec_screen,width=10,textvariable=width,state='disable')
        width_box.place(x=200,y=400)
        height_box = Entry(rec_screen,width=10,textvariable=height,state='disable')
        height_box.place(x=300,y=400)
        ###############################  Combobox ###############################
        format_of_video1 =  Combobox(rec_screen,textvariable =video_format1,state='readonly')
        format_of_video1['value'] =  ['mpg','mp4','m4a','m4v','m4b','webm','mov','wmv','f4b']
        format_of_video1.current(1)
        format_of_video1.place(x=800,y=100)
        ##################################  Chekbutton ############################
        Checkbutton(rec_screen,text='Record System sound',variable=record_system_sound).place(x=80,y=200)
        Checkbutton(rec_screen,text='Highlight mouse pointer',variable=hightlight_mouse_pointer).place(x=300,y=200)
        Checkbutton(rec_screen,text='Play video after recording',variable=play_video1).place(x=500,y=200)
        ##################################  Radiobutton ###########################
        Radiobutton(rec_screen,text='Full screen',width=15,value='Full screen',variable=screen_area,command=full_screen).place(x=80,y=300)
        Radiobutton(rec_screen,text='Custom size',width=15,value='Custom size',variable=screen_area,command=custom_size).place(x=80,y=400)
        Radiobutton(rec_screen,text='Select screen',width=15,value='Select screen',variable=screen_area,command=select_screen).place(x=80,y=500)
        ##################################  Buttons ################################
        Button(rec_screen,text='Browse',command=browse_path).place(x=800,y=20)
        Button(rec_screen,text='Start',command=start_screen_rec).place(x=300,y=550)
        Button(rec_screen,text='Pause',command=pause_screen_rec,state='disable').place(x=400,y=550)
        Button(rec_screen,text='Stop',command=stop_screen_rec,state='disable').place(x=500,y=550)
        rec_screen.mainloop()
# -------------------------------------  RECORD PC SCREEN ENDS ----------------------------- 
    if choose_option_for_video_rec.get()=='Record webcam and PC screen':
        pass
def record_video():
    media.destroy()
    #################################  video recorder window #########################
    global video_rec,choose_option_for_video_rec
    video_rec = Tk()
    video_rec.geometry('500x500')
    video_rec.resizable(0,0)
    video_rec.title('Video Recorder')
    ############################### Textvariables #############################
    choose_option_for_video_rec = StringVar()
    ################################ Radio buttons #############################
    Radiobutton(video_rec,text='Record from webcam',width=30,value='Record from webcam',variable=choose_option_for_video_rec).place(x=100,y=100)
    Radiobutton(video_rec,text='Record PC screen',width=30,value='Record PC screen',variable=choose_option_for_video_rec).place(x=100,y=200)
    Radiobutton(video_rec,text='Record webcam and PC screen',width=30,value='Record webcam and PC screen',variable=choose_option_for_video_rec).place(x=100,y=300)
    ################################# Button ################################
    Button(video_rec,text='Next',command=choose_next).place(x=150,y=450)
    video_rec.mainloop()
# ----------------------------------- END OF VIDEO RECORDER -------------------------------------
task = ['Resume','Pause']
def browse_dir():
    global dir_to_save_audio
    dir_to_save_audio = filedialog.askdirectory()
    if dir_to_save_audio!='':
        path_to_save.delete(0,END)
        path_to_save.insert(INSERT,dir_to_save_audio)
def stop_audio_rec():
    global value_to_stop
    value_to_stop = 1
    pause_btn['state'] = 'disable'
    stop_btn['state'] = 'disable'
    start_btn['state'] = 'enable'
def start():
    global  value_to_stop 
    value_to_stop = 0
    if os.path.exists(os.getcwd()+'/'+'dfhfhfhearggsh'):
        shutil.rmtree('dfhfhfhearggsh')
    audio_number = 1
    current_path = os.getcwd()
    os.mkdir('dfhfhfhearggsh')
    os.chdir('dfhfhfhearggsh')
    frequency = 44180
    seconds = 3
    while value_to_stop==0:
        print(value_to_stop)
        if pause_btn['text'] != 'Resume' or value_to_stop!=0 :
            try:
                if pause_btn['text'] == 'Resume' or value_to_stop!=0 :
                    continue
                recorded_file = rec(int(seconds*frequency), samplerate=frequency, channels=2)
                if pause_btn['text'] == 'Resume' or value_to_stop!=0:
                    continue
                wait()
                if pause_btn['text'] == 'Resume' and value_to_stop!=0:
                    continue
                wavfile.write(f'{audio_number}.mp3', frequency, recorded_file)
                audio_number+=1
            except PermissionError:
                messagebox.showwarning('','Please run the software as administrator')
                os.chdir(path_to_save_recorded_audio.get())
                shutil.rmtree('dfhfhfhearggsh')
                return
            except Exception as e:
                print(e)
    try:
        with open('final_audio.txt','w') as f:
            for i in range(1,audio_number):
                if os.path.exists(f'{i}.mp3'):
                    f.write(f'file {i}.mp3\n')
            f.close()
        subprocess.check_output(f'ffmpeg -safe 0 -f concat -i final_audio.txt {name_of_audio_file.get()}.{audio_format.get()}',shell=True)
        shutil.move(f'{name_of_audio_file.get()}.{audio_format.get()}',f'{current_path}')
        os.chdir(current_path)
        shutil.rmtree('dfhfhfhearggsh')
        if reduce_noise.get()==1 or plot_graph.get()==1:
            subprocess.check_output(f'ffmpeg -i {name_of_audio_file.get()}.{audio_format.get()} {name_of_audio_file.get()}.wav',shell=True)
            rate, data = wavfile.read(f'{name_of_audio_file.get()}.wav')
            os.remove(f'{name_of_audio_file.get()}.wav')
            if reduce_noise.get()==1:
                sound_processing = Progressbar(sound_rec,mode='indeterminate',length=300)
                processing_label = Label(text='Processing your audio')
                processing_label.place(x=480,y=250)
                sound_processing.place(x=400,y=300)
                sound_processing.start()
                clear_audio = noisereduce.reduce_noise(audio_clip = data, noise_clip= data[:], verbose = True)
                print(clear_audio,type(clear_audio),dir(clear_audio))
                messagebox.showinfo('',dir(clear_audio))
                sound_processing.destroy()
                processing_label.destroy()
            if plot_graph.get()==1:
                plt.plot(data)
                plt.show()
        if play_after_rec.get()==1:
            os.startfile(f'{name_of_audio_file.get()}.{audio_format.get()}')
    except Exception as e:
        print(e)
def start_audio_rec():
    if path_to_save_recorded_audio.get()=='':
        messagebox.showwarning('','Give destinaton to save the audio after recording')
        return
    if name_of_audio_file.get()=='':
        messagebox.showwarning('','Give a name to save the audio after recording')
        return
    if not os.path.exists(path_to_save_recorded_audio.get()):
        messagebox.showerror('','Given path to save audio not exists ')
        return
    if os.path.exists(f'{path_to_save_recorded_audio.get()}/{name_of_audio_file.get()}.{audio_format.get()}'):
        messagebox.showwarning('','Given file name already exists at given location')
        return
    os.chdir(path_to_save_recorded_audio.get())
    global lets_start
    pause_btn['state'] = 'enable'
    stop_btn['state'] = 'enable'
    lets_start = threading.Thread(target=start)
    lets_start.daemon = 1
    lets_start.start()
    start_btn['state'] = 'disable'
def pause_audio_rec():
    pause_btn['text'] = task[0]
    remove = task[0]
    task.remove(remove)
    task.append(remove)
def record_audio():
    media.destroy()
    #############################  Main window ##################################
    global sound_rec,start_btn,pause_btn,stop_btn,value_to_stop 
    sound_rec = Tk()
    sound_rec.geometry('1000x600')
    sound_rec.title('Sound recorder')
    sound_rec.resizable(0,0)
    ################################  Textvariable ############################
    global path_to_save,path_to_save_recorded_audio,name_of_audio_file,audio_format,play_after_rec,plot_graph,choose_mic,reduce_noise
    play_after_rec = IntVar()
    plot_graph = IntVar()
    name_of_audio_file = StringVar()
    path_to_save_recorded_audio = StringVar()
    audio_format = StringVar()
    choose_mic = StringVar()
    reduce_noise = IntVar()
    value_to_stop = 0
    ############################ Labels ######################################
    Label(sound_rec,text='Path to save audio').place(x=20,y=20)
    Label(sound_rec,text='Name of file').place(x=20,y=100)
    Label(sound_rec,text='Choose device').place(x=20,y=200)
    ############################ Entry box ##################################
    path_to_save = Entry(sound_rec,width=100,textvariable=path_to_save_recorded_audio)
    Entry(sound_rec,width=100,textvariable=name_of_audio_file).place(x=150,y=100)
    path_to_save.place(x=150,y=20)
    #########################   Checkbuttons ################################
    Checkbutton(sound_rec,text='Reduce Noise',variable=reduce_noise).place(x=50,y=300)
    Checkbutton(sound_rec,text='Play audio after recording',variable=play_after_rec).place(x=50,y=400)
    Checkbutton(sound_rec,text='Plot graph of recorded audio',variable=plot_graph).place(x=50,y=500)
    ###########################  Combobox ##################################
    audio_formats = Combobox(sound_rec,textvariable=audio_format,state='readonly')
    audio_formats['values'] = ['mp3','wav','flac','aac','wma','ogg','mid','aif','4mp']
    audio_formats.current(0)
    audio_formats.place(x=800,y=100)
    list_of_mic = []
    number_of_devices = pyaudio.PyAudio().get_host_api_info_by_index(0).get('deviceCount')
    for i in range(0,number_of_devices):
        if 'Input' in pyaudio.PyAudio().get_device_info_by_host_api_device_index(0,i).get("name"):
            continue
        if pyaudio.PyAudio().get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
            list_of_mic.append(pyaudio.PyAudio().get_device_info_by_host_api_device_index(0,i).get("name"))
    microphones = Combobox(sound_rec,width=40,textvariable=choose_mic,values=list_of_mic,state='readonly')
    microphones.current(0)
    microphones.place(x=150,y=200)
    ########################### Buttons #####################################
    Button(sound_rec,text='Browse',command=browse_dir).place(x=800,y=20)
    start_btn =  Button(sound_rec,width=20,text='Start',command=start_audio_rec)
    start_btn.place(x=500,y=450)
    pause_btn  = Button(sound_rec,width=20,text='Pause',command=pause_audio_rec,state='disable')
    pause_btn.place(x=500,y=500)
    stop_btn = Button(sound_rec,width=20,text='Stop',command=stop_audio_rec,state='disable')
    stop_btn.place(x=500,y=550)
    sound_rec.mainloop()
# ------------------------------------ END OF SOUND RECORDER --------------------------------------
def choose_file():
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(window,'Select a File','/','Video file(*mpg;*mp4;*m4a;*m4v;*m4b;*web;*mov;*wmv;*f4b) ;; Audio file(*mp3;*wav,*flac;*aac;*wma;*ogg;*mid;*aif;*4mp)')
def play_media():
    media.destroy()
    #####################  Media player ########################
    global window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Media Player")
    window.setGeometry(350,100,700,500)
    ############################# Textvariables ########################
    ############################# Menu #################################
    ############################# Canvas ###############################
    ############################## Buttons #############################
    choose_file_btn = QtWidgets.QPushButton(window)
    choose_file_btn.setGeometry(100,100,100,30)
    choose_file_btn.clicked.connect(choose_file)
    choose_file_btn.setText("Choose File")
    window.show()
    sys.exit(app.exec_())
# ------------------------------------- END OF PLAY MEDIA -------------------------------------------
####################### Buttons #########################
Button(media,text='Combine audio and video',width=30,command=combiner).place(x=60,y=20)
Button(media,text='Seperate audio and video',width=30,command=seperator).place(x=60,y=100)
Button(media,text='Record video',width=30,command=record_video).place(x=60,y=180)
Button(media,text='Record audio',width=30,command=record_audio).place(x=60,y=260)
Button(media,text='Play media',width=30,command=play_media).place(x=60,y=340)
media.mainloop()