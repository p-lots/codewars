import Foundation

func disemvowel(_ s: String) -> String {
    var vowels = CharacterSet()
    vowels.insert(charactersIn: "AEIOUaeiou")
    return String(s.unicodeScalars.filter { !vowels.contains($0) })
}
