import vars.currencyVars as currencyVars, classes.buttonClass as buttonClass, vars.infoboxVars as infoboxVars, vars.upgradeVars as upgradeVars

#genButton
textList = ["Click to gen"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["genCurrency", currencyVars.energy, 1]
drawConditionsList = None
updateTextList = None
infobox = None
genButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 320, 150, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#buyGasButton
textList = ["Buy Gas"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = []
drawConditionsList = [upgradeVars.bigBangUpgrade, "level", ">=", 1]
updateTextList = None
infobox = infoboxVars.buyGasInfobox
buyGasButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 320, 200, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)
































#Buttons