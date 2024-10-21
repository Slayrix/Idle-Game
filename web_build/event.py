import pygame as pg
import menu, upgrade, button, game

def eventCheck(running):
    for event in pg.event.get():
        running = checkIfQuit(event, running)
        mouseClickCheck(event)    
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

    if menu.menuVar.currentMenu == "shop":
        if button.genEnergyUpgradeButton.rect.collidepoint(event.pos):
            upgrade.buyUpgrade(upgrade.genEnergyUpgrade)
    
        if button.matterGenUpgradeButton.rect.collidepoint(event.pos):
            upgrade.buyUpgrade(upgrade.matterGenUpgrade)

        if button.genEnergyUpgradeBuffButton.rect.collidepoint(event.pos):
            upgrade.buyUpgradeBuff(upgrade.genEnergyUpgradeBuff)
    
        if button.shopBackButton.rect.collidepoint(event.pos):
            menu.menuVar.setCurrentMenuToDefaultMenu()