func rgb(_ r: Int, _ g: Int, _ b: Int) -> String {
    return String(format: "%02X%02X%02X", clamp(r), clamp(g), clamp(b))
}

func clamp(_ n: Int) -> Int {
    if n > 255 { return 255 }
    else if n < 0 { return 0 }
    else { return n }
}