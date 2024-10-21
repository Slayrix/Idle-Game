import pygame as pg

pg.init()

class text:
    def __init__(self):
        self.font = pg.font.Font("arial.ttf", 30)
    
    def setText(self, text: str, textColor, backgroundColor = None):
        self.text = self.font.render(text, True, textColor, backgroundColor)

energyText = text()
matterText = text()