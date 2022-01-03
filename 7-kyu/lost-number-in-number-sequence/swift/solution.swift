func findDeletedNumber(_ array: [Int], _ mixArray: [Int]) -> Int {
    return array.reduce(0, +) - mixArray.reduce(0, +)
}