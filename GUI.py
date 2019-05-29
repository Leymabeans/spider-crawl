import sys
from tkinter import *


class NathansButton:
    def __init__(self, master):
        frame = Frame(master, width=500, height=500)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", bg="green")
        self.printButton.pack(side=LEFT)
        self.printButton.bind("<Button-1>", self.printMessage)

        self.quitButton = Button(frame, text="Exit", bg="red")
        self.quitButton.pack(side=LEFT)
        self.quitButton.bind("<Button-1>", self.exit)

    def printMessage(self, event):
        print("This actually worked")

    def exit(self, event):
        sys.exit()
root = Tk()
n = NathansButton(root)
root.mainloop()