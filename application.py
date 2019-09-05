#Imports===================================
from tkinter import *
import tkinter.messagebox


#Displays advanced options to user=========
def adv_options(event): 
    newwin = Toplevel(root)
    display = Label(newwin, text="Change the number of threads below")
    display.pack()  


#Initializes the crawler===================
def crawl(event):
    print("Crawling")


#Default messages for the user==========
def success():
    tkinter.messagebox.showinfo('Success', 'Website Successfully Crawled')

def alert():
    answer = tkinter.messagebox.askquestion('Exit Application', 'Are you sure you want to exit Spider Crawl?')
    if answer == 'yes':
        sys.exit()


#Presets and variables=====================
dark = '#0f0f0f'
light = '#ffffff'
title_font = ('arial', 32, 'bold')
instructions_font = ('arial', 9)

#Window configuration======================
root = Tk()
root.wm_iconbitmap('./crawler.ico')
root.wm_title('Spider Crawl')
root.geometry('350x250')
root.resizable(0, 0)
root.config(bg=dark)
info = Frame(root, bg=dark, width=350, height=50)
prompt = Frame(root, bg=light, width=350, height=200)

#Prompt and Entry==========================
title = Label(info, text="Spider Crawl", font=title_font, bg=dark, fg=light)
instructions = Label(info, text="Please insert project name and website URL below", font=instructions_font, bg=dark, fg=light)
project_name = Entry(prompt)
url = Entry(prompt)
submit =Button(prompt, text="Crawl", bg=dark, fg=light)
options =Button(prompt, text="Advanced Options", bg=dark, fg=light)


#Display all elements======================
info.pack(side=TOP)
prompt.pack(side=BOTTOM, fill=X)
title.grid(row=0)
instructions.grid(row=1)
project_name.grid(row=2)
url.grid(row=3)
submit.grid(row=4)
submit.bind("<Button-1>", crawl)
options.grid(row=5)
options.bind("<Button-1>", adv_options)
root.mainloop()