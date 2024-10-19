from tkinter import *

class currency:
    def __init__(self):
        self.amount = 0
        self.idleGen = 0
    
    def addOne(self):
        self.amount = self.amount + 1
    
    def addXAmount(self, x):
        self.amount = self.amount + x
    
    def subXAmount(self, x):
        self.amount = self.amount - x

    def startIdleGen(self):
        self.idleGen = 1

energy = currency()
matter = currency()

def changeText(objectVar, text):
    objectVar.config(state=NORMAL)
    objectVar.delete(1.0, END)
    objectVar.insert(INSERT, text)
    objectVar.config(state=DISABLED)

def updateText():
    changeText(energyAmountText, "Energy: " + str(energy.amount))
    changeText(matterAmountText, "Matter: " + str(matter.amount))

def genEnergy():
    energy.addOne()
    updateText()

def startBigBang():
    if energy.amount >= 10:
        energy.subXAmount(10)
        matter.startIdleGen()
        matterAmountText.place(width=100, height=20, y=50)
        startBigBangButton.forget()
        updateText()

def gameLoop():
    if energy.amount >= 10 and matter.idleGen == 1:
        energy.subXAmount(10)
        matter.addXAmount(.01)
    updateText()
    gameWindow.after(1000, gameLoop)

gameWindow = Tk()

gameWindow.geometry("500x500")

energyGenButton = Button(text="Click to Gen", command=genEnergy)
startBigBangButton = Button(text="Start Big Bang\nCosts: 10 Energy", command=startBigBang)

energyAmountText = Text()
matterAmountText = Text()

energyAmountText.place(width=100, height=20)

energyGenButton.pack()
startBigBangButton.pack()

updateText()
gameWindow.after(1000, gameLoop)
mainloop()