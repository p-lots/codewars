import Foundation

func isDigit(_ ch: Character) -> Bool {
    switch ch {
        case "0", "1", "2", "3", "4", "5", "6", "7", "8", "9":
        return true
        default:
        return false
    }
}

func shouldReturnNilString(_ str: String) -> Bool {
    var colonCount : Int = 0
    for ch in str.characters {
        if ch == ":" { colonCount += 1 }
        else if !isDigit(ch) { return true }
    }
    return colonCount != 2
}

func correct(_ timeString: String?) -> String? {
    guard timeString != nil && timeString!.characters.count > 0 else { return timeString }
    if shouldReturnNilString(timeString!) { return nil }
    let timeStrComponents = timeString!.components(separatedBy: ":")
    var hours : Int = Int(timeStrComponents[0])!
    var minutes : Int = Int(timeStrComponents[1])!
    var seconds : Int = Int(timeStrComponents[2])!
    if (hours <= 23 && minutes <= 59 && seconds <= 59) { return timeString }
    if seconds > 59 {
        minutes += seconds / 60
        seconds %= 60
    }
    if minutes > 59 {
        hours += minutes / 60
        minutes %= 60
    }
    if hours > 23 {
        hours %= 24
    }
    return String(format: "%02d:%02d:%02d", hours, minutes, seconds)
}