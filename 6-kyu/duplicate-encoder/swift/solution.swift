extension String {
    func countChar(_ charToCount: Character) -> Int {
        return self.reduce(0) { (acc: Int, next: Character) -> Int in
            return acc + ((next == charToCount) ? 1 : 0)
        }
    }
}

func duplicateEncode(_ word: String) -> String {
    return word.lowercased().reduce("") { (acc: String, next: Character) -> String in
        return acc + ((word.lowercased().countChar(next) == 1) ? "(" : ")")
    }
}
