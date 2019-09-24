func stringy(_ size: Int) -> String {
    var shouldBeOne = false
    return (1...size).reduce("") { accum, _ in
        shouldBeOne = !shouldBeOne
        if shouldBeOne {
            return accum + "1"
        }
        else {
            return accum + "0"
        }
    }
}