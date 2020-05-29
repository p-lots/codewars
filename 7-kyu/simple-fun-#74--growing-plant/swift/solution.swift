func growingPlant(_ upSpeed: Int, _ downSpeed: Int, _ desiredHeight: Int) -> Int {
    var currHeight = upSpeed, ret = 1
    while currHeight < desiredHeight {
        currHeight += upSpeed - downSpeed
        ret += 1
    }
    return ret
}