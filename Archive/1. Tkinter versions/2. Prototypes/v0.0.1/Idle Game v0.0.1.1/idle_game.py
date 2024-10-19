from tkinter import *

class currency:
    def __init__(self):
        self.amount = 0
        self.idleGen = 0
        self.gainPerSecond = 0
        self.costToGen = 0
    
    def addOne(self):
        self.amount = self.amount + 1
    
    def addXAmount(self, x):
        self.amount = round(self.amount + x, 2)
    
    def subXAmount(self, x):
        self.amount = round(self.amount - x, 2)

    def startIdleGen(self):
        self.idleGen = 1
    
    def addOneGainPerSecond(self):
        self.gainPerSecond = self.gainPerSecond + 1
    
    def addXGainPerSecond(self, x):
        self.gainPerSecond = round(self.gainPerSecond + x, 2)

    def addXCostToGen(self, x):
        self.costToGen = self.costToGen + x
    
class upgrade:
    def __init__(self):
        self.level = 0
    
    def setCost(self, x):
        self.cost = x

    def increaseLevelByOne(self):
        self.level = self.level + 1

    def increaseCost(self):
        self.increaseLevelByOne()
        self.cost = round(self.cost*(1+.1)**self.level, 2)

energy = currency()
matter = currency()

genEnergyUpgrade = upgrade()
genEnergyUpgrade.setCost(.05)

matterGenIncreaseUpgrade = upgrade()
matterGenIncreaseUpgrade.setCost(.15)

def changeText(objectVar, text):
    objectVar.config(state=NORMAL)
    objectVar.delete(1.0, END)
    objectVar.insert(INSERT, text)
    objectVar.config(state=DISABLED)

def changeButtonText(objectVar, text):
    objectVar.config(text=text)

def updateText():
    changeText(energyAmountText, "Energy: " + str(energy.amount))
    changeText(matterAmountText, "Matter: " + str(matter.amount))
    changeText(energyProducedPerSecondText, "Energy+/s: " + str(energy.gainPerSecond))

    changeButtonText(genEnergyUpgradeButton, "Auto gen 1 energy every second\nCosts: " + str(genEnergyUpgrade.cost))
    changeButtonText(matterGenIncreaseUpgradeButton, "Double Matter Generation\nWill increase energy consumption by +10\nCosts: 0.15 Matter")

def genEnergy():
    energy.addOne()
    updateText()

def startBigBang():
    if energy.amount >= 10:
        energy.subXAmount(10)
        matter.addXGainPerSecond(.01)
        matter.addXCostToGen(10)
        matterAmountText.place(width=100, height=20, y=50)
        startBigBangButton.forget()
        updateText()

def getEnergyUpgrade():
    if matter.amount >= genEnergyUpgrade.cost:
        matter.subXAmount(genEnergyUpgrade.cost)
        genEnergyUpgrade.increaseCost()
        if energy.gainPerSecond == 0:
            energy.startIdleGen()
        energy.addOneGainPerSecond()
        updateText()

def getMatterGenIncreaseUpgrade():
    if matter.amount >= matterGenIncreaseUpgrade.cost:
        matter.subXAmount(matterGenIncreaseUpgrade.cost)
        matter.addXGainPerSecond(matter.gainPerSecond)
        matter.addXCostToGen(10)
        updateText()
        matterGenIncreaseUpgradeButton.forget()

def gameLoop():
    if energy.amount >= matter.costToGen and matter.gainPerSecond > 0:
        energy.subXAmount(matter.costToGen)
        matter.addXAmount(matter.gainPerSecond)

    if energy.idleGen == 1:
        energy.addXAmount(energy.gainPerSecond)

    updateText()
    gameWindow.after(1000, gameLoop)

gameWindow = Tk()

gameWindow.geometry("500x500")

energyGenButton = Button(text="Click to Gen", command=genEnergy)
startBigBangButton = Button(text="Start Big Bang\nCosts: 10 Energy", command=startBigBang)
genEnergyUpgradeButton = Button(command=getEnergyUpgrade)
matterGenIncreaseUpgradeButton = Button(command=getMatterGenIncreaseUpgrade)

energyAmountText = Text()
matterAmountText = Text()
energyProducedPerSecondText = Text()

energyAmountText.place(width=100, height=20)
energyProducedPerSecondText.place(width=120, height=20, y=20)

energyGenButton.pack()
startBigBangButton.pack()
genEnergyUpgradeButton.pack()
matterGenIncreaseUpgradeButton.pack()

updateText()
gameWindow.after(1000, gameLoop)
mainloop()