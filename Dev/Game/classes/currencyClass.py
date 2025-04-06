class currency:
    def __init__(self):
        self.amount = 0
        self.gainPerSecond = 0
        self.costToGen = 0

    def addOne(self):
        self.amount += 1
    
    def addAmount(self, x):
        self.amount = round(self.amount + x, 2)

    def subAmount(self, x):
        self.amount = round(self.amount - x, 2)
    
    def addGainPerSecond(self, x):
        self.gainPerSecond += x

    def addCostToGen(self, x):
        self.costToGen += x