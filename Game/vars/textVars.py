import classes.textClass as textClass, vars.currencyVars as currencyVars, vars.upgradeVars as upgradeVars

energyText = textClass.text(["defaultMenu", "shop", "cheats"], (255, 255, 255), 0, 0, ["Energy ", [currencyVars.energy, "amount"]])
matterText = textClass.text(["defaultMenu", "shop", "cheats"], (255, 255, 255), 0, 50, ["Matter ", [currencyVars.matter, "amount"]], [upgradeVars.bigBangUpgrade, "level", ">", 0])