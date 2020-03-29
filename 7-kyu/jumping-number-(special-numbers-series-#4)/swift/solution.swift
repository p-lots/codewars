func jumpingNumber(_ number: Int) -> String {
    guard number > 9 else { return "Jumping!!" }
    let numberArr = String(number).compactMap { Int(String($0)) }
    let numberArrZipped = zip(numberArr, numberArr[1...])
    for (x, y) in numberArrZipped {
        if abs(x - y) != 1 { return "Not!!" }
    }
    return "Jumping!!"
}