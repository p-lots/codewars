func expressionMatter(_ a: Int, _ b: Int, _ c: Int) -> Int {
    let ret = [a * (b + c), a * b * c, a + b + c, (a + b) * c]
    return ret.max() ?? 0
}
