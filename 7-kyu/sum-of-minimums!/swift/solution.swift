func sumOfMinimums(_ numbers: [[Int]]) -> Int {
    numbers.compactMap { $0.min() }.reduce(0, +)
}