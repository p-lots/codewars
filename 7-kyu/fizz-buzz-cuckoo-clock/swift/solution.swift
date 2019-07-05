func fizzBuzzCuckooClock(_ time: String) -> String {
    let timeComponents = time.components(separatedBy: ":")
    let hours = Int(timeComponents[0])!
    let minutes = Int(timeComponents[1])!
    if minutes == 0 {
        return Array(repeating: "Cuckoo", count: (hours % 12 == 0 ? 12 : hours > 12 ? hours - 12 : hours)).joined(separator: " ")
    }
    else if minutes == 30 {
        return "Cuckoo"
    }
    else if minutes % 15 == 0 {
        return "Fizz Buzz"
    }
    else if minutes % 5 == 0 {
        return "Buzz"
    }
    else if minutes % 3 == 0 {
        return "Fizz"
    }
    return "tick"
}