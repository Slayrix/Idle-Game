import classes.textClass as textClass, vars.currencyVars as currencyVars, vars.upgradeVars as upgradeVars

activeMenuList = ["defaultMenu", "shop", "cheats"]
xPos = 0
yPos = 0
updateTextList = ["Energy ", [currencyVars.energy, "amount"]]
drawConditions = None
energyText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions)

activeMenuList = ["defaultMenu", "shop", "cheats"]
xPos = 0
yPos = 30
updateTextList = ["Matter ", [currencyVars.matter, "amount"]]
drawConditions = [upgradeVars.bigBangUpgrade, "level", ">", 0]
matterText = textClass.text(activeMenuList, (255, 255, 255), xPos, yPos, updateTextList, drawConditions)