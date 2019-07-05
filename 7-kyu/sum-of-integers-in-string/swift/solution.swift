import Foundation

func sumOfIntegersInString(_ string: String) -> Int {
    return string.components(separatedBy: CharacterSet.decimalDigits.inverted).map { Int($0) ?? 0 }.reduce(0, +)
}