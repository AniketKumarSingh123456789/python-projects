import googletrans,tkinter,clipboard,os
from googletrans import Translator
from tkinter import ttk,messagebox,filedialog
from tkinter import *
from tkinter.ttk import *
##############################  Main window ###########################
tranlator = Tk()
tranlator.title('Translator')
tranlator.geometry('1000x600')
tranlator.resizable(0,0)
############################### Textvariables ##########################
global input_text,translated_text,language,languages,language2
language = StringVar()
language2 = StringVar()
LANGUAGES2 = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (simplified)',
    'zh-tw': 'Chinese (traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Jannada',
    'kk': 'Jazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}
LANGUAGES = {
    'Det': 'Detect language',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (simplified)',
    'zh-tw': 'Chinese (traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Jannada',
    'kk': 'Jazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}
#############################  Functions ###########################
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
def paste():
  input_text.insert(INSERT,clipboard.paste())
def show_hindi_translation():
  if input_text.get(1.0,END)=='':
    messagebox.showwarning('',"Enter some text first")
    return
  translated_text.delete(1.0,END)
  try:
    transation_class = Translator(['translate.google.com'])
    lang = list(LANGUAGES)[list(LANGUAGES.values()).index(language.get())]
    lang2 = list(LANGUAGES.values())
    lang3 = list(LANGUAGES2)[list(LANGUAGES2.values()).index(language2.get())]
    src = lang
    if lang=='Det':
      Language = transation_class.detect(input_text.get(1.0,END)).lang
      index = list(LANGUAGES).index(Language)
      translated_text.delete(1.0,END)
      translated_text.insert(INSERT,lang2[index])
      src = lang2[index]
    translated_text1 = transation_class.translate([input_text.get(1.0,END)], src = src , dest=lang3)
    for translation in translated_text1:
      translated_text.insert(INSERT,translation.text)
  except:
    messagebox.showwarning('','Please check your internet connection')
    return
def copy():
  clipboard.copy(translated_text.get(1.0,END))
def save():
  save_loc  = filedialog.asksaveasfilename(title='Save file',filetypes=(('Text file','*.txt'),('All files' ,'*.*')))
  the_file,the_path = path_extractor(save_loc)
  os.chdir(the_path)
  if '.' not in the_file:
    messagebox.showwarning('','Type the extension of file')
    return
  text_file = open(f'{the_file}.txt', 'a')
  text_file.close()
  with open(f'{the_file}.txt','w',encoding='utf-8') as text_file:
    text_file.write(translated_text.get(1.0,END))
  try:
    os.rename(f'{the_file}.txt',f'{the_file}')
  except FileExistsError:
    messagebox.showerror('','File of this name already exists')
  messagebox.showinfo('','File saved')
def detect():
  try:
    transation_class = Translator(['translate.google.com'])
    lang = list(LANGUAGES)[list(LANGUAGES.values()).index(language.get())]
    lang2 = list(LANGUAGES.values())
    lang3 = list(LANGUAGES2)[list(LANGUAGES2.values()).index(language2.get())]
    Language = transation_class.detect(input_text.get(1.0,END)).lang
    index = list(LANGUAGES).index(Language)
    translated_text.delete(1.0,END)
    translated_text.insert(INSERT,lang2[index])
  except:
    messagebox.showwarning('','Please check your internet connection')
    return
###############################  Label ################################
Label(tranlator,text='Enter the text').place(x=20,y=20)
Label(tranlator,text='Translated text').place(x=15,y=300)
##############################  Combobox ##############################
languages = Combobox(tranlator,textvariable=language,state='readonly')
list_of_languages = list(LANGUAGES.values())
languages['values'] = list(LANGUAGES.values())
languages.current(22)
languages.place(x=750,y=50)
languages2 = Combobox(tranlator,textvariable=language2,state='readonly')
list_of_languages2 = list(LANGUAGES2.values())
languages2['values'] = list(LANGUAGES2.values())
languages2.current(37)
languages2.place(x=750,y=350)
#################################  Text widget #########################
input_text = Text(tranlator,width=70,height=17,font=(20))
input_text.place(x=100,y=20)
translated_text = Text(tranlator,width=70,height=17,font=(50))
translated_text.place(x=100,y=300)
##################################  Buttons #############################
Button(tranlator,text='Paste',command=paste).place(x=900,y=50)
Button(tranlator,text='Show  translation',command=show_hindi_translation).place(x=860,y=150)
Button(tranlator,text='Copy',command=copy).place(x=890,y=350)
Button(tranlator,text='Save',command=save).place(x=860,y=500)
Button(tranlator,text='Detect language',command=detect).place(x=860,y=200)
tranlator.mainloop()
