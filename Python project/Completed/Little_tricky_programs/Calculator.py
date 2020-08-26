import tkinter
from tkinter import ttk,messagebox
from tkinter import *
from tkinter.ttk import *
########################  Main window ##########################
calc = Tk()
calc.title('Calculator')
calc.geometry('400x400')
calc.resizable(0,0)
#######################  Functions ###########################
def zero():
    entry.insert(INSERT,'0')
def one():
    entry.insert(INSERT,'1')
def two():
    entry.insert(INSERT,'2')
def three():
    entry.insert(INSERT,'3')
def four():
    entry.insert(INSERT,'4')
def five():
    entry.insert(INSERT,'5')
def six():
    entry.insert(INSERT,'6')
def seven():
    entry.insert(INSERT,'7')
def eight():
    entry.insert(INSERT,'8')
def nine():
    entry.insert(INSERT,'9')
def erase():
    not_erase = problem.get()[:-1]
    entry.delete(0,END)
    entry.insert(INSERT,not_erase)
def decimal():
    entry.insert(INSERT,'.')
def equate():
    try:
        solution = eval(problem.get())
        entry.delete(0,END)
        entry.insert(INSERT,solution)
    except ZeroDivisionError:
        messagebox.showerror('','Division by zero is not possible')
    except:
        messagebox.showwarning('','Invalid equation')
def square_root():
    question = problem.get()
    entry.delete(0,END)
    try:
        entry.insert(INSERT,eval(question)**0.5)
    except:
        messagebox.showwarning('','Invalid equation')
def add():
    entry.insert(INSERT,'+')
def subtract():
    entry.insert(INSERT,'-')
def multiply():
    entry.insert(INSERT,'*')
def divide():
    entry.insert(INSERT,'/')
def all_clear():
    entry.delete(0,END)
def reciprocal():
    question = problem.get()
    entry.delete(0,END)
    try:
        entry.insert(INSERT,1/eval(question))
    except:
        messagebox.showwarning('','Invalid equation')
########################  Entry ##############################
global entry,problem
problem = StringVar()
entry = Entry(calc,width=60,textvariable=problem)
entry.place(x=20,y=20)
######################## Buttons #############################
Button(calc,width=5,text='0',command=zero).place(x=80,y=350)
Button(calc,width=5,text='1',command=one).place(x=140,y=350)
Button(calc,width=5,text='2',command=two).place(x=200,y=350)
Button(calc,width=5,text='3',command=three).place(x=80,y=300)
Button(calc,width=5,text='4',command=four).place(x=140,y=300)          
Button(calc,width=5,text='5',command=five).place(x=200,y=300)
Button(calc,width=5,text='6',command=six).place(x=80,y=250)
Button(calc,width=5,text='7',command=seven).place(x=140,y=250)         
Button(calc,width=5,text='8',command=eight).place(x=200,y=250)
Button(calc,width=5,text='9',command=nine).place(x=80,y=200)
Button(calc,width=5,text='.',command=decimal).place(x=140,y=200)
Button(calc,width=5,text='+',command=add).place(x=200,y=200)
Button(calc,width=5,text='-',command=subtract).place(x=200,y=150)
Button(calc,width=5,text='*',command=multiply).place(x=260,y=250)
Button(calc,width=5,text='/',command=divide).place(x=260,y=150)
Button(calc,width=5,text='√',command=square_root).place(x=260,y=200)
Button(calc,width=5,text='←',command=erase).place(x=80,y=150)
Button(calc,width=10,text='=',command=equate).place(x=260,y=350)
Button(calc,width=5,text='C',command=all_clear).place(x=140,y=150)
Button(calc,width=5,text='1/x',command=reciprocal).place(x=260,y=300)
calc.mainloop()