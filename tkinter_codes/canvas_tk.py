import tkinter

root = tkinter.Tk()

C = tkinter.Canvas(root, bg = 'blue', height=250, width=300)

cord = 10, 50, 260, 100

arc = C.create_polygon(cord, fill = 'red')

C.pack()

root.mainloop()