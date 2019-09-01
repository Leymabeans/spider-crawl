#Imports and Functions=====================================
from tkinter import *
from messages import *
import tkinter.messagebox


#Displays advanced options to user========================
def adv_options(): 
    newwin = Toplevel(root)
    display = Label(newwin, text="Change the number of threads below")
    display.pack()  





#Window frames==============================================
root = Tk()
information = Frame(root)
information.pack(side=TOP)
prompt = Frame(root)
prompt.pack(side=BOTTOM)

#Prompt and entry==========================================
title = Label(information, text="Webcrawler Application")
instructions = Label(information, text="Please insert project name and website URL below")
project_name = Entry(prompt)
url = Entry(prompt)
submit =Button(prompt, text="Crawl", command=crawl)
options =Button(prompt, text="Advanced Options", command=adv_options)
root.mainloop()




