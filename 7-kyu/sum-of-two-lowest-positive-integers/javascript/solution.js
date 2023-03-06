func sumOfTwoSmallestIntegersIn(_ array: [Int]) -> Int {
  let min = array.min()!
  var nextMin = array.max()!
  for n in array {
    if (n < nextMin && n > min) {
      nextMin = n
    }
  }
  return min + nextMin
}