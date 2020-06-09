func firstNonConsecutive (_ arr: [Int]) -> Int? {
    let properArr = Array(arr[0]...(arr.count + 1 + arr[0]))
    for (x, y) in zip(properArr, arr) {
        if x != y {
            return y
        }
    }
    return nil
}