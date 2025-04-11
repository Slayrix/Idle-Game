import operations as op

class upgrade:
    def __init__(self, cost, currencyCost, growthRate = 0):
        self.cost = cost
        self.currencyCost = currencyCost
        self.level = 0
        self.growthRate = growthRate
    
    def increaseCost(self):
        self.cost = round(self.cost*(1+self.growthRate)**self.level, 2)
    
    def buyUpgradeCheck(self):
        if self.currencyCost.amount >= self.cost:
            self.currencyCost.subAmount(self.cost)
            self.level += 1
            self.increaseCost()
            return True
        else:
            return False

class genUpgrade(upgrade):
    def __init__(self, cost, currencyCost, growthRate = 0, increaseGenPerSecondCurrency = None, operation1 = None, increaseGenPerSecondAmount = None, increaseCostPerGenCurrency = None, operation2 = None, increaseCostPerGenAmount = None):
        super().__init__(cost, currencyCost, growthRate)
        self.increaseGenPerSecondCurrency = increaseGenPerSecondCurrency
        self.increaseGenPerSecondAmount = increaseGenPerSecondAmount
        self.increaseCostPerGenCurrency = increaseCostPerGenCurrency
        self.increaseCostPerGenAmount = increaseCostPerGenAmount
        self.operation1 = operation1
        self.operation2 = operation2
        self.functions = {
            "increaseGenPerSecondAmount": self.setIncreaseGenPerSecondAmount
        }
    
    def setIncreaseGenPerSecondAmount(self, operation, amountIncrease):
        newAmount = op.ops[operation](self.increaseGenPerSecondAmount, amountIncrease)
        self.increaseGenPerSecondAmount = newAmount
        self.increaseGenPerSecondCurrency.setGenPerSecond(self.level*newAmount)

    def buyUpgrade(self):
        if self.buyUpgradeCheck() == True:
            if self.increaseGenPerSecondCurrency != None:
                genPerSecondIncreaseVal = op.ops[self.operation1](self.increaseGenPerSecondCurrency.gainPerSecond, self.increaseGenPerSecondAmount)
                self.increaseGenPerSecondCurrency.setGenPerSecond(genPerSecondIncreaseVal)
            if self.increaseCostPerGenCurrency != None:
                costToGenIncreaseVal = op.ops[self.operation2](self.increaseCostPerGenCurrency.costToGen, self.increaseCostPerGenAmount)
                self.increaseCostPerGenCurrency.setCostToGen(costToGenIncreaseVal)

class upgradeBuff(upgrade):
    def __init__(self, cost, currencyCost, upgradeBuffed, upgradeVarBuffed, operation, amountIncrease, growthRate = 0):
        super().__init__(cost, currencyCost, growthRate)
        self.upgradeBuffed = upgradeBuffed
        self.upgradeVarBuffed = upgradeVarBuffed
        self.operation = operation
        self.amountIncrease = amountIncrease
    
    def buyUpgrade(self):
        if self.buyUpgradeCheck() == True:
            self.upgradeBuffed.functions[self.upgradeVarBuffed](self.operation, self.amountIncrease)