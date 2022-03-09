from tkinter import *
from PIL import Image, ImageTk
from os import listdir, stat
from os.path import isfile, join

def onClickNext():
    i = obj.getVal()
    if(i < len(myImageLabels) - 1):
        myImageLabels[i].grid_remove()
        obj.increment()
        # print("next" + str(i))    
        i = obj.getVal()
        myImageLabels[i].grid(row=0, column=0,columnspan=3)
        status = Label(root, text = "Image " + str(obj.getVal() + 1) + " of " + str(obj.n),  bd=1)
        status.grid_remove()
        status.grid(row=2, column=0, columnspan=3)
        if(prevBtn["state"] == "disabled"):
            prevBtn["state"] = "normal"
        
    if(obj.getVal() >= len(myImageLabels) - 1):
        nextBtn["state"] = "disabled"

def onClickPrev():
    i = obj.getVal()
    if(i > 0):
        myImageLabels[i].grid_remove()
        obj.decrement()
        i = obj.getVal()
        # print("prev" + str(i))
        myImageLabels[i].grid(row=0, column=0,columnspan=3)
        status = Label(root, text = "Image " + str(obj.getVal() + 1) + " of " + str(obj.n),  bd=1)
        status.grid_remove()
        status.grid(row=2, column=0, columnspan=3)
        if(nextBtn["state"] == "disabled"):
            nextBtn["state"] = "normal"
        
    if(obj.getVal() <= 0):
        prevBtn["state"] = "disabled"
        
class Tracker:
    
    def __init__(self, j):
        self.i = 0
        self.n = j
    
    def increment(self):
        if(self.i < self.n - 1):
            self.i = self.i + 1
    
    def decrement(self):
        if(self.i > 0):
            self.i = self.i - 1
    
    def getVal(self):
        return self.i


if (__name__ == '__main__'):

    root = Tk()

    myPath = "images/"
    myImagesPath = [myPath + f for f in listdir(myPath) if isfile(join(myPath,f))]
    print(myImagesPath)
    # Images need a container to put on, so we are using Label as a container here.
    myImages = []
    myImageLabels = []
    for k in myImagesPath:
        myImages.append(ImageTk.PhotoImage(Image.open(k)))
        myImageLabels.append(Label(image=myImages[len(myImages) - 1]))
    obj = Tracker(len(myImageLabels))
    status = Label(root, text = "Image " + str(obj.getVal() + 1) + " of " + str(obj.n),  bd=1)
    nextBtn = Button(root, text=">>", command= lambda: onClickNext())
    prevBtn = Button(root, text="<<", command= lambda: onClickPrev(), state="disabled")
    exitBtn = Button(root, text="Exit", command=root.quit)
    myImageLabels[obj.getVal()].grid(row=0, column=0,columnspan=3)
    prevBtn.grid(row=1, column=0)
    exitBtn.grid(row=1, column=1)
    nextBtn.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=E+W)

    root.mainloop()