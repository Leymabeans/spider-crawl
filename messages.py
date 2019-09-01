#Default messages for the user=============================
def success():
    tkinter.messagebox.showinfo('Success', 'Website Successfully Crawled')

def alert():
    answer = tkinter.messagebox.askquestion('Exit Application', 'Are you sure you want to exit this program?')
    if answer == 'yes':
        sys.exit()