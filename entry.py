from tkinter import *

root = Tk()
myEntry = Entry(width=25, fg="white", bg="black", justify="center")
myEntry.pack()

def whenClicked():
    Label(text="We are gladly welcoming you, Mr."+myEntry.get()).pack()

myButton = Button(command=whenClicked, text="Greet me!")
myButton.pack()

root.mainloop()
