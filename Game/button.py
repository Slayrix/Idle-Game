import pygame as pg
import game, upgrade

class button:
    def __init__(self, textList, textColor, xPos, yPos):
        self.font = pg.font.Font("arial.ttf", 30)
        self.lineVarList = []
        self.setButton(textList, textColor, xPos, yPos)

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

def createButtons(buttonVarList):
    for buttonList in buttonVarList:
        buttonVar = buttonList[0]
        buttonVar.setButton(*buttonList[1])

genButton = button(["Click to gen"], (255, 255, 255), 150, 100)
shopButton = button(["Shop"], (255, 255, 255), 150, 150)
shopBackButton = button(["Back"], (255, 255, 255), 100, 100)
bigBangButton = button(["Start Big Bang", str(upgrade.bigBangUpgrade.cost) + " Energy"], (255, 255, 255), 150, 150)
genEnergyUpgradeButton = button(["Upgrade 1", "Auto gen +" + str(upgrade.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", str(upgrade.genEnergyUpgrade.cost) + " Matter"], (255, 255, 255), 150, 230)
matterGenUpgradeButton = button(["Double Matter Generation", "Increases energy consumption by +10", str(upgrade.matterGenUpgrade.cost) + " Matter"], (255, 255, 255), 150, 350)
genEnergyUpgradeBuffButton = button(["Double Energy Generation of Upgrade 1", str(upgrade.genEnergyUpgradeBuff.cost) + " Matter"], (255, 255, 255), 150, 470)