import pygame as pg
import list, upgrade, game

pg.init()

class text:
    def __init__(self, activeMenuList, xPos, yPos, drawConditions: list = None):
        self.font = pg.font.Font("arial.ttf", 30)
        self.activeMenu = activeMenuList
        self.drawConditions = drawConditions
        self.xPos = xPos
        self.yPos = yPos
        textList.list += [self]
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)

    def drawText(self):
        game.gameScreen.blit(self.text, (self.xPos, self.yPos))

    def showText(self):
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

textList = list.list()

energyText = text(["defaultMenu", "shop", "cheats"], 0, 0)
matterText = text(["defaultMenu", "shop", "cheats"], 0, 50, [upgrade.bigBangUpgrade, "level", ">", 0])