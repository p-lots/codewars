func stringy(_ size: Int) -> String {
    return (1...size).reduce("") { $0 + ($1 % 2 == 1 ? "1" : "0") }
}