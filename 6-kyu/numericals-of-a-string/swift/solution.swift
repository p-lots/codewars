func numericals(_ str: String) -> String {
    var ret = String()
    var counts = [Character: Int]()
    for ch in str {
        if let currChCount = counts[ch] {
            counts[ch] = currChCount + 1
            ret += String(currChCount + 1)
        } else {
            ret += String(1)
            counts[ch] = 1
        }
    }
    return ret
}