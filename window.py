from email.mime import image
from tkinter import *
from PIL import ImageTk, Image

def openWindow():
    global myImg
    window = Toplevel()
    window.title("New Window")

    myImg = ImageTk.PhotoImage(Image.open("images/icon.png"))
    myLabel = Label(window, image=myImg).pack(padx=20, pady=20)

    Button(window, text="Close This Window!", command=window.destroy).pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Windows Creation")

    btn = Button(root, text="Open a new window", command=openWindow)
    btn.pack(padx=80, pady=30)
    Button(root, text="Close This Window!", command=root.destroy).pack(pady=40)

    root.mainloop()