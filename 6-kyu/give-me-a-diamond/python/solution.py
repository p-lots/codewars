func diamond(_ size: Int) -> String? {
  if size % 2 == 0 || size <= 0 { 
    return nil
  }    
  var ret = ""
  var spacesBefore : Int = size / 2
  for n in stride(from: 1, to: size + 1, by: 2) {
    for _ in 0..<spacesBefore {
      ret += " "
    }
    for _ in 0..<n {
      ret += "*"
    }
    spacesBefore -= 1
    ret += "\n"
  }
  spacesBefore = 1
  for n in stride(from: size - 2, to: 0, by: -2) {
    for _ in 0..<spacesBefore {
      ret += " "
    }
    for _ in 0..<n {
      ret += "*"
    }
    spacesBefore += 1
    ret += "\n"
  }
  return Optional(ret)
}