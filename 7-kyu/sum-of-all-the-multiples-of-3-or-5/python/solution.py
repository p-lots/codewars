func findSum(_ n: Int) -> Int {
    var sum : Int = 0
    for num in 3...n {
        if num % 5 == 0 || num % 3 == 0 {
            sum += num
        }
    }
    return sum
}