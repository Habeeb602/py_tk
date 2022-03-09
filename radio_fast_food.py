from tkinter import *
from PIL import ImageTk, Image

def getUserOption(option):
    return Label(root, text=option.get()).pack()


if __name__ == "__main__":
    root = Tk()
    
    TYPES = [
        ("Pani Puri", "Pani Puri"),
        ("Cauliflower Manchurian", "Cauliflower Manchurian"),
        ("Chicken Fried Rice", "Chicken Fried Rice"),
        ("Egg Noodles", "Egg Noodles"),
        ("Biriyani", "Biriyani")
    ]

    # Biriyani is the default userOption 
    userOption = StringVar(value="Biriyani")

    for text, value in TYPES:
        Radiobutton(root, text=text, value=value, variable=userOption).pack(anchor=W)

    Button(root, text="Get User-Selected Food", command= lambda: getUserOption(userOption)).pack()

    root.mainloop()

