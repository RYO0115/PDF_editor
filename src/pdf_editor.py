import os, sys
import glob

import tkinter


root = tkinter.Tk()
root.title("PDF Editor")
root.geometry("800x600")


# 1line text box
editbox = tkinter.Entry(width = 50)
#editbox.pack()
editbox.place(x=50, y=50)

exec_button = tkinter.Button(text = "Merge", width = 20)
#exec_button.Bind("<Button-1>", )
#exec_button.pack()
exec_button.place(x=60, y=100)

reset_button = tkinter.Button(text = "Reset", width = 20)
reset_button.place(x=260, y=100)



root.mainloop()