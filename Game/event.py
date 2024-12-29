import pygame as pg
import menu, button, cheats

def eventCheck(running):
    for event in pg.event.get():
        running = checkIfQuit(event, running)
        mouseClickCheck(event)
        checkIfKeyPressed(event)
    return running

def checkIfQuit(event, running):
    if event.type == pg.QUIT:
        running = False
    return running

def mouseClickCheck(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        checkIfButtonClicked(event)
        
def checkIfButtonClicked(event):
    for buttonVar in button.buttonList.list:
        if buttonVar.rect.collidepoint(event.pos):
            buttonVar.buttonClicked()

    if menu.menuVar.currentMenu == "cheats":
        if cheats.cheatsTextBox.textBoxRect.collidepoint(event.pos):
            cheats.cheatsTextBox.setSelected(True)
        elif not cheats.cheatsTextBox.textBoxRect.collidepoint(event.pos):
            cheats.cheatsTextBox.setSelected(False)
        if button.cheatsBackButton.rect.collidepoint(event.pos):
            menu.menuVar.setCurrentMenuToDefaultMenu()

def checkIfKeyPressed(event):
    shiftPressed = checkIfShiftPressed()
    if event.type == pg.KEYDOWN and event.key >= 97 and event.key <= 122:
        if shiftPressed == True:
            subAmount = 32
        else:
            subAmount = 0
        if cheats.cheatsTextBox.selected == True:
            cheats.cheatsTextBox.addTextToTextBox(chr(event.key - subAmount))
    elif event.type == pg.KEYDOWN and event.key >= 48 and event.key <= 57:
        if cheats.cheatsTextBox.selected == True:
            cheats.cheatsTextBox.addTextToTextBox(chr(event.key))
    if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
        if cheats.cheatsTextBox.selected == True:
            cheats.cheatsTextBox.delTextFromTextBox()

def checkIfShiftPressed():
    pressedKeys = pg.key.get_pressed()
    if pressedKeys[pg.K_LSHIFT]:
        shiftPressed = True
    else:
        shiftPressed = False
    return shiftPressed