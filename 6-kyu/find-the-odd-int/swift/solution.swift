func findIt(_ seq: [Int]) -> Int {
    var counts: [Int: Int] = [:]
    for n in seq {
        if let currNCount = counts[n] {
            counts[n] = currNCount + 1
        } else {
            counts[n] = 1
        }
    }
    var ret = 0
    for (num, cnt) in counts {
        if cnt % 2 == 1 {
            ret = num
            break
        }
    }
    return ret
}