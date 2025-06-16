import core.listVars as listVars

class currency:
    def __init__(self, currencyVarCostToGen = None):
        listVars.currencyList.list += [self]
        self.amount = 0
        self.gainPerSecond = 0
        self.costToGen = 0
        self.currencyVarCostToGen = currencyVarCostToGen

    def addOne(self):
        self.amount += 1
    
    def addAmount(self, x):
        self.amount = round(self.amount + x, 2)

    def subAmount(self, x):
        self.amount = round(self.amount - x, 2)
    
    def addGainPerSecond(self, x):
        self.gainPerSecond += x
    
    def setGenPerSecond(self, newGenPerSecond):
        self.gainPerSecond = newGenPerSecond

    def addCostToGen(self, x):
        self.costToGen += x
    
    def setCostToGen(self, newCostToGen):
        self.costToGen = newCostToGen

    def genFunction(self):
        if self.currencyVarCostToGen != None:
            if self.currencyVarCostToGen.amount >= self.costToGen:
                self.addAmount(self.gainPerSecond)
                self.currencyVarCostToGen.subAmount(self.costToGen)
        else:
            self.addAmount(self.gainPerSecond)