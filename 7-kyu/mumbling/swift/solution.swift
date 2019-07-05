import Foundation

func accum(_ s: String) -> String {
    guard !s.isEmpty else { return "" }
    return (1...s.characters.count).map { i -> String in
        let idx = s.index(s.startIndex, offsetBy: i - 1)
        return String(repeating: String(s[idx]), count: i)
    }.joined(separator: "-").capitalized
}