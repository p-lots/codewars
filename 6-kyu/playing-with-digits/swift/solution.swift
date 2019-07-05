import Foundation

func digPow(for number: Int, using power: Int) -> Int {
    let numArr = String(number).characters.map { Int(String($0)) ?? 0 }
    var p = power - 1
    let sum = numArr.reduce(0) { p += 1; return $0 + Int(pow(Double($1), Double(p))) }
    return sum % number == 0 ? sum / number : -1
}