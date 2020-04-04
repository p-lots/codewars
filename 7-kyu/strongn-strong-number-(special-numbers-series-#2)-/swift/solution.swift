func strongNumber(_ number: Int) -> String {
    let numberArr = String(number).compactMap { Int(String($0)) }
    let factorialSum = numberArr.map { factorial($0) }.reduce(0, +)
    return number == factorialSum ? "STRONG!!!!" : "Not Strong !!"
}

func factorial(_ number: Int) -> Int {
    guard number > 2 else { return number }
    return (2...number).reduce(1, *)
}