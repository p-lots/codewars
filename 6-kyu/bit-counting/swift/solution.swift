func countBits(_ n: Int) -> Int {
    return String(n, radix: 2).reduce(0) { acc, ch in return acc + (ch == "1" ? 1 : 0) }
}