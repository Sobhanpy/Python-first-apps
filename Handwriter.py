import pywhatkit
print('''
Hello I'm NEVIS 
I can print handwritten your text
     ''')
text = input("Enter a text: ")
Handwritten =  pywhatkit.text_to_handwriting(text)
print(Handwritten)