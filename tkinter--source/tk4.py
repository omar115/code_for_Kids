import tkinter
def fun():
    print("100 Taka")

window = tkinter.Tk()
window.title("Welcome to Tkinter World :-)")
window.geometry('500x500')

for i in range(5):
    button = tkinter.Button(window, text="button",
                        command=fun)
    button.pack()

window.mainloop()