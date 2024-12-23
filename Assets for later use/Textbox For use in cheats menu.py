import pygame as pg

pg.init()
screen = pg.display.set_mode((1000, 1000))

class textBox:
    def __init__(self, xPos, yPos):
        self.textString = ""
        self.xPos = xPos
        self.yPos = yPos
        self.selected = False
        self.font = pg.font.Font("arial.ttf", 20)
        self.text = self.font.render(self.textString, True, (0, 0, 0))

        self.textBoxRect = self.text.get_rect()
        self.textBoxRect.height = self.text.get_height()
        self.textBoxRect.width = 150
        self.textBoxRect.x = xPos
        self.textBoxRect.y = yPos

        self.boarderRect = pg.Rect(0, 0, 0, 0)
        self.boarderRect.height = self.textBoxRect.height + 10
        self.boarderRect.width = 160
        self.boarderRect.x = xPos - 5
        self.boarderRect.y = yPos - 5
    
    def drawTextBox(self):
        if self.selected == True:
            pg.draw.rect(screen, (200, 200, 200), self.boarderRect)
        else:
            pg.draw.rect(screen, (92, 92, 92), self.boarderRect)
        pg.draw.rect(screen, (255, 255, 255), self.textBoxRect)
        screen.blit(self.text, (self.xPos, self.yPos))
    
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
            
def checkIfKeyPressed(event):
    shiftPressed = checkIfShiftPressed()
    if event.type == pg.KEYDOWN and event.key >= 97 and event.key <= 122:
        if shiftPressed == True:
            subAmount = 32
        else:
            subAmount = 0
        if test.selected == True:
            test.addTextToTextBox(chr(event.key - subAmount))
    elif event.type == pg.KEYDOWN and event.key >= 48 and event.key <= 57:
        if test.selected == True:
            test.addTextToTextBox(chr(event.key))
    if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
        if test.selected == True:
            test.delTextFromTextBox()

def eventCheck(running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if test.textBoxRect.collidepoint(event.pos):
                test.setSelected(True)

            if not test.textBoxRect.collidepoint(event.pos):
                test.setSelected(False)
        checkIfKeyPressed(event)   
    return running
    
def checkIfShiftPressed():
    pressedKeys = pg.key.get_pressed()
    if pressedKeys[pg.K_LSHIFT]:
        shiftPressed = True
    else:
        shiftPressed = False
    return shiftPressed

test = textBox(100, 100)

def main():
    running = True
    while running:
        test.drawTextBox()
        pg.display.update()
        running = eventCheck(running)
            
main()
pg.quit()