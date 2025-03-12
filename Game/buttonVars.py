import button, buttonGroup, currency, upgrade

energyCheatButton = button.button(["Add Energy"], ["cheats"], (255, 255, 255), 0, 0, buttonGroup.cheatsButtonGroup, ["cheat", currency.energy])
matterCheatButton = button.button(["Add Matter"], ["cheats"], (255, 255, 255), 0, 0, buttonGroup.cheatsButtonGroup, ["cheat", currency.matter])

genButton = button.button(["Click to gen"], ["defaultMenu"], (255, 255, 255), 150, 100, None, ["genCurrency", 1, currency.energy])
shopButton = button.button(["Shop"], ["defaultMenu"], (255, 255, 255), 150, 150, None, ["changeMenu", "shop"], [upgrade.bigBangUpgrade, "level", ">", 0])
shopBackButton = button.button(["Back"], ["shop"], (255, 255, 255), 150, 150, None, ["changeMenu", "default"])
bigBangButton = button.button(["Start Big Bang", str(upgrade.bigBangUpgrade.cost) + " Energy"], ["defaultMenu"], (255, 255, 255), 150, 150, None, ["buyUpdrade", upgrade.bigBangUpgrade], [upgrade.bigBangUpgrade, "level", "=", 0])
genEnergyUpgradeButton = button.button(["Upgrade 1", "Auto gen +" + str(upgrade.genEnergyUpgrade.increaseGenPerSecondAmount) + " energy per second per upgrade", str(upgrade.genEnergyUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 0, 0, buttonGroup.upgradeButtonGroup, ["buyUpdrade", upgrade.genEnergyUpgrade], None, [[["Auto gen +", [upgrade.genEnergyUpgrade, "increaseGenPerSecondAmount"], " energy per second per upgrade"], 1], [[[upgrade.genEnergyUpgrade, "cost"], " Matter"], 2]])
matterGenUpgradeButton = button.button(["Double Matter Generation", "Increases energy consumption by +10", str(upgrade.matterGenUpgrade.cost) + " Matter"], ["shop"], (255, 255, 255), 0, 0, buttonGroup.upgradeButtonGroup, ["buyUpdrade", upgrade.matterGenUpgrade], None, [[[[upgrade.matterGenUpgrade, "cost"], " Matter"], 2]])
genEnergyUpgradeBuffButton = button.button(["Double Energy Generation of Upgrade 1", str(upgrade.genEnergyUpgradeBuff.cost) + " Matter"], ["shop"], (255, 255, 255), 0, 0, buttonGroup.upgradeButtonGroup, ["buyUpdrade", upgrade.genEnergyUpgradeBuff])
cheatsMenuButton = button.button(["Open Cheats Menu"], ["defaultMenu"], (255, 255, 255), 100, 300, None, ["changeMenu", "cheats"])
cheatsBackButton = button.button(["Go Back"], ["cheats"], (255, 255, 255), 100, 300, None, ["changeMenu", "default"])