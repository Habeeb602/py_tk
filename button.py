from tkinter import *

root = Tk()

def whenYouClick():
    myLabel1 = Label(root, text="Hey!,You clicked the button!")
    myLabel1.pack()

myButton = Button(root, text="Click ME!", padx=35, pady=20, bg="black", fg="white", command=whenYouClick)

myButton.pack()

root.mainloop()