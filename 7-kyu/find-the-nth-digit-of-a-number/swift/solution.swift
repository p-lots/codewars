import Foundation

func findDigit(_ num:Int, _ nth: Int) -> Int {
  guard nth > 0 else { return -1 }
  guard nth <= String(num).count else { return 0 }
  let numArr = abs(num).description.compactMap { Int(String($0)) }
  return numArr[numArr.count - nth]
}