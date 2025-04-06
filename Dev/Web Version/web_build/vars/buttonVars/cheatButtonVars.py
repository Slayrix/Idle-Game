import vars.buttonGroupVars as buttonGroupVars, vars.currencyVars as currencyVars, classes.buttonClass as buttonClass

#energyCheatButton
textList = ["Add Energy"]
activeMenuList = ["cheats"]
buttonGroup = buttonGroupVars.cheatsButtonGroup
buttonFunctionality = ["cheat", currencyVars.energy]
drawConditionsList = None
updateTextList = None
energyCheatButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#matterCheatButton
textList = ["Add Matter"]
activeMenuList = ["cheats"]
buttonGroup = buttonGroupVars.cheatsButtonGroup
buttonFunctionality = ["cheat", currencyVars.matter]
drawConditionsList = None
updateTextList = None
matterCheatButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)