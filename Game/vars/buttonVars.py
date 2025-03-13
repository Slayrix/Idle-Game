import classes.buttonClass as buttonClass, vars.currencyVars as currencyVars, vars.upgradeVars as upgradeVars, vars.buttonGroupVars as buttonGroupVars

energyCheatButton = buttonClass.button(["Add Energy"], ["cheats"], (255, 255, 255), 0, 0, buttonGroupVars.cheatsButtonGroup, ["cheat", currencyVars.energy])
matterCheatButton = buttonClass.button(["Add Matter"], ["cheats"], (255, 255, 255), 0, 0, buttonGroupVars.cheatsButtonGroup, ["cheat", currencyVars.matter])

genButton = buttonClass.button(["Click to gen"], ["defaultMenu"], (255, 255, 255), 150, 100, None, ["genCurrency", 1, currencyVars.energy])
shopButton = buttonClass.button(["Shop"], ["defaultMenu"], (255, 255, 255), 150, 150, None, ["changeMenu", "shop"], [upgradeVars.bigBangUpgrade, "level", ">", 0])
shopBackButton = buttonClass.button(["Back"], ["shop"], (255, 255, 255), 150, 150, None, ["changeMenu", "default"])
bigBangButton = buttonClass.button(["Start Big Bang", str(upgradeVars.bigBangUpgrade.cost) + " Energy"], ["defaultMenu"], (255, 255, 255), 150, 150, None, ["buyUpdrade", upgradeVars.bigBangUpgrade], [upgradeVars.bigBangUpgrade, "level", "=", 0])
genEnergyUpgradeButton = buttonClass.button(["Upgrade 1", "Auto gen +" + str(upgradeVars.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", str(upgradeVars.genEnergyUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 0, 0, buttonGroupVars.upgradeButtonGroup, ["buyUpdrade", upgradeVars.genEnergyUpgrade], None, [[["Auto gen +", [upgradeVars.genEnergyUpgrade, "increaseGenPerSecondAmount"], " energy per second per upgrade"], 1], [[[upgradeVars.genEnergyUpgrade, "cost"], " Matter"], 2]])
matterGenUpgradeButton = buttonClass.button(["Double Matter Generation", "Increases energy consumption by +10", str(upgradeVars.matterGenUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 0, 0, buttonGroupVars.upgradeButtonGroup, ["buyUpdrade", upgradeVars.matterGenUpgrade], None, [[[[upgradeVars.matterGenUpgrade, "cost"], " Matter"], 2]])
genEnergyUpgradeBuffButton = buttonClass.button(["Double Energy Generation of Upgrade 1", str(upgradeVars.genEnergyUpgradeBuff.cost) + " Matter"], ["shop"], (255, 255, 255), 0, 0, buttonGroupVars.upgradeButtonGroup, ["buyUpdrade", upgradeVars.genEnergyUpgradeBuff])
cheatsMenuButton = buttonClass.button(["Open Cheats Menu"], ["defaultMenu"], (255, 255, 255), 100, 300, None, ["changeMenu", "cheats"])
cheatsBackButton = buttonClass.button(["Go Back"], ["cheats"], (255, 255, 255), 100, 300, None, ["changeMenu", "default"])