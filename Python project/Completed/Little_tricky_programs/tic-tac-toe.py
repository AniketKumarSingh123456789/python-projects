import tkinter
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import *
tic = Tk()
tic.geometry('600x600')
tic.resizable(0,0)
tic.title('Tic Tac Toe')
def winning():
    if (btn1['text']=='X') and (btn2['text']=='X') and (btn3['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn4['text']=='X') and (btn5['text']=='X') and (btn6['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn7['text']=='X') and (btn8['text']=='X') and (btn9['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn1['text']=='X') and (btn4['text']=='X') and (btn7['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn2['text']=='X') and (btn5['text']=='X') and (btn8['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn3['text']=='X') and (btn6['text']=='X') and (btn9['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn1['text']=='X') and (btn5['text']=='X') and (btn9['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn3['text']=='X') and (btn5['text']=='X') and (btn7['text']=='X'):
        if messagebox.askyesno('','Cross wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn1['text']=='O') and (btn2['text']=='O') and (btn3['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn4['text']=='O') and (btn5['text']=='O') and (btn6['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn7['text']=='O') and (btn8['text']=='O') and (btn9['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn1['text']=='O') and (btn4['text']=='O') and (btn7['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn2['text']=='O') and (btn5['text']=='O') and (btn8['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn3['text']=='O') and (btn6['text']=='O') and (btn9['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn1['text']=='O') and (btn5['text']=='O') and (btn9['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    if (btn3['text']=='O') and (btn5['text']=='O') and (btn7['text']=='O'):
        if messagebox.askyesno('','Circle wins\nDo you want to play again? ')==True:
            for i in btn_list:
                i['text'] = ''
            return
        exit()
    for i in btn_list:
        if i['text'] == '':
            return
    if messagebox.askyesno('','Match Draw\n Do you want to play again?')== True:
        for i in btn_list:
            i['text'] = ''
        return
    exit()
def cross():
    global cross_count,circle_count,not_filled
    cross_count = 0
    circle_count = 0
    not_filled = 9
    for i in btn_list:
        if (i['text']=='X'):
            cross_count+=1
            not_filled-=1
        if (i['text']=='O'):
            circle_count+=1
            not_filled-=1
    if not_filled==0:
        winning()
        return
def btn1_cross():
    cross()
    if btn1['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn1['text'] = 'X' 
    else:
        btn1['text'] = 'O'
    winning()
def btn2_cross():
    cross()
    if btn2['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn2['text'] = 'X' 
    else:
        btn2['text'] = 'O'
    winning()
def btn3_cross():
    cross()
    if btn3['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn3['text'] = 'X' 
    else:
        btn3['text'] = 'O'
    winning() 
def btn4_cross():
    cross()
    if btn4['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn4['text'] = 'X' 
    else:
        btn4['text'] = 'O'
    winning()
def btn5_cross():
    cross()
    if btn5['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn5['text'] = 'X' 
    else:
        btn5['text'] = 'O'
    winning()  
def btn6_cross():
    cross()
    if btn6['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn6['text'] = 'X' 
    else:
        btn6['text'] = 'O'
    winning() 
def btn7_cross():
    cross()
    if btn7['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn7['text'] = 'X' 
    else:
        btn7['text'] = 'O'
    winning()
def btn8_cross():
    cross()
    if btn8['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn8['text'] = 'X' 
    else:
        btn8['text'] = 'O'
    winning()  
def btn9_cross():
    cross()
    if btn9['text'] != '':
        return
    if (cross_count==0 and circle_count==0) or (not_filled!=9 and cross_count==circle_count):
        btn9['text'] = 'X' 
    else:
        btn9['text'] = 'O'
    winning() 
def restart():
    cross()
    if not_filled==9:
        return
    choice = messagebox.askyesno('','Are you sure?')
    if choice==True:
        for i in btn_list:
            i['text'] = ''
    return
###########################  Labels ########################
for i in range(20,570,10):
    Label(tic,text='|').place(x=200,y=i)
    Label(tic,text='|').place(x=350,y=i)
for i in range(20,570,10):
    Label(tic,text='_').place(x=i,y=150)
    Label(tic,text='_').place(x=i,y=300)
###########################  Buttons ########################
global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn_list
btn1 = Button(tic,text='',command=btn1_cross)
btn1.place(x=100,y=50)
btn2 = Button(tic,text='',command=btn2_cross)
btn2.place(x=100,y=250)
btn3 = Button(tic,text='',command=btn3_cross)
btn3.place(x=100,y=450)
btn4 = Button(tic,text='',command=btn4_cross)
btn4.place(x=250,y=50)
btn5 = Button(tic,text='',command=btn5_cross)
btn5.place(x=250,y=250)
btn6 = Button(tic,text='',command=btn6_cross)
btn6.place(x=250,y=450)
btn7 = Button(tic,text='',command=btn7_cross)
btn7.place(x=450,y=50)
btn8 = Button(tic,text='',command=btn8_cross)
btn8.place(x=450,y=250)
btn9 = Button(tic,text='',command=btn9_cross)
btn9.place(x=450,y=450)
Button(tic,text='Restart game',command=restart).place(x=450,y=550)
btn_list = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
tic.mainloop()