from tkinter import ttk,messagebox
from tkinter import *
from tkinter.ttk import *
########################  Main window ##########################
calc = Tk()
calc.title('Calculator')
calc.geometry('600x600')
calc.resizable(0,0)
#######################  Function ###########################
def calculate():
    if num1.get()=='' or num2.get()=='':
        return
    try:
        float(num1.get())
        float(num2.get())
    except:
        messagebox.showerror('','Only numbers are allowed')
        return
    try:
        if operation.get()=="Add":
            answer_label['text'] = f"The sum is :  {float(num1.get())+float(num2.get())}"
        if operation.get()=="Subtract":
            answer_label['text'] = f"The sum is :  {float(num1.get())-float(num2.get())}"
        if operation.get()=="Multiply":
            answer_label['text'] = f"The sum is :  {float(num1.get())*float(num2.get())}"
        if operation.get()=="Divide":
            answer_label['text'] = f"The sum is :  {float(num1.get())/float(num2.get())}"
        if operation.get()=="Remainder":
            answer_label['text'] = f"The sum is :  {float(num1.get())%float(num2.get())}"
    except ZeroDivisionError:
        messagebox.showerror("","Division by zero is not possible")
###################### Textvariables  ######################
global num1,num2,operation,answer_label
num1 = StringVar()
num2 = StringVar()
operation = StringVar()
####################  Labels #########################
Label(calc,text="First number").place(x=20,y=30)
Label(calc,text="Second number").place(x=20,y=200)
Label(calc,text="Choose operation").place(x=20,y=350)
answer_label = Label(calc,text="")
answer_label.place(x=200,y=450)
####################  Combobox  ##########################
operations = Combobox(calc,width=15,textvariable=operation,values=["Add","Subtract","Multiply","Divide","Remainder"],state='readonly')
operations.current(0)
operations.place(x=160,y=350)
###################### Entry boxes ########################
Entry(calc,width=60,textvariable=num1).place(x=120,y=30)
Entry(calc,width=60,textvariable=num2).place(x=120,y=200)
######################## Button #############################
Button(calc,width=20,text="Calculate",command=calculate).place(x=200,y=550)

calc.mainloop()