import Foundation

func spinWords(in sentence: String) -> String {
    return sentence.components(separatedBy: " ").map { $0.count >= 5 ? String($0.reversed()) : $0 }.joined(separator: " ")
}