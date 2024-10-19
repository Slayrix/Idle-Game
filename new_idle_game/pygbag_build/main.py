import pygame as pg
import time, asyncio

pg.init()
screen = pg.display.set_mode((1000, 1000))

class currency:
    def __init__(self):
        self.amount = 0
        self.gainPerSecond = 0
        self.costToGen = 0

    def addOne(self):
        self.amount += 1
    
    def addAmount(self, x):
        self.amount = round(self.amount + x, 2)

    def subAmount(self, x):
        self.amount = round(self.amount - x, 2)
    
    def addGainPerSecond(self, x):
        self.gainPerSecond += x

    def addCostToGen(self, x):
        self.costToGen += x

class upgrade():
    def __init__(self, cost, currencyCost, growthRate = 0, increaseGenPerSecondCurrency = None, increaseGenPerSecondAmount = None, increaseCostPerGenCurrency = None, increaseCostPerGenAmount = None):
        self.cost = cost
        self.currencyCost = currencyCost
        self.level = 0
        self.growthRate = growthRate
        self.increaseGenPerSecondCurrency = increaseGenPerSecondCurrency
        self.increaseGenPerSecondAmount = increaseGenPerSecondAmount
        self.increaseCostPerGenCurrency = increaseCostPerGenCurrency
        self.increaseCostPerGenAmount = increaseCostPerGenAmount
    
    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

class upgradeBuff():
    def __init__(self, cost, currencyCost, upgradeBuffed, upgradeVarBuffed, buffedAmount, growthRate = 0):
        self.cost = cost
        self.currencyCost = currencyCost
        self.level = 0
        self.upgradeBuffed = upgradeBuffed
        self.upgradeVarBuffed = upgradeVarBuffed
        self.buffedAmount = buffedAmount
        self.growthRate = growthRate

    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

class text:
    def __init__(self):
        self.font = pg.font.Font("arial.ttf", 30)
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)

class button():
    def __init__(self, textList: list, textColor, xPos: int, yPos: int):
        self.font = pg.font.Font("arial.ttf", 30)
        self.lineVarList = []
        self.textColor = textColor
        widthList = []
        height = 0
        i = 0
        for e in textList:
            self.lineVarList += [self.font.render(textList[i], True, self.textColor)]
            if i == 0:
                self.rect = self.lineVarList[i].get_rect()
            widthList += [self.lineVarList[i].get_width()]
            height += self.lineVarList[i].get_height()
            i += 1
        self.rect.width = max(widthList)
        self.rect.height = height
        self.rect.x = xPos
        self.rect.y = yPos
    
    def drawButton(self, buttonColor):
        pg.draw.rect(screen, buttonColor, self.rect)
        widthL = []
        for e in self.lineVarList:
            widthL += [e.get_width()]
        yOffset = 0
        for e in self.lineVarList:
            if e.get_width() == max(widthL):
                screen.blit(e, (self.rect.x, self.rect.y + yOffset))
                yOffset += e.get_height()
            else:
                screen.blit(e, (self.rect.x + (max(widthL) / 2) - (e.get_width() / 2), self.rect.y + yOffset))
                yOffset += e.get_height()
    
    def updateText(self, text: str, line: int):
        self.lineVarList[line] = self.font.render(text, True, self.textColor)

energy = currency()
matter = currency()

bigBangUpgrade = upgrade(10, energy, 0, matter, .01, matter, 10)
genEnergyUpgrade = upgrade(.05, matter, .1, energy, 1)
matterGenUpgrade = upgrade(.15, matter, 6, matter, "double", matter, 10)

genEnergyUpgradeBuff = upgradeBuff(.5, matter, genEnergyUpgrade, "increaseGenPerSecondAmount", "double")

energyText = text()
matterText = text()

genButton = button(["Click to gen"], (255, 255, 255), 150, 100)
bigBangButton = button(["Start Big Bang", str(bigBangUpgrade.cost) + " Energy"], (255, 255, 255), 150, 150)
genEnergyUpgradeButton = button(["Upgrade 1", "Auto gen +1 energy per second", str(genEnergyUpgrade.cost) + " Matter"], (255, 255, 255), 150, 230)
matterGenUpgradeButton = button(["Double Matter Generation", "Increases energy consumption by +10", str(matterGenUpgrade.cost) + " Matter"], (255, 255, 255), 150, 350)
genEnergyUpgradeBuffButton = button(["Double Energy Generation of Upgrade 1", str(genEnergyUpgradeBuff.cost) + " Matter"], (255, 255, 255), 150, 470)

