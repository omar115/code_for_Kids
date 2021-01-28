import tkinter
from tkinter import *
from tkinter.ttk import *

translator_window= tkinter.Tk()
translator_window.title("Language Translator \U0001f600")
translator_window.geometry('600x400')
translator_window.configure(bg='gray')

window_label=tkinter.Label(translator_window,text="Personal translator",font=('Arial', 10))
window_label.place(x=200, y=10)

Input=tkinter.Label(translator_window,text="Input",font=('Arial', 15),background='dark green', foreground='light green',height=1,width=9)
Input.place(x=180, y=75)

Output=tkinter.Label(translator_window,text="Output",font=('Arial', 15),background='dark green', foreground='light green',height=1, width=9)
Output.place(x=180, y=230)

text1=Text(translator_window, height=5, width=30,bg='#f2ffe6')
text1.place(x=100,y=125)

text2=Text(translator_window, height=5, width=30, bg='#7fffd4' )
text2.place(x=100, y=280)

style = Style() #style function

style.configure('TButton', font=('Robot', 15, 'bold', 'italic'), foreground='black', bg='green')

btn = Button(translator_window, text='Bengali', command = None)  
btn.place(x=400,y=100)

btn = Button(translator_window, text='French', command = None)  
btn.place(x=400,y=150)

btn2=Button(translator_window, text="Japanese", command=None)
btn2.place(x=400,y=200)

btn3=Button(translator_window, text="Arabic", command=None)
btn3.place(x=400,y=250)

btn3=Button(translator_window, text="Korean", command=None)
btn3.place(x=400,y=300)

translator_window.mainloop()