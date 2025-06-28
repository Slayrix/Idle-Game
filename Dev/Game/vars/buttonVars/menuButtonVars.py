import classes.buttonClass as buttonClass, vars.upgradeVars as upgradeVars, vars.buttonGroupVars as buttonGroupVars

#shopButton
textList = ["Shop"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "shop"]
drawConditionsList = [upgradeVars.bigBangUpgrade, "level", ">", 0]
updateTextList = None
shopButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 35, 335, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#shopBackButton
textList = ["Back"]
activeMenuList = ["shop"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "defaultMenu"]
drawConditionsList = None
updateTextList = None
shopBackButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 35, 335, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#settingsButton
textList = ["Settings"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "settings"]
drawConditionsList = None
updateTextList = None
infobox = None
settingsButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 600, 20, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#settingsBackButton
textList = ["Back"]
activeMenuList = ["settings"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "defaultMenu"]
drawConditionsList = None
updateTextList = None
infobox = None
settingsBackButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 35, 335, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#cheatsMenuButton
textList = ["Open Cheats Menu"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "cheats"]
drawConditionsList = None
updateTextList = None
cheatsMenuButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 550, 335, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#cheatsBackButton
textList = ["Back"]
activeMenuList = ["cheats"]
buttonGroup = None
buttonFunctionality = ["changeMenu", "defaultMenu"]
drawConditionsList = None
updateTextList = None
cheatsBackButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 35, 335, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#changeResForward
textList = [">"]
activeMenuList = ["settings"]
buttonGroup = None
buttonFunctionality = ["changeResolution", "forward"]
drawConditionsList = None
updateTextList = None
infobox = None
changeResForward = buttonClass.button(textList, activeMenuList, (255, 255, 255), 400, 100, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#changeResBack
textList = ["<"]
activeMenuList = ["settings"]
buttonGroup = None
buttonFunctionality = ["changeResolution", "backward"]
drawConditionsList = None
updateTextList = None
infobox = None
changeResBack = buttonClass.button(textList, activeMenuList, (255, 255, 255), 235, 100, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#saveButton
textList = ["Save Game"]
activeMenuList = ["settings"]
buttonGroup = None
buttonFunctionality = ["saveGame"]
drawConditionsList = None
updateTextList = None
infobox = None
saveButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 320, 150, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#loadButton
textList = ["Load Game"]
activeMenuList = ["settings"]
buttonGroup = None
buttonFunctionality = ["loadGame"]
drawConditionsList = None
updateTextList = None
infobox = None
saveButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 320, 180, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#quitButton
textList = ["Quit Game"]
activeMenuList = ["settings"]
buttonGroup = None
buttonFunctionality = ["quitGame"]
drawConditionsList = None
updateTextList = None
infobox = None
quitButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 320, 210, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)