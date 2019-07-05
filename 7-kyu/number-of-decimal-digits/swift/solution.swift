import Foundation

func digits(num n: UInt64) -> Int {
  if n == 0 {
    return 1
  }
  var n_copy = n, ret = 0
  while n_copy > 0 {
    n_copy /= 10
    ret += 1
  }
  return ret
}