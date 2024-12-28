import game, text, button, cheats

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
    game.gameScreen.blit(text.energyText.text, (0,0))
    game.gameScreen.blit(text.matterText.text, (0,50))

    if menuVar.currentMenu == "cheats":
        cheats.cheatsTextBox.drawTextBox()

menuVar = menu()