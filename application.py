#Imports and Functions=====================================
from tkinter import *
import tkinter.messagebox





#Window frames==============================================
root = Tk()
root.geometry("600x400")
information = Frame(root)
information.pack(side=TOP)
prompt = Frame(root)
prompt.pack(side=BOTTOM)
action = Frame(root)
action.pack(side=LEFT)

#Prompt and entry==========================================
title = Label(information, text="Webcrawler Application")
instructions = Label(information, text="Please insert project name and website URL below")
project_name = Entry(prompt)
url = Entry(prompt)
submit =Button(action, text="Crawl", command=crawl)
options =Button(action, text="Advanced Options", command=adv_options)

insert1.pack(side=LEFT, padx=2, pady=2)
print1.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
root.mainloop()





#Default messages for the user=============================
def success():
    tkinter.messagebox.showinfo('Success', 'Website Successfully Crawled')

def alert():
    answer = tkinter.messagebox.askquestion('Exit Application', 'Are you sure you want to exit this program?')
    if answer == 'yes':
        sys.exit()




#Holding function
def doNothing():
    print("Do nothing")

def adv_options(): # new window definition
    newwin = Toplevel(root)
    display = Label(newwin, text="Humm, see a new window !")
    display.pack()  



