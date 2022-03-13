from tkinter import *
from PIL import ImageTk, Image

def showValue():
    Label(root, text=chkVar1.get()).pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Checkbox")
    root.geometry("680x420+650+275")

    chkVar1 = StringVar()

    chk1 = Checkbutton(root, text="Do you wanna build a Snowman?", variable=chkVar1, onvalue="Snowman", offvalue="No-man")
    chk1.deselect()
    chk1.pack()

    btn = Button(root, text="Get!", command=showValue).pack()

    root.mainloop()