import time,tkinter,pyttsx3
from time import *
from tkinter import *
wisher = Tk()
def wish_me():
	list1 = list(localtime())
	wish = pyttsx3.init()
	if list1[3] < 12:
		wish.say('Good morning sir')
		wish.runAndWait()
	if list1[3] > 12 and list1[3] < 17:
		wish.say('Good Afternoon sir ')
		wish.runAndWait()
	if list1[3] == 12:
		wish.say('Good noon sir')
		wish.runAndWait()
	if list1[3] > 19:
		wish.say('Good night sir')
		wish.runAndWait()
Button(wisher,text='Wish me',width = 7, height = 1, command=wish_me).place(x= 50, y=50)
wisher.mainloop()
