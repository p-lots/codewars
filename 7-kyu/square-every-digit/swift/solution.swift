func squareDigits(_ num: Int) -> Int {
    let numSq = String(num).compactMap { Int(String($0)) }.map { $0 * $0 }
    return Int(numSq.reduce("") { $0 + String($1) })!
}