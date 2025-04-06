import menu, classes.upgradeClass as upgradeClass, vars.textBoxVars as textBoxVars

def genCurrency(functionVars):
    currencyVar = functionVars[0]
    amount = functionVars[1]
    currencyVar.addAmount(amount)

def changeMenu(functionVars):
    menuChange = functionVars[0]
    if menuChange == "default":
        menu.menuVar.setCurrentMenuToDefaultMenu()
    elif menuChange == "shop":
        menu.menuVar.setCurrentMenuToShop()
    elif menuChange == "cheats":
        menu.menuVar.setCurrentMenuToCheats()

def buyUpgrade(functionVars):
    upgradeClass.buyUpgrade(functionVars[0])

def cheat(functionVars):
    currencyVar = functionVars[0]
    try:
        amount = int(textBoxVars.cheatsTextBox.textString)
        currencyVar.addAmount(amount)
    except ValueError:
        pass

buttonFunctionality = {
    "genCurrency": genCurrency,
    "changeMenu": changeMenu,
    "buyUpgrade": buyUpgrade,
    "cheat": cheat
}