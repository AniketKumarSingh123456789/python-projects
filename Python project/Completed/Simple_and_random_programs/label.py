import tkinter
from tkinter import ttk
root=tkinter.Tk()
lis1 = ['Show label','Hide label']
lis2 = ['','This is label']
global x,y
def change():
    lis1.append(lis1[0])
    lis1.remove(lis1[0])
    lis2.append(lis2[0])
    lis2.remove(lis2[0])
    x['text'] = lis1[0]
    y['text'] = lis2[0]
x = tkinter.ttk.Button(root,text=lis1[0],command=change)
x.place(x=300,y=100)
y = tkinter.ttk.Label(root,text=lis2[0])
y.place(x=300,y=200)
root.mainloop()