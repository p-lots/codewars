func dontGiveMeFive(_ start: Int, _ end: Int) -> Int {
    let rangeFiltered = (start...end).filter { !String($0).contains("5") }
    return Array(rangeFiltered).count
}