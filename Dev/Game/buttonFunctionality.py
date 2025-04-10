import core.menu as menu, classes.upgradeClass as upgradeClass, core.listVars as listVars

def genCurrency(functionVars):
    currencyVar = functionVars[0]
    amount = functionVars[1]
    currencyVar.addAmount(amount)

def changeMenu(functionVars):
    newMenu = functionVars[0]
    menu.menuVar.setCurrentMenu(newMenu)

def buyUpgrade(functionVars):
    upgradeClass.buyUpgrade(functionVars[0])

def cheat(functionVars):
    currencyVar = functionVars[0]
    for object in listVars.objectList.list:
        if object[1] == "textBox":
            textBoxVar = object[0]
            textBoxVar.textBoxAddCurrency(currencyVar)

buttonFunctionality = {
    "genCurrency": genCurrency,
    "changeMenu": changeMenu,
    "buyUpgrade": buyUpgrade,
    "cheat": cheat
}