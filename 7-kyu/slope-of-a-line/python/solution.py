def getSlope(p1, p2):
    ''' Return the slope of the line through p1 and p2'''
    rise = p2[1] - p1[1]
    run = p2[0] - p1[0]
    return rise / run if run != 0 else None
