from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Images")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='images/icon.png'))

myImg = ImageTk.PhotoImage(Image.open("images/icon.png"))
myLabel = Label(image=myImg)
myLabel.pack()




exitButton = Button(root, text="Exit button", command=root.quit)
exitButton.pack()
root.mainloop()
