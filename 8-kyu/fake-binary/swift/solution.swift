func fakeBin(digits: String) -> String {
  return digits.map { return (Int(String($0))! < 5 ? "0" : "1") }.joined()
}