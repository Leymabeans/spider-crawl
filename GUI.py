#Imports for program
from tkinter import *


def doNothing():
    print("Do nothing")


#Menu and Submenu======================================================
root = Tk()
menu = Menu(root)
subMenu = Menu(menu, tearoff=0)
subMenu2 = Menu(menu, tearoff=0)
root.config(menu=menu)

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="Delete Project...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

menu.add_cascade(label="Edit", command=doNothing)
subMenu2.add_command(label="Undo Typing", command=doNothing)



#Toolbar===============================================================
toolbar = Frame(root, bg="lightblue")
insert1 = Button(toolbar, text="insert Image", command=doNothing)
print1 = Button(toolbar, text="Print", command=doNothing)

insert1.pack(side=LEFT, padx=2, pady=2)
print1.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)



#Status Bar===========================================================
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill= X)
root.mainloop()