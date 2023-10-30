#tools
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
# variable=============================================================================================
bg='#201A31'
fg='#0DF5E3'
time = 60
score = 0
colorlist = ['White', 'Red', 'Blue', 'Purple', 'Yellow', 'Black', 'Green']
# window setting=======================================================================================
win = Tk()
win.geometry('780x400+300+150')
win.config(bg=bg)
win.title('ColorGame')
#functions=============================================================================================
def start():
    game()
    if time != 0 :
        countdown()
def shcolor():
    shuffle(colorlist)
shcolor() 
def countdown():
    global time
    if time > 0 :
        time -= 1
        timelable.config(text=f'Time: {time}')
        win.after(1000, countdown)
        if time == 0 :
            messagebox.showwarning('FINISH', 'The time is up!!!')
def game():
    global score
    selectcolor = choice(colorlist)
    shuffle(colorlist)
    selectcolorfg = choice(colorlist)
    selectcolorfg.lower()
    mainlable.config(text=selectcolor, fg=selectcolorfg, bg=bg)
    userinput = str(mainentry.get())
    userinput.lower()
    if userinput == selectcolorfg :
        score = 0
        score += 1
        scorelable.config(f'Score: {score}')
        mainentry.delete(0, END)
        mainentry.focus()
        game()
#entry==================================================================================================
mainentry = Entry(bg=fg, fg=bg, font='belguim 40', width=10, border=6)
mainentry.place(x=220, y=200)
mainlable = Label(text="emptystring", font='belguim 70', width=10, bg=fg, fg=bg)
mainlable.place(x=110, y=50)
timelable = Label(text=f'Time:{time}', bg=bg, fg=fg, width=6, font='belguim 20')
timelable.place(x=10, y=10)
scorelable = Label(text=f'Score:{score}', bg=bg, fg=fg, font='belguim 20', width=6)
scorelable.place(x=670, y=10)
#button==================================================================================================
startbutton = Button(command=start, text='Start', bg=fg, fg=bg, font='belguim 20', width=8, activebackground=bg, activeforeground=fg, relief='ridge', border=7)
startbutton.place(x=315, y=300)
startbutton.bind('<Return>', start())
# mainloop===============================================================================================
win.mainloop()