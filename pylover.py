# Tools
from tkinter import messagebox
from math import sin, cos
from turtle import *
from tkinter import li
#  Function
def hearta(k):
    return 15*sin(k)**3

def heartb(k):
    return 12 *cos(k)-5*\
        cos(2*k)-2*\
                cos(3*k)-\
                cos(4*k)

#  Message box

request = messagebox.askyesno('Answer', 'Do you love me?')

if request == False:
    for i in range(100):
        pleas_message = messagebox.askyesno('Pleas', 'Plaes')
        if pleas_message == True :
            thank_message  = messagebox.showinfo('(:', 'I LOVE YOU TOO')
            break
        else:
            pleas_message = messagebox.askyesno('Pleas', 'Plaes')
else:
    thank_message  = messagebox.showinfo(':)', 'I LOVE YOU TOO')

#  Heart Part

speed(900)
bgcolor('#000000')
for i in range(10000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range(5):
        color('#FC0FC0')
    goto(0,0)


#  Done App

done()