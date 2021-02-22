# import tkinter as tk
from tkinter import *
from google_trans_new import google_translator


root = Tk()
translator = google_translator()
root.geometry("1500x1000")
root.title("Your Favourite Translator")
root.configure(bg = 'Linen')
text = translator.translate('Hello', lang_tgt='bn')
print(text)

def convert():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='bn')
    print(out)
    text2.insert('end', out)

def convert2():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ja')
    print(out)
    text2.insert('end', out)

def convert3():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='hi')
    print(out)
    text2.insert('end', out)

def convert4():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='fr')
    print(out)
    text2.insert('end', out)

def convert5():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='it')
    print(out)
    text2.insert('end', out)

def convert6():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='af')
    print(out)
    text2.insert('end', out)

def convert7():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='nl')
    print(out)
    text2.insert('end', out)

def convert8():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='el')
    print(out)
    text2.insert('end', out)

def convert9():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='he')
    print(out)
    text2.insert('end', out)

def convert10():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='th')
    print(out)
    text2.insert('end', out)

def deleting():
    text1.delete('1.0', 'end')
    
def deleting2():
    text2.delete('1.0', 'end')

Bng = Button(root, text = "Bangla", padx= 50, pady = 12, bg = "PaleGreen", command = convert)
Jpn = Button(root, text= "Japaneese", padx = 50, pady = 12, bg = "PaleGreen", command = convert2)
Hnd = Button(root, text = "Hindi", padx = 50, pady = 12, bg = "PaleGreen", command = convert3)
Frn = Button(root, text = "Fench", padx = 50, pady = 12, bg = "PaleGreen", command = convert4)
Itl = Button(root, text = "Italian", padx = 50, pady = 12, bg = "PaleGreen", command = convert5)
Afr = Button(root, text = "Afrikaans", padx = 50, pady = 12, bg = "PaleGreen", command = convert6)
Dtch = Button(root, text = "Dutch", padx = 50, pady = 12, bg = "PaleGreen", command = convert7) 
Grk = Button(root, text = "Greek", padx = 50, pady = 12, bg = "PaleGreen", command = convert8)
Hrw = Button(root, text = "Hebrew", padx = 50, pady = 12, bg = "PaleGreen", command = convert9)
Tha = Button(root, text = "Thai", padx = 50, pady = 12, bg = "PaleGreen", command = convert10)

label  = Label(root, text = "Input", padx = 50, pady = 2, bg = 'LightCyan', font = ("Arial", 17))
text1 = Text(root, height = 2, width = 50, bg = 'Plum')
label2 = Label(root, text = "Output", padx = 50, pady = 2,bg = 'LightCyan', font = ("Arial", 17))
text2 = Text(root, height = 2, width = 50, bg = "Plum")

close_button = Button(root, text='Close', padx=50, pady=12, bg='Sienna', command = root.destroy)

del1 = Button(root, text = 'Clear Input', padx=50, pady=12, bg = 'Sienna', command =deleting)
del2 = Button(root, text = 'Clear Output', padx=50, pady=12, bg = 'Sienna', command =deleting2)

Trns = Button(root, text ='Translator', padx = 110, pady =50, bg = 'LightGoldenRodYellow', font = ('Impact', 20))


Bng.place(x = 1050, y = 230)
Jpn.place(x = 1040, y = 330)
Hnd.place(x = 1060, y = 430)
Frn.place(x = 1060, y = 530)
Itl.place(x = 1060, y = 630)
Afr.place(x = 860, y = 230)
Dtch.place(x = 860, y = 330)
Grk.place(x = 860, y = 430)
Hrw.place(x = 860, y = 530)
Tha.place(x = 860, y = 630)
label.place(x = 370, y = 210)
text1.place(x = 240, y = 250)
label2.place(x = 370,y =400)
text2.place(x = 240, y = 440)
Trns.place(x = 610, y = 0)
close_button.place(x=1360, y=0)
del1.place(x=360, y=294)
del2.place(x=360,y=484)

root.mainloop()