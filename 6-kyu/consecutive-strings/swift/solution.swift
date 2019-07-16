func longestConsec(_ strarr: [String], _ k: Int) -> String {
    guard !strarr.isEmpty && k <= strarr.count && k > 0 else { return "" }
    var ret = [String]()
    for i in 0..<strarr.count {
        var str: String = ""
        if i + k < strarr.count {
            str = strarr[i..<(i + k)].joined()
        } else {
            str = strarr[i..<strarr.count].joined()
        }
        ret.append(str)
    }
    if let result = ret.max(by: {$0.characters.count < $1.characters.count }) {
        return result
    } else {
        return ""
    }
}