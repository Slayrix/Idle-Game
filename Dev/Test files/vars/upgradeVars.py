import classes.upgradeClass as upgradeClass, vars.currencyVars as currencyVars

bigBangUpgrade = upgradeClass.genUpgrade(10, currencyVars.energy, 0, currencyVars.matter, .01, currencyVars.matter, 10)
genEnergyUpgrade = upgradeClass.genUpgrade(.05, currencyVars.matter, .1, currencyVars.energy, 1)
matterGenUpgrade = upgradeClass.genUpgrade(.15, currencyVars.matter, 6, currencyVars.matter, "double", currencyVars.matter, 10)

genEnergyUpgradeBuff = upgradeClass.upgradeBuff(.5, currencyVars.matter, genEnergyUpgrade, "increaseGenPerSecondAmount", "double")