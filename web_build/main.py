import pygame as pg
import time, asyncio, menu, currency, upgrade, text, button, screen

def genEnergy():
    currency.energy.addOne()
    updateScreen()

def updateScreen():
    screen.gameScreen.fill((0, 0, 0))

    text.energyText.setText("Energy: " + str(currency.energy.amount), (255, 255, 255))
    text.matterText.setText("Matter: "+ str(currency.matter.amount), (255, 255, 255))

    button.genEnergyUpgradeButton.updateText("Auto gen +" + str(upgrade.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", 1)
    button.genEnergyUpgradeButton.updateText(str(upgrade.genEnergyUpgrade.cost) + " Matter", 2)
    button.matterGenUpgradeButton.updateText(str(upgrade.matterGenUpgrade.cost) + " Matter", 2)

    menu.displayMenu()

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
        
def buyUpgradeBuff(upgradeBuff: upgrade.upgradeBuff):
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
    currency.energy.addAmount(currency.energy.gainPerSecond)

    if currency.energy.amount >= currency.matter.costToGen:
        currency.energy.subAmount(currency.matter.costToGen)
        currency.matter.addAmount(currency.matter.gainPerSecond)

def gameTick(tick):
    tick += 1
    if tick >= 100: # If a second passes
        calculations()
        tick = 0
    return tick

def eventCheck(running):
    for event in pg.event.get():
        running = checkIfQuit(event, running)
        mouseClickCheck(event)    
    return running

def checkIfQuit(event, running):
    if event.type == pg.QUIT:
        running = False
    return running

def mouseClickCheck(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        checkIfButtonClicked(event)
        
def checkIfButtonClicked(event):
    if menu.menuVar.currentMenu == "defaultMenu":
        if button.shopButton.rect.collidepoint(event.pos) and upgrade.bigBangUpgrade.level >= 1:
            menu.menuVar.setCurrentMenuToShop()

        if button.genButton.rect.collidepoint(event.pos):
            genEnergy()
    
        if button.bigBangButton.rect.collidepoint(event.pos) and upgrade.bigBangUpgrade.level <= 0:
            buyUpgrade(upgrade.bigBangUpgrade)

    if menu.menuVar.currentMenu == "shop":
        if button.genEnergyUpgradeButton.rect.collidepoint(event.pos):
            buyUpgrade(upgrade.genEnergyUpgrade)
    
        if button.matterGenUpgradeButton.rect.collidepoint(event.pos):
            buyUpgrade(upgrade.matterGenUpgrade)

        if button.genEnergyUpgradeBuffButton.rect.collidepoint(event.pos):
            buyUpgradeBuff(upgrade.genEnergyUpgradeBuff)
    
        if button.shopBackButton.rect.collidepoint(event.pos):
            menu.menuVar.setCurrentMenuToDefaultMenu()
  
async def main():
    tick = 0
    running = True
    while running:
        running = eventCheck(running)
        updateScreen()
        tick = gameTick(tick)
        time.sleep(.01)
        await asyncio.sleep(0)

asyncio.run(main())
pg.quit()