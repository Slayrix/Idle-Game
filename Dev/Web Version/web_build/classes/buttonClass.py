import pygame as pg, game, menu, vars.listVars as listVars, classes.buttonGroupClass as buttonGroupClass, operations as op, buttonFunctionality

class button:
    def __init__(self, textList, activeMenuList: list, textColor, xPos, yPos, buttonGroup: buttonGroupClass.buttonGroup, buttonFunctionality: list, drawConditions: list = None, updateTextList: list = None):
        pg.font.init()
        listVars.buttonList.list += [self]
        self.font = pg.font.Font("arial.ttf", 30)
        self.textList = textList
        self.textColor = textColor
        self.xPos = xPos
        self.yPos = yPos
        self.setButton()
        self.setButtonXYPosition(10000, 10000)
        self.activeMenu = activeMenuList
        self.drawConditions = drawConditions
        self.buttonFunctionality = buttonFunctionality
        self.updateTextList = updateTextList
        self.visible = False
        if buttonGroup != None:
            buttonGroup.addButtonToGroup(self)

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
    
    def buttonClicked(self):
        #Functionality of the buttons
        if self.visible == True:
            buttonFunction = self.buttonFunctionality[0]
            buttonFunctionVars = self.buttonFunctionality[1:]
            buttonFunctionality.buttonFunctionality[buttonFunction](buttonFunctionVars)