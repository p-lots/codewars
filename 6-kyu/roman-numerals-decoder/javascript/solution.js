import Foundation

func solution(_ string: String) -> Int {
    var romanArr = string.characters.map { String($0) }
    let lookupTable: [String: Int] = ["I": 1, "IV": 4, "V": 5,
        "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100,
        "CD": 400, "D": 500, "CM": 900, "M": 1000]
    var ret = 0
    while !romanArr.isEmpty {
        var toAdd = romanArr.remove(at: 0)
        if !romanArr.isEmpty {
            if let frontOfRomanArrLookup = lookupTable[romanArr[0]],
            let toAddLookup = lookupTable[toAdd],
            frontOfRomanArrLookup > toAddLookup {
                let temp = romanArr.remove(at: 0)
                toAdd += temp
            }
        }
        if let toAddLookup = lookupTable[toAdd] {
            ret += toAddLookup
        }
    }
    return ret
}