import Foundation

func getTotal(_ lookup: [Int], _ str: String) -> Int {
    var ret = 0
    let counts = str.components(separatedBy: " ").flatMap { Int($0) }
    for (ix, count) in counts.enumerated() {
        ret += count * lookup[ix]
    }
    return ret
}

func evaluate(good: String, vsEvil evil: String) -> String {
    let goodLookup: [Int] = [ 1, 2, 3, 3, 4, 10 ]
    let evilLookup: [Int] = [ 1, 2, 2, 2, 3, 5, 10 ]
    let goodTotal = getTotal(goodLookup, good), evilTotal = getTotal(evilLookup, evil)
    return goodTotal > evilTotal ? "Battle Result: Good triumphs over Evil"
                                 : goodTotal == evilTotal ? "Battle Result: No victor on this battle field"
                                                          : "Battle Result: Evil eradicates all trace of Good"
}