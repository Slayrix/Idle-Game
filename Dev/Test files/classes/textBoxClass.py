import pygame as pg, core.game as game, core.listVars as listVars, core.menu as menu, core.settings as settings

class textBox:
    def __init__(self, xPos, yPos):
        pg.font.init()
        self.font = pg.font.Font("arial.ttf", settings.fontSize)
        listVars.objectList.list += [[self, "textBox"]]
        self.textString = ""
        self.refXPos = xPos
        self.refYPos = yPos
        self.selected = False
        self.text = self.font.render(self.textString, True, (0, 0, 0))

        self.textBoxRect = self.text.get_rect()
        self.textBoxRect.height = self.text.get_height()
        self.textBoxRect.width = 150 * settings.resolutionScale[0]
        self.calcXYPos()
        self.textBoxRect.x = self.xPos
        self.textBoxRect.y = self.yPos

        self.boarderRect = pg.Rect(0, 0, 0, 0)
        self.boarderRect.height = self.textBoxRect.height + (10 * settings.resolutionScale[0])
        self.boarderRect.width = 160 * settings.resolutionScale[0]
        self.boarderRect.x = self.xPos - (self.boarderRect.width - self.textBoxRect.width)/2
        self.boarderRect.y = self.yPos - (self.boarderRect.height - self.textBoxRect.height)/2
    
    def calcXYPos(self):
        self.xPos = (self.refXPos * settings.resolutionScale[0]) - (self.textBoxRect.width/2)
        self.yPos = (self.refYPos * settings.resolutionScale[1]) - (self.textBoxRect.height/2)

    def drawTextBox(self):
        if self.selected == True:
            pg.draw.rect(game.gameScreen, (200, 200, 200), self.boarderRect)
        else:
            pg.draw.rect(game.gameScreen, (92, 92, 92), self.boarderRect)
        pg.draw.rect(game.gameScreen, (255, 255, 255), self.textBoxRect)
        game.gameScreen.blit(self.text, (self.xPos, self.yPos))
    
    def setSelected(self, bool):
        self.selected = bool
    
    def addTextToTextBox(self, c):
        if self.text.get_width() < self.textBoxRect.width - 10:
            self.textString += c
            self.text = self.font.render(self.textString, True, (0, 0, 0))
    
    def delTextFromTextBox(self):
        if len(self.textString) > 0:
            self.textString = self.textString[0:len(self.textString) - 1]
            self.text = self.font.render(self.textString, True, (0, 0, 0))
    
    def textBoxLetterPressed(self, shiftPressed, checkAlphabetList):
        if shiftPressed == True:
            checkAlphabetList[1] = checkAlphabetList[1].upper()
        for object in listVars.objectList.list:
            if object[1] == "textBox":
                textBoxVar = object[0]
                if textBoxVar.selected == True:
                    textBoxVar.addTextToTextBox(checkAlphabetList[1])

    def textBoxNumPressed(self, checkNumList):
        for object in listVars.objectList.list:
            if object[1] == "textBox":
                textBoxVar = object[0]
                if textBoxVar.selected == True:
                    textBoxVar.addTextToTextBox(checkNumList[1])

    def textBoxDelChar(self):
        for object in listVars.objectList.list:
            if object[1] == "textBox":
                textBoxVar = object[0]
                if textBoxVar.selected == True:
                    textBoxVar.delTextFromTextBox()
    
    def textBoxSetSelected(self, event):
        if menu.menuVar.currentMenu == "cheats":
            if self.textBoxRect.collidepoint(event.pos):
                self.setSelected(True)
            elif not self.textBoxRect.collidepoint(event.pos):
                self.setSelected(False)
    
    def drawTextBoxCheck(self):
        if menu.menuVar.currentMenu == "cheats":
            self.drawTextBox()
    
    def textBoxAddCurrency(self, currencyVar):
        try:
            amount = int(self.textString)
            currencyVar.addAmount(amount)
        except ValueError:
            pass