func digitalRoot(of number: Int) -> Int {
    let n = String(number).compactMap { Int(String($0)) }.reduce(0, +)
    return n > 10 ? digitalRoot(of: n) : n
}