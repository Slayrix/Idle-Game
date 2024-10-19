import pygame as pg

pg.init()

screen = pg.display.set_mode((1000, 1000))

class button():
    def __init__(self, textList: list, textColor, xPos, yPos):
        self.font = pg.font.Font("arial.ttf", 30)
        self.lineVarList = []
        widthList = []
        height = 0
        i = 0
        for e in textList:
            self.lineVarList += [self.font.render(textList[i], True, textColor)]
            if i == 0:
                self.rect = self.lineVarList[i].get_rect()
            widthList += [self.lineVarList[i].get_width()]
            height += self.lineVarList[i].get_height()
            i += 1
        self.rect.width = max(widthList)
        self.rect.height = height
        self.rect.x = xPos
        self.rect.y = yPos
    
    def drawButton(self, buttonColor):
        pg.draw.rect(screen, buttonColor, self.rect)
        widthL = []
        for e in self.lineVarList:
            widthL += [e.get_width()]
        yOffset = 0
        for e in self.lineVarList:
            if e.get_width() == max(widthL):
                screen.blit(e, (self.rect.x, self.rect.y + yOffset))
                yOffset += e.get_height()
            else:
                screen.blit(e, (self.rect.x + (max(widthL) / 2) - (e.get_width() / 2), self.rect.y + yOffset))
                yOffset += e.get_height()
        



button1 = button(["111", "123412", "123"], (255, 255, 255), 100, 100)
button1.drawButton((92, 92, 92))









pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()