import pygame as pg, vars.listVars as listVars, menu

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
    for currencyVar in listVars.currencyList.list:
        currencyVar.genFunction()

gameScreen = pg.display.set_mode((1000, 1000))