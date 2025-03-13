class upgrade:
    def __init__(self, cost, currencyCost, growthRate = 0):
        self.cost = cost
        self.currencyCost = currencyCost
        self.level = 0
        self.growthRate = growthRate
    
    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

class genUpgrade(upgrade):
    def __init__(self, cost, currencyCost, growthRate = 0, increaseGenPerSecondCurrency = None, increaseGenPerSecondAmount = None, increaseCostPerGenCurrency = None, increaseCostPerGenAmount = None):
        super().__init__(cost, currencyCost, growthRate)
        self.increaseGenPerSecondCurrency = increaseGenPerSecondCurrency
        self.increaseGenPerSecondAmount = increaseGenPerSecondAmount
        self.increaseCostPerGenCurrency = increaseCostPerGenCurrency
        self.increaseCostPerGenAmount = increaseCostPerGenAmount

class upgradeBuff(upgrade):
    def __init__(self, cost, currencyCost, upgradeBuffed, upgradeVarBuffed, buffedAmount, growthRate = 0):
        super().__init__(cost, currencyCost, growthRate)
        self.upgradeBuffed = upgradeBuffed
        self.upgradeVarBuffed = upgradeVarBuffed
        self.buffedAmount = buffedAmount

def buyUpgrade(upgrade):
    if upgrade.currencyCost.amount >= upgrade.cost:
        upgrade.currencyCost.subAmount(upgrade.cost)
        upgrade.level += 1
        upgrade.increaseCost()
        if type(upgrade) == genUpgrade:
            if upgrade.increaseGenPerSecondCurrency != None:
                if upgrade.increaseGenPerSecondAmount == "double":
                    upgrade.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.increaseGenPerSecondCurrency.gainPerSecond)
                else:
                    upgrade.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.increaseGenPerSecondAmount)
            if upgrade.increaseCostPerGenCurrency != None:
                upgrade.increaseCostPerGenCurrency.addCostToGen(upgrade.increaseCostPerGenAmount)
        elif type(upgrade) == upgradeBuff:
            if upgrade.upgradeVarBuffed == "increaseGenPerSecondAmount":
                if upgrade.buffedAmount == "double":
                    upgrade.upgradeBuffed.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.upgradeBuffed.level*upgrade.upgradeBuffed.increaseGenPerSecondAmount)
                    upgrade.upgradeBuffed.increaseGenPerSecondAmount += upgrade.upgradeBuffed.increaseGenPerSecondAmount
                else:
                    upgrade.upgradeBuffed.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.upgradeBuffed.level*upgrade.buffedAmount)
                    upgrade.upgradeBuffed.increaseGenPerSecondAmount += upgrade.buffedAmount