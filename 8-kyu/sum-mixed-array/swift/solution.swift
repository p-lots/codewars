func sumMix(_ arr: [Any]) -> Int {
    var ret = 0
    for elem in arr {
        if type(of: elem) == String.self {
            ret += Int(elem as! String)!
        } else {
            ret += elem as! Int
        }
    }
    return ret
}