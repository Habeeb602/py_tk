from tkinter import *
from PIL import Image, ImageTk

def showVal():
    Label(root, text=menuVar.get()).pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Dropdown Menu")
    root.geometry("680x420+650+275")

    options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    menuVar = StringVar()
    menuVar.set(options[0])

    lbl = Label(root, text="Which Day you LOVE the MOST?").pack()

    dropDown = OptionMenu(root, menuVar, *options).pack()


    btn = Button(root, text="Get Selected Option", command=showVal).pack()

    

    root.mainloop()
