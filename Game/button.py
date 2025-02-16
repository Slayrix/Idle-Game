import pygame as pg
import game, upgrade, listClass, menu, currency, buttonGroup

class button:
    def __init__(self, textList, activeMenuList: list, textColor, xPos, yPos, buttonGroup: buttonGroup, buttonFunctionality: list, drawConditions: list = None, updateTextList: list = None):
        pg.font.init()
        self.font = pg.font.Font("arial.ttf", 30)
        self.lineVarList = []
        self.xPos = xPos
        self.yPos = yPos
        self.setButton(textList, textColor)
        self.activeMenu = activeMenuList
        buttonList.list += [self]
        self.drawConditions = drawConditions
        self.buttonFunctionality = buttonFunctionality
        self.updateTextList = updateTextList
        self.visible = False
        if buttonGroup != None:
            buttonGroup.addButtonToGroup(self)

    def setButton(self, textList: list, textColor):
        #Creates button rect and calculates the width and height of the button
        self.textColor = textColor
        widthList = []
        height = 0
        i = 0
        for e in textList:
            self.lineVarList += [self.font.render(textList[i], True, self.textColor)]
            if i == 0:
                self.rect = self.lineVarList[i].get_rect()
            widthList += [self.lineVarList[i].get_width()]
            height += self.lineVarList[i].get_height()
            i += 1
        self.rect.width = max(widthList)
        self.rect.height = height
        self.setButtonXYPosition(10000, 10000)

    def setSelfXYPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def setButtonXYPosition(self, xPos, yPos):
        self.rect.x = xPos
        self.rect.y = yPos
    
    def drawButton(self, buttonColor):
        #Draws the button to the screen
        self.setButtonXYPosition(self.xPos, self.yPos)
        pg.draw.rect(game.gameScreen, buttonColor, self.rect)
        widthL = []
        for e in self.lineVarList:
            widthL += [e.get_width()]
        yOffset = 0
        for e in self.lineVarList:
            if e.get_width() == max(widthL):
                game.gameScreen.blit(e, (self.rect.x, self.rect.y + yOffset))
                yOffset += e.get_height()
            else:
                game.gameScreen.blit(e, (self.rect.x + (max(widthL) / 2) - (e.get_width() / 2), self.rect.y + yOffset))
                yOffset += e.get_height()
    
    def updateText(self, text: str, line: int):
        self.lineVarList[line] = self.font.render(text, True, self.textColor)

    def checkUpdateText(self):
        #Checks to see if any of the button text needs to be updated
        if self.updateTextList == None:
            return
        else:
            for listElement in self.updateTextList:
                strVar = ""
                for element in listElement:
                    if type(element) == int:
                        self.updateText(strVar, element)
                    else:
                        for i in element:
                            if type(i) == list:
                                upgradeVar = i[0]
                                if i[1] == "increaseGenPerSecondAmount":
                                    strVar += str(upgradeVar.increaseGenPerSecondAmount)
                                elif i[1] == "cost":
                                    strVar += str(upgradeVar.cost)
                            else:
                                strVar += i

    def showButton(self):
        #Checks to see if the button should be drawn
        showButton = False
        for menuVar in self.activeMenu:
            if menuVar == menu.menuVar.currentMenu:
                conditions = self.drawConditions
                if conditions == None:
                    showButton = True
                else:
                    objVar = conditions[0]
                    if conditions[1] == "level":
                        if conditions[2] == "=":
                            if objVar.level == conditions[3]:
                                showButton = True
                        elif conditions[2] == ">":
                            if objVar.level > conditions[3]:
                                showButton = True
            else:
                showButton = False
        if showButton == True:
            self.drawButton((92, 92, 92))
            self.visible = True
        else:
            self.setButtonXYPosition(10000, 10000)
            self.visible = False
    
    def buttonClicked(self):
        #Functionality of the buttons
        if self.visible == True:
            if self.buttonFunctionality[0] == "genCurrency":
                upgradeVar = self.buttonFunctionality[2]
                upgradeVar.addAmount(self.buttonFunctionality[1])
            elif self.buttonFunctionality[0] == "changeMenu":
                if self.buttonFunctionality[1] == "default":
                    menu.menuVar.setCurrentMenuToDefaultMenu()
                elif self.buttonFunctionality[1] == "shop":
                    menu.menuVar.setCurrentMenuToShop()
                elif self.buttonFunctionality[1] == "cheats":
                    menu.menuVar.setCurrentMenuToCheats()
            elif self.buttonFunctionality[0] == "buyUpdrade":
                upgrade.buyUpgrade(self.buttonFunctionality[1])

buttonList = listClass.list()

energyCheatButton = button(["Add Energy"], ["cheats"], (255, 255, 255), 50, 200, buttonGroup.cheatsButtonGroup, [0])
matterCheatButton = button(["Add Matter"], ["cheats"], (255, 255, 255), 250, 200, buttonGroup.cheatsButtonGroup, [0])

genButton = button(["Click to gen"], ["defaultMenu"], (255, 255, 255), 150, 100, None, ["genCurrency", 1, currency.energy])
shopButton = button(["Shop"], ["defaultMenu"], (255, 255, 255), 150, 150, None, ["changeMenu", "shop"], [upgrade.bigBangUpgrade, "level", ">", 0])
shopBackButton = button(["Back"], ["shop"], (255, 255, 255), 150, 150, None, ["changeMenu", "default"])
bigBangButton = button(["Start Big Bang", str(upgrade.bigBangUpgrade.cost) + " Energy"], ["defaultMenu"], (255, 255, 255), 150, 150, None, ["buyUpdrade", upgrade.bigBangUpgrade], [upgrade.bigBangUpgrade, "level", "=", 0])
genEnergyUpgradeButton = button(["Upgrade 1", "Auto gen +" + str(upgrade.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", str(upgrade.genEnergyUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 150, 230, None, ["buyUpdrade", upgrade.genEnergyUpgrade], None, [[["Auto gen +", [upgrade.genEnergyUpgrade, "increaseGenPerSecondAmount"], " energy per second per upgrade"], 1], [[[upgrade.genEnergyUpgrade, "cost"], " Matter"], 2]])
matterGenUpgradeButton = button(["Double Matter Generation", "Increases energy consumption by +10", str(upgrade.matterGenUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 150, 350, None, ["buyUpdrade", upgrade.matterGenUpgrade], None, [[[[upgrade.matterGenUpgrade, "cost"], " Matter"], 2]])
genEnergyUpgradeBuffButton = button(["Double Energy Generation of Upgrade 1", str(upgrade.genEnergyUpgradeBuff.cost) + " Matter"], ["shop"], (255, 255, 255), 150, 470, None, ["buyUpdrade", upgrade.genEnergyUpgradeBuff])
cheatsMenuButton = button(["Open Cheats Menu"], ["defaultMenu"], (255, 255, 255), 100, 300, None, ["changeMenu", "cheats"])
cheatsBackButton = button(["Go Back"], ["cheats"], (255, 255, 255), 100, 300, None, ["changeMenu", "default"])