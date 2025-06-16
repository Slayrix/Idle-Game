import pygame as pg, core.chars as chars, core.listVars as listVars

quitGame = False

def eventCheck(running):
    for event in pg.event.get():
        running = checkIfQuit(event, running)
        mouseClickCheck(event)
        checkIfKeyPressed(event)
    return running

def checkIfQuit(event, running):
    if event.type == pg.QUIT or quitGame == True:
        running = False
    return running

def mouseClickCheck(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        checkIfButtonClicked(event)
        
def checkIfButtonClicked(event):
    for buttonVar in listVars.buttonList.list:
        if buttonVar.rect.collidepoint(event.pos):
            buttonVar.buttonClicked()

    for object in listVars.objectList.list:
        if object[1] == "textBox":
            textBoxVar = object[0]
            textBoxVar.textBoxSetSelected(event)

def checkIfKeyPressed(event):
    shiftPressed = checkIfShiftPressed()
    checkAlphabetList = checkIfletterPressed(event)
    checkNumList = checkIfNumPressed(event)
    for object in listVars.objectList.list:
        if object[1] == "textBox":
            textBoxVar = object[0]
            if checkAlphabetList != False:
                textBoxVar.textBoxLetterPressed(shiftPressed, checkAlphabetList)
            if checkNumList != False:
                textBoxVar.textBoxNumPressed(checkNumList)
            if checkIfBackspacePressed(event) == True:
                textBoxVar.textBoxDelChar()

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

def checkIfBackspacePressed(event):
    if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
        return True
    else:
        return False