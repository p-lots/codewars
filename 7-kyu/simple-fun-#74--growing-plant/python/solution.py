def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    ret = 1
    while height < desiredHeight:
        height += upSpeed
        ret += 1
        height -= downSpeed
    return ret