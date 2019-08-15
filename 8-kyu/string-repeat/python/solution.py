func repeatStr(_ n: Int, _ string: String) -> String {
    if n < 1 {
        return ""
    }
    var ret : String = string
    for _ in 1..<n {
        ret += string
    }
    return ret
}