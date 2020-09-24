import Foundation

func encryptFunc(_ text: String) -> String {
    if let firstAscii = text.first?.asciiValue {
        if text.count == 1 {
            return String(firstAscii)
        }
        var textArr = Array(text)
        textArr = Array(textArr[1...])
        textArr.swapAt(0, textArr.count - 1)
        return String(firstAscii) + String(textArr)
    }
    return ""
}

func encryptThis(text: String) -> String {
    guard !text.isEmpty else { return "" }
    return text.components(separatedBy: " ").map { encryptFunc($0) }.joined(separator: " ")
}
