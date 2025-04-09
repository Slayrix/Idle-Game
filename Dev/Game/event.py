import pygame as pg, menu, vars.listVars as listVars, vars.textBoxVars as textBoxVars, chars

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
    checkAlphabetList = checkIfletterPressed(event)
    checkNumList = checkIfNumPressed(event)
    if checkAlphabetList != False:
        if shiftPressed == True:
            checkAlphabetList[1] = checkAlphabetList[1].upper()
        if textBoxVars.cheatsTextBox.selected == True:
            textBoxVars.cheatsTextBox.addTextToTextBox(checkAlphabetList[1])
    if checkNumList != False:
        if textBoxVars.cheatsTextBox.selected == True:
            textBoxVars.cheatsTextBox.addTextToTextBox(checkNumList[1])
    if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
        if textBoxVars.cheatsTextBox.selected == True:
            textBoxVars.cheatsTextBox.delTextFromTextBox()

def checkIfletterPressed(event):
    if event.type == pg.KEYDOWN and event.key in chars.pgAlphabet:
        return [True, chars.pgAlphabet[event.key]]
    else:
        return False

def checkIfNumPressed(event):
    if event.type == pg.KEYDOWN and event.key in chars.pgNums:
        return [True, chars.pgNums[event.key]]
    else:
        return False

def checkIfShiftPressed():
    pressedKeys = pg.key.get_pressed()
    if pressedKeys[pg.K_LSHIFT]:
        shiftPressed = True
    else:
        shiftPressed = False
    return shiftPressed