from tkinter import *

class clicks:
    def __init__(self):
        self.amount = 0
    
    def addOne(self):
        self.amount = self.amount + 1

c = clicks()

def function():
    c.addOne()
    clickAmountText.config(state=NORMAL)
    clickAmountText.delete(1.0, END)
    clickAmountText.insert(INSERT, "Clicks: " + str(c.amount))
    clickAmountText.config(state=DISABLED)

gameWindow = Tk()

gameWindow.geometry("500x500")

clickGenButton = Button(text="Click to Gen", command=function)
clickAmountText = Text()
clickAmountText.insert(INSERT, "Clicks: " + str(c.amount))
clickAmountText.config(state=DISABLED)

clickAmountText.place(width=100, height=20)
clickGenButton.pack()

mainloop()