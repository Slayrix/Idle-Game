import pygame as pg, core.listVars as listVars, core.game as game

class infobox:
    def __init__(self, textList, textColor, updateTextList = None):
        pg.font.init()
        listVars.infoboxList.list += [self]
        self.font = pg.font.Font("arial.ttf", 30)
        self.textList = textList
        self.textColor = textColor
        self.setInfobox()
        self.setInfoboxXYPosition(10000, 10000)
        self.updateTextList = updateTextList
    
    def setInfobox(self):
        #Creates infobox rect and calculates the width and height of the infobox
        self.lineVarList = []
        widthList = []
        height = 0
        i = 0
        for e in self.textList:
            self.lineVarList += [self.font.render(self.textList[i], True, self.textColor)]
            if i == 0:
                self.rect = self.lineVarList[i].get_rect()
            widthList += [self.lineVarList[i].get_width()]
            height += self.lineVarList[i].get_height()
            i += 1
        self.rect.width = max(widthList)
        self.rect.height = height

    def setInfoboxXYPosition(self, xPos, yPos):
        self.rect.x = xPos
        self.rect.y = yPos
    
    def drawInfobox(self, buttonColor):
        #Draws the textbox to the screen
        self.setPosToMouseCursor()
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
    
    def setPosToMouseCursor(self):
        mousePos = pg.mouse.get_pos()
        self.setInfoboxXYPosition(mousePos[0] + 10, mousePos[1] + 20)
    
    def updateText(self, text: str, line: int):
        self.textList[line] = text
        self.setInfobox()
    
    def checkUpdateText(self):
        #Checks to see if any of the button text needs to be updated
        if self.updateTextList != None:
            for lineList in self.updateTextList:
                strVar = ""
                for element in lineList:
                    if type(element) == int:
                        self.updateText(strVar, element)
                    else:
                        for i in element:
                            if type(i) == list:
                                objVar = i[0]
                                strVar += str(getattr(objVar, i[1]))
                            else:
                                strVar += i
        else:
            return