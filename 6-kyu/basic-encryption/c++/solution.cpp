func encrypt(text:String, rule:Int) -> String {
  //guard !text.isEmpty else { return text }
  var ret = String()
  var ascii = text.asciiArray
  for i in 0..<ascii.count {
      let curr: Int = Int(ascii[i])
      let converted = curr + rule
      ret.append(Character(UnicodeScalar(converted % 256)!))
  }
  return ret
}