func century(_ year: Int) -> Int {
    return year / 100 + (year % 100 > 0 ? 1 : 0)
}