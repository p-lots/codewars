func descendingOrder(of number: Int) -> Int {
    let numArr : [Int] = String(number).compactMap { Int(String($0)) }
    let numArrSorted = numArr.sorted(by: >)
    let result = numArrSorted.reduce(0) { $0 * 10 + $1 }
    return result
}