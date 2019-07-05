func encryptFunc(_ word: String) -> String {
    let firstLetter = String(word[word.startIndex]).unicodeScalars
    let firstToReplace = String(firstLetter[firstLetter.startIndex].value)
    guard word.count > 1 else { return firstToReplace }
    let lastLetter = String(word[word.index(before: word.endIndex)])
    guard word.count > 2 else { return firstToReplace + lastLetter }
    let secondLetter = String(word[word.index(word.startIndex, offsetBy: 1)])
    let beginMiddle = word.index(word.startIndex, offsetBy: 2)
    let endMiddle = word.index(before: word.endIndex)
    let middleLetters = String(word[beginMiddle..<endMiddle])
    return firstToReplace + lastLetter + middleLetters + secondLetter
}

func encryptThis(text: String) -> String {
    guard !text.isEmpty else { return "" }
    return text.components(separatedBy: " ").map { encryptFunc($0) }.joined(separator: " ")
}