from tkinter import *
import googletrans
from googletrans import Translator

#print(googletrans.LANGUAGES)

root = Tk()

trans = Translator()


root.configure(background='aqua')

root.geometry('500x500')

root.title('Personal Translator')

label1 = Label(root, text='text',fg='black',bg='white')

label2 = Label(root,text='Converted Results',fg='black',bg='white')

label1.grid(row=0, column=1)

def convert():
    input_text = text1.get("1.0", "end")
    # print(input_text)
    #textx = btn.cget('text')
    output = trans.translate(input_text, dest='korean')
    
    print(output)
    print(output.text)
    
    text2.insert('end', output.text)
    
    
    
text1 = Text(root, height=5, width = 25, font='arial')
text2 = Text(root, height=5, width=25, font='arial')


btn = Button(root, text='arabic', bg='red', fg='black', command = None)
btn.grid(row=1, column=2, padx=10, pady=10)

btn2x = Button(root, text='বাংলা', bg='red', fg='black', command = convert)
btn2x.grid(row=1, column=3, padx=10, pady=10)

btn3 = Button(root, text='gujarati', bg='red', fg='black')
btn3.grid(row=1, column=4, padx=10, pady=10)

text1.grid(row=1, column=1, padx=10, pady=10)
text2.grid(row=2, column=1, padx=10, pady=10)

def clear():
    text1.delete(1.0, END)
    text2.delete(1.0,END)

btn2 = Button(root, text='clear', bg='green',fg='black', command = clear)
btn2.grid(row=4,column=1, padx=10, pady=10)

btnExit = Button(root, text='close', bg='red',fg='white', command=root.destroy)
btnExit.grid(row=5, column=1, padx=10, pady=10)
root.mainloop()
