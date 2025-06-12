resolutionList = [
    [640, 360],
    [1280, 720],
    [1920, 1080],
    [2560, 1440]
]

resolution = resolutionList[0]

def calcResolutionScale(resolution):
    resolutionScale = [resolution[0]/640, resolution[1]/360]
    return resolutionScale

resolutionScale = calcResolutionScale(resolution)

def calcFontSize(refSize, resolutionScale):
    return int(round(refSize * min(resolutionScale)))
    
refFontSize = 18
infoboxRefFontSize = 12

fontSize = calcFontSize(refFontSize, resolutionScale)
infoboxFontSize = calcFontSize(infoboxRefFontSize, resolutionScale)