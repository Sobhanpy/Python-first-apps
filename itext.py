import pywhatkit
import tkinter
import os
print("Please select your image: ")
image = tkinter.filedialog.askopenfilename()
name = input("Enter the name of the text file to save the text: ")
p = pywhatkit.image_to_ascii_art(image,name)
dir = os.chdir()
print("""
Text file saved successfully
address : {0}\{1}.txt""").format(dir,name)
print(p)
input()