#commands
#pip install googletrans==3.1.0a0

from tkinter import *
from googletrans import Translator


root = Tk()

trans = Translator()


root.configure(background='aqua')

root.geometry('500x500')

root.title('Personal Translator')

label1 = Label(root, text='Write your text here',fg='black',bg='white')

label2 = Label(root,text='Converted Results',fg='black',bg='white')

label1.grid(row=0, column=1)

text1 = Text(root, height=5, width = 25, font='arial')
text2 = Text(root, height=5, width=25, font='arial')

def convert():
    input_text = text1.get("1.0", "end")
    # print(input_text)
    out = trans.translate(input_text, dest='fr')
    print(out.text)
    text2.insert('end', out.text)


btn = Button(root, text='convert', bg='red', fg='black', command=convert)
btn.grid(row=2, column=1, padx=10, pady=10)

text1.grid(row=1, column=1, padx=10, pady=10)
text2.grid(row=3, column=1, padx=10, pady=10)

def clear():
    text1.delete(1.0, END)
    text2.delete(1.0,END)

btn2 = Button(root, text='clear', bg='green',fg='black',command=clear)
btn2.grid(row=4,column=1, padx=10, pady=10)

root.mainloop()