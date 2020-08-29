let lookupTable: [String: Int] = [
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
    "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
    "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
    "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
]

func getScore(_ name: String) -> Int {
    return name.compactMap { lookupTable[String($0).uppercased()] }.reduce(0, +) + name.count
}

func rank(_ st: String, _ we: [Int], _ n: Int) -> String {
    guard !st.isEmpty else { return "No participants" }
    let names = st.components(separatedBy: ",")
    guard names.count >= n else { return "Not enough participants" }
    let scoresWithoutWeights = names.map { getScore($0) }
    let scoresWithWeights = zip(scoresWithoutWeights, we).map { $0.0 * $0.1 }
    let namesScores = zip(names, scoresWithWeights).sorted { (lhs: (String, Int), rhs: (String, Int)) -> Bool in
        if (lhs.1 == rhs.1) { return lhs.0 < rhs.0 }
        return lhs.1 > rhs.1
    }
    return namesScores[n - 1].0
}
