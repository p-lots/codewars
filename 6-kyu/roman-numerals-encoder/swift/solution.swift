func solution(_ number:Int) -> String {
    var n = number
    let lookupTable: [Int: String] = [
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L",
        40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    ]
    let lookupTableSorted = lookupTable.sorted(by: { $0 > $1 })
    let result = lookupTableSorted.map { (num, rom) -> String in
        var ret: String = ""
        while n >= num {
            ret += rom
            n -= num
        }
        return ret
    }
    return result.joined()
}