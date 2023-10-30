# Import tools

import sqlite3
from tkinter import *
from tkinter import messagebox

# Variables

bg = '#201A31'
fg = '#0DF5E3'

# Create a connection to the database

conn = sqlite3.connect('E:/Python/Database/contact_list.db')
c = conn.cursor()

# Create a table if it doesn't exist

c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (name TEXT, family TEXT, number TEXT, address TEXT)''')

# Create the GUI

root = Tk()
root.title("Contact List")
root.geometry('1000x530+50+50')
root.configure(bg=bg)
root.resizable(0, 0)
# Create the labels and entries for the contact information

name_lable = Label(text='نام :', font='roya 20', bg=bg, fg=fg)
name_lable.place(x=100, y=25)

name_entry = Entry(fg=bg, bg=fg, font='roya 20', width=19)
name_entry.place(x=150, y=25)

family_lable = Label(text='نام خانوادگی:', font='roya 20', bg=bg, fg=fg)
family_lable.place(x=450, y=25)

family_entry = Entry(fg=bg, bg=fg, font='rora 20', width=23)
family_entry.place(x=580, y=25)

address_lable = Label(text='آدرس:', font='roya 20', bg=bg, fg=fg)
address_lable.place(x=500, y=100)

address_entry = Entry(fg=bg, bg=fg, font='roya 20', width=23)
address_entry.place(x=580, y=100)

number_lable = Label(text='شماره تماس:', fg=fg, bg=bg, font='roya 20')
number_lable.place(x=25, y=100)

number_entry = Entry(fg=bg, bg=fg, font='roya 20', width=19)
number_entry.place(x=150, y=100)

# Create the listbox and scrollbar

scrollbar = Scrollbar()
scrollbar.place(x=960, y=170, height=340)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.configure(bg='#00FFFF', fg='#DC143C', width=39, height=9, font='belguim 24')
listbox.place(x=250, y=170)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# Create the insert button

def insert_contact():
    name = name_entry.get()
    family = family_entry.get()
    number = number_entry.get()
    address = address_entry.get()

    if name == "" or family == "" or number == "" or address == "":
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    c.execute("INSERT INTO contacts VALUES (?, ?, ?, ?)", (name, family, number, address))
    conn.commit()

    listbox.insert(END, f"{name} {family} {number} {address}")
    name_entry.delete(0, END)
    family_entry.delete(0, END)
    number_entry.delete(0, END)
    address_entry.delete(0, END)

insert_button = Button(command = insert_contact, text='اضافه کردن', fg=bg, bg=fg, font='roya 16', activebackground=bg, activeforeground=fg, width=15)
insert_button.place(x=70, y=170)

# Create the clear button
def clear_entries():
    name_entry.delete(0, END)
    family_entry.delete(0, END)
    number_entry.delete(0, END)
    address_entry.delete(0, END)

clear_button = Button(root, text="پاک کردن", command=clear_entries, fg=bg, bg=fg, font='roya 16', activebackground=bg, activeforeground=fg, width=15)
clear_button.place(x=70, y=240)

# Create the fetch button

def fetch_contact():
    selected = listbox.curselection()
    if not selected:
        return messagebox.showinfo

    name, family = listbox.get(selected[0]).split()

    c.execute("SELECT * FROM contacts WHERE name=? AND family=?", (name, family))
    contact = c.fetchone()
    name_entry.delete(0, END)
    name_entry.insert(0, contact[0])
    family_entry.delete(0, END)
    family_entry.insert(0, contact[1])
    number_entry.delete(0, END)
    number_entry.insert(0, contact[2])
    address_entry.delete(0, END)
    address_entry.insert(0, contact[3])

fetch_button = Button(root, text="گرفتن", command=fetch_contact, fg=bg, bg=fg, font='roya 16', activebackground=bg, activeforeground=fg, width=15)
fetch_button.place(x=70, y=310)

# Create the delete button

def delete_contact():
    askdelete=messagebox.askyesno('Delete', 'Do you want delete this line?')
    if askdelete == True:
        curselection = listbox.curselection()
        listbox.delete(curselection)
        conn.remove(curselection)

delete_buttum = Button(command=delete_contact, text='حذف', fg=bg, bg=fg, font='roya 16', activebackground=bg, activeforeground=fg, width=15)
delete_buttum.place(x=70, y=380)

# Create the delete button

def delete_all():
    if messagebox.askyesno('Delete all', 'Do you want delet all data?') == True:
        listbox.delete(0, END)
        c.execute("Delet from contact where *")
        conn.commit()
deleteall_buttum = Button(command=delete_all, text=' حذف همه', fg=bg, bg=fg, font='roya 16', activebackground=bg, activeforeground=fg, width=15)
deleteall_buttum.place(x=70, y=450)

# Populate the listbox with existing contacts

c.execute("SELECT name, family, number, address FROM contacts")
contacts = c.fetchall()
for contact in contacts:
    listbox.insert(END, f"{contact[0]} {contact[1]}")

# Run the GUI

root.mainloop()

# Close the connection to the database when the GUI is closed

conn.close()