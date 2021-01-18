#commands
#pip install googletrans==3.1.0a0

from tkinter import *
import googletrans
from googletrans import Translator


root = Tk()

trans = Translator()


root.configure(background='aqua')

root.geometry('500x500')

root.title('Personal Translator')

label1 = Label(root, text='text',fg='black',bg='white')

label2 = Label(root,text='Converted Results',fg='black',bg='white')

label1.grid(row=0, column=1)

text1 = Text(root, height=5, width = 25, font='arial')
text2 = Text(root, height=5, width=25, font='arial')

# print(googletrans.LANGUAGES)

def convert():
    input_text = text1.get("1.0", "end")
    # print(input_text)
    textx = btn.cget('text')
    print('the text is ',textx)
    out = trans.translate(input_text, dest=textx)
    print(out.text)
    text2.insert('end', out.text)

def convert2():
    input_text = text1.get("1.0", "end")
    # print(input_text)
    textx = btn2x.cget('text')
    print('the text is ',textx)
    out = trans.translate(input_text, dest=textx)
    print(out.text)
    text2.insert('end', out.text)

def convert3():
    input_text = text1.get("1.0", "end")
    # print(input_text)
    textx = btn3.cget('text')
    print('the text is ',textx)
    out = trans.translate(input_text, dest=textx)
    print(out.text)
    text2.insert('end', out.text)

btn = Button(root, text='arabic', bg='red', fg='black', command=convert)
btn.grid(row=1, column=2, padx=10, pady=10)

btn2x = Button(root, text='bengali', bg='red', fg='black', command=convert2)
btn2x.grid(row=1, column=3, padx=10, pady=10)

btn3 = Button(root, text='gujarati', bg='red', fg='black', command=convert3)
btn3.grid(row=1, column=4, padx=10, pady=10)

text1.grid(row=1, column=1, padx=10, pady=10)
text2.grid(row=2, column=1, padx=10, pady=10)

def clear():
    text1.delete(1.0, END)
    text2.delete(1.0,END)

btn2 = Button(root, text='clear', bg='green',fg='black',command=clear)
btn2.grid(row=4,column=1, padx=10, pady=10)

root.mainloop()