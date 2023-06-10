func squareSum(_ vals: [Int]) -> Int {
    return vals.reduce(0) { $0 + $1 * $1 }
}