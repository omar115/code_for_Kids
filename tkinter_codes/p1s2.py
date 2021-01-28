from tkinter import *
root = Tk()


root.configure(background='aqua')

root.geometry('500x500')

root.title('Personal Translator')

label1 = Label(root, text='text',fg='black',bg='white')

label2 = Label(root,text='Converted Results',fg='black',bg='white')

label1.grid(row=0, column=1)

#get == you can extract the text from anything
#insert == you can insert text or something

def convert():
    inputText = text1.get("1.0", "end")
    #1.0 == take first character, end = last character
    print(inputText)
    
    text2.insert('end', inputText)
    
    
text1 = Text(root, height=5, width = 25, font='arial')
text2 = Text(root, height=5, width=25, font='arial')

btn = Button(root, text='arabic', bg='red', fg='black', command = convert)
btn.grid(row=1, column=2, padx=10, pady=10)

btn2x = Button(root, text='bengali', bg='red', fg='black')
btn2x.grid(row=1, column=3, padx=10, pady=10)

text1.grid(row=1, column=1, padx=10, pady=10)
text2.grid(row=2, column=1, padx=10, pady=10)
