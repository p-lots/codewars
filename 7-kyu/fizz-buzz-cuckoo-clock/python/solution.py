func fizzBuzzCuckooClock(_ time: String) -> String {
    let timeComponents = time.components(separatedBy: ":")
    let hours = Int(timeComponents[0])!
    let minutes = Int(timeComponents[1])!
    if minutes == 0 {
        if hours % 12 == 0 {
            var ret : String = "Cuckoo"
            for _ in 1..<12 {
                ret += " Cuckoo"
            }
            return ret
        }
        else if hours > 12 {
            let mod12 = hours % 12
            var ret : String = "Cuckoo"
            for _ in 1..<mod12 {
                ret += " Cuckoo"
            }
            return ret
        }
        var ret : String = "Cuckoo"
        for _ in 1..<hours {
            ret += " Cuckoo"
        }
        return ret
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