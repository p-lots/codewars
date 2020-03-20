func addLetters(_ letters: [Character]) -> Character {
    guard !letters.isEmpty else { return "z" }
    print(letters)
    let total = letters.compactMap { $0.asciiValue }.reduce(0) { $0 + $1 - 96 }
    if total % 26 == 0 {
        return "z"
    }
    return Character(Unicode.Scalar(total % 26 + 96))
}