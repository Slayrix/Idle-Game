from tkinter import *

class currency:
    def __init__(self):
        self.amount = 0
        self.gainPerSecond = 0
        self.costToGen = 0
    
    def addOne(self):
        self.amount = self.amount + 1
    
    def addXAmount(self, x):
        self.amount = round(self.amount + x, 2)
    
    def subXAmount(self, x):
        self.amount = round(self.amount - x, 2)
    
    def addOneGainPerSecond(self):
        self.gainPerSecond = self.gainPerSecond + 1
    
    def addXGainPerSecond(self, x):
        self.gainPerSecond = round(self.gainPerSecond + x, 2)

    def addXCostToGen(self, x):
        self.costToGen = self.costToGen + x

    def subXCostToGen(self, x):
        self.costToGen = self.costToGen - x
    
class upgrade:
    def __init__(self):
        self.level = 0
        self.growthRate = 0
        self.currencyIncreaseAmount = 0
    
    def setCost(self, x):
        self.cost = x
    
    def setGrowthRate(self, x):
        self.growthRate = x
    
    def setCurrencyIncreaseAmount(self, x):
        self.currencyIncreaseAmount = x
    
    def addXCurrencyIncreaseAmount(self, x):
        self.currencyIncreaseAmount = self.currencyIncreaseAmount + x

    def increaseLevelByOne(self):
        self.level = self.level + 1

    def increaseCost(self):
        self.increaseLevelByOne()
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

class menu:
    def __init__(self):
        self.menu = "main"
        self.cheats = False
    
    def enableCheats(self):
        self.cheats = True
    
    def changeMenu(self, x):
        self.menu = x

energy = currency()
matter = currency()

bigBangUpgrade = upgrade()
bigBangUpgrade.setCost(10)

genEnergyUpgrade = upgrade()
genEnergyUpgrade.setCost(.05)
genEnergyUpgrade.setGrowthRate(.1)
genEnergyUpgrade.setCurrencyIncreaseAmount(1)

doubleMatterGenUpgrade = upgrade()
doubleMatterGenUpgrade.setCost(.15)
doubleMatterGenUpgrade.setGrowthRate(6)

doubleUpgrade1EnergyGenUpgrade = upgrade()
doubleUpgrade1EnergyGenUpgrade.setCost(.5)

decreaseMatterGenCostUpgrade = upgrade()
decreaseMatterGenCostUpgrade.setCost(1)
decreaseMatterGenCostUpgrade.setGrowthRate(.15)

currentMenu = menu()
currentMenu.enableCheats() #Disable to disable cheats

def displayMenu():
    if currentMenu.menu == "main":
        shopBackButton.forget()
        startBigBangButton.forget()
        genEnergyUpgradeButton.forget()
        doubleMatterGenUpgradeButton.forget()
        doubleUpgrade1EnergyGenUpgradeButton.forget()
        decreaseMatterGenCostButton.forget()
        shopBackButton.forget()

        energyAmountText.place(width=100, height=20)

        energyGenButton.pack()

        if bigBangUpgrade.level > 0:
            matterAmountText.place(width=100, height=20, y=50)
            openShopButton.pack()
            startBigBangButton.forget()
        else:
            if energy.amount >= 10:
                startBigBangButton.pack()
        
        if genEnergyUpgrade.level > 0:
            energyProducedPerSecondText.place(width=120, height=20, y=20)

    elif currentMenu.menu == "shop":
        energyGenButton.forget()
        openShopButton.forget()

        genEnergyUpgradeButton.pack()
        doubleMatterGenUpgradeButton.pack()
        doubleUpgrade1EnergyGenUpgradeButton.pack()
        decreaseMatterGenCostButton.pack()
        shopBackButton.pack()

        if bigBangUpgrade.level > 0:
            matterAmountText.place(width=100, height=20, y=50)
            startBigBangButton.forget()

        if genEnergyUpgrade.level > 0:
            energyProducedPerSecondText.place(width=120, height=20, y=20)

        if doubleMatterGenUpgrade.level > 2:
            doubleMatterGenUpgradeButton.forget()
        
        if doubleUpgrade1EnergyGenUpgrade.level > 0:
            doubleUpgrade1EnergyGenUpgradeButton.forget()
    
    if currentMenu.cheats == True:
            cheatList.place(x=10, y=300)
            cheatTextBox.place(width=100, height=20, x=20, y=270)
            cheatButton.place(x=25, y=470)
    
