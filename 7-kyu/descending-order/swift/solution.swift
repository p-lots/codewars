func descendingOrder(of number: Int) -> Int {
    let arr: [Int] = String(number).compactMap { Int(String($0)) }
    return arr.sorted(by: >).reduce(0) { $0 * 10 + $1 }
}