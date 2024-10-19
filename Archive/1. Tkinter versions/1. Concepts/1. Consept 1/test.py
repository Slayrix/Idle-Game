class clicks:
    def __init__(self):
        self.amount = 0
    
    def addOne(self):
        self.amount = self.amount + 1

c = clicks()

def function():
    while True:
        i = input("Type 1 to gen")
        if  i == "1":
            c.addOne()
            print(c.amount)

function()