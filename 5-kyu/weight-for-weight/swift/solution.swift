import Foundation

func makeDigitSum(_ n: Int) -> Int {
    let digits = String(n).compactMap { Int(String($0)) }
    return digits.reduce(0, +)
}

func sortWeights(_ lhs: Int, _ rhs: Int) -> Bool {
    let lhsDigSum = makeDigitSum(lhs), rhsDigSum = makeDigitSum(rhs)
    if lhsDigSum == rhsDigSum {
        return String(lhs) < String(rhs)
    }
    return lhsDigSum < rhsDigSum
}

func orderWeight(_ s: String) -> String {
    let sTrimmed = s.trimmingCharacters(in: .whitespaces)
    guard !sTrimmed.isEmpty else { return "" }
    let sArr = sTrimmed.components(separatedBy: " ")
        .filter { !$0.isEmpty }
        .map { $0.compactMap { Int(String($0)) }.reduce(0) { total, n in total * 10 + n } }
    return sArr.sorted(by: sortWeights).map { String($0) }.joined(separator: " ")
}