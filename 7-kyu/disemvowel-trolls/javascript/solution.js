func disemvowel(_ s: String) -> String {
    var strArray = Array(s.characters)
    strArray = strArray.filter({ !isVowel($0) })
    return String(strArray)
}

func isVowel(_ s: Character) -> Bool {
    return s == "a" || s == "e" || s == "i" || s == "o" || s == "u" || s == "A" || s == "E" || s == "I" || s == "O" || s == "U"
}