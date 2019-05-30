#Imports for program
from tkinter import *


def doNothing():
    print("Do nothing")


root = Tk()

menu = Menu(root)
subMenu = Menu(menu)
subMenu2 = Menu(menu)

root.config(menu=menu)

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="Delete Project...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

menu.add_cascade(label="Edit", command=doNothing)
subMenu2.add_command(label="Undo Typing", command=doNothing)
root.mainloop()
