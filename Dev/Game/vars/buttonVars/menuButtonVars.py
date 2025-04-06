import classes.buttonClass as buttonClass, vars.currencyVars as currencyVars, vars.upgradeVars as upgradeVars, vars.buttonGroupVars as buttonGroupVars

#genButton
textList = ["Click to gen"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["genCurrency", currencyVars.energy, 1]
drawConditionsList = None
updateTextList = None
genButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 150, 100, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#shopButton
textList = ["Shop"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "shop"]
drawConditionsList = [upgradeVars.bigBangUpgrade, "level", ">", 0]
updateTextList = None
shopButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 150, 150, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#shopBackButton
textList = ["Back"]
activeMenuList = ["shop"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "default"]
drawConditionsList = None
updateTextList = None
shopBackButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 150, 150, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#cheatsMenuButton
textList = ["Open Cheats Menu"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "cheats"]
drawConditionsList = None
updateTextList = None
cheatsMenuButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 100, 300, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#cheatsBackButton
textList = ["Go Back"]
activeMenuList = ["cheats"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "default"]
drawConditionsList = None
updateTextList = None
cheatsBackButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 100, 300, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)