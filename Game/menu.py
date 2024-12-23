import game, currency, upgrade, text, button, cheats

class menu:
    def __init__(self):
        self.currentMenu = "defaultMenu"
    
    def setCurrentMenuToDefaultMenu(self):
        self.currentMenu = "defaultMenu"

    def setCurrentMenuToShop(self):
        self.currentMenu = "shop"

def displayMenu():
    if menuVar.currentMenu == "defaultMenu":
        game.gameScreen.blit(text.energyText.text, (0,0))

        button.genButton.drawButton((92, 92, 92))
    
        if upgrade.bigBangUpgrade.level == 0 and currency.energy.amount >= upgrade.bigBangUpgrade.cost:
            button.bigBangButton.drawButton((92, 92, 92))
        elif upgrade.bigBangUpgrade.level >= 1:
            game.gameScreen.blit(text.matterText.text, (0,50))
            button.shopButton.drawButton((92, 92, 92))
        
        cheats.cheatsTextBox.drawTextBox()
    elif menuVar.currentMenu == "shop":
        game.gameScreen.blit(text.energyText.text, (0,0))
        game.gameScreen.blit(text.matterText.text, (0,50))

        button.shopBackButton.drawButton((92, 92, 92))

        button.genEnergyUpgradeButton.drawButton((92, 92, 92))
        button.matterGenUpgradeButton.drawButton((92, 92, 92))
        button.genEnergyUpgradeBuffButton.drawButton((92, 92, 92))

menuVar = menu()