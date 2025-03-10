class Solution {
  static func twosum(numbers: [Double], target: Double) -> [Int] {
    var lookupTable = [Double: Int]()
    for (idx, num) in numbers.enumerated() {
      let complement = target - num
      if let otherIdx = lookupTable[complement] {
        return [otherIdx, idx]
      }
      lookupTable[num] = idx
    }
    return [-1, -1]
  }
}