def declareClass(className, classType, argumentList = None):
    if argumentList == None:
        className = classType()
    else:
        className = classType(*argumentList)
    return className