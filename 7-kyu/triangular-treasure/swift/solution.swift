func triangular(_ n: Int) -> Int {
    if n < 1 { return 0 }
    else if n == 1 { return 1 }
    return (1...n).reduce(0, +)
}