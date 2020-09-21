func stockList(_ listOfArt: [String], _ listOfCat: [String]) -> String {
    guard !listOfArt.isEmpty && !listOfCat.isEmpty else { return "" }
    var codeCounts: [Character: Int] = [:]
    for item in listOfArt {
        let tempArr = item.components(separatedBy: " ")
        let code = tempArr[0]
        let count = Int(tempArr[1]) ?? 0
        let currValCount = codeCounts[code[code.startIndex]] ?? 0
        codeCounts.updateValue(currValCount + count, forKey: code[code.startIndex])
    }
    let ret = listOfCat.map { (item: String) -> String in
        let key = item[item.startIndex]
        return "(\(key) : \(codeCounts[key] ?? 0))"
    }
    return ret.joined(separator: " - ")
}