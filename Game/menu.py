import screen, currency, upgrade, text, button

class menu:
    def __init__(self):
        self.currentMenu = "defaultMenu"
    
    def setCurrentMenuToDefaultMenu(self):
        self.currentMenu = "defaultMenu"

    def setCurrentMenuToShop(self):
        self.currentMenu = "shop"

def displayMenu():
    if menuVar.currentMenu == "defaultMenu":
        screen.gameScreen.blit(text.energyText.text, (0,0))

        button.genButton.drawButton((92, 92, 92))
    
        if upgrade.bigBangUpgrade.level == 0 and currency.energy.amount >= upgrade.bigBangUpgrade.cost:
            button.bigBangButton.drawButton((92, 92, 92))
        elif upgrade.bigBangUpgrade.level >= 1:
            screen.gameScreen.blit(text.matterText.text, (0,50))
            button.shopButton.drawButton((92, 92, 92))
    elif menuVar.currentMenu == "shop":
        screen.gameScreen.blit(text.energyText.text, (0,0))
        screen.gameScreen.blit(text.matterText.text, (0,50))

        button.shopBackButton.drawButton((92, 92, 92))

        button.genEnergyUpgradeButton.drawButton((92, 92, 92))
        button.matterGenUpgradeButton.drawButton((92, 92, 92))
        button.genEnergyUpgradeBuffButton.drawButton((92, 92, 92))

menuVar = menu()