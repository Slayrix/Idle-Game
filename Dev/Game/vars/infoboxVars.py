import classes.infoboxClass as infoboxClass, vars.upgradeVars as upgradeVars

textList = ["Cost: " + str(upgradeVars.bigBangUpgrade.cost) + " Energy"]
updateTextList = None
bigBangInfobox = infoboxClass.infobox(textList, (255, 255, 255), updateTextList)

textList = ["Auto gen +" + str(upgradeVars.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", "Cost: " + str(upgradeVars.genEnergyUpgrade.cost) + " Matter"]
updateTextList = [[["Auto gen +", [upgradeVars.genEnergyUpgrade, "increaseGenPerSecondAmount"], " energy per second per upgrade"], 0], [["Cost: ", [upgradeVars.genEnergyUpgrade, "cost"], " Matter"], 1]]
genEnergyUpgradeInfobox = infoboxClass.infobox(textList, (255, 255, 255), updateTextList)

textList = ["Double Matter Generation", "Increases energy consumption by +10", "Cost: " + str(upgradeVars.matterGenUpgrade.cost) + " Matter"]
updateTextList = [[["Cost: ", [upgradeVars.matterGenUpgrade, "cost"], " Matter"], 2]]
matterGenUpgradeInfobox = infoboxClass.infobox(textList, (255, 255, 255), updateTextList)

textList = ["Double Energy Generation of Upgrade 1", "Cost: ", str(upgradeVars.genEnergyUpgradeBuff.cost) + " Matter"]
updateTextList = None
genEnergyUpgradeBuffInfobox = infoboxClass.infobox(textList, (255, 255, 255), updateTextList)

textList = ["+1 Gas", "Cost: 9999"]
updateTextList = None
buyGasInfobox = infoboxClass.infobox(textList, (255, 255, 255), updateTextList)