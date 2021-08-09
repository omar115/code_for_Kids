from tkinter import *

root = Tk()
root.title("My Paint App")
root.geometry("800x800")

def paint(e):
    
    # starting position
    x1 = e.x - 1
    y1 = e.y - 1

    # ending position
    x2 = e.x + 1
    y2 = e.y + 1

    # draw the canvas
    my_canvas.create_line(x1,y1,x2,y2, fill='red', smooth=True)

my_canvas = Canvas(root, width=600, height=400, bg='white')
my_canvas.pack(pady=20)




my_canvas.bind('<B1-Motion>', paint)



root.mainloop() 