import Foundation

func evenOrOdd(_ number:Int) -> String {
    var n = abs(number)
    while n > 1 {
        n -= 2
    }
    return n == 1 ? "Odd" : "Even"
}