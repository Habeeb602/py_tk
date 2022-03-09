from email.mime import image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

def openFile():
    global myImg
    filedialog.
    filename =filedialog.askopenfilename(initialdir="/home/habeeb/py_tk", title="Open a Image", filetypes=( ("PNG Files", "*.png"), ("JPG Files","*.jpg"), ("All Files", "*.*") ))
    # Label(root, text=filename).pack(padx=20, pady=30)
    myImg = ImageTk.PhotoImage(Image.open(filename))
    myLabel = Label(root, image=myImg).pack(padx=40, pady=40)


if __name__ == "__main__":
    root = Tk()
    
    btn = Button(root, text="Open a File", command=openFile).pack(padx=30, pady=40)

    root.mainloop()