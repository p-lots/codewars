func som(_ x: Int, _ y: Int) -> Int {
    x + y
}
func maxi(_ x: Int, _ y: Int) -> Int {
    max(x, y)
}
func mini(_ x: Int, _ y: Int) -> Int {
    min(x, y)
}
func gcdi(_ x: Int, _ y: Int) -> Int {
    var x = abs(x)
    var y = abs(y)
    while true {
        if x == 0 {
            return y
        }
        y %= x
        if y == 0 {
            return x
        }
        x %= y
    }
}
func lcmu(_ a: Int, _ b: Int) -> Int {
    let a = abs(a)
    let b = abs(b)
    let t = gcdi(a, b)
    return t > 0 ? a / t * b : 0
}

func operArray(_ fn: (Int, Int) -> Int, _ a: [Int], _ iniVal: Int) -> [Int] {
    var ret: [Int] = [fn(a[0], iniVal)]
    for number in a[1...] {
        let lastIdx = ret.count - 1
        let result = fn(ret[lastIdx], number)
        ret.append(result)
    }
    return ret
    
} 