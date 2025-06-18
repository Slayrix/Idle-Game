import classes.textClass as textClass, vars.currencyVars as currencyVars, vars.upgradeVars as upgradeVars, core.settings as settings

activeMenuList = ["defaultMenu", "shop", "cheats"]
xPos = 0
yPos = 0
updateTextList = ["Energy ", [currencyVars.energy, "amount"]]
drawConditions = None
textType = "currency"
energyText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions, textType)

activeMenuList = ["defaultMenu", "shop", "cheats"]
xPos = 0
yPos = 20
updateTextList = ["Matter ", [currencyVars.matter, "amount"]]
drawConditions = [upgradeVars.bigBangUpgrade, "level", ">", 0]
textType = "currency"
matterText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions, textType)

activeMenuList = ["settings"]
xPos = 320
yPos = 100
updateTextList = [str(settings.resolution[0]), "x", str(settings.resolution[1])]
drawConditions = None
textType = None
currentResolutionText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions, textType)

activeMenuList = ["settings"]
xPos = 320
yPos = 70
updateTextList = ["Resolution"]
drawConditions = None
textType = None
resolutionText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions, textType)