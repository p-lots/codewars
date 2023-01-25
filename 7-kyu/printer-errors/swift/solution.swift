import Foundation

func printerError(_ s: String) -> String {
    var invalidChars = CharacterSet()
    invalidChars.insert(charactersIn: "nopqrstuvwxyz")
    let numInvalidChars: Int = s.unicodeScalars.reduce(0) { (acc: Int, nextChar: UnicodeScalar) -> Int in
        return acc + (invalidChars.contains(nextChar) ? 1 : 0)
    }
    return "\(numInvalidChars)/\(s.count)"
}