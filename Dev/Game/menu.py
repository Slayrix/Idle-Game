import vars.listVars as listVars

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
        textVar.showText()

    for object in listVars.objectList.list:
        if object[1] == "textBox":
            textBoxVar = object[0]
            textBoxVar.drawTextBoxCheck()

menuVar = menu()