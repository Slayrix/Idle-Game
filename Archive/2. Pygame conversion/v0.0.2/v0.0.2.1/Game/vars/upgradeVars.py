import classes.upgradeClass as upgradeClass, vars.currencyVars as currencyVars

#Gen Upgrades
cost = 10
currencyCost = currencyVars.energy
growthRate = 0
increaseGenPerSecondCurrency = currencyVars.matter
operation1 = "+"
increaseGenPerSecondAmount = .01
increaseCostPerGenCurrency = currencyVars.matter
operation2 = "+"
increaseCostPerGenAmount = 10
bigBangUpgrade = upgradeClass.genUpgrade(cost, currencyCost, growthRate, increaseGenPerSecondCurrency, operation1, increaseGenPerSecondAmount, increaseCostPerGenCurrency, operation2, increaseCostPerGenAmount)

cost = .05
currencyCost = currencyVars.matter
growthRate = .1
increaseGenPerSecondCurrency = currencyVars.energy
operation1 = "+"
increaseGenPerSecondAmount = 1
increaseCostPerGenCurrency = None
operation2 = None
increaseCostPerGenAmount = None
genEnergyUpgrade = upgradeClass.genUpgrade(cost, currencyCost, growthRate, increaseGenPerSecondCurrency, operation1, increaseGenPerSecondAmount, increaseCostPerGenCurrency, operation2, increaseCostPerGenAmount)

cost = .15
currencyCost = currencyVars.matter
growthRate = 6
increaseGenPerSecondCurrency = currencyVars.matter
operation1 = "*"
increaseGenPerSecondAmount = 2
increaseCostPerGenCurrency = currencyVars.matter
operation2 = "+"
increaseCostPerGenAmount = 10
matterGenUpgrade = upgradeClass.genUpgrade(cost, currencyCost, growthRate, increaseGenPerSecondCurrency, operation1, increaseGenPerSecondAmount, increaseCostPerGenCurrency, operation2, increaseCostPerGenAmount)


#Upgrade Buffs
cost = .5
currencyCost = currencyVars.matter
upgradeBuffed = genEnergyUpgrade
upgradeVarBuffed = "increaseGenPerSecondAmount"
operation = "*"
amountIncrease = 2
growthRate = 0
genEnergyUpgradeBuff = upgradeClass.upgradeBuff(cost, currencyCost, upgradeBuffed, upgradeVarBuffed, operation, amountIncrease, growthRate)