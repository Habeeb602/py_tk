from cgitb import text
from tkinter import *
from PIL import Image, ImageTk

def getValue(ver, hor):
    Label(root, text=f"Vertical Scale = {ver.get()}").pack()
    Label(root, text=f"Horizontal Scale = {hor.get()}").pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Slider")
    # Geometry  Width_Of_The_Window x Height_Of_The_Window + Position_Of_The_Window_From_Left + Position_Of_The_Window_From_Top
    # geometry specifies size and position of the root window.
    root.geometry("680x420+650+275")

    vScale = Scale(root, from_=0, to=250)
    vScale.pack()

    hScale = Scale(root, from_=0, to=250, orient=HORIZONTAL)
    hScale.pack()

    btn = Button(root, text="Print Value", command=lambda: getValue(vScale, hScale)).pack()

    root.mainloop()