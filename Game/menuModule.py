class menu:
    def __init__(self):
        self.currentMenu = "defaultMenu"
    
    def setCurrentMenuToDefaultMenu(self):
        self.currentMenu = "defaultMenu"

    def setCurrentMenuToShop(self):
        self.currentMenu = "shop"

def displayMenu(menuVar, screen, textList, buttonList, upgradeList, currencyList):
    energyText = textList[0]
    matterText = textList[1]

    genButton = buttonList[0]
    bigBangButton = buttonList[1]
    shopButton = buttonList[2]
    shopBackButton = buttonList[3]
    genEnergyUpgradeButton = buttonList[4]
    matterGenUpgradeButton = buttonList[5]
    genEnergyUpgradeBuffButton = buttonList[6]

    bigBangUpgrade = upgradeList[0]

    energy = currencyList[0]
    if menuVar.currentMenu == "defaultMenu":
        screen.blit(energyText.text, (0,0))

        genButton.drawButton((92, 92, 92))
    
        if bigBangUpgrade.level == 0 and energy.amount >= bigBangUpgrade.cost:
            bigBangButton.drawButton((92, 92, 92))
        elif bigBangUpgrade.level >= 1:
            screen.blit(matterText.text, (0,50))
            shopButton.drawButton((92, 92, 92))
    elif menuVar.currentMenu == "shop":
        screen.blit(energyText.text, (0,0))
        screen.blit(matterText.text, (0,50))

        shopBackButton.drawButton((92, 92, 92))

        genEnergyUpgradeButton.drawButton((92, 92, 92))
        matterGenUpgradeButton.drawButton((92, 92, 92))
        genEnergyUpgradeBuffButton.drawButton((92, 92, 92))

