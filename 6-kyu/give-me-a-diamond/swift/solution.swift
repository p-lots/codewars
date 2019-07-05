func diamond(_ size: Int) -> String? {
    guard size % 2 == 1 && size > 0 else { return nil }
    var ret = ""
    var spacesBefore = size / 2
    for n in stride(from: 1, to: size + 1, by: 2) {
        ret += String(repeating: " ", count: spacesBefore)
        ret += String(repeating: "*", count: n) + "\n"
        spacesBefore -= 1
    }
    spacesBefore = 1
    for n in stride(from: size - 2, to: 0, by: -2) {
        ret += String(repeating: " ", count: spacesBefore)
        ret += String(repeating: "*", count: n) + "\n"
        spacesBefore += 1
    }
    return ret
}