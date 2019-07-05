import Foundation

func countArare(_ n: Int) -> String {
    if n == 1 { return "anane" }
    return Array(repeating: "adak", count: n / 2).joined(separator: " ") + (n % 2 > 0 ? " anane" : "")
}