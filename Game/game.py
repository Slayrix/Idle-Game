import pygame as pg
import currency, text, button, upgrade, menu

def updateScreen():
    gameScreen.fill((0, 0, 0))

    text.energyText.setText("Energy: " + str(currency.energy.amount), (255, 255, 255))
    text.matterText.setText("Matter: "+ str(currency.matter.amount), (255, 255, 255))

    button.genEnergyUpgradeButton.updateText("Auto gen +" + str(upgrade.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", 1)
    button.genEnergyUpgradeButton.updateText(str(upgrade.genEnergyUpgrade.cost) + " Matter", 2)
    button.matterGenUpgradeButton.updateText(str(upgrade.matterGenUpgrade.cost) + " Matter", 2)

    menu.displayMenu()

    pg.display.update()

def gameTick(tick):
    tick += 1
    if tick >= 100: # If a second passes
        calculations()
        tick = 0
    return tick

def calculations():
    currency.energy.addAmount(currency.energy.gainPerSecond)

    if currency.energy.amount >= currency.matter.costToGen:
        currency.energy.subAmount(currency.matter.costToGen)
        currency.matter.addAmount(currency.matter.gainPerSecond)

def genEnergy():
    currency.energy.addOne()

gameScreen = pg.display.set_mode((1000, 1000))