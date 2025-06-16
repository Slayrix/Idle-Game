import pygame as pg, core.game as game, core.menu as menu, core.listVars as listVars, classes.buttonGroupClass as buttonGroupClass, operations as op, buttonFunctionality, core.settings as settings

class button:
    def __init__(self, textList, activeMenuList: list, textColor, xPos, yPos, buttonGroup: buttonGroupClass.buttonGroup, buttonFunctionality: list, drawConditions: list = None, updateTextList: list = None, infoboxVar = None):
        pg.font.init()
        listVars.buttonList.list += [self]
        self.font = pg.font.Font("arial.ttf", settings.fontSize)
        self.textList = textList
        self.textColor = textColor
        self.refXPos = xPos
        self.refYPos = yPos
        self.setButton()
        self.calcXYPos()
        self.setButtonXYPosition(10000, 10000)
        self.infoboxVar = infoboxVar
        self.activeMenu = activeMenuList
        self.drawConditions = drawConditions
        self.buttonFunctionality = buttonFunctionality
        self.updateTextList = updateTextList
        self.visible = False
        if buttonGroup != None:
            buttonGroup.addButtonToGroup(self)
    
    def resizeButton(self):
        self.font = pg.font.Font("arial.ttf", settings.fontSize)
        self.setButton()
        self.calcXYPos()
        
    def calcXYPos(self):
        self.xPos = (settings.resolutionScale[0] * self.refXPos) - (self.rect.width/2)
        self.yPos = (settings.resolutionScale[1] * self.refYPos) - (self.rect.height/2)

    def setButton(self):
        #Creates button rect and calculates the width and height of the button
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
        self.textList[line] = text
        self.setButton()

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
    
    def checkIfMouseIsOverButton(self):
        mousePos = pg.mouse.get_pos()
        return self.rect.collidepoint(mousePos[0], mousePos[1])

    def showButton(self):
        #Checks to see if the button should be drawn
        showButton = False
        for menuVar in self.activeMenu:
            if menuVar == menu.menuVar.currentMenu:
                conditions = self.drawConditions
                if conditions != None:
                    objVar = conditions[0]
                    attrVal = getattr(objVar, conditions[1])
                    if op.ops[conditions[2]](attrVal, conditions[3]) == True:
                        showButton = True
                else:
                    showButton = True
            else:
                showButton = False
        if showButton == True:
            self.drawButton((92, 92, 92))
            self.visible = True
        else:
            self.setButtonXYPosition(10000, 10000)
            self.visible = False
            
        if self.infoboxVar != None:
            if self.checkIfMouseIsOverButton() == True and showButton == True:
                self.infoboxVar.showInfobox(True)
            else:
                self.infoboxVar.showInfobox(False)
    
    def buttonClicked(self):
        #Functionality of the buttons
        if self.visible == True:
            if len(self.buttonFunctionality) > 1:
                buttonFunction = self.buttonFunctionality[0]
                buttonFunctionVars = self.buttonFunctionality[1:]
                buttonFunctionality.buttonFunctionality[buttonFunction](buttonFunctionVars)
            else:
                buttonFunction = self.buttonFunctionality[0]
                buttonFunctionality.buttonFunctionality[buttonFunction]()