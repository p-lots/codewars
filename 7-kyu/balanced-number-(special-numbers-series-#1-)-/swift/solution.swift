func balancedNumber(_ number: Int) -> String {
    guard number > 99 else { return "Balanced" }
    let numberArr = String(number).compactMap { Int(String($0)) }
    var middle = numberArr.count / 2
    if numberArr.count % 2 == 0 {
        middle -= 1
    }
    let lhs = numberArr[0..<middle]
    let rhs = numberArr[(numberArr.count - middle)...]
    let lhsSum = lhs.reduce(0, +)
    let rhsSum = rhs.reduce(0, +)
    return lhsSum == rhsSum ? "Balanced" : "Not Balanced"
}