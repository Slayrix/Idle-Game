import vars.upgradeVars as upgradeVars, classes.buttonClass as buttonClass, vars.buttonGroupVars as buttonGroupVars

#bigBangUpgradeButton
textList = ["Start Big Bang", str(upgradeVars.bigBangUpgrade.cost) + " Energy"]
activeMenuList = ["defaultMenu"]
buttonGroup = None
buttonFunctionality = ["buyUpdrade", upgradeVars.bigBangUpgrade]
drawConditionsList = [upgradeVars.bigBangUpgrade, "level", "=", 0]
updateTextList = None
bigBangUpgradeButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 150, 150, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#genEnergyUpgradeButton
textList = ["Upgrade 1", "Auto gen +" + str(upgradeVars.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", str(upgradeVars.genEnergyUpgrade.cost) + " Matter"]
activeMenuList = ["shop"]
buttonGroup = buttonGroupVars.upgradeButtonGroup
buttonFunctionality = ["buyUpdrade", upgradeVars.genEnergyUpgrade]
drawConditionsList = None
updateTextList = [["Auto gen +", [upgradeVars.genEnergyUpgrade, "increaseGenPerSecondAmount"], " energy per second per upgrade"], 1], [[[upgradeVars.genEnergyUpgrade, "cost"], " Matter"], 2]
genEnergyUpgradeButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#matterGenUpgradeButton
textList = ["Double Matter Generation", "Increases energy consumption by +10", str(upgradeVars.matterGenUpgrade.cost) + " Matter"]
activeMenuList = ["shop"]
buttonGroup = buttonGroupVars.upgradeButtonGroup
buttonFunctionality = ["buyUpdrade", upgradeVars.matterGenUpgrade]
drawConditionsList = None
updateTextList = [[[[upgradeVars.matterGenUpgrade, "cost"], " Matter"], 2]]
matterGenUpgradeButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)

#genEnergyUpgradeBuffButton
textList = ["Double Energy Generation of Upgrade 1", str(upgradeVars.genEnergyUpgradeBuff.cost) + " Matter"]
activeMenuList = ["shop"]
buttonGroup = buttonGroupVars.upgradeButtonGroup
buttonFunctionality = ["buyUpdrade", upgradeVars.genEnergyUpgradeBuff]
drawConditionsList = None
updateTextList = None
genEnergyUpgradeBuffButton = buttonClass.button(textList, activeMenuList, (255, 255, 255), 0, 0, buttonGroup, buttonFunctionality, drawConditionsList, updateTextList)