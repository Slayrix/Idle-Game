import pygame as pg, core.game as game, core.menu as menu, core.listVars as listVars, operations as op

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
        strVar = ""
        if self.updateTextList != None:
            for i in self.updateTextList:
                if type(i) == list:
                    objVar = i[0]
                    strVar += str(getattr(objVar, i[1]))
                else:
                    strVar += i
            self.setText(strVar)
            
    def showText(self):
        for menuVar in self.activeMenu:
            if menuVar == menu.menuVar.currentMenu:
                conditions = self.drawConditions
                if conditions != None:
                    objVar = conditions[0]
                    attrVal = getattr(objVar, conditions[1])
                    if op.ops[conditions[2]](attrVal, conditions[3]) == True:
                        self.drawText()
                else:
                    self.drawText()