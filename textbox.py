import pygame as pg

pg.init()
screen = pg.display.set_mode((1000, 1000))

class textBox:
    def __init__(self, xPos, yPos):
        self.font = pg.font.Font("arial.ttf", 20)
        self.text = self.font.render("", True, (0, 0, 0))

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
        pg.draw.rect(screen, (92, 92, 92), self.boarderRect)
        pg.draw.rect(screen, (255, 255, 255), self.textBoxRect)
    
    def isSelected(self):
        pass
test = textBox(100, 100)
test.drawTextBox()

pg.display.update()

def checkIfKeyPressed(event):
    shiftPressed = checkIfShiftPressed()
    if event.type == pg.KEYDOWN and event.key >= 97 and event.key <= 122:
            if shiftPressed == True:
                subAmount = 32
            else:
                subAmount = 0
            print(chr(event.key - subAmount))

def eventCheck(running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if test.textBoxRect.collidepoint(event.pos):
                test.isSelected()
        checkIfKeyPressed(event)   
    return running
    
def checkIfShiftPressed():
    pressedKeys = pg.key.get_pressed()
    if pressedKeys[pg.K_LSHIFT]:
        shiftPressed = True
    else:
        shiftPressed = False
    return shiftPressed

def main():
    running = True
    while running:
        running = eventCheck(running)
            
main()
pg.quit()