func validParentheses(_ str: String) -> Bool {
  var queue: [Character] = []
  var isValid = true
  for ch in str {
    if ch == "(" {
      queue.append(ch)
    } else if ch == ")" {
      if !queue.isEmpty && queue[0] == "(" {
        isValid = true
        queue.removeFirst()
      } else {
        isValid = false
        break
      }
    }
  }
  return queue.count == 0 && isValid
}