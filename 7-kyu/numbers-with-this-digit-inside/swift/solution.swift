import Foundation

func numbersWithDigitInside(_ x: Int64, _ d: Int64) -> [Int64] {
    let foundNums = (1...x).filter { String($0).contains(String(d)) }
    let total = foundNums.reduce(0, +)
    let product = foundNums.count > 0 ? foundNums.reduce(1, *) : 0
    return [Int64(foundNums.count), total, product]
}
