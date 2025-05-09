import pygame as pg
import currency, text, button, menu

def updateScreen():
    gameScreen.fill((0, 0, 0))

    for buttonVar in button.buttonList.list:
        buttonVar.checkUpdateText()
    
    for textVar in text.textList.list:
        textVar.checkUpdateText()

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