#Imports for program
import sys
from tkinter import *


#Holds functionality for program
class NathansButton:
    def __init__(self, master):
        frame = Frame(master, width=500, height=500)
        frame.pack()

        #Button that prints message when printed
        self.printButton = Button(frame, text="Print Message", bg="green")
        self.printButton.pack(side=LEFT)
        self.printButton.bind("<Button-1>", self.printMessage)

        #Button for exiting the program
        self.quitButton = Button(frame, text="Exit", bg="red")
        self.quitButton.pack(side=LEFT)
        self.quitButton.bind("<Button-1>", self.exit)

    #Prints the message when printButton is clicked
    def printMessage(self, event):
        print("This actually worked")

    #Exits program when quitButton is clicked
    def exit(self, event):
        sys.exit()


root = Tk()
n = NathansButton(root)
root.mainloop()