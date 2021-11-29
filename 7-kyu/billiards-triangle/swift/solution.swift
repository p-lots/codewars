func pyramid(_ balls: Int) -> Int {
    var balls = balls
    var ret = 0
    var nextRow = 1
    while balls > 0 {
        ret += 1
        nextRow += 1
        balls -= nextRow
    }
    return ret
}
