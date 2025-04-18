#resolution = (640, 360)
resolution = (1280, 720)
#resolution = (1920, 1080)
#resolution = (2560, 1440)
resolutionScale = [resolution[0]/640, resolution[1]/360]

refFontSize = 18
infoboxRefFontSize = 12
fontSize = int(round(refFontSize * min(resolutionScale)))
infoboxFontSize = int(round(infoboxRefFontSize * min(resolutionScale)))