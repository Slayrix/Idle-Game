import pygame as pg
import upgrade, game, menu, currency, listVars

pg.init()

class text:
    def __init__(self, activeMenuList, textColor, xPos, yPos, updateTextList: list = None, drawConditions: list = None):
        self.font = pg.font.Font("arial.ttf", 30)
        self.activeMenu = activeMenuList
        self.textColor = textColor
        self.drawConditions = drawConditions
        self.xPos = xPos
        self.yPos = yPos
        listVars.textList.list += [self]
        self.updateTextList = updateTextList
    
    def setText(self, text: str, backgroundColor = None):
        self.text = self.font.render(text, True, self.textColor, backgroundColor)

    def drawText(self):
        game.gameScreen.blit(self.text, (self.xPos, self.yPos))
    
    def checkUpdateText(self):
        if self.updateTextList == None:
            return
        else:
            strVar = ""
            for e in self.updateTextList:
                if type(e) == list:
                    currencyVar = e[0]
                    if e[1] == "amount":
                        strVar += str(currencyVar.amount)
                else:
                    strVar += e
            self.setText(strVar)
            
    def showText(self):
        for menuVar in self.activeMenu:
            if menuVar == menu.menuVar.currentMenu:
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
        return False

energyText = text(["defaultMenu", "shop", "cheats"], (255, 255, 255), 0, 0, ["Energy ", [currency.energy, "amount"]])
matterText = text(["defaultMenu", "shop", "cheats"], (255, 255, 255), 0, 50, ["Matter ", [currency.matter, "amount"]], [upgrade.bigBangUpgrade, "level", ">", 0])