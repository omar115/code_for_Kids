from tkinter import *

root = Tk()

root.title("MP3 Player")
root.geometry("800x800")

playlist_box = Listbox(root, bg='black', fg="green", width=60)
playlist_box.pack(pady=20)

root.mainloop()