def genEnergy():
    energy.addOne()
    updateScreen()

def updateScreen():
    screen.fill((0, 0, 0))

    energyText.setText("Energy: " + str(energy.amount), (255, 255, 255))
    matterText.setText("Matter: "+ str(matter.amount), (255, 255, 255))

    genButton.drawButton((92, 92, 92))
    
    genEnergyUpgradeButton.updateText(str(genEnergyUpgrade.cost) + " Matter", 2)
    genEnergyUpgradeButton.drawButton((92, 92, 92))

    matterGenUpgradeButton.updateText(str(matterGenUpgrade.cost) + " Matter", 2)
    matterGenUpgradeButton.drawButton((92, 92, 92))

    genEnergyUpgradeBuffButton.drawButton((92, 92, 92))

    if bigBangUpgrade.level == 0:
        bigBangButton.drawButton((92, 92, 92))
    
    screen.blit(energyText.text, (0,0))
    screen.blit(matterText.text, (0,50))

    pg.display.update()

def buyUpgrade(upgrade: upgrade):
    if upgrade.currencyCost.amount >= upgrade.cost:
        upgrade.currencyCost.subAmount(upgrade.cost)
        upgrade.level += 1
        upgrade.increaseCost()
        if upgrade.increaseGenPerSecondCurrency != None:
            if upgrade.increaseGenPerSecondAmount == "double":
                upgrade.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.increaseGenPerSecondCurrency.gainPerSecond)
            else:
                upgrade.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.increaseGenPerSecondAmount)
        if upgrade.increaseCostPerGenCurrency != None:
            upgrade.increaseCostPerGenCurrency.addCostToGen(upgrade.increaseCostPerGenAmount)
        
def buyUpgradeBuff(upgradeBuff: upgradeBuff):
    if upgradeBuff.currencyCost.amount >= upgradeBuff.cost:
        upgradeBuff.currencyCost.subAmount(upgradeBuff.cost)
        upgradeBuff.level += 1
        upgradeBuff.increaseCost()
        if upgradeBuff.upgradeVarBuffed == "increaseGenPerSecondAmount":
            if upgradeBuff.buffedAmount == "double":
                upgradeBuff.upgradeBuffed.increaseGenPerSecondCurrency.addGainPerSecond(upgradeBuff.upgradeBuffed.level*upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount)
                upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount += upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount
            else:
                upgradeBuff.upgradeBuffed.increaseGenPerSecondCurrency.addGainPerSecond(upgradeBuff.upgradeBuffed.level*upgradeBuff.buffedAmount)
                upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount += upgradeBuff.buffedAmount
            
def calculations():
    energy.addAmount(energy.gainPerSecond)

    if energy.amount >= matter.costToGen:
        energy.subAmount(matter.costToGen)
        matter.addAmount(matter.gainPerSecond)

def gameTick(tick):
    tick += 1
    if tick >= 100: # If a second passes
        calculations()
        tick = 0
    return tick

async def main():
    running = True
    tick = 0
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if genButton.rect.collidepoint(event.pos):
                    genEnergy()
                
                if bigBangButton.rect.collidepoint(event.pos):
                    buyUpgrade(bigBangUpgrade)
                
                if genEnergyUpgradeButton.rect.collidepoint(event.pos):
                    buyUpgrade(genEnergyUpgrade)
                
                if matterGenUpgradeButton.rect.collidepoint(event.pos):
                    buyUpgrade(matterGenUpgrade)

                if genEnergyUpgradeBuffButton.rect.collidepoint(event.pos):
                    buyUpgradeBuff(genEnergyUpgradeBuff)
            
        updateScreen()
        tick = gameTick(tick)
        time.sleep(.01)
        await asyncio.sleep(0)

asyncio.run(main())
pg.quit()