def changeMenu(x):
    currentMenu.changeMenu(x)
    updateText()

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

    changeButtonText(genEnergyUpgradeButton, "Upgrade 1\nAuto gen +" +  str(genEnergyUpgrade.currencyIncreaseAmount) + " energy every second\nCosts: " + str(genEnergyUpgrade.cost) + " Matter")
    changeButtonText(doubleMatterGenUpgradeButton, "Double Matter Generation\nWill increase energy consumption by +10\nCosts: " + str(doubleMatterGenUpgrade.cost) + " Matter")
    changeButtonText(doubleUpgrade1EnergyGenUpgradeButton, "Double Energy Generation of Upgrade 1\nCosts: " + str(doubleUpgrade1EnergyGenUpgrade.cost) + " Matter")
    changeButtonText(decreaseMatterGenCostButton, "Decrease Energy Cost to Generate Matter By 1\nCosts: " + str(decreaseMatterGenCostUpgrade.cost) + " Matter")

    displayMenu()

def genEnergy():
    energy.addOne()
    updateText()

def buyUpgrade(currencySpent, upgradeVar, currencyUpgraded, amountGainPerSecondAdded, amountCostToGenAdded, amountCostToGenSubbed, upgradeBuff, buffedUpgrade, upgradeBuffAmount):
    if currencySpent.amount >= upgradeVar.cost:
        currencySpent.subXAmount(upgradeVar.cost)
        upgradeVar.increaseCost()
        currencyUpgraded.addXGainPerSecond(amountGainPerSecondAdded)
        currencyUpgraded.addXCostToGen(amountCostToGenAdded)
        currencyUpgraded.subXCostToGen(amountCostToGenSubbed)
        if upgradeBuff == True:
            currencyUpgraded.addXGainPerSecond(buffedUpgrade.currencyIncreaseAmount * buffedUpgrade.level)
            buffedUpgrade.addXCurrencyIncreaseAmount(upgradeBuffAmount)
    updateText()

def cheat():
    currencyChoice = cheatList.get(cheatList.curselection()).lower()
    amount = int(cheatTextBox.get(1.0, END))
    if currencyChoice == "energy":
        energy.addXAmount(amount)
    elif currencyChoice == "matter":
        matter.addXAmount(amount)
    updateText()

def gameLoop():
    if energy.amount >= matter.costToGen and matter.gainPerSecond > 0:
        energy.subXAmount(matter.costToGen)
        matter.addXAmount(matter.gainPerSecond)
    energy.addXAmount(energy.gainPerSecond)

    updateText()
    gameWindow.after(1000, gameLoop)

gameWindow = Tk()

gameWindow.geometry("500x500")

energyGenButton = Button(text="Click to Gen", command=genEnergy)
startBigBangButton = Button(text="Start Big Bang\nCosts: 10 Energy", command= lambda: buyUpgrade(energy, bigBangUpgrade, matter, .01, 10, 0, False, 0, 0))
genEnergyUpgradeButton = Button(command= lambda: buyUpgrade(matter, genEnergyUpgrade, energy, genEnergyUpgrade.currencyIncreaseAmount, 0, 0, False, 0, 0))
doubleMatterGenUpgradeButton = Button(command= lambda: buyUpgrade(matter, doubleMatterGenUpgrade, matter, matter.gainPerSecond, 10, 0, False, 0, 0))
doubleUpgrade1EnergyGenUpgradeButton = Button(command = lambda: buyUpgrade(matter, doubleUpgrade1EnergyGenUpgrade, energy, 0, 0, 0, True, genEnergyUpgrade, genEnergyUpgrade.currencyIncreaseAmount))
decreaseMatterGenCostButton = Button(command = lambda: buyUpgrade(matter, decreaseMatterGenCostUpgrade, matter, 0, 0, 1, False, 0, 0))
openShopButton = Button(text="Shop", command= lambda: changeMenu("shop"))
shopBackButton = Button(text="Back", command= lambda: changeMenu("main"))

energyAmountText = Text()
matterAmountText = Text()
energyProducedPerSecondText = Text()
cheatTextBox = Text()

cheatList = Listbox()
cheatList.insert(1, "Energy")
cheatList.insert(2, "Matter")
cheatButton = Button(text="Press to Cheat", command= cheat)

updateText()
gameWindow.after(1000, gameLoop)
mainloop()