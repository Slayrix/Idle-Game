class test:
    def __init__(self, testVal):
        self.test1 = testVal

class test2(test):
    def __init__(self, testVal, test2Val):
        super().__init__(testVal)
        self.test2 = test2Val

thing = test2(1, 2)

print(thing.test1, thing.test2)