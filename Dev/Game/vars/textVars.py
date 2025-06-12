import classes.textClass as textClass, vars.currencyVars as currencyVars, vars.upgradeVars as upgradeVars, core.settings as settings

activeMenuList = ["defaultMenu", "shop", "cheats"]
xPos = 40
yPos = 40
updateTextList = ["Energy ", [currencyVars.energy, "amount"]]
drawConditions = None
energyText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions)

activeMenuList = ["defaultMenu", "shop", "cheats"]
xPos = 38
yPos = 60
updateTextList = ["Matter ", [currencyVars.matter, "amount"]]
drawConditions = [upgradeVars.bigBangUpgrade, "level", ">", 0]
matterText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions)

activeMenuList = ["settings"]
xPos = 320
yPos = 100
updateTextList = [str(settings.resolution[0]), "x", str(settings.resolution[1])]
drawConditions = None
resolutionText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions)