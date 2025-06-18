import core.menu as menu, core.listVars as listVars, core.settings as settings, core.game as game, pygame as pg, vars.textVars as textVars, core.event as event, core.saveLoad as saveLoad

def genCurrency(functionVars):
    currencyVar = functionVars[0]
    amount = functionVars[1]
    currencyVar.addAmount(amount)

def changeMenu(functionVars):
    newMenu = functionVars[0]
    menu.menuVar.setCurrentMenu(newMenu)

def buyUpgrade(functionVars):
    upgradeVar = functionVars[0]
    upgradeVar.buyUpgrade()

def cheat(functionVars):
    currencyVar = functionVars[0]
    for object in listVars.objectList.list:
        if object[1] == "textBox":
            textBoxVar = object[0]
            textBoxVar.textBoxAddCurrency(currencyVar)

def changeResolution(functionVars):
    forwardBackward = functionVars[0]
    currentIndex = settings.resolutionList.index(settings.resolution)
    if forwardBackward == "forward":
        newIndex = currentIndex + 1
        if newIndex > len(settings.resolutionList) - 1:
            newIndex = 0
    else:
        newIndex = currentIndex - 1
        if newIndex < 0:
            newIndex = len(settings.resolutionList) - 1
    settings.resolution = settings.resolutionList[newIndex]
    settings.resolutionScale = settings.calcResolutionScale(settings.resolution)
    settings.fontSize = settings.calcFontSize(settings.refFontSize, settings.resolutionScale)
    settings.infoboxFontSize = settings.calcFontSize(settings.infoboxRefFontSize, settings.resolutionScale)
    pg.display.quit()
    game.gameScreen = pg.display.set_mode(settings.resolution)
    setObjsToNewResolution()

def setObjsToNewResolution():
    textVars.currentResolutionText.changeText([str(settings.resolution[0]), "x", str(settings.resolution[1])])
    for button in listVars.buttonList.list:
        button.resizeButton()
    for text in listVars.textList.list:
        text.resizeText()
    for buttonGroup in listVars.buttonGroupList.list:
        buttonGroup.resizeButtonGroup()
    for infobox in listVars.infoboxList.list:
        infobox.resizeInfoboxFont()
    for object in listVars.objectList.list:
        if object[1] == "textBox":
            object[0].resizeTextBox()

def saveGame():
    saveLoad.saveData()

def loadGame():
    saveLoad.loadData()

def quitGame():
    event.quitGame = True
    
buttonFunctionality = {
    "genCurrency": genCurrency,
    "changeMenu": changeMenu,
    "buyUpgrade": buyUpgrade,
    "cheat": cheat,
    "changeResolution": changeResolution,
    "saveGame": saveGame,
    "loadGame": loadGame,
    "quitGame": quitGame
}