import text, button, cheats

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
    for buttonVar in button.buttonList.list:
        for menu in buttonVar.activeMenu:
            if menu == menuVar.currentMenu:
                if buttonVar.showButton() == True:
                    buttonVar.drawButton((92, 92, 92))
    
    for textVar in text.textList.list:
        for menu in textVar.activeMenu:
            if menu == menuVar.currentMenu:
                if textVar.showText() == True:
                    textVar.drawText()

    if menuVar.currentMenu == "cheats":
        cheats.cheatsTextBox.drawTextBox()

menuVar = menu()