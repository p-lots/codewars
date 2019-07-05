func rgb(_ r: Int, _ g: Int, _ b: Int) -> String {
    return String(format: "%02X%02X%02X", clamp(r), clamp(g), clamp(b))
}

func clamp(_ n: Int) -> Int {
    return min(max(n, 0), 255)
}