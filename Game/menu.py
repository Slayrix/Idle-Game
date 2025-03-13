import vars.listVars as listVars, vars.textBoxVars as textBoxVars

class menu:
    def __init__(self):
        self.currentMenu = "defaultMenu"
    
    def setCurrentMenuToDefaultMenu(self):
        self.currentMenu = "defaultMenu"

    def setCurrentMenuToShop(self):
        self.currentMenu = "shop"
    
    def setCurrentMenuToCheats(self):
        self.currentMenu = "cheats"

def displayMenu():
    for buttonVar in listVars.buttonList.list:
        buttonVar.showButton()
    
    for textVar in listVars.textList.list:
        if textVar.showText() == True:
            textVar.drawText()

    if menuVar.currentMenu == "cheats":
        textBoxVars.cheatsTextBox.drawTextBox()

menuVar = menu()