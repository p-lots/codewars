func digitalRoot(of number: Int) -> Int {
    let n = String(number).map { Int(String($0)) ?? 0 }.reduce(0, +)
    return n > 10 ? digitalRoot(of: n) : n
}