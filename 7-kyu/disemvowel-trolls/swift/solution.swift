func disemvowel(_ s: String) -> String {
    return String(s.filter { !isVowel($0) })
}

func isVowel(_ c: Character) -> Bool {
    return c == "A" || c == "E" || c == "I" || c == "O" || c == "U"
    || c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
}