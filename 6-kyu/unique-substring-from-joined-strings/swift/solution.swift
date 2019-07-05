import Foundation

func longestSubstring(_ a: String, _ b: String) -> Int {
    guard !a.isEmpty else { return b.count }
    guard !b.isEmpty else { return a.count }
    guard a != b else { return 0 }
    var filterSet = Set(a)
    filterSet.formIntersection(Set(b))
    let combinedStringAB: String = a + b
    let combinedStringBA: String = b + a
    let abSplit = combinedStringAB.split(whereSeparator: { filterSet.contains($0) })
    let baSplit = combinedStringBA.split(whereSeparator: { filterSet.contains($0) })
    let substrCombinedArr = abSplit + baSplit
    if let ret = substrCombinedArr.max(by: { $0.count < $1.count }) {
        return ret.count
    } else {
        return 0
    }
}