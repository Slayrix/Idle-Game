import pygame as pg, menu, vars.listVars as listVars, vars.textBoxVars as textBoxVars

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
    for buttonVar in listVars.buttonList.list:
        if buttonVar.rect.collidepoint(event.pos):
            buttonVar.buttonClicked()
    
    if menu.menuVar.currentMenu == "cheats":
        if textBoxVars.cheatsTextBox.textBoxRect.collidepoint(event.pos):
            textBoxVars.cheatsTextBox.setSelected(True)
        elif not textBoxVars.cheatsTextBox.textBoxRect.collidepoint(event.pos):
            textBoxVars.cheatsTextBox.setSelected(False)

def checkIfKeyPressed(event):
    shiftPressed = checkIfShiftPressed()
    if event.type == pg.KEYDOWN and event.key >= 97 and event.key <= 122:
        if shiftPressed == True:
            subAmount = 32
        else:
            subAmount = 0
        if textBoxVars.cheatsTextBox.selected == True:
            textBoxVars.cheatsTextBox.addTextToTextBox(chr(event.key - subAmount))
    elif event.type == pg.KEYDOWN and event.key >= 48 and event.key <= 57:
        if textBoxVars.cheatsTextBox.selected == True:
            textBoxVars.cheatsTextBox.addTextToTextBox(chr(event.key))
    if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
        if textBoxVars.cheatsTextBox.selected == True:
            textBoxVars.cheatsTextBox.delTextFromTextBox()

def checkIfShiftPressed():
    pressedKeys = pg.key.get_pressed()
    if pressedKeys[pg.K_LSHIFT]:
        shiftPressed = True
    else:
        shiftPressed = False
    return shiftPressed