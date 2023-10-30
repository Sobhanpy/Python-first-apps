#tools

from tkinter import*
from tkinter import messagebox

#variable

bg = '#201A31'
fg = '#0DF5E3'
time = 0

#functions

# Start Button Function
def start():
  global time
  if time > 0 :
    start_button.config(state= DISABLED)  
    time -= 1
    time_lable.config(text=time)
    time_lable.after(1000, start)

    if time == 0:
        start_button.config(state= NORMAL)  
        resart_button.config(state= NORMAL)
        messagebox.showwarning('Timer', 'Time is Up')
        empty_string = StringVar()
        main_entry.config(text=empty_string)

#  Restart Button Function

def restart():
    time = 0
    main_entry.delete(0, END)
    time_lable.config(text=f'{time}')

#  Set Button Function

def set():
    global time
    timee = StringVar()
    timee = main_entry.get()
    time = int(timee)
    time_lable.config(text=time)

#config

win = Tk()
win.geometry('600x500+350+125')
win.configure(bg=bg)
win.title('Timer')

#button & lable & entry

time_lable= Label(bg=bg, fg=fg, text=time, font='belguim 150', width=5)
time_lable.place(x=2, y=20)

main_entry =Entry(fg=bg, bg =fg, width=12, font='belguim 25')
main_entry.place(x=350, y=250)

start_button = Button(command=start, text='Start', bg=fg, fg=bg, activebackground=bg, activeforeground=fg, width=8, font='belguim 20')
start_button.place(x=230, y=340)

resart_button = Button(command=restart, text='Restart', bg=fg, fg=bg, activebackground=bg, activeforeground=fg, width=8, font='belguim 20')
resart_button.place(x=70, y=340)

set_button = Button(command=set, text='Set', bg=fg, fg=bg, activebackground=bg, activeforeground=fg, width=8, font='belguim 20')
set_button.place(x=390, y=340)

# Page Mainoloop

win.mainloop()