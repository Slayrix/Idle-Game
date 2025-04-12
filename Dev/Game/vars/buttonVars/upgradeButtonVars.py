import vars.upgradeVars as upgradeVars, classes.buttonClass as buttonClass, vars.buttonGroupVars as buttonGroupVars, vars.infoboxVars as infoboxVars

#bigBangUpgradeButton
textList = ["Start Big Bang"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["buyUpgrade", upgradeVars.bigBangUpgrade]
drawConditionsList = [upgradeVars.bigBangUpgrade, "level", "=", 0]
updateTextList = None
infobox = infoboxVars.bigBangInfobox
bigBangUpgradeButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 150, 150, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#genEnergyUpgradeButton
textList = ["Upgrade 1"]
activeMenuList = ["shop"]
buttonGroup = buttonGroupVars.upgradeButtonGroup
buttonFunctionality = ["buyUpgrade", upgradeVars.genEnergyUpgrade]
drawConditionsList = None
updateTextList = None
infobox = infoboxVars.genEnergyUpgradeInfobox
genEnergyUpgradeButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#matterGenUpgradeButton
textList = ["Upgrade 2"]
activeMenuList = ["shop"]
buttonGroup = buttonGroupVars.upgradeButtonGroup
buttonFunctionality = ["buyUpgrade", upgradeVars.matterGenUpgrade]
drawConditionsList = None
updateTextList = None
infobox = infoboxVars.matterGenUpgradeInfobox
matterGenUpgradeButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)

#genEnergyUpgradeBuffButton
textList = ["Upgrade 3"]
activeMenuList = ["shop"]
buttonGroup = buttonGroupVars.upgradeButtonGroup
buttonFunctionality = ["buyUpgrade", upgradeVars.genEnergyUpgradeBuff]
drawConditionsList = None
updateTextList = None
infobox = infoboxVars.genEnergyUpgradeBuffInfobox
genEnergyUpgradeBuffButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList, infobox)