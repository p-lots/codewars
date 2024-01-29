func divisors(_ n: UInt32) -> UInt32 {
    UInt32((1...n).filter { n % $0 == 0 }.count)
}