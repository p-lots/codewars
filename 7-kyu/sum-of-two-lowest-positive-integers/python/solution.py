func sumOfTwoSmallestIntegersIn(_ array: [Int]) -> Int {
  return array.sorted()[0] + array.sorted()[1]
}