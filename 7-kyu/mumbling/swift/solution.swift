import Foundation

func accum(_ s: String) -> String {
    guard !s.isEmpty else { return "" }
    return s.enumerated().map { (i, ch) -> String in
        return String(repeating: String(ch), count: i + 1)
    }.joined(separator: "-").capitalized
}