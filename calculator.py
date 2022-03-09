from tkinter import *

def enterNumber(number):
    current = inputBox.get()
    inputBox.delete(0,'end')
    inputBox.insert(0, current + number)

def createNumbersBtn(txt):
    return Button(root, text=txt, padx=40, pady=25, activeforeground="white", activebackground="black",command= lambda: enterNumber(txt))

def clearEntry():
    inputBox.delete(0,'end')

def getNumber(oper):
    if(inputBox.get() != ""):
        nums.append(int(inputBox.get()))
        opers.append(oper)
        inputBox.delete(0,'end')

def equals():
    if(len(nums) > 0):
        nums.append(int(inputBox.get()))
        res = nums[0]
        print(nums)
        print(opers)
        for i in range(1, len(nums)):
            j = i - 1
            if(opers[j] == "+"):
                res = res + nums[i]
            elif(opers[j] == '-'):
                res = res - nums[i]
            elif(opers[j] == '*'):
                res = res * nums[i]
            elif(opers[j] == '/'):
                res = res // nums[i]
            elif(opers[j] == '*'):
                res = res % nums[i]
        inputBox.delete(0,'end')
        inputBox.insert(0, str(res))
        nums.clear()
        opers.clear()

# Main function
if __name__=="__main__":

    root = Tk()
    root.title("Simple Calculator")
    nums = []
    opers = []
    inputBox = Entry(root, width=30, border=2, borderwidth=5)
    btnZero = createNumbersBtn("0")
    btnOne = createNumbersBtn("1")
    btnTwo = createNumbersBtn("2")
    btnThree = createNumbersBtn("3")
    btnFour = createNumbersBtn("4")
    btnFive = createNumbersBtn("5")
    btnSix = createNumbersBtn("6")
    btnSeven = createNumbersBtn("7")
    btnEight = createNumbersBtn("8")
    btnNine = createNumbersBtn("9")
    btnAdd = Button(root, text = "+", padx=40, pady=25,activeforeground="white", activebackground="black", command=lambda: getNumber('+'))
    btnSub = Button(root, text = "-", padx=40, pady=25,activeforeground="white", activebackground="black", command=lambda: getNumber('-'))
    btnMul = Button(root, text = "*", padx=40, pady=25,activeforeground="white", activebackground="black", command=lambda: getNumber('*'))
    btnDiv = Button(root, text = "/", padx=40, pady=25,activeforeground="white", activebackground="black", command=lambda: getNumber('/'))
    btnMod = Button(root, text = "%", padx=40, pady=25,activeforeground="white", activebackground="black", command=lambda: getNumber('%'))
    btnClear = Button(root, text = "Clear", padx=80, pady=25,activeforeground="white", activebackground="black", command=clearEntry)
    btnEqual = Button(root, text = "  =  ", padx=80, pady=25,activeforeground="white", activebackground="black", command=equals)


    inputBox.grid(row=0, column=0, columnspan=3)

    btnSeven.grid(row=1, column=0)
    btnEight.grid(row=1, column=1)
    btnNine.grid(row=1, column=2)
    
    btnFour.grid(row=2, column=0)
    btnFive.grid(row=2, column=1)
    btnSix.grid(row=2, column=2)

    btnOne.grid(row=3, column=0)
    btnTwo.grid(row=3, column=1)
    btnThree.grid(row=3, column=2)

    btnZero.grid(row=4, column=0)
    btnClear.grid(row=4, column=1, columnspan=2)
    
    btnAdd.grid(row=5, column=0)
    btnSub.grid(row=5, column=1)
    btnMul.grid(row=5, column=2)

    btnMod.grid(row=6, column=0)
    btnEqual.grid(row=6, column=1, columnspan=2)

    root.mainloop()