from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def messageMe():
    
    response = messagebox.askyesnocancel("Message Box", "Hello Everyone!")
    # Label(root, text=response).pack()

    if (response == 1):
        Label(root, text="You Clicked YES!!!").pack()
    elif(response == 0):
        Label(root, text="You Clicked NO!!!").pack()
    else:
        Label(root, text="You Clicked CANCEL!!!").pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Message Box")

    Button(root, text="Click Me!", command=messageMe).pack(padx=100, pady=40)    

    root.mainloop()

