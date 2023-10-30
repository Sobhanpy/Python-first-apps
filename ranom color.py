from tkinter import *
from random import choice

# Variables

bg = '#FFFFFF'
fg = '#FF1493'
cod = '#'

# functions

def random():
    colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'D', 'C', 'E', 'F']
    final_color = '#'
    for _ in range(6):
        final_color += choice(colors)
    win.config(bg=final_color)
    codcolorlable.config(text=final_color)

# window gonfigure

win = Tk()
win.geometry("450x480+500+150")

# Button

nextbutton = Button(text="NEXT", command=random, fg=bg, bg=fg, font='belguim 12', height=2, width=15)
nextbutton.place(x=150, y=400)

# Lable

codcolorlable = Label(text="Color code", fg=bg, bg=fg, font='belguim 18', height=2, width=20)
codcolorlable.place(x=80, y=320)

# mainloop

win.mainloop()