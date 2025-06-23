import json, core.listVars as listVars

def saveData():
    saveDataList = []
    currencyObjectData = []
    for currencyObject in listVars.currencyList.list:
        currencyObjectData += [currencyObject.convertDataToDict()]
    saveDataList += [currencyObjectData]
    upgradeObjectData = []
    for upgradeObject in listVars.upgradeList.list:
        upgradeObjectData += [upgradeObject.convertDataToDict()]
    saveDataList += [upgradeObjectData]
    with open("saveData.json", "w") as file: 
        json.dump(saveDataList, file)
    print("Game Saved")

def loadData():
    with open("saveData.json", "r") as file:
        saveData = json.load(file)
        currencySaveData = saveData[0]
        upgradeSaveData = saveData[1]
        i = 0
        for currencyObjectData in currencySaveData:
            listVars.currencyList.list[i].setData(currencyObjectData)
            i += 1
        i = 0
        for upgradeObjectData in upgradeSaveData:
            listVars.upgradeList.list[i].setData(upgradeObjectData)
            i += 1  
    print("Save Loaded")