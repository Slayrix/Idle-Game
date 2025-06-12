import pygame as pg, core.game as game, core.menu as menu, math, core.listVars as listVars, core.settings as settings

class buttonGroup:
    def __init__(self, activeMenu: list, xPos, yPos, width, height):
        listVars.buttonGroupList.list += [self]
        self.activeMenu = activeMenu
        self.refXPos = xPos
        self.refYPos = yPos
        self.refWidth = width
        self.refHeight = height
        self.calcXYPos()
        self.calcWH()
        self.buttonList = []
        self.createRect(self.xPos, self.yPos, self.width, self.height)

    def resizeButtonGroup(self):
        self.calcXYPos()
        self.calcWH()
        self.createRect(self.xPos, self.yPos, self.width, self.height)
    
    def addButtonToGroup(self, button):
        self.buttonList += [button]

    def calcXYPos(self):
        self.xPos = settings.resolutionScale[0] * self.refXPos
        self.yPos = settings.resolutionScale[1] * self.refYPos
    
    def calcWH(self):
        self.width = settings.resolutionScale[0] * self.refWidth
        self.height = settings.resolutionScale[1] * self.refHeight
    
    def createRect(self, xPos, yPos, width, height):
        self.rect = pg.Rect(xPos, yPos, width, height)
    
    def drawButtonGroup(self):
        pg.draw.rect(game.gameScreen, (140, 140, 140), self.rect)
    
    def showButtonGroup(self):
        for menuVar in self.activeMenu:
            if menuVar == menu.menuVar.currentMenu:
                self.calcButtonPos()
                self.drawButtonGroup()

    def calcButtonPos(self):
        x = self.xPos
        y = self.yPos + 10
        i = 0
        totalLineLength = 0
        biggestHeight = 0
        buttonPosList = []
        currentLineList = []
        while i <= len(self.buttonList) - 1:
            button = self.buttonList[i]
            if totalLineLength + button.rect.width < self.width:
                if button.rect.height > biggestHeight:
                    biggestHeight = button.rect.height
                currentLineList += [[x, y]]
                x += button.rect.width + 10
                totalLineLength += button.rect.width + 10
                i += 1
            else:
                offset = self.calcOffset(totalLineLength)
                currentLineList += [offset]
                buttonPosList += [currentLineList]
                currentLineList = []
                x = self.xPos
                y += biggestHeight + 10
                biggestHeight = 0
                totalLineLength = 0
        if totalLineLength != 0:
            offset = self.calcOffset(totalLineLength)
            currentLineList += [offset]
            buttonPosList += [currentLineList]
        self.applyPosOffset(buttonPosList)

    def calcOffset(self, totalLineLength):
        totalLineLength -= 10
        remainingSpace = self.width - totalLineLength
        return math.floor(remainingSpace/2)

    def applyPosOffset(self, buttonPosList):
        newButtonPosList = []
        for line in buttonPosList:
            offset = line[-1]
            line = line[:-1]
            tempList = []
            for cord in line:
                x = cord[0] + offset
                tempList += [[x, cord[1]]]
            newButtonPosList += tempList
        self.changeButtonPos(newButtonPosList)
    
    def changeButtonPos(self, newButtonPosList):
        i = 0
        for button in self.buttonList:
            pos = newButtonPosList[i]
            button.setSelfXYPosition(pos[0], pos[1])
            i += 1