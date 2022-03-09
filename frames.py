from cgitb import text
from tkinter import *
from PIL import ImageTk, Image

def labelGenerator():
    return Label(frame, text="How Dare You!").pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Frames in Tkinter")

    # The Padding (padx, pady) while creating, gives padding inside the element. It makes the element BIGGER.
    frame = LabelFrame(root, text="This is my frame...", padx=20, pady=20)
    btn = Button(frame, text="Don't Click Me!", command=labelGenerator)

    # The Padding (padx, pady) while packing, give padding outside the element. It makes the element MORE SPACIOUS.
    frame.pack(padx=30, pady=30)
    btn.pack(padx=60, pady=60)

    root.mainloop()
