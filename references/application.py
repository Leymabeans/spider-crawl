#Imports and Functions
from tkinter import *
import tkinter.messagebox

#Holding function
def doNothing():
    print("Do nothing")

#Success Message
def success():
    tkinter.messagebox.showinfo('Success', 'Image Inserted')

#Preventative Message
def alert():
    answer = tkinter.messagebox.askquestion('Exit Application', 'Are you sure you want to exit this program?')

    if answer == 'yes':
        sys.exit()


#=================================================
root = Tk()

#Menu and Submenu
menu = Menu(root)
fileSub = Menu(menu)
editSub = Menu(menu)

#Configuration
fileSub = Menu(menu, tearoff=0)
editSub = Menu(menu, tearoff=0)
root.config(menu=menu)

#Adding items to menu
menu.add_cascade(label="File", menu=fileSub)
menu.add_cascade(label="Edit", menu=editSub)

#Adding items to File Tab
fileSub.add_command(label="New Project", command=doNothing)
fileSub.add_command(label="New File", command=doNothing)
fileSub.add_command(label="Save As", command=doNothing)
fileSub.add_command(label="Exit", command=alert)

#Adding items to Edit Tab
editSub.add_command(label="Undo", command=doNothing)
editSub.add_command(label="Redo", command=doNothing)
editSub.add_separator()
editSub.add_command(label="Copy", command=doNothing)
editSub.add_command(label="Cut", command=doNothing)
editSub.add_command(label="Paste", command=doNothing)




#Toolbar===============================================================
toolbar = Frame(root, bg="lightblue")
insert1 = Button(toolbar, text="insert Image", command=success)
print1 = Button(toolbar, text="Print", command=doNothing)

insert1.pack(side=LEFT, padx=2, pady=2)
print1.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)



#Status Bar===========================================================
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill= X)
root.mainloop()




