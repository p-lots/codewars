func digitize(_ num:Int) -> [Int] {
    return String(num).compactMap { Int(String($0)) }.reversed()
}