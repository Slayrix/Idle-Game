import pygame as pg
import currency, listVars, listVars, menu, buttonGroup

def updateScreen():
    gameScreen.fill((0, 0, 0))

    for buttonVar in listVars.buttonList.list:
        buttonVar.checkUpdateText()
    
    for textVar in listVars.textList.list:
        textVar.checkUpdateText()
    
    for buttonGroupVar in listVars.buttonGroupList.list:
        buttonGroupVar.showButtonGroup()

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

gameScreen = pg.display.set_mode((1000, 1000))