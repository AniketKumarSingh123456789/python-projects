import tkinter,subprocess,speech_recognition,googletrans,os,gtts,threading
from tkinter import ttk,filedialog,messagebox
from tkinter import *
from tkinter.ttk import *
from googletrans import Translator
from gtts import gTTS
##########################  Main window  #####################
dubber = Tk()
dubber.geometry('900x400')
dubber.title('Dubber')
dubber.resizable(0,0)
########################## Textvariables #####################
global path,path_of_video
path_of_video = StringVar()
########################### Functions ########################
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

def browse_video_file():
    global video_file_path
    video_file_path = filedialog.askopenfilename(initialdir='/',title='Select a video',filetypes=(('Video file','*.mp4;*.webm;*.mpeg'),('Video file','*.m4a;*.m4v;*.m4b;*.f4b;.mov;*.wmv')))
    path.delete(0,END)
    path.insert(INSERT,video_file_path)

def extract_audio():
    global the_path,the_video_file_name,progress
    the_video_file_name,the_path = path_extractor(video_file_path)
    os.chdir(the_path)
    subprocess.check_output(f'ffmpeg -i "{the_video_file_name}" -vn "output.wav" ',shell=True)
    subprocess.check_output(f'ffmpeg -i "{the_video_file_name}" -an -vcodec copy "output.mp4" ',shell=True)
    print('\nAudio extracted successfully\nVideo extracted successfully')
    ######################## Progress ########################
    progress = Progressbar(dubber,length=700,mode='determinate',maximum=100,value=0)
    progress.place(x=20,y=200)
    progress.start()
    progress['value'] = 20
    progress.update()

def extract_text_from_audio():
    extract_audio()
    recognize = speech_recognition.Recognizer()
    with speech_recognition.AudioFile('output.wav') as speech:
        recognize.adjust_for_ambient_noise(speech)
        print('Extracting audio from file')
        chunk_size = 254
        with open('output.txt','a')as audio_text:
            while True:
                try:
                    x = recognize.recognize_google(recognize.listen(speech))[chunk_size-chunk_size:chunk_size]
                except speech_recognition.UnknownValueError:
                    break
                audio_text.write(f'{x} ')
                chunk_size+=254
            print('Text written succesfully')
            progress['value'] = 40
            progress.update()
def translate_text():
    extract_text_from_audio()
    with open('output.txt',encoding='utf-8') as text_file:
        transation_class = Translator(['translate.google.com','translate.google.co.kr'])
        translated_text1 = transation_class.translate([text_file.read()], dest='hi')
        with open('output2.txt','a',encoding='utf-8') as text_file2:
            for translation in translated_text1:
                text_file2.write(translation.text)
    print('Hindi text file generated')
    progress['value'] = 50
    progress.update()


def creating_audio_from_translated_text():
    translate_text()
    with open('output2.txt',encoding='utf-8') as gen_audio:
        text_of_file = gen_audio.read()
    speak = gTTS(text_of_file,lang='hi')
    speak.save('audio.mp3')
    print('Hindi audio generated')
    progress['value'] = 70
    progress.update()
def merging_new_audio_with_video():
    thread = threading.Thread(target=creating_audio_from_translated_text())
    thread.daemon =1
    thread.start()
    subprocess.check_output(f'ffmpeg -i "audio.mp3" -i "output.mp4" -vcodec copy "Final_dubbed_hindi_video.mp4"',shell=True)
    print('Movie dubbed in hindi')
    progress['value'] = 100
    progress.update()
    progress.destroy()
########################## Label #############################
Label(dubber,text='Enter the path of video').place(x=20,y=20)
########################## Entry box ######################
path = Entry(dubber,width=100,textvariable=path_of_video)
path.place(x = 170,y=20)
########################### Button #######################
Button(dubber,text='Browse',command=browse_video_file).place(x=800,y=20)
Button(dubber,text='Start Dubbing',command=merging_new_audio_with_video).place(x=300,y=300)
dubber.mainloop()