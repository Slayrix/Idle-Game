import pygame as pg
import time, asyncio

pg.init()
screen = pg.display.set_mode((1000, 1000))

class currency:
    def __init__(self):
        self.amount = 0
        self.gainPerSecond = 0

    def addOne(self):
        self.amount += 1
    
    def addAmount(self, x):
        self.amount = round(self.amount + x, 2)

    def subAmount(self, x):
        self.amount = round(self.amount - x, 2)
    
    def addOneGainPerSecond(self):
        self.gainPerSecond += 1

class upgrade():
    def __init__(self, cost, currency, growthRate = 0):
        self.cost = cost
        self.currency = currency
        self.level = 0
        self.growthRate = growthRate
    
    def setCost(self, x):
        self.cost = x
    
    def setCurrency(self, currency: currency):
        self.currency = currency
    
    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

class text:
    def __init__(self):
        self.font = pg.font.SysFont("arial", 30)
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)

class button:
    def __init__(self):
        self.font = pg.font.SysFont("arial", 30)
        self.bottomFont = pg.font.SysFont("arial", 30)
        self.bottomTextActive = False
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)
    
    def setBottomText(self, text: str, textColor, backgroundColor = None):
        self.bottomText = self.bottomFont.render(text, True, textColor, backgroundColor)

        while self.text.get_width() > self.bottomText.get_width():
            text = text + " "
            self.bottomText = self.bottomFont.render(text, True, textColor, backgroundColor)

        self.bottomTextActive = True
    
    def setButton(self, x, y):
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.bottomTextActive == True:
            self.bottomRect = self.bottomText.get_rect()
            self.bottomRect.x = x
            self.bottomRect.y = y+self.text.get_height()

energy = currency()
matter = currency()

bigBangUpgrade = upgrade(10, energy)
genEnergyUpgrade = upgrade(.05, matter, .1)

energyText = text()
matterText = text()

genButton = button()
genButton.setText("Click to gen", (255, 255, 255), (92, 92, 92))
genButton.setButton(150, 100)

bigBangButton = button()
bigBangButton.setText("Start Big Bang", (255, 255, 255), (92, 92, 92))
bigBangButton.setBottomText(str(bigBangUpgrade.cost) + " Energy", (255, 255, 255), (92, 92, 92))
bigBangButton.setButton(150, 150)

genEnergyUpgradeButton = button()
genEnergyUpgradeButton.setText("Auto gen +1 energy per second", (255, 255, 255), (92, 92, 92))
genEnergyUpgradeButton.setBottomText(str(genEnergyUpgrade.cost) + " Matter", (255, 255, 255), (92, 92, 92))
genEnergyUpgradeButton.setButton(150, 230)

def genEnergy():
    energy.addOne()
    updateScreen()

def updateScreen():
    screen.fill((0, 0, 0))

    energyText.setText("Energy: " + str(energy.amount), (255, 255, 255))
    matterText.setText("Matter: "+ str(matter.amount), (255, 255, 255))

    genEnergyUpgradeButton.setBottomText(str(genEnergyUpgrade.cost) + " Matter", (255, 255, 255), (92, 92, 92))

    screen.blit(genButton.text, genButton.rect)

    if bigBangUpgrade.level == 0:
        screen.blit(bigBangButton.text, bigBangButton.rect)
        screen.blit(bigBangButton.bottomText, bigBangButton.bottomRect)
    
    screen.blit(genEnergyUpgradeButton.text, genEnergyUpgradeButton.rect)
    screen.blit(genEnergyUpgradeButton.bottomText, genEnergyUpgradeButton.bottomRect)

    screen.blit(energyText.text, (0,0))
    screen.blit(matterText.text, (0,50))

    pg.display.update()

def buyUpgrade(upgrade: upgrade, gainPerSecondIncrease = False, gainPerSecondCurrency: currency = None):
    if upgrade.currency.amount >= upgrade.cost:
        upgrade.currency.subAmount(upgrade.cost)
        upgrade.level += 1
        upgrade.increaseCost()
        if gainPerSecondIncrease == True:
            gainPerSecondCurrency.addOneGainPerSecond()

def calculations():
    energy.addAmount(energy.gainPerSecond)

    if bigBangUpgrade.level >= 1 and energy.amount >= 10:
        energy.subAmount(10)
        matter.addAmount(.01)

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
                
                if bigBangButton.rect.collidepoint(event.pos) or bigBangButton.bottomRect.collidepoint(event.pos):
                    buyUpgrade(bigBangUpgrade)
                
                if genEnergyUpgradeButton.rect.collidepoint(event.pos) or genEnergyUpgradeButton.bottomRect.collidepoint(event.pos):
                    buyUpgrade(genEnergyUpgrade, True, energy)

        updateScreen()
        tick = gameTick(tick)
        time.sleep(.01)
        await asyncio.sleep(0)

asyncio.run(main())
pg.quit()