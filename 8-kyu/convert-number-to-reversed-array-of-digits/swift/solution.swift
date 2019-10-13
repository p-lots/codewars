func digitize(_ num:Int) -> [Int] {
    return String(num).characters.flatMap { Int(String($0)) }.reversed()
}