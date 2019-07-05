func disemvowel(_ s: String) -> String {
    let result = String(s.characters.filter { !isVowel($0) })
    return result
}

func isVowel(_ c: Character) -> Bool {
    return c == "A" || c == "E" || c == "I" || c == "O" || c == "U"
    || c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
}