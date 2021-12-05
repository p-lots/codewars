import Foundation

func maskify(_ string: String) -> String {
    if string.count <= 4 {
      return string
    }
    return string.enumerated()
        .map { (i: Int, ch: Character) -> String in
            return i < string.count - 4 ? "#" : String(ch)
        }.joined()
}