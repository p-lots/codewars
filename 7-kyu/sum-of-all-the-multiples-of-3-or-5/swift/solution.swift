/*
func findSum(_ n: Int) -> Int {
    var ret : Int = 0
    for num in 3...n {
        if num % 3 == 0 || num % 5 == 0 {
            ret += num
        }
    }
    return ret
}
*/

func findSum(_ n: Int) -> Int {
    return (3...n).filter { $0 % 3 == 0 || $0 % 5 == 0 }.reduce(0, +)
}