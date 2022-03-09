from tkinter import *
from PIL import ImageTk, Image

def printVal(r):
    print(r.get())

if __name__ == "__main__":
    root = Tk()
    root.title("Radio Buttons")

    # Tkinter variables are initialized through class constructors
    # And accessed through .get() method
    # Radiobutton only uses Tkinter variables 
    # IntVar() for Integer, StrVar for String ...
    r = IntVar()
    # Option 1 is the Default radio button selected...
    r.set(1)
    Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: printVal(r)).pack()
    Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: printVal(r)).pack()
    # print(r.get())

    root.mainloop()