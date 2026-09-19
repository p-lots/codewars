func check<T: Equatable>(_ a: [T], _ x: T) -> Bool {
    return a.filter { $0 == x }.count == 1
}
