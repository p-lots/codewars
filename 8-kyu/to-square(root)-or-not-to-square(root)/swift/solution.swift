import Foundation

func squareOrSquareRoot(_ input: [Int]) -> [Int] {
    let test = { (num: Int) -> Bool in sqrt(Double(num)).truncatingRemainder(dividingBy: 1.0) == 0.0 }
    return input.map { test($0) ? Int(sqrt(Double($0))) : $0 * $0 }
}