class Solution {
    static func twosum(numbers: [Int], target: Int) -> [Int] {
        var lookup_table = [Int: Int]()
        var ret = [Int]()
        for (i, num) in numbers.enumerated() {
            let diff = target - num
            if let complement = lookup_table[diff] {
                ret = [complement, i]
            } else {
                lookup_table.updateValue(i, forKey: num)
            }
        }
        return ret
    }
}