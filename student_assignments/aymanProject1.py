import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import webbrowser
import googletrans
from googletrans import Translator
from google_trans_new import google_translator

translator = google_translator()

translator_window= tkinter.Tk()
translator_window.title("Transly\U0001f600")
translator_window.geometry('800x500')
translator_window.configure(bg='#f2ffe6')


window_label=tkinter.Label(translator_window,text="Transly",font=('Helvetica', 15))
window_label.place(x=200, y=10)

Input = tkinter.Label(translator_window, text="Your Language", font=('Impact', 15), background='#b3ff66', foreground='#408000', height=1, width=15)
Input.place(x=150, y=75)

Output = tkinter.Label(translator_window, text="Translated Language", font=('Impact', 15), background='#b3ff66', foreground='#408000', height=1, width=17)
Output.place(x=150, y=300)


Input_text = Text(translator_window, height=5, width=30,background='#d9ffb3', foreground="#1a3300")
Input_text.place(x=100,y=125)

Output_text = Text(translator_window, height=5, width=30,background='#d9ffb3', foreground="#1a3300")
Output_text.place(x=100, y=350)

def test(target_language):
    var=target_language
    input_text = Input_text.get("1.0", "end")
    print(input_text)

    out = translator.translate(input_text, lang_tgt=var)
    print('translated text is ', out)
    Output_text.insert('end', out)

#Buttons


photo1 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/bangladesh.png')
photoimage1 = photo1.subsample(10, 10)

style = Style() 

#style.configure('W.TButton', font=('Helvetica', 10, 'bold' ), foreground='black', bg='green')
style.configure('W.TButton', font=('Montserrat', 10, 'bold'),foreground='black',background='green')


btn = Button(translator_window, image=photoimage1, text='Bengali', style='W.TButton', compound=RIGHT, command=lambda: test('bn'))
btn.place(x=400,y=50)

photo2 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/france.png')
photoimage2 = photo2.subsample(10, 10)

btn1 = Button(translator_window, image=photoimage2,text='French', style='W.TButton', compound=RIGHT, command=lambda: test('fr'))
btn1.place(x=600,y=50)

photo3 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/japan.png')
photoimage3 = photo3.subsample(10, 10)

btn2 = Button(translator_window, image=photoimage3, text="Japanese", style='W.TButton', compound=RIGHT, command=lambda: test('ja'))
btn2.place(x=400,y=100)

photo4 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/saudi-arabia.png')
photoimage4 = photo4.subsample(10, 10)

btn3 = Button(translator_window, image=photoimage4, text="Arabic",style='W.TButton', compound=RIGHT, command=lambda: test('ar'))
btn3.place(x=600,y=100)

photo5 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/south-korea.png')
photoimage5 = photo5.subsample(10, 10)

btn4 = Button(translator_window, image=photoimage5, text="Korean",style='W.TButton', compound=RIGHT, command=lambda: test('ko'))
btn4.place(x=400,y=150)

photo6 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/spain.png')
photoimage6 = photo6.subsample(10, 10)

btn5 = Button(translator_window, image=photoimage6, text='Spanish',style='W.TButton', compound=RIGHT, command=lambda: test('es'))
btn5.place(x=600,y=150)

photo7 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/china.png')
photoimage7 = photo7.subsample(10, 10)

btn6 = Button(translator_window, image=photoimage7, text="Mandarin",style='W.TButton', compound=RIGHT, command=lambda: test('zh'))
btn6.place(x=400,y=200)

photo8 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/italy.png')
photoimage8 = photo8.subsample(10, 10)

btn7 = Button(translator_window, image=photoimage8, text="Italian",style='W.TButton', compound=RIGHT, command=lambda: test('it'))
btn7.place(x=600,y=200)

photo9 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/mali.png')
photoimage9 = photo9.subsample(10, 10)

btn8 = Button(translator_window, image=photoimage9, text="Afrikaan",style='W.TButton', compound=RIGHT, command=lambda: test('af'))
btn8.place(x=400,y=250)

photo10 = PhotoImage(file=r'/home/akash/git_workspace/code_for_Kids/student_assignments/india.png')
photoimage10 = photo10.subsample(10, 10)

btn9 = Button(translator_window, image=photoimage10, text="Hindi",style='W.TButton', compound=RIGHT, command=lambda: test('hi'))
btn9.place(x=600,y=250)  

style1 = Style()
style1.configure('W.TButton', font=('Montserrat', 10, 'bold'), background='black',foreground='white')

def clear():
    Input_text.delete("1.0", "end")

Delete_btn = Button(translator_window, text='Clear input text',style='W.TButton', command=clear)
Delete_btn.place(x=100, y=210)

def clear2():
    Output_text.delete("1.0", "end")

Delete_btn2 = Button(translator_window, text='Clear output text', style='W.TButton',command=clear2)
Delete_btn2.place(x=100, y=435)

btnExit = Button(translator_window, text='EXIT', style='W.TButton', command=translator_window.destroy)
btnExit.grid(row=5, column=1, padx=10, pady=10)


translator_window.mainloop()