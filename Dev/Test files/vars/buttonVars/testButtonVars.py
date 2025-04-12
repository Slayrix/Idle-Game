import classes.buttonClass as buttonClass, vars.infoboxVars as infoboxVars

#buttonName
textList = ["Test Button"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = []
drawConditionsList = None
updateTextList = None
test = buttonClass.button(textList, activeMenuList, (255, 255, 255), 100, 100, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infoboxVars.testInfobox)