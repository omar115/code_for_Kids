import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window= tkinter.Tk()
window.geometry("950x800")
window.title("Custom Translator Buildup")
window.configure(bg= 'gray')

# photo = PhotoImage(file= 'C:/Users/Mahmud Reza/Documents/Input.png')
# photoimage = photo.subsample(10, 10)
style = Style()
style.configure('TButton', font=('Papyrus', 15), bd='5', foreground= 'Dark Red', background= 'Crimson')
btn = Button(window, text= '        Personal Translator        ', style= 'TButton', compound= RIGHT, command= None)


# photo = PhotoImage(file= 'C:/Users/Mahmud Reza/Documents/output.png')
# photoimage = photo.subsample(10, 10)
btn0 = Button(window, text= '        Personal Translator        ', style= 'TButton', compound= RIGHT, command= None)
label= Label(window, text= "     Input     ", font= ('Times New Roman', 15),  background= '#00CED1')
label1= Label(window, text= "     Output     ", font= ('Times New Roman', 15),  background= '#00CED1')
text2= Text(window, height= 5, width= 40, bg= "Bisque")

def convert():
    inputText= text1.get("1.0", "end")
    print(inputText)
    text2.insert('end', inputText)
    
text1= Text(window, height= 5, width= 40, bg= "Bisque")
    
btn1 = tkinter.Button(window, text="Bangla", bg='brown', font=('Times New Roman', 12), fg='orange', command= convert) 
btn1.place(x=600,y=300)
btn2= tkinter.Button(window, text="Korean", bg='brown', font=('Times New Roman', 12), fg='orange') 
btn2.place(x=600,y=350)
btn3 = tkinter.Button(window, text="Hindi", bg='brown', font=('Times New Roman', 12), fg='orange') 
btn3.place(x=600, y=400)
btn4 = tkinter.Button(window, text="Japanese", bg='brown', font=('Times New Roman', 12), fg='orange')
btn4.place(x=600, y=450)
btn5 = tkinter.Button(window, text="Chinese", bg='brown', font=('Times New Roman', 12), fg='orange')
btn5.place(x=600, y=500)
btn6 = tkinter.Button(window, text="Urdu", bg='brown', font=('Times New Roman', 12), fg='orange')
btn6.place(x=750, y=300)
btn7 = tkinter.Button(window, text="Spanish", bg='brown', font=('Times New Roman', 12), fg='orange')
btn7.place(x=750, y=350)
btn8 = tkinter.Button(window, text="French", bg='brown', font=('Times New Roman', 12), fg='orange')
btn8.place(x=750, y=400)
btn9 = tkinter.Button(window, text="Arabic", bg='brown', font=('Times New Roman', 12), fg='orange')
btn9.place(x=750, y=450)
btn10 = tkinter.Button(window, text="Italian", bg='brown', font=('Times New Roman', 12), fg='orange')
btn10.place(x=750, y=500)

btn.place(x=80, y=0)
label.place(x=150, y=162)
text1.place(x=0, y=200)
text2.place(x=0 , y= 500)
label1.place(x=150, y=462)
window.mainloop()