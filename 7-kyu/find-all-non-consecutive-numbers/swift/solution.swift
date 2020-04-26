func allNonConsecutive (_ arr: [Int]) -> [(Int, Int)] {
    var ret: [(Int, Int)] = []
    guard arr.count > 1 else { return ret }
    var properVal = arr[0]
    for (idx, val) in arr.enumerated() {
        if val != properVal {
            ret.append((idx, val))
            properVal = val
        }
        properVal += 1
    }
    return ret
}