func stockList(_ listOfArt: [String], _ listOfCat: [String]) -> String {
    guard !listOfArt.isEmpty && !listOfCat.isEmpty else { return String() }
    var codeCounts: [Character: Int] = [:]
    for item in listOfArt {
        let tempArr = item.components(separatedBy: " ")
        let code = tempArr[0]
        let count = Int(tempArr[1])!
        let codeIndex = code.index(code.startIndex, offsetBy: 0)
        if let currValCount = codeCounts[code[codeIndex]] {
            codeCounts.updateValue(currValCount + count, forKey: code[codeIndex])
        } else {
            codeCounts.updateValue(count, forKey: code[codeIndex])
        }
    }
    let ret = listOfCat.map {
        (item: String) -> String in
        let key = item[item.index(item.startIndex, offsetBy: 0)]
        if let keyCount = codeCounts[key] {
            return "(\(key) : \(keyCount))"
        } else {
            return "(\(key) : 0)"
        }
    }
    return ret.joined(separator: " - ")
}