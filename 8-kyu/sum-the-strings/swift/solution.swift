func sum_str(_ a: String, _ b: String) -> String {
    if let aInt = Int(a) {
        if let bInt = Int(b) {
            return "\(aInt + bInt)"
        }
        return "\(aInt)"
    }
    if let bInt = Int(b) {
        return "\(bInt)"
    }
    return "0"
}
