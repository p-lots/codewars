func persistence(for num: Int) -> Int {
    var numStr = String(num)
    guard numStr.count > 1 else { return 0 }
    var ret = 0
    while numStr.count > 1 {
        let next = numStr.compactMap { Int(String($0)) }.reduce(1, *)
        numStr = String(next)
        ret += 1
    }
    return ret
}