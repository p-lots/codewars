import Foundation

func nbDig(_ n: Int, _ d: Int) -> Int {
    let arr = (0...n).map { String($0 * $0) }.filter { $0.contains(String(d)) }
    return arr.reduce(0) { $0 + $1.reduce(0) { $0 + ($1 == Character(String(d)) ? 1 : 0) } }
}