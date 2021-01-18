from tkinter import *

root = Tk()
root.geometry("1000x800")
root.title("Translator")
root.configure(bg = 'Linen')

Bng = Button(root, text = "Bangla", padx= 50, pady = 12, bg = "PaleGreen")
Jpn = Button(root, text= "Japaneese", padx = 50, pady = 12, bg = "PaleGreen")
Hnd = Button(root, text = "Hindi", padx = 50, pady = 12, bg = "PaleGreen")
Frn = Button(root, text = "Fench", padx = 50, pady = 12, bg = "PaleGreen")
Itl = Button(root, text = "Italian", padx = 50, pady = 12, bg = "PaleGreen")
label  = Label(root, text = "Input", padx = 50, pady = 2, bg = 'LightCyan', font = ("Arial", 17))
text1 = Text(root, height = 2, width = 50, bg = 'Plum')
label2 = Label(root, text = "Output", padx = 50, pady = 2,bg = 'LightCyan', font = ("Arial", 17))
text2 = Text(root, height = 2, width = 50, bg = "Plum")
Trns = Button(root, text ='Translator', padx = 110, pady =50, bg = 'LightGoldenRodYellow', font = ('Impact', 20))


Bng.place(x = 750, y = 230)
Jpn.place(x = 740, y = 330)
Hnd.place(x = 760, y = 430)
Frn.place(x = 760, y = 530)
Itl.place(x = 760, y = 630)
label.place(x = 210, y = 210)
text1.place(x = 40, y = 250)
label2.place(x = 210,y =400)
text2.place(x = 40, y = 440)
Trns.place(x = 300, y = 0)

root.mainloop()