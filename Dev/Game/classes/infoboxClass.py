import pygame as pg, core.listVars as listVars, core.game as game, core.settings as settings

class infobox:
    def __init__(self, textList, textColor, updateTextList = None):
        pg.font.init()
        listVars.infoboxList.list += [self]
        self.draw = False
        self.font = pg.font.Font("arial.ttf", settings.infoboxFontSize)
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
        self.borderRect = pg.Rect(0,0,0,0)
        self.borderRect.width = max(widthList) + 4
        self.borderRect.height = height + 4

    def setInfoboxXYPosition(self, xPos, yPos):
        self.rect.x = xPos
        self.rect.y = yPos
        self.borderRect.x = xPos - 2
        self.borderRect.y = yPos - 2
    
    def showInfobox(self, showVal):
        if showVal == True:
            self.draw = True
        else:
            self.draw = False
            self.setInfoboxXYPosition(10000, 10000)

    def drawInfobox(self, buttonColor):
        #Draws the textbox to the screen
        if self.draw == True:
            self.setPosToMouseCursor()
            pg.draw.rect(game.gameScreen, (30,30,30), self.borderRect)
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
        infoboxPos = self.checkIfInfoboxInWindow(mousePos)
        self.setInfoboxXYPosition(infoboxPos[0], infoboxPos[1])

    def checkIfInfoboxInWindow(self, mousePos):
        maxX = mousePos[0] + self.borderRect.width + 10
        maxY = mousePos[1] + self.borderRect.height + 20
        maxXInWindow = self.checkPos(maxX, settings.resolution[0])
        maxYInWindow = self.checkPos(maxY, settings.resolution[1])
        if maxXInWindow == True:
            if maxYInWindow == True:
                return (mousePos[0] + 10, mousePos[1] + 20)
            else:
                y = settings.resolution[1] - self.borderRect.height
                return (mousePos[0] + 10, y)
        else:
            x = settings.resolution[0] - self.borderRect.width
            return (x, mousePos[1] + 20)
    
    def checkPos(self, pos, resolutionVal):
        if pos < resolutionVal:
            return True
        else:
            return False
        
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