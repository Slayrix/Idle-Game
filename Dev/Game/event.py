import pygame as pg, menu, vars.listVars as listVars, vars.textBoxVars as textBoxVars

pgAlphabet = {
    pg.K_a: "a", 
    pg.K_b: "b", 
    pg.K_c: "c", 
    pg.K_d: "d", 
    pg.K_e: "e", 
    pg.K_f: "f", 
    pg.K_g: "g", 
    pg.K_h: "h", 
    pg.K_i: "i", 
    pg.K_j: "j", 
    pg.K_k: "k", 
    pg.K_l: "l", 
    pg.K_m: "m", 
    pg.K_n: "n", 
    pg.K_o: "o", 
    pg.K_p: "p", 
    pg.K_q: "q", 
    pg.K_r: "r", 
    pg.K_s: "s",  
    pg.K_t: "t", 
    pg.K_u: "u", 
    pg.K_v: "v", 
    pg.K_w: "w", 
    pg.K_x: "x", 
    pg.K_y: "y", 
    pg.K_z: "z"
}

pgNums = {
    pg.K_0: "0",
    pg.K_1: "1",
    pg.K_2: "2",
    pg.K_3: "3",
    pg.K_4: "4",
    pg.K_5: "5",
    pg.K_6: "6",
    pg.K_7: "7",
    pg.K_8: "8",
    pg.K_9: "9",
}

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
    if event.type == pg.KEYDOWN and event.key in pgAlphabet:
        return [True, pgAlphabet[event.key]]
    else:
        return False

def checkIfNumPressed(event):
    if event.type == pg.KEYDOWN and event.key in pgNums:
        return [True, pgNums[event.key]]
    else:
        return False

def checkIfShiftPressed():
    pressedKeys = pg.key.get_pressed()
    if pressedKeys[pg.K_LSHIFT]:
        shiftPressed = True
    else:
        shiftPressed = False
    return shiftPressed