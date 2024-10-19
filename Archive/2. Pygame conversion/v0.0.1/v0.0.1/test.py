import pygame as pg

pg.init()
screen = pg.display.set_mode((500, 500))

class text:
    def __init__(self):
        self.font = pg.font.SysFont('arial', 30)
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)

class button:
    def __init__(self):
        self.font = pg.font.SysFont('arial', 30)
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)
    
    def setButton(self, x, y):
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y

currency = 0
currencyText = text()
currencyText.setText("Currency: " + str(currency), (255, 255, 255))

genButton = button()
genButton.setText("Click to gen", (255, 255, 255), (92, 92, 92))
genButton.setButton(100, 50)

def updateScreen():
    screen.fill((0, 0, 0))

    screen.blit(genButton.text, genButton.rect)
    screen.blit(currencyText.text, (0,0))

    pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if genButton.rect.collidepoint(event.pos):
                currency += 1
                currencyText.setText("Currency: " + str(currency), (255, 255, 255))
    updateScreen()

pg.quit()