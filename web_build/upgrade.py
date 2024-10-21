import currency

class upgrade:
    def __init__(self, cost, currencyCost, growthRate = 0, increaseGenPerSecondCurrency = None, increaseGenPerSecondAmount = None, increaseCostPerGenCurrency = None, increaseCostPerGenAmount = None):
        self.cost = cost
        self.currencyCost = currencyCost
        self.level = 0
        self.growthRate = growthRate
        self.increaseGenPerSecondCurrency = increaseGenPerSecondCurrency
        self.increaseGenPerSecondAmount = increaseGenPerSecondAmount
        self.increaseCostPerGenCurrency = increaseCostPerGenCurrency
        self.increaseCostPerGenAmount = increaseCostPerGenAmount
    
    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

class upgradeBuff:
    def __init__(self, cost, currencyCost, upgradeBuffed, upgradeVarBuffed, buffedAmount, growthRate = 0):
        self.cost = cost
        self.currencyCost = currencyCost
        self.level = 0
        self.upgradeBuffed = upgradeBuffed
        self.upgradeVarBuffed = upgradeVarBuffed
        self.buffedAmount = buffedAmount
        self.growthRate = growthRate

    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)

def buyUpgrade(upgrade: upgrade):
    if upgrade.currencyCost.amount >= upgrade.cost:
        upgrade.currencyCost.subAmount(upgrade.cost)
        upgrade.level += 1
        upgrade.increaseCost()
        if upgrade.increaseGenPerSecondCurrency != None:
            if upgrade.increaseGenPerSecondAmount == "double":
                upgrade.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.increaseGenPerSecondCurrency.gainPerSecond)
            else:
                upgrade.increaseGenPerSecondCurrency.addGainPerSecond(upgrade.increaseGenPerSecondAmount)
        if upgrade.increaseCostPerGenCurrency != None:
            upgrade.increaseCostPerGenCurrency.addCostToGen(upgrade.increaseCostPerGenAmount)
        
def buyUpgradeBuff(upgradeBuff: upgradeBuff):
    if upgradeBuff.currencyCost.amount >= upgradeBuff.cost:
        upgradeBuff.currencyCost.subAmount(upgradeBuff.cost)
        upgradeBuff.level += 1
        upgradeBuff.increaseCost()
        if upgradeBuff.upgradeVarBuffed == "increaseGenPerSecondAmount":
            if upgradeBuff.buffedAmount == "double":
                upgradeBuff.upgradeBuffed.increaseGenPerSecondCurrency.addGainPerSecond(upgradeBuff.upgradeBuffed.level*upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount)
                upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount += upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount
            else:
                upgradeBuff.upgradeBuffed.increaseGenPerSecondCurrency.addGainPerSecond(upgradeBuff.upgradeBuffed.level*upgradeBuff.buffedAmount)
                upgradeBuff.upgradeBuffed.increaseGenPerSecondAmount += upgradeBuff.buffedAmount

bigBangUpgrade = upgrade(10, currency.energy, 0, currency.matter, .01, currency.matter, 10)
genEnergyUpgrade = upgrade(.05, currency.matter, .1, currency.energy, 1)
matterGenUpgrade = upgrade(.15, currency.matter, 6, currency.matter, "double", currency.matter, 10)

genEnergyUpgradeBuff = upgradeBuff(.5, currency.matter, genEnergyUpgrade, "increaseGenPerSecondAmount", "double")