func isPrime(_ n: UInt) -> Bool {
    guard n > 1 else { return false }
    guard n != 2 else { return true }
    guard n % 2 == 1 else { return false }
    for i in stride(from: 3, through: n, by: 2) {
        if n % i == 0 && n != i {
            return false
        }
    }
    return true
}

func numPrimoral(_ number: UInt) -> UInt {
    var primeCount: UInt = 1, ret: UInt = 1, i: UInt = 0
    while primeCount <= number {
        if isPrime(i) {
            ret *= i
            primeCount += 1
        }
        i += 1
    }
    return ret
}