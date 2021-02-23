func oddOne(_ arr: [Int]) -> Int? {
  var ret: Int? = nil
  for (i, n) in arr.enumerated() {
    if abs(n) % 2 == 1 {
      ret = i
      return ret
    }
  }
  return ret
}