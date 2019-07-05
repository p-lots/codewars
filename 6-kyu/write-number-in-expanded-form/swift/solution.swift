func expandedForm(_ num: Int) -> String {
    let numArr = String(num).characters.map { String($0) }
    var zeroesCount = numArr.count
    return numArr.map { zeroesCount -= 1; return $0 == "0" ? "" : $0 + String(repeating: "0", count: zeroesCount) }.filter { $0 != "" }.joined(separator: " + ")
}