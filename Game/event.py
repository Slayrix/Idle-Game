import pygame as pg
import menu, upgrade, button, game, cheats

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
    if menu.menuVar.currentMenu == "defaultMenu":
        if button.shopButton.rect.collidepoint(event.pos) and upgrade.bigBangUpgrade.level >= 1:
            menu.menuVar.setCurrentMenuToShop()

        if button.genButton.rect.collidepoint(event.pos):
            game.genEnergy()
    
        if button.bigBangButton.rect.collidepoint(event.pos) and upgrade.bigBangUpgrade.level <= 0:
            upgrade.buyUpgrade(upgrade.bigBangUpgrade)
        
        if button.cheatsMenuButton.rect.collidepoint(event.pos):
            menu.menuVar.setCurrentMenuToCheats()
    elif menu.menuVar.currentMenu == "shop":
        if button.genEnergyUpgradeButton.rect.collidepoint(event.pos):
            upgrade.buyUpgrade(upgrade.genEnergyUpgrade)
    
        if button.matterGenUpgradeButton.rect.collidepoint(event.pos):
            upgrade.buyUpgrade(upgrade.matterGenUpgrade)

        if button.genEnergyUpgradeBuffButton.rect.collidepoint(event.pos):
            upgrade.buyUpgrade(upgrade.genEnergyUpgradeBuff)
    
        if button.shopBackButton.rect.collidepoint(event.pos):
            menu.menuVar.setCurrentMenuToDefaultMenu()
    elif menu.menuVar.currentMenu == "cheats":
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