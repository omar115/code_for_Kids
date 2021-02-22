import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from google_trans_new import google_translator
import webbrowser

window= tkinter.Tk()
window.geometry("3100x3100")
window.title("Custom Translator Buildup")
window.configure(bg= 'Slategray')
translator = google_translator()
style = Style()
style.configure('TButton', font=('Garamond', 25), bd='10', foreground= 'Firebrick', background= 'Dimgray')

def allclear(): 
    text1.delete('1.0', tkinter.END)
    text2.delete('1.0', tkinter.END)
    text3.delete('1.0', tkinter.END)
    
def clear9(): 
    text3.delete('1.0', tkinter.END)

def help():
    messagebox.showinfo("!Help", '''Unfortunately, our translator doesn't support translating from some oher language other than english. So here is what you can do:
            1) Click the button below which will take you to a global online free translator.
            2) Go and choose in which language you want to enter your text (e.g. Detect Language --> Selected Language.
            3) Copy/paste any of the results in the global free translator (Input or Output) and then paste it in our Input (Enter text) box then select the language you want to be have it translated into.
            4) Voila, you can now use our trnaslator to translate from Detect Language --> Selected Language.
                **Notice** We will try to improve our translator and bring the Detect Language (or any language other than english along with enlish too) --> Selected Language.
                            !!!    Thank You    !!!''')

def convert():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='bn')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='bn', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert2():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ko')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ko', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert3():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='hi')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='hi', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert4():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ja')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ja', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert5():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='zh-TW')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='zh-TW', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert6():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ur')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ur', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert7():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='es')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='es', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert8():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='fr')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='fr', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert9():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ar')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ar', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert10():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ru')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ru', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)


def convert11():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ru')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ru', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert12():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='bg')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='bg', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)
    
def convert13():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='cs')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='cs', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert14():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='hr')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='hr', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert15():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='de')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='de', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert16():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='he')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='he', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert17():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='gu')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='gu', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert18():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='kn')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='kn', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert19():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='la')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='la', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert20():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='mk')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='mk', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert21():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='th')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='th', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert22():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='af')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='af', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert23():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='sq')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='sq', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert24():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='am')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='am', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert25():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='bu')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='bu', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert26():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='et')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='et', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert27():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='da')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='da', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert28():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='nl')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='nl', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert29():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ka')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ka', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert30():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ka')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ka', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert31():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='el')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='el', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert32():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='haw')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='haw', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert33():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ga')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ga', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert34():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='id')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='id', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert35():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='jv')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='jv', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert36():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ms')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ms', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert37():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ml')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ml', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)
    

def convert38():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='mn')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='mn', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert39():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ne')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ne', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert40():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='ps')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='ps', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert41():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='sl')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='sl', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert42():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='so')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='so', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert43():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='sw')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='sw', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

def convert44():
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt='my')
    print(out)
    text2.insert('end', out)
    pronounce = translator.translate(input_text, lang_src='en', lang_tgt='my', pronounce=True)
    print(pronounce)
    text3.insert('end', pronounce)

btn0 = Button(window, text= '        Universal Translator        ', style= 'TButton', compound= RIGHT, command= None)
btn0.pack()
label= Label(window, text= "   Enter Text   ", font= ('Times New Roman', 15),  background= 'Khaki')
label1= Label(window, text= "  Translation  ", font= ('Times New Roman', 15),  background= 'Khaki')
text2= Text(window, height= 5, width= 40, bg= "Bisque")
text3= Text(window, height=3, width=40, bg= "Bisque")

def destroy():
    window.destroy()
    
exit1= tkinter.Button(window, text= "  Exit  ",  font= ('Times New Roman', 17), background='Maroon', foreground='White', command= destroy)

def clear():
    text2.delete('1.0', tkinter.END)

def clear2():
    text1.delete('1.0', tkinter.END)

clr9 = tkinter.Button(window, text="Clear", bg='Dimgray', font=('Georgia', 13), fg='Old lace', command= clear9) 
label3= Label(window, text= "   Pronounciation   ", font= ('Times New Roman', 15),  background= 'Khaki')
clr = tkinter.Button(window, text="Clear", bg='Dimgray', font=('Georgia', 13), fg='Old lace', command= clear) 
clr2 = tkinter.Button(window, text="Clear", bg='Dimgray', font=('Georgia', 13), fg='Old lace', command= clear2)
clr3 = tkinter.Button(window, text="Clear All", bg='Dimgray', font=('Georgia', 13), fg='Old lace', command= allclear)
text1= Text(window, height= 5, width= 40, bg= "Bisque")

btn1 = tkinter.Button(window, text="Bangla", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert) 
btn1.place(x=400,y=300)
btn2= tkinter.Button(window, text="Korean", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert2) 
btn2.place(x=400,y=350)
btn3 = tkinter.Button(window, text="Hindi", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert3) 
btn3.place(x=400, y=400)
btn4 = tkinter.Button(window, text="Japanese", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert4)
btn4.place(x=400, y=450)
btn5 = tkinter.Button(window, text="Chinese", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert5)
btn5.place(x=400, y=500)
btn6 = tkinter.Button(window, text="Urdu", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert6)
btn6.place(x=500, y=300)
btn7 = tkinter.Button(window, text="Spanish", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert7)
btn7.place(x=500, y=350)
btn8 = tkinter.Button(window, text="French", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert8)
btn8.place(x=500, y=400)
btn9 = tkinter.Button(window, text="Arabic", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert9)
btn9.place(x=510, y=450)
btn10 = tkinter.Button(window, text="Russian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert10)
btn10.place(x=500, y=500)
btn11 = tkinter.Button(window, text="Bulgarian", bg='Dimgray', font=('Lucida Handwriting', 11), fg='Black', command= convert11)
btn11.place(x=583, y=300)
btn12 = tkinter.Button(window, text="Czech", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert12)
btn12.place(x=600, y=350)
btn13 = tkinter.Button(window, text="Croatian", bg='Dimgray', font=('Lucida Handwriting', 11), fg='Black', command= convert13)
btn13.place(x=595, y=400)
btn14 = tkinter.Button(window, text="German", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert14)
btn14.place(x=600, y=450)
btn15 = tkinter.Button(window, text="Hebrew", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert15)
btn15.place(x=600, y=500)
btn16 = tkinter.Button(window, text="Gujarati", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert16)
btn16.place(x=700, y=300)
btn17 = tkinter.Button(window, text="Kannada", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert17)
btn17.place(x=700, y=350)
btn18 = tkinter.Button(window, text="Latin", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert18)
btn18.place(x=700, y=400)
btn19 = tkinter.Button(window, text="Macedonian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert19)
btn19.place(x=700, y=450)
btn20 = tkinter.Button(window, text="Thai", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert20)
btn20.place(x=700, y=500)

btn21 = tkinter.Button(window, text="Help", bg='Dimgray', font=('Georgia', 13), fg='Old lace', command= help)
btn21.place(x=400, y=150)
btn22 = tkinter.Button(window, text="Click Help, follow the instructions, then CLICK ME", bg='Dimgray', font=('Georgia', 13), fg='Old lace', command= None)
btn22.place(x=400, y=100)

def Translator(event):
    webbrowser.open_new_tab('https://translate.google.com/')

btn22.bind('<Button-1>',Translator)


btn23 = tkinter.Button(window, text="Afrikaans", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert21)
btn23.place(x=820, y=300)
btn24 = tkinter.Button(window, text="Albanian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert22)
btn24.place(x=820, y=350)
btn25 = tkinter.Button(window, text="Amharic", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert23)
btn25.place(x=820, y=400)
btn26 = tkinter.Button(window, text="Belarusian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert24)
btn26.place(x=840, y=450)
btn27 = tkinter.Button(window, text="English", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert25)
btn27.place(x=780, y=500)
btn28 = tkinter.Button(window, text="Estonian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert26)
btn28.place(x=940, y=300)
btn29 = tkinter.Button(window, text="Danish", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert27)
btn29.place(x=940, y=350)
btn30 = tkinter.Button(window, text="Dutch", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert28)
btn30.place(x=940, y=400)
btn31 = tkinter.Button(window, text="Georgian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert29)
btn31.place(x=965, y=450)
btn32 = tkinter.Button(window, text="Greek", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert30)
btn32.place(x=880, y=500)
btn33 = tkinter.Button(window, text="Hawaiian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert31)
btn33.place(x=1050, y=300)
btn34 = tkinter.Button(window, text="Irish", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert33)
btn34.place(x=1050, y=350)
btn35 = tkinter.Button(window, text="Indonesian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert34)
btn35.place(x=1030, y=400)
btn36 = tkinter.Button(window, text="Javanese", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert35)
btn36.place(x=1075, y=450)
btn37 = tkinter.Button(window, text="Malay", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert36)
btn37.place(x=960, y=500)
btn38 = tkinter.Button(window, text="Malayalam", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert37)
btn38.place(x=400, y=550)
btn39 = tkinter.Button(window, text="Mongolian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert38)
btn39.place(x=535, y=550)
btn40 = tkinter.Button(window, text="Nepali", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert39)
btn40.place(x=1120, y=350)
btn43 = tkinter.Button(window, text="Pashto", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert40)
btn43.place(x=1050, y=500)
btn46 = tkinter.Button(window, text="Slovenian", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert41)
btn46.place(x=1300, y=400)
btn47 = tkinter.Button(window, text="Somali", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert42)
btn47.place(x=1300, y=450)
btn48 = tkinter.Button(window, text="Swahili", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert43)
btn48.place(x=1300, y=500)
btn48 = tkinter.Button(window, text="Burmese", bg='Dimgray', font=('Lucida Handwriting', 12), fg='Black', command= convert44)
btn48.place(x=670, y=550)



clr3.place(x=400, y=200)
label.place(x=100, y=162)
text1.place(x=5, y=200)
text2.place(x=5 , y= 500)
label1.place(x=100, y=462)
exit1.place(x= 690, y=600)
clr.place (x=275, y= 462)
clr2.place (x=275, y=162)
text3.place (x= 5, y = 350)
clr9.place(x= 275, y = 310)
label3.place(x= 80, y= 310)
window.mainloop()