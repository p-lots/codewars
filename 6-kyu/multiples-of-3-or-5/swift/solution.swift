func solution(_ num: Int) -> Int {
  guard num > 3 else { return num == 3 ? 3 : 0 }
  return (3..<num).filter { $0 % 5 == 0 || $0 % 3 == 0 }.reduce(0, +)
}