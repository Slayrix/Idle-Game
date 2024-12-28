import pygame as pg
import game, upgrade, list

class button:
    def __init__(self, textList, activeMenuList: list, textColor, xPos, yPos, name, drawConditions: list = None):
        self.font = pg.font.Font("arial.ttf", 30)
        self.lineVarList = []
        self.setButton(textList, textColor, xPos, yPos)
        self.activeMenu = activeMenuList
        buttonList.list += [self]
        self.drawConditions = drawConditions

        self.name = name

    def setButton(self, textList: list, textColor, xPos: int, yPos: int):
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
        self.rect.x = xPos
        self.rect.y = yPos
    
    def drawButton(self, buttonColor):
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
    
    def showButton(self):
        conditions = self.drawConditions
        if conditions == None:
            return True
        else:
            val = False
            objVar = conditions[0]
            if conditions[1] == "level":
                if conditions[2] == "=":
                    if objVar.level == conditions[3]:
                        val = True
                elif conditions[2] == ">":
                    if objVar.level > conditions[3]:
                        val = True
                if val == True:
                    return True
                else:
                    return False

buttonList = list.list()

genButton = button(["Click to gen"], ["defaultMenu"], (255, 255, 255), 150, 100, "genButton")
shopButton = button(["Shop"], ["defaultMenu"], (255, 255, 255), 150, 150, "shopButton", [upgrade.bigBangUpgrade, "level", ">", 0])
shopBackButton = button(["Back"], ["shop"], (255, 255, 255), 100, 100, "shopBackButton")
bigBangButton = button(["Start Big Bang", str(upgrade.bigBangUpgrade.cost) + " Energy"], ["defaultMenu"], (255, 255, 255), 150, 150, "bigBangButton", [upgrade.bigBangUpgrade, "level", "=", 0])
genEnergyUpgradeButton = button(["Upgrade 1", "Auto gen +" + str(upgrade.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", str(upgrade.genEnergyUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 150, 230, "genEnergyUpgradeButton")
matterGenUpgradeButton = button(["Double Matter Generation", "Increases energy consumption by +10", str(upgrade.matterGenUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 150, 350, "matterGenUpgradeButton")
genEnergyUpgradeBuffButton = button(["Double Energy Generation of Upgrade 1", str(upgrade.genEnergyUpgradeBuff.cost) + " Matter"], ["shop"], (255, 255, 255), 150, 470, "genEnergyUpgradeBuffButton")
cheatsMenuButton = button(["Open Cheats Menu"], ["defaultMenu"], (255, 255, 255), 100, 400, "cheatsMenuButton")
cheatsBackButton = button(["Go Back"], ["cheats"], (255, 255, 255), 100, 400, "cheatsBackButton")