func encrypt(text:String, rule:Int) -> String {
    return text.asciiArray.map { Int($0) + rule }.map { String(Character(UnicodeScalar($0 % 256)!)) }.joined()
}