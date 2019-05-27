from tkinter import *


root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Choose website", fg="red")
button2 = Button(topFrame, text="Pick how many pages", fg="red")
button3 = Button(topFrame, text="Choose threads", fg="red")
button4 = Button(bottomFrame, text="Start web crawler", fg="red